#!/usr/bin/env python3
"""Shared Arabic normalization helpers for registry, lexicon storage, and search."""

from __future__ import annotations

import re
import unicodedata

DIACRITICS_RE = re.compile(r"[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED]")
WHITESPACE_RE = re.compile(r"\s+")
PUNCT_TRANSLATION = str.maketrans(
    {
        "ـ": "",
        "“": '"',
        "”": '"',
        "‘": "'",
        "’": "'",
        '"': " ",
        "'": " ",
        "،": " ",
        "؛": " ",
        "؟": " ",
        "/": " ",
        "\\": " ",
        "-": " ",
        "_": " ",
        ":": " ",
        ";": " ",
        ",": " ",
        ".": " ",
        "!": " ",
        "[": " ",
        "]": " ",
        "(": " ",
        ")": " ",
        "{": " ",
        "}": " ",
    }
)


def normalize_arabic(text: str | None) -> str | None:
    if text is None:
        return None
    text = unicodedata.normalize("NFKC", text)
    text = text.strip().lower().translate(PUNCT_TRANSLATION)
    text = DIACRITICS_RE.sub("", text)
    text = (
        text.replace("أ", "ا")
        .replace("إ", "ا")
        .replace("آ", "ا")
        .replace("ٱ", "ا")
        .replace("ؤ", "و")
        .replace("ئ", "ي")
        .replace("ة", "ه")
        .replace("ى", "ي")
    )
    text = WHITESPACE_RE.sub(" ", text)
    return text.strip()


def normalize_for_sort(text: str | None) -> str:
    normalized = normalize_arabic(text)
    return normalized or ""


def tokenize_search_query(text: str | None) -> list[str]:
    normalized = normalize_arabic(text)
    if not normalized:
        return []
    return [token for token in normalized.split(" ") if token]
