#!/usr/bin/env python3
"""Fetch Arabic Wikisource pages with polite retry/backoff and provenance headers.

This helper is intended for source acquisition in the Arabic agent library repo.
It uses only the Python standard library so it works in minimal environments.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, unquote, urlencode, urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "data/registry/sources.json"
API_URL = "https://ar.wikisource.org/w/api.php"
DEFAULT_USER_AGENT = "HermesArabicAgentLibrary/1.0 (+https://github.com/Saad5400/arabic-agent-library)"


@dataclass
class PagePayload:
    requested_title: str
    canonical_title: str
    canonical_url: str
    page_id: int | None
    revision_id: int | None
    fetched_at: str
    content: str
    response_bytes: int


def load_registry() -> list[dict[str, Any]]:
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def decode_wikisource_title(url: str) -> str:
    parsed = urlparse(url)
    if "/wiki/" not in parsed.path:
        raise ValueError(f"not a Wikisource wiki URL: {url}")
    title = parsed.path.split("/wiki/", 1)[1]
    title = unquote(title).replace("_", " ")
    if parsed.query:
        query_title = parse_qs(parsed.query).get("title")
        if query_title:
            title = query_title[0].replace("_", " ")
    return title


def resolve_title(args: argparse.Namespace) -> tuple[str, str | None]:
    if args.title:
        return args.title, None
    registry = load_registry()
    for entry in registry:
        if entry.get("id") != args.source_id:
            continue
        original_url = entry.get("original_url")
        if not isinstance(original_url, str):
            raise SystemExit(f"registry entry {args.source_id} has no Wikisource original_url")
        return decode_wikisource_title(original_url), args.source_id
    raise SystemExit(f"source id not found in registry: {args.source_id}")


def fetch_json(params: dict[str, Any], *, user_agent: str, timeout: int, max_retries: int, base_sleep: float) -> dict[str, Any]:
    last_error: Exception | None = None
    for attempt in range(1, max_retries + 1):
        req = Request(f"{API_URL}?{urlencode(params)}", headers={"User-Agent": user_agent})
        try:
            with urlopen(req, timeout=timeout) as response:
                raw = response.read()
            return json.loads(raw.decode("utf-8"))
        except HTTPError as exc:
            last_error = exc
            if exc.code == 429 and attempt < max_retries:
                retry_after = exc.headers.get("Retry-After")
                if retry_after is not None:
                    sleep_for = float(retry_after)
                else:
                    sleep_for = base_sleep * (2 ** (attempt - 1)) + random.uniform(0.0, 0.5)
                print(f"HTTP 429 from Wikisource; sleeping {sleep_for:.1f}s before retry {attempt + 1}/{max_retries}", file=sys.stderr)
                time.sleep(sleep_for)
                continue
            raise
        except URLError as exc:
            last_error = exc
            if attempt < max_retries:
                sleep_for = base_sleep * (2 ** (attempt - 1)) + random.uniform(0.0, 0.5)
                print(f"network error {exc}; sleeping {sleep_for:.1f}s before retry {attempt + 1}/{max_retries}", file=sys.stderr)
                time.sleep(sleep_for)
                continue
            raise
    if last_error is not None:
        raise last_error
    raise RuntimeError("unreachable retry loop")


def fetch_page(title: str, *, user_agent: str, timeout: int, max_retries: int, base_sleep: float) -> PagePayload:
    params = {
        "action": "query",
        "prop": "revisions|info",
        "titles": title,
        "rvprop": "ids|content",
        "rvslots": "main",
        "inprop": "url",
        "redirects": 1,
        "format": "json",
        "formatversion": 2,
    }
    data = fetch_json(params, user_agent=user_agent, timeout=timeout, max_retries=max_retries, base_sleep=base_sleep)
    page = data["query"]["pages"][0]
    if page.get("missing"):
        raise SystemExit(f"page not found: {title}")
    revisions = page.get("revisions") or []
    if not revisions:
        raise SystemExit(f"page has no revision content: {title}")
    revision = revisions[0]
    content = revision["slots"]["main"].get("content", "")
    fetched_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    canonical_title = page.get("title", title)
    canonical_url = page.get("fullurl") or f"https://ar.wikisource.org/wiki/{canonical_title.replace(' ', '_')}"
    response_bytes = len(content.encode("utf-8"))
    return PagePayload(
        requested_title=title,
        canonical_title=canonical_title,
        canonical_url=canonical_url,
        page_id=page.get("pageid"),
        revision_id=revision.get("revid"),
        fetched_at=fetched_at,
        content=content,
        response_bytes=response_bytes,
    )


def render_raw_file(payload: PagePayload, *, source_id: str | None) -> str:
    header = [
        f"# Arabic Wikisource raw capture",
        f"- requested_title: {payload.requested_title}",
        f"- canonical_title: {payload.canonical_title}",
        f"- canonical_url: {payload.canonical_url}",
        f"- source_id: {source_id or ''}",
        f"- fetched_at_utc: {payload.fetched_at}",
        f"- page_id: {payload.page_id}",
        f"- revision_id: {payload.revision_id}",
        f"- content_sha256: {hashlib.sha256(payload.content.encode('utf-8')).hexdigest()}",
        "- note: This file preserves raw page wikitext for provenance before any downstream cleaning.",
        "",
    ]
    return "\n".join(header) + payload.content.rstrip() + "\n"


def infer_output_path(args: argparse.Namespace, source_id: str | None, canonical_title: str) -> Path:
    if args.output:
        return Path(args.output)
    if source_id:
        slug = source_id
    else:
        slug = canonical_title.replace("/", "-").replace(" ", "-")
    return ROOT / "data/raw" / f"{slug}.wikitext.txt"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Fetch Arabic Wikisource page wikitext with backoff and provenance headers.")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--source-id", help="Registry source id whose original_url points at Arabic Wikisource")
    source.add_argument("--title", help="Explicit Arabic Wikisource page title to fetch")
    parser.add_argument("--output", help="Output path; defaults to data/raw/<source-id>.wikitext.txt or title-derived name")
    parser.add_argument("--stdout", action="store_true", help="Print raw capture to stdout instead of writing a file")
    parser.add_argument("--timeout", type=int, default=30, help="Per-request timeout in seconds")
    parser.add_argument("--max-retries", type=int, default=6, help="Maximum attempts for transient failures / 429s")
    parser.add_argument("--base-sleep", type=float, default=4.0, help="Base backoff sleep in seconds")
    parser.add_argument("--user-agent", default=DEFAULT_USER_AGENT, help="HTTP User-Agent string")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    requested_title, source_id = resolve_title(args)
    payload = fetch_page(
        requested_title,
        user_agent=args.user_agent,
        timeout=args.timeout,
        max_retries=args.max_retries,
        base_sleep=args.base_sleep,
    )
    rendered = render_raw_file(payload, source_id=source_id)
    if args.stdout:
        sys.stdout.write(rendered)
    else:
        output_path = infer_output_path(args, source_id, payload.canonical_title)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(rendered, encoding="utf-8")
        try:
            output_label = str(output_path.relative_to(ROOT))
        except ValueError:
            output_label = str(output_path)
        print(json.dumps({
            "requested_title": payload.requested_title,
            "canonical_title": payload.canonical_title,
            "canonical_url": payload.canonical_url,
            "source_id": source_id,
            "output_path": output_label,
            "content_sha256": hashlib.sha256(payload.content.encode("utf-8")).hexdigest(),
            "content_bytes": payload.response_bytes,
            "revision_id": payload.revision_id,
        }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
