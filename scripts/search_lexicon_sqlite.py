#!/usr/bin/env python3
"""Search the Arabic lexicon SQLite database with normalized + fuzzy matching."""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sqlite3
import sys
from pathlib import Path
from typing import Any

from arabic_normalization import normalize_arabic, tokenize_search_query

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB_PATH = ROOT / "data/sqlite/arabic-lexicon.sqlite3"
FTS_TOKEN_RE = re.compile(r"[0-9A-Za-z\u0600-\u06FF]+")


def connect_db(path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def base_result(row: sqlite3.Row) -> dict[str, Any]:
    return {
        "id": row["id"],
        "source_id": row["source_id"],
        "source_entry_id": row["source_entry_id"],
        "headword": row["headword"],
        "headword_normalized": row["headword_normalized"],
        "root": row["root"],
        "root_normalized": row["root_normalized"],
        "definition_summary": row["definition_summary"],
        "entry_text": row["entry_text"],
        "page_start": row["page_start"],
        "page_end": row["page_end"],
        "section_ref": row["section_ref"],
        "match_reasons": [],
        "score": 0.0,
    }


def merge_results(results: dict[int, dict[str, Any]], row: sqlite3.Row, *, score: float, reason: str) -> None:
    item = results.setdefault(row["id"], base_result(row))
    item["score"] = max(item["score"], score)
    if reason not in item["match_reasons"]:
        item["match_reasons"].append(reason)


def exact_matches(conn: sqlite3.Connection, query_norm: str, source_id: str | None, results: dict[int, dict[str, Any]]) -> None:
    sql = """
        SELECT * FROM lexicon_entries
        WHERE (headword_normalized = ? OR root_normalized = ?)
    """
    params: list[Any] = [query_norm, query_norm]
    if source_id:
        sql += " AND source_id = ?"
        params.append(source_id)
    for row in conn.execute(sql, params):
        reason = "exact_headword" if row["headword_normalized"] == query_norm else "exact_root"
        merge_results(results, row, score=1.0, reason=reason)


def like_matches(conn: sqlite3.Connection, query_norm: str, source_id: str | None, results: dict[int, dict[str, Any]]) -> None:
    sql = """
        SELECT * FROM lexicon_entries
        WHERE (
          headword_normalized LIKE ? OR
          root_normalized LIKE ? OR
          definition_summary_normalized LIKE ? OR
          entry_text_normalized LIKE ?
        )
    """
    pattern = f"%{query_norm}%"
    params: list[Any] = [pattern, pattern, pattern, pattern]
    if source_id:
        sql += " AND source_id = ?"
        params.append(source_id)
    sql += " ORDER BY sort_key LIMIT 50"
    for row in conn.execute(sql, params):
        merge_results(results, row, score=0.82, reason="normalized_substring")


def sanitize_fts_tokens(tokens: list[str]) -> list[str]:
    sanitized: list[str] = []
    for token in tokens:
        sanitized.extend(FTS_TOKEN_RE.findall(token))
    return sanitized


def fts_matches(conn: sqlite3.Connection, tokens: list[str], source_id: str | None, results: dict[int, dict[str, Any]]) -> None:
    tokens = sanitize_fts_tokens(tokens)
    if not tokens:
        return
    match_query = " OR ".join(f'"{token}"*' for token in tokens)
    sql = """
        SELECT e.*, bm25(lexicon_entries_fts, 1.0, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1) AS rank
        FROM lexicon_entries_fts
        JOIN lexicon_entries e ON e.id = lexicon_entries_fts.rowid
        WHERE lexicon_entries_fts MATCH ?
    """
    params: list[Any] = [match_query]
    if source_id:
        sql += " AND e.source_id = ?"
        params.append(source_id)
    sql += " ORDER BY rank LIMIT 50"
    for row in conn.execute(sql, params):
        score = max(0.35, 0.9 - min(abs(row["rank"]), 20) / 25)
        merge_results(results, row, score=score, reason="fts_prefix")


def fuzzy_matches(conn: sqlite3.Connection, query_norm: str, source_id: str | None, results: dict[int, dict[str, Any]], threshold: float) -> None:
    sql = "SELECT * FROM lexicon_entries"
    params: list[Any] = []
    if source_id:
        sql += " WHERE source_id = ?"
        params.append(source_id)
    sql += " ORDER BY sort_key"
    scored: list[tuple[float, sqlite3.Row, str]] = []
    for row in conn.execute(sql, params):
        candidates = {
            "fuzzy_headword": row["headword_normalized"] or "",
            "fuzzy_root": row["root_normalized"] or "",
        }
        best_ratio = 0.0
        best_reason = "fuzzy_headword"
        for reason, candidate in candidates.items():
            if not candidate:
                continue
            ratio = difflib.SequenceMatcher(a=query_norm, b=candidate).ratio()
            if query_norm in candidate or candidate in query_norm:
                ratio = max(ratio, 0.74)
            if ratio > best_ratio:
                best_ratio = ratio
                best_reason = reason
        if best_ratio >= threshold:
            scored.append((best_ratio, row, best_reason))
    for ratio, row, reason in sorted(scored, key=lambda item: (-item[0], item[1]["sort_key"], item[1]["id"]))[:50]:
        merge_results(results, row, score=ratio, reason=reason)


def render_json(results: list[dict[str, Any]], query: str, query_norm: str) -> str:
    payload = {
        "query": query,
        "query_normalized": query_norm,
        "result_count": len(results),
        "results": results,
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


def render_text(results: list[dict[str, Any]], query: str, query_norm: str) -> str:
    lines = [f"query: {query}", f"query_normalized: {query_norm}", f"results: {len(results)}", ""]
    for index, result in enumerate(results, start=1):
        lines.extend(
            [
                f"[{index}] {result['headword']}  (score={result['score']:.3f}; reasons={', '.join(result['match_reasons'])})",
                f"    source_id: {result['source_id']}",
                f"    root: {result['root'] or '-'}",
                f"    definition: {(result['definition_summary'] or '').strip() or '-'}",
                f"    entry_text: {result['entry_text'][:220].replace(chr(10), ' ')}",
            ]
        )
        if result.get("page_start") is not None or result.get("page_end") is not None:
            lines.append(f"    pages: {result.get('page_start')} - {result.get('page_end')}")
        if result.get("section_ref"):
            lines.append(f"    section_ref: {result['section_ref']}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Search Arabic lexicon SQLite records.")
    parser.add_argument("query", help="Query string to search")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB_PATH, help=f"SQLite database path (default: {DEFAULT_DB_PATH})")
    parser.add_argument("--source-id", help="Restrict results to one source id")
    parser.add_argument("--limit", type=int, default=10, help="Maximum results to print")
    parser.add_argument("--fuzzy-threshold", type=float, default=0.62, help="Minimum fuzzy ratio for near-match fallback")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="Output format")
    return parser


def main() -> int:
    try:
        args = build_parser().parse_args()
        query_norm = normalize_arabic(args.query) or ""
        if not query_norm:
            print("query is empty after normalization", file=sys.stderr)
            return 2

        conn = connect_db(args.db)
        try:
            results: dict[int, dict[str, Any]] = {}
            exact_matches(conn, query_norm, args.source_id, results)
            like_matches(conn, query_norm, args.source_id, results)
            fts_matches(conn, tokenize_search_query(args.query), args.source_id, results)
            fuzzy_matches(conn, query_norm, args.source_id, results, args.fuzzy_threshold)
        finally:
            conn.close()

        ranked = sorted(
            results.values(),
            key=lambda item: (-item["score"], item["headword_normalized"], item["id"]),
        )[: args.limit]

        if args.format == "json":
            print(render_json(ranked, args.query, query_norm))
        else:
            print(render_text(ranked, args.query, query_norm), end="")
        return 0
    except (OSError, sqlite3.Error) as exc:
        print(f"search_lexicon_sqlite error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
