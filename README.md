# Arabic Agent Library

Arabic Agent Library is a source-grounded corpus-building project for AI agents that need to write strong Modern Standard Arabic with better diction, style, rhetoric, and source awareness.

The repository is not meant to be a generic Arabic dataset dump. Its goal is to build a traceable pipeline:

1. discover trustworthy Arabic sources
2. ingest raw files or canonical digital texts
3. extract or clean UTF-8 text
4. synthesize compact agent-friendly Markdown packs

Every output should stay linked to a real source through a central registry.

## Why this project exists

Many Arabic outputs from AI systems are understandable but stylistically weak, flattened, repetitive, or detached from classical and high-quality reference material. This project aims to create reusable Arabic reference packs that help downstream agents:

- choose stronger and clearer fusha wording
- distinguish between eloquence, clarity, and ornament
- borrow patterns from real Arabic reference works
- cite provenance instead of relying on vague style advice

## Current repository status

This repo already contains the first end-to-end slice of the pipeline:

- a registry with 13 curated source entries
- source policy and extraction/synthesis specs
- one ingested reference source
- one cleaned text excerpt
- one first Markdown knowledge pack
- one additional downloaded poetry source waiting for extraction work

Current registry summary:

- total entries: 13
- categories:
  - dictionary: 3
  - rhetoric: 2
  - grammar-style: 2
  - reference: 3
  - poetry: 3
- statuses:
  - candidate: 9
  - queued: 2
  - downloaded: 1
  - synthesized: 1

## What has been built so far

### 1) Project design and governance

- `docs/source-selection-policy.md`
- `docs/text-extraction-spec.md`
- `docs/markdown-pack-spec.md`
- `docs/plans/2026-05-21-arabic-agent-library-plan.md`

These documents define what sources are acceptable, how raw files become text, and how agent-facing Markdown should be structured.

### 2) Central source registry

- `data/registry/sources.schema.json`
- `data/registry/sources.json`
- `scripts/registry_tool.py`

The registry keeps:

- source id
- title / author
- category
- source type
- status
- URLs and mirrors
- local artifact paths
- duplicate keys
- provenance notes

Validation helpers already exist in `scripts/registry_tool.py`.

### 3) First real source pipeline

The first source pushed through the pipeline is:

- `reference-sinaatayn`
- title: `كتاب الصناعتين الكتابة والشعر`
- author: `أبو هلال العسكري`

Tracked artifacts:

- raw OCR sidecar: `data/raw/reference-sinaatayn.ia-djvu.txt`
- cleaned excerpt: `data/text/reference-sinaatayn-opening.txt`
- first Markdown pack: `data/markdown/reference-sinaatayn-balagha-fasaha.md`

This is the first proof that the pipeline is real, not just planning.

### 4) Additional acquired source

A second source has already been downloaded and committed for future work:

- `poetry-diwan-al-mutanabbi`
- raw scan PDF: `data/raw/poetry-diwan-al-mutanabbi.ia.pdf`
- raw OCR sidecar: `data/raw/poetry-diwan-al-mutanabbi.ia-djvu.txt`

This source is acquired but not yet extracted into cleaned text or Markdown.

## Repository structure

- `README.md` — project overview and current state
- `docs/` — policy, specs, plan, and handoff notes
- `data/registry/` — source registry and schema
- `data/raw/` — downloaded source files or OCR sidecars
- `data/text/` — extracted / cleaned UTF-8 text
- `data/markdown/` — agent-facing synthesized knowledge packs
- `scripts/` — project utilities

## Key files

- `docs/HANDOFF.md` — best file for another agent to read first
- `data/registry/sources.json` — authoritative working set
- `scripts/registry_tool.py` — validation and duplicate checks
- `data/markdown/reference-sinaatayn-balagha-fasaha.md` — first example of final output shape

## Validation commands

From the repo root:

```bash
python3 scripts/registry_tool.py lint
python3 scripts/registry_tool.py check-duplicates
```

## OCR environment notes

An OCR environment was prepared locally during development but is intentionally not committed.

Local path used during development:

- `.venv-ocr/`

Installed stack used locally:

- `uv`
- `torch` CPU build
- `marker-pdf`
- `surya-ocr`

The repo itself does not yet include a reproducible setup script for OCR. A next contributor can either:

- recreate the environment manually with `uv`, or
- formalize it into a committed setup script / requirements file.

## Highest-priority next steps

1. Extract a clean text artifact from `poetry-diwan-al-mutanabbi`
2. Update its registry entry with local artifact paths and status changes
3. Expand the `reference-sinaatayn` coverage beyond the opening excerpt
4. Produce more agent-facing Markdown packs from real text, not only registry metadata
5. Add reproducible OCR/bootstrap scripts so another agent can resume without local guesswork

## Non-goals

This repository is not currently:

- a polished product
- a full Arabic corpus
- a finished benchmark
- a packaged Python library

It is an actively structured build-out of a traceable Arabic knowledge library for future agent use.

## Handoff note

If another agent is continuing this project, start with:

1. `docs/HANDOFF.md`
2. `data/registry/sources.json`
3. `scripts/registry_tool.py`
4. the existing artifacts under `data/raw/`, `data/text/`, and `data/markdown/`
