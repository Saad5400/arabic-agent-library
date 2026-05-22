#!/usr/bin/env python3
"""Export Arabic lexicon SQLite content to JSON, JSONL, or CSV."""

from __future__ import annotations

import argparse
import csv
import json
import sqlite3
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB_PATH = ROOT / "data/sqlite/arabic-lexicon.sqlite3"

FIELDS = [
    "id",
    "source_id",
    "source_entry_id",
    "headword",
    "headword_normalized",
    "root",
    "root_normalized",
    "definition_summary",
    "definition_summary_normalized",
    "usage_notes",
    "usage_notes_normalized",
    "entry_text",
    "entry_text_normalized",
    "examples_json",
    "metadata_json",
    "provenance_json",
    "page_start",
    "page_end",
    "section_ref",
    "sort_key",
    "content_sha256",
    "created_at",
    "updated_at",
]


def connect_db(path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def fetch_rows(conn: sqlite3.Connection, source_id: str | None, limit: int | None) -> list[dict[str, Any]]:
    sql = "SELECT {} FROM lexicon_entries".format(", ".join(FIELDS))
    params: list[Any] = []
    if source_id:
        sql += " WHERE source_id = ?"
        params.append(source_id)
    sql += " ORDER BY source_id, sort_key, id"
    if limit is not None:
        sql += " LIMIT ?"
        params.append(limit)
    return [dict(row) for row in conn.execute(sql, params)]


def decode_json_columns(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    decoded = []
    for row in rows:
        item = dict(row)
        item["examples"] = json.loads(item.pop("examples_json"))
        item["metadata"] = json.loads(item.pop("metadata_json"))
        item["provenance"] = json.loads(item.pop("provenance_json"))
        decoded.append(item)
    return decoded


def export_json(output: Path, rows: list[dict[str, Any]], pretty: bool) -> None:
    payload = decode_json_columns(rows)
    output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2 if pretty else None) + ("\n" if pretty else ""),
        encoding="utf-8",
    )


def export_jsonl(output: Path, rows: list[dict[str, Any]]) -> None:
    decoded = decode_json_columns(rows)
    with output.open("w", encoding="utf-8") as handle:
        for row in decoded:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def export_csv(output: Path, rows: list[dict[str, Any]]) -> None:
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def infer_format(output: Path, explicit: str | None) -> str:
    if explicit:
        return explicit
    suffix = output.suffix.lower()
    if suffix == ".json":
        return "json"
    if suffix == ".jsonl":
        return "jsonl"
    if suffix == ".csv":
        return "csv"
    raise SystemExit("could not infer export format; pass --format json|jsonl|csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Export Arabic lexicon SQLite records.")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB_PATH, help=f"SQLite database path (default: {DEFAULT_DB_PATH})")
    parser.add_argument("--output", type=Path, required=True, help="Destination file path")
    parser.add_argument("--format", choices=["json", "jsonl", "csv"], help="Override export format")
    parser.add_argument("--source-id", help="Filter by source id")
    parser.add_argument("--limit", type=int, help="Maximum rows to export")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    return parser


def main() -> int:
    try:
        args = build_parser().parse_args()
        args.output.parent.mkdir(parents=True, exist_ok=True)
        export_format = infer_format(args.output, args.format)
        conn = connect_db(args.db)
        try:
            rows = fetch_rows(conn, args.source_id, args.limit)
        finally:
            conn.close()

        if export_format == "json":
            export_json(args.output, rows, args.pretty)
        elif export_format == "jsonl":
            export_jsonl(args.output, rows)
        else:
            export_csv(args.output, rows)

        print(json.dumps({
            "db": str(args.db),
            "output": str(args.output),
            "format": export_format,
            "rows": len(rows),
            "source_id": args.source_id,
        }, ensure_ascii=False))
        return 0
    except (OSError, json.JSONDecodeError, sqlite3.Error) as exc:
        print(f"export_lexicon_sqlite error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
