# خطة تنفيذ مكتبة البلاغة والفصاحة للوكيل العربي

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Build a source-grounded Arabic knowledge library that helps AI agents write correct, eloquent Modern Standard Arabic using curated real references.

**Architecture:** The project is split into three pipelines: source discovery, text extraction/cleaning, and Markdown knowledge synthesis. Every artifact should be traceable back to a real source through a central registry that prevents duplicates and preserves provenance.

**Tech Stack:** Markdown, JSON, Python scripts, optional OCR/PDF extraction tooling later.

---

## مراحل المشروع

### المرحلة الأولى: السجل وسياسة اختيار المصادر
- Define what counts as an acceptable source.
- Create a registry schema with unique IDs, URLs, titles, authors, categories, status, and duplication checks.
- Create the first curated seed list.

### المرحلة الثانية: اقتناء المواد الخام
- Add scripts and conventions for downloading or referencing sources.
- Store raw files separately from metadata.
- Track ingestion status and failures.

### المرحلة الثالثة: استخراج النص وتنقيحه
- Convert PDF/EPUB/HTML/TXT into UTF-8 text.
- Remove scanning noise, page headers, repeated footers, and broken line wraps.
- Store cleaned text with links back to source IDs.

### المرحلة الرابعة: تركيب الحزم المعرفية بصيغة ماركداون
- Produce agent-friendly Markdown packs by topic.
- Keep each file concise, navigable, and source-backed.
- Separate quotation material from distilled guidance.

### المرحلة الخامسة: المراجعة والتوسعة
- Add quality checks.
- Expand source coverage without duplication.
- Periodically rebuild Markdown outputs from improved text.

---

## تفصيل المهام الأولى

### المهمة الأولى: إنشاء مخطط السجل
**Objective:** Define a single structure for source tracking.

**Files:**
- Create: `data/registry/sources.schema.json`
- Create: `data/registry/sources.json`

**Verification:**
- JSON files are valid.
- Every source entry can track provenance, format, status, and duplicate detection fields.

### المهمة الثانية: ضبط سياسة اختيار المصادر
**Objective:** Make source acceptance criteria explicit.

**Files:**
- Create: `docs/source-selection-policy.md`

**Verification:**
- Policy distinguishes primary references, secondary references, and excluded material.
- Policy explains how to avoid low-quality or duplicated sources.

### المهمة الثالثة: زرع الدفعة الأولى من المصادر المرشحة
**Objective:** Add an initial list of trusted targets to pursue.

**Files:**
- Modify: `data/registry/sources.json`

**Verification:**
- The list covers dictionaries, rhetoric/style books, grammar/style references, and poetry.
- Each candidate has a category and acquisition status.

### المهمة الرابعة: تحديد أعراف استخراج النص
**Objective:** Standardize how raw sources become text.

**Files:**
- Create: `docs/text-extraction-spec.md`

**Verification:**
- Spec covers file naming, encoding, cleanup rules, and provenance fields.

### المهمة الخامسة: تحديد صورة المخرج بصيغة ماركداون
**Objective:** Specify what an agent-facing knowledge file should look like.

**Files:**
- Create: `docs/markdown-pack-spec.md`
- Create: `data/markdown/_template.md`

**Verification:**
- Template is easy for an AI agent to scan.
- Template keeps source citations and distilled guidance separate.

### المهمة السادسة: بناء أول مثال مكتمل المسار
**Objective:** Take one source from registry to text to Markdown.

**Files:**
- Create/Modify: under `data/raw/`, `data/text/`, `data/markdown/`

**Verification:**
- One complete example exists with traceable provenance.

---

## قواعد العمل

- Never add a source without registry metadata.
- Never overwrite provenance.
- Prefer smaller, verifiable steps over bulk imports.
- Re-check duplicates by title, author, URL, and content hash when possible.
- Keep the final Markdown optimized for AI reading, not human book layout.

## الخطوة المقترحة التالية

Start with Task 1 and Task 2: define the source registry schema and source selection policy before collecting real materials.
