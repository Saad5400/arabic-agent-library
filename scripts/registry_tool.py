#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

from arabic_normalization import normalize_arabic

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "data/registry/sources.json"
SCHEMA_PATH = ROOT / "data/registry/sources.schema.json"


def load_registry() -> list:
    if not REGISTRY_PATH.exists():
        return []
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def load_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def save_registry(data: list) -> None:
    REGISTRY_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def refresh_duplicate_keys(data: list) -> int:
    changed = 0
    for entry in data:
        dup = entry.setdefault("duplicate_keys", {})
        title = normalize_arabic(entry.get("title"))
        author = normalize_arabic(entry.get("author"))
        if dup.get("normalized_title") != title:
            dup["normalized_title"] = title
            changed += 1
        if dup.get("normalized_author") != author:
            dup["normalized_author"] = author
            changed += 1
        dup.setdefault("content_sha256", None)
    return changed


def find_duplicates(data: list) -> list[tuple[str, str, str]]:
    seen = {}
    duplicates = []
    for entry in data:
        key = (
            entry.get("duplicate_keys", {}).get("normalized_title"),
            entry.get("duplicate_keys", {}).get("normalized_author"),
        )
        if key in seen and any(key):
            duplicates.append((seen[key], entry.get("id"), "title+author"))
        else:
            seen[key] = entry.get("id")
    return duplicates


def lint_registry(data: list, schema: dict) -> list[str]:
    errors: list[str] = []
    item_schema = schema["items"]
    properties = item_schema["properties"]
    required = set(item_schema.get("required", []))
    enums = {
        key: set(value["enum"])
        for key, value in properties.items()
        if isinstance(value, dict) and "enum" in value
    }

    seen_ids: set[str] = set()
    for index, entry in enumerate(data, start=1):
        label = entry.get("id") or f"entry#{index}"
        missing = sorted(key for key in required if key not in entry)
        if missing:
            errors.append(f"{label}: missing required fields: {', '.join(missing)}")

        entry_id = entry.get("id")
        if isinstance(entry_id, str):
            if entry_id in seen_ids:
                errors.append(f"{label}: duplicate id {entry_id}")
            seen_ids.add(entry_id)

        for field, allowed in enums.items():
            value = entry.get(field)
            if value is not None and value not in allowed:
                errors.append(f"{label}: invalid {field}={value!r}")

        duplicate_keys = entry.get("duplicate_keys") or {}
        if duplicate_keys.get("normalized_title") != normalize_arabic(entry.get("title")):
            errors.append(f"{label}: duplicate_keys.normalized_title is stale")
        if duplicate_keys.get("normalized_author") != normalize_arabic(entry.get("author")):
            errors.append(f"{label}: duplicate_keys.normalized_author is stale")

        original_url = entry.get("original_url")
        if original_url is not None and (not isinstance(original_url, str) or not re.match(r"https?://", original_url)):
            errors.append(f"{label}: invalid original_url {original_url!r}")

        for mirror_url in entry.get("mirror_urls", []):
            if not isinstance(mirror_url, str) or not re.match(r"https?://", mirror_url):
                errors.append(f"{label}: invalid mirror URL {mirror_url!r}")

        raw_file = entry.get("raw_file")
        if raw_file is not None and (not isinstance(raw_file, str) or not raw_file.startswith("data/raw/")):
            errors.append(f"{label}: invalid raw_file path {raw_file!r}")

        text_file = entry.get("text_file")
        if text_file is not None and (not isinstance(text_file, str) or not text_file.startswith("data/text/")):
            errors.append(f"{label}: invalid text_file path {text_file!r}")

        for output_path in entry.get("markdown_outputs", []):
            if not isinstance(output_path, str) or not output_path.startswith("data/markdown/"):
                errors.append(f"{label}: invalid markdown output path {output_path!r}")

    errors.extend(
        f"possible duplicate: {left} <-> {right} ({reason})"
        for left, right, reason in find_duplicates(data)
    )
    return errors


def cmd_refresh() -> int:
    data = load_registry()
    changed = refresh_duplicate_keys(data)
    save_registry(data)
    print(f"refreshed duplicate keys for {len(data)} entries; field updates: {changed}")
    return 0


def cmd_check_duplicates() -> int:
    data = load_registry()
    duplicates = find_duplicates(data)
    if not duplicates:
        print("no duplicate title/author pairs found")
        return 0
    for left, right, reason in duplicates:
        print(f"possible duplicate: {left} <-> {right} ({reason})")
    return 1


def cmd_lint() -> int:
    data = load_registry()
    schema = load_schema()
    errors = lint_registry(data, schema)
    if errors:
        for error in errors:
            print(error)
        return 1
    print(f"registry OK: {len(data)} entries validated")
    return 0


def cmd_audit_wikisource() -> int:
    try:
        import requests
    except ImportError:
        print("requests is required for audit-wikisource")
        return 2

    data = load_registry()
    headers = {"User-Agent": "Hermes ArabicAgentLibrary/1.0"}
    base = "https://ar.wikisource.org/w/api.php"
    checked = 0
    missing = 0

    for entry in data:
        original_url = entry.get("original_url")
        if not isinstance(original_url, str) or "ar.wikisource.org/wiki/" not in original_url:
            continue

        title = requests.utils.unquote(original_url.split("/wiki/", 1)[1]).replace("_", " ")
        response = requests.get(
            base,
            params={
                "action": "query",
                "titles": title,
                "prop": "info",
                "inprop": "url",
                "format": "json",
                "utf8": 1,
            },
            timeout=30,
            headers=headers,
        )
        response.raise_for_status()
        page = next(iter(response.json()["query"]["pages"].values()))
        checked += 1
        exists = "missing" not in page
        if not exists:
            missing += 1

        print(
            json.dumps(
                {
                    "id": entry.get("id"),
                    "requested_title": title,
                    "exists": exists,
                    "canonical_title": page.get("title"),
                    "canonical_url": page.get("fullurl"),
                },
                ensure_ascii=False,
            )
        )

    print(f"checked {checked} Wikisource-linked entries; missing={missing}")
    return 1 if missing else 0


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: registry_tool.py [refresh|check-duplicates|lint|audit-wikisource]")
        return 2
    command = sys.argv[1]
    if command == "refresh":
        return cmd_refresh()
    if command == "check-duplicates":
        return cmd_check_duplicates()
    if command == "lint":
        return cmd_lint()
    if command == "audit-wikisource":
        return cmd_audit_wikisource()
    print(f"unknown command: {command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
