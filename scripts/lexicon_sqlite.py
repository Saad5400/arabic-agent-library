#!/usr/bin/env python3
"""Initialize and populate the Arabic lexicon SQLite database."""

from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
import sys
from pathlib import Path
from typing import Any, Iterable

from arabic_normalization import normalize_arabic, normalize_for_sort

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB_PATH = ROOT / "data/sqlite/arabic-lexicon.sqlite3"
DEFAULT_SCHEMA_PATH = ROOT / "data/registry/lexicon.schema.sql"
DEFAULT_REGISTRY_PATH = ROOT / "data/registry/sources.json"


class LexiconError(Exception):
    pass


REQUIRED_INPUT_FIELDS = {"source_id", "headword", "entry_text"}


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def connect_db(path: Path) -> sqlite3.Connection:
    ensure_parent(path)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db(db_path: Path, schema_path: Path) -> None:
    conn = connect_db(db_path)
    try:
        schema = schema_path.read_text(encoding="utf-8")
        conn.executescript(schema)
        conn.commit()
    finally:
        conn.close()


def load_registry(path: Path) -> list[dict[str, Any]]:
    return json.loads(path.read_text(encoding="utf-8"))


def sync_sources(conn: sqlite3.Connection, registry_entries: Iterable[dict[str, Any]]) -> int:
    count = 0
    for entry in registry_entries:
        title = entry.get("title") or entry["id"]
        author = entry.get("author")
        conn.execute(
            """
            INSERT INTO sources (
              id, title, title_normalized, author, author_normalized,
              category, source_type, language_stage, original_url, notes, registry_json, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(id) DO UPDATE SET
              title=excluded.title,
              title_normalized=excluded.title_normalized,
              author=excluded.author,
              author_normalized=excluded.author_normalized,
              category=excluded.category,
              source_type=excluded.source_type,
              language_stage=excluded.language_stage,
              original_url=excluded.original_url,
              notes=excluded.notes,
              registry_json=excluded.registry_json,
              updated_at=CURRENT_TIMESTAMP
            """,
            (
                entry["id"],
                title,
                normalize_arabic(title) or "",
                author,
                normalize_arabic(author),
                entry.get("category"),
                entry.get("source_type"),
                entry.get("language_stage"),
                entry.get("original_url"),
                entry.get("notes"),
                json.dumps(entry, ensure_ascii=False, sort_keys=True),
            ),
        )
        count += 1
    return count


