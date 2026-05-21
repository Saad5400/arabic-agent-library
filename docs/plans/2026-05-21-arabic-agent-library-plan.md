# Arabic Agent Library Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Build a source-grounded Arabic knowledge library that helps AI agents write correct, eloquent Modern Standard Arabic using curated real references.

**Architecture:** The project is split into three pipelines: source discovery, text extraction/cleaning, and Markdown knowledge synthesis. Every artifact should be traceable back to a real source through a central registry that prevents duplicates and preserves provenance.

**Tech Stack:** Markdown, JSON, Python scripts, optional OCR/PDF extraction tooling later.

---

## Project phases

### Phase 1: Registry and source policy
- Define what counts as an acceptable source.
- Create a registry schema with unique IDs, URLs, titles, authors, categories, status, and duplication checks.
- Create the first curated seed list.

### Phase 2: Raw source ingestion
- Add scripts and conventions for downloading or referencing sources.
- Store raw files separately from metadata.
- Track ingestion status and failures.

### Phase 3: Text extraction and cleanup
- Convert PDF/EPUB/HTML/TXT into UTF-8 text.
- Remove scanning noise, page headers, repeated footers, and broken line wraps.
- Store cleaned text with links back to source IDs.

### Phase 4: Markdown knowledge synthesis
- Produce agent-friendly Markdown packs by topic.
- Keep each file concise, navigable, and source-backed.
- Separate quotation material from distilled guidance.

### Phase 5: Review and expansion
- Add quality checks.
- Expand source coverage without duplication.
- Periodically rebuild Markdown outputs from improved text.

---

## Initial task breakdown

### Task 1: Create registry schema
**Objective:** Define a single structure for source tracking.

**Files:**
- Create: `data/registry/sources.schema.json`
- Create: `data/registry/sources.json`

**Verification:**
- JSON files are valid.
- Every source entry can track provenance, format, status, and duplicate detection fields.

### Task 2: Define source selection policy
**Objective:** Make source acceptance criteria explicit.

**Files:**
- Create: `docs/source-selection-policy.md`

**Verification:**
- Policy distinguishes primary references, secondary references, and excluded material.
- Policy explains how to avoid low-quality or duplicated sources.

### Task 3: Seed the first source candidates
**Objective:** Add an initial list of trusted targets to pursue.

**Files:**
- Modify: `data/registry/sources.json`

**Verification:**
- The list covers dictionaries, rhetoric/style books, grammar/style references, and poetry.
- Each candidate has a category and acquisition status.

### Task 4: Define text extraction conventions
**Objective:** Standardize how raw sources become text.

**Files:**
- Create: `docs/text-extraction-spec.md`

**Verification:**
- Spec covers file naming, encoding, cleanup rules, and provenance fields.

### Task 5: Define Markdown output format
**Objective:** Specify what an agent-facing knowledge file should look like.

**Files:**
- Create: `docs/markdown-pack-spec.md`
- Create: `data/markdown/_template.md`

**Verification:**
- Template is easy for an AI agent to scan.
- Template keeps source citations and distilled guidance separate.

### Task 6: Build first end-to-end example
**Objective:** Take one source from registry to text to Markdown.

**Files:**
- Create/Modify: under `data/raw/`, `data/text/`, `data/markdown/`

**Verification:**
- One complete example exists with traceable provenance.

---

## Working rules

- Never add a source without registry metadata.
- Never overwrite provenance.
- Prefer smaller, verifiable steps over bulk imports.
- Re-check duplicates by title, author, URL, and content hash when possible.
- Keep the final Markdown optimized for AI reading, not human book layout.

## Next recommended action

Start with Task 1 and Task 2: define the source registry schema and source selection policy before collecting real materials.