def normalize_json_field(value: Any, *, fallback: Any) -> str:
    if value is None:
        value = fallback
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def normalize_entry_payload(payload: dict[str, Any]) -> dict[str, Any]:
    missing = sorted(field for field in REQUIRED_INPUT_FIELDS if payload.get(field) is None)
    if missing:
        raise LexiconError(f"entry is missing required fields: {', '.join(missing)}")

    headword = str(payload["headword"]).strip()
    root = payload.get("root")
    entry_text = str(payload["entry_text"]).strip()
    source_id = str(payload["source_id"]).strip()
    raw_source_entry_id = payload.get("source_entry_id")
    source_entry_id = str(raw_source_entry_id).strip() if raw_source_entry_id is not None else None
    if not source_id:
        raise LexiconError("source_id cannot be empty")
    if not headword:
        raise LexiconError("entry headword cannot be empty")
    if not entry_text:
        raise LexiconError("entry_text cannot be empty")
    definition_summary = payload.get("definition_summary")
    usage_notes = payload.get("usage_notes")
    metadata_json = normalize_json_field(payload.get("metadata"), fallback={})
    provenance_json = normalize_json_field(payload.get("provenance"), fallback={})
    examples_json = normalize_json_field(payload.get("examples"), fallback=[])

    normalized = {
        "source_id": source_id,
        "source_entry_id": source_entry_id or None,
        "headword": headword,
        "headword_normalized": normalize_arabic(headword) or headword,
        "root": root.strip() if isinstance(root, str) and root.strip() else None,
        "entry_text": entry_text,
        "entry_text_normalized": normalize_arabic(entry_text) or entry_text,
        "definition_summary": definition_summary.strip() if isinstance(definition_summary, str) and definition_summary.strip() else None,
        "usage_notes": usage_notes.strip() if isinstance(usage_notes, str) and usage_notes.strip() else None,
        "examples_json": examples_json,
        "metadata_json": metadata_json,
        "provenance_json": provenance_json,
        "page_start": payload.get("page_start"),
        "page_end": payload.get("page_end"),
        "section_ref": payload.get("section_ref"),
    }
    normalized["root_normalized"] = normalize_arabic(normalized["root"])
    normalized["definition_summary_normalized"] = normalize_arabic(normalized["definition_summary"])
    normalized["usage_notes_normalized"] = normalize_arabic(normalized["usage_notes"])
    normalized["sort_key"] = normalize_for_sort(normalized["headword"])

    sha_payload = {
        "source_id": normalized["source_id"],
        "source_entry_id": normalized["source_entry_id"],
        "headword_normalized": normalized["headword_normalized"],
        "root_normalized": normalized["root_normalized"],
        "entry_text_normalized": normalized["entry_text_normalized"],
        "definition_summary_normalized": normalized["definition_summary_normalized"],
        "usage_notes_normalized": normalized["usage_notes_normalized"],
        "examples_json": json.loads(examples_json),
        "metadata_json": json.loads(metadata_json),
        "provenance_json": json.loads(provenance_json),
        "page_start": normalized["page_start"],
        "page_end": normalized["page_end"],
        "section_ref": normalized["section_ref"],
    }
    normalized["content_sha256"] = hashlib.sha256(
        json.dumps(sha_payload, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()
    if not normalized["source_entry_id"]:
        identity_payload = {
            "source_id": normalized["source_id"],
            "headword_normalized": normalized["headword_normalized"],
            "root_normalized": normalized["root_normalized"],
            "page_start": normalized["page_start"],
            "page_end": normalized["page_end"],
            "section_ref": normalized["section_ref"],
        }
        identity_sha = hashlib.sha256(
            json.dumps(identity_payload, ensure_ascii=False, sort_keys=True).encode("utf-8")
        ).hexdigest()
        normalized["source_entry_id"] = f"{normalized['headword_normalized']}-{identity_sha[:16]}"
    return normalized


def iter_input_records(path: Path) -> Iterable[dict[str, Any]]:
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return []
    if path.suffix.lower() == ".jsonl":
        return [json.loads(line) for line in text.splitlines() if line.strip()]
    payload = json.loads(text)
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict) and isinstance(payload.get("entries"), list):
        return payload["entries"]
    raise LexiconError("input must be JSON array, JSONL, or object with an 'entries' list")


def import_entries(conn: sqlite3.Connection, records: Iterable[dict[str, Any]]) -> tuple[int, int]:
    inserted = 0
    updated = 0
    for record in records:
        entry = normalize_entry_payload(record)
        cursor = conn.execute(
            "SELECT id FROM lexicon_entries WHERE source_id = ? AND source_entry_id = ?",
            (entry["source_id"], entry["source_entry_id"]),
        )
        existing = cursor.fetchone()
        conn.execute(
            """
            INSERT INTO lexicon_entries (
              source_id, source_entry_id, headword, headword_normalized,
              root, root_normalized, entry_text, entry_text_normalized,
              definition_summary, definition_summary_normalized,
              usage_notes, usage_notes_normalized,
              examples_json, metadata_json, provenance_json,
              page_start, page_end, section_ref, sort_key, content_sha256, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(source_id, source_entry_id) DO UPDATE SET
              headword=excluded.headword,
              headword_normalized=excluded.headword_normalized,
              root=excluded.root,
              root_normalized=excluded.root_normalized,
              entry_text=excluded.entry_text,
              entry_text_normalized=excluded.entry_text_normalized,
              definition_summary=excluded.definition_summary,
              definition_summary_normalized=excluded.definition_summary_normalized,
              usage_notes=excluded.usage_notes,
              usage_notes_normalized=excluded.usage_notes_normalized,
              examples_json=excluded.examples_json,
              metadata_json=excluded.metadata_json,
              provenance_json=excluded.provenance_json,
              page_start=excluded.page_start,
              page_end=excluded.page_end,
              section_ref=excluded.section_ref,
              sort_key=excluded.sort_key,
              content_sha256=excluded.content_sha256,
              updated_at=CURRENT_TIMESTAMP
            """,
            (
                entry["source_id"],
                entry["source_entry_id"],
                entry["headword"],
                entry["headword_normalized"],
                entry["root"],
                entry["root_normalized"],
                entry["entry_text"],
                entry["entry_text_normalized"],
                entry["definition_summary"],
                entry["definition_summary_normalized"],
                entry["usage_notes"],
                entry["usage_notes_normalized"],
                entry["examples_json"],
                entry["metadata_json"],
                entry["provenance_json"],
                entry["page_start"],
                entry["page_end"],
                entry["section_ref"],
                entry["sort_key"],
                entry["content_sha256"],
            ),
        )
        if existing is None:
            inserted += 1
        else:
            updated += 1
    return inserted, updated


def cmd_init(args: argparse.Namespace) -> int:
    init_db(args.db, args.schema)
    print(json.dumps({"db": str(args.db), "schema": str(args.schema), "status": "initialized"}, ensure_ascii=False))
    return 0


def cmd_sync_sources(args: argparse.Namespace) -> int:
    conn = connect_db(args.db)
    try:
        count = sync_sources(conn, load_registry(args.registry))
        conn.commit()
    finally:
        conn.close()
    print(json.dumps({"db": str(args.db), "synced_sources": count}, ensure_ascii=False))
    return 0


def cmd_import_json(args: argparse.Namespace) -> int:
    conn = connect_db(args.db)
    try:
        inserted, updated = import_entries(conn, iter_input_records(args.input))
        conn.commit()
    finally:
        conn.close()
    print(json.dumps({"db": str(args.db), "input": str(args.input), "inserted": inserted, "updated": updated}, ensure_ascii=False))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage the Arabic lexicon SQLite database.")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB_PATH, help=f"SQLite database path (default: {DEFAULT_DB_PATH})")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Create the SQLite database schema")
    init_parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA_PATH, help=f"Schema SQL path (default: {DEFAULT_SCHEMA_PATH})")
    init_parser.set_defaults(func=cmd_init)

    sync_parser = subparsers.add_parser("sync-sources", help="Copy registry sources into the SQLite sources table")
    sync_parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY_PATH, help=f"Registry JSON path (default: {DEFAULT_REGISTRY_PATH})")
    sync_parser.set_defaults(func=cmd_sync_sources)

    import_parser = subparsers.add_parser("import-json", help="Import lexicon entries from JSON, JSONL, or {entries:[...]} payloads")
    import_parser.add_argument("--input", type=Path, required=True, help="Input file path")
    import_parser.set_defaults(func=cmd_import_json)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return args.func(args)
    except LexiconError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    except (OSError, json.JSONDecodeError, sqlite3.Error) as exc:
        print(f"lexicon_sqlite error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
