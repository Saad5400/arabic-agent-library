# مذكرة تسليم: مكتبة البلاغة والفصاحة للوكيل العربي

Read this file before making changes.

## غاية المشروع

Build a source-grounded Arabic reference library that helps AI agents write better fusha by learning from real Arabic sources rather than generic style heuristics.

The project pipeline is:

1. source discovery and triage
2. raw acquisition
3. text extraction / cleaning
4. Markdown synthesis for agent consumption

## صورة الحالة عند التسليم

The project has moved beyond planning and already contains real artifacts.

### حال السجل المركزي

- 13 total source entries
- categories covered: dictionary, rhetoric, grammar-style, reference, poetry
- one source is synthesized end-to-end
- one additional poetry source is downloaded but not yet processed further

### أول مسار اكتمل طرفاه

Source id: `reference-sinaatayn`

Artifacts:

- raw OCR text: `data/raw/reference-sinaatayn.ia-djvu.txt`
- cleaned excerpt: `data/text/reference-sinaatayn-opening.txt`
- synthesized pack: `data/markdown/reference-sinaatayn-balagha-fasaha.md`

What this proves:

- registry -> raw -> text -> markdown works at least once
- the project is no longer just schema and docs

### مصدر مضاف جرى اقتناؤه

Source id: `poetry-diwan-al-mutanabbi`

Artifacts already present locally:

- `data/raw/poetry-diwan-al-mutanabbi.ia.pdf`
- `data/raw/poetry-diwan-al-mutanabbi.ia-djvu.txt`

Interpretation:

- acquisition has happened
- extraction / cleanup / synthesis still remain

## ملفات لا غنى عنها

### ابدأ بهذه الملفات

- `README.md`
- `data/registry/sources.json`
- `scripts/registry_tool.py`
- `docs/source-selection-policy.md`
- `docs/text-extraction-spec.md`
- `docs/markdown-pack-spec.md`

### أمثلة المخرجات الموجودة

- `data/text/reference-sinaatayn-opening.txt`
- `data/markdown/reference-sinaatayn-balagha-fasaha.md`

## ما يصح البناء عليه وما لا يزال ناقصًا

### ما يصح الاعتماد عليه الآن

- repository structure
- registry schema
- source policy
- extraction and markdown specs
- duplicate normalization logic in `scripts/registry_tool.py`
- first synthesized example from `reference-sinaatayn`
- downloaded mutanabbi raw artifacts

### ما يزال محتاجًا إلى استكمال

- OCR/bootstrap is not yet formalized into repo scripts
- only one source has text + markdown output
- mutanabbi raw artifacts are present, but follow-through is incomplete
- no comprehensive automated test suite yet
- no packaging / release process

## الخطوة التالية المقترحة

Best next concrete task:

1. process `poetry-diwan-al-mutanabbi`
2. create a cleaned text artifact under `data/text/`
3. update the matching registry entry with `raw_file`, `text_file`, and status
4. synthesize one small Markdown pack from that text

Why this is the best next step:

- it turns the second real source into another end-to-end proof
- it grows the corpus with a different category (poetry)
- it avoids wasting another iteration on metadata-only polishing

## أوامر التحقق

Run from repo root:

```bash
python3 scripts/registry_tool.py lint
python3 scripts/registry_tool.py check-duplicates
```

Expected current behavior:

- lint should pass
- duplicate check should report no duplicate title/author pairs

## ملاحظات بيئة التعرّف الضوئي على الحروف

A local OCR environment was used during development but is intentionally not committed.

Local stack previously used:

- `uv`
- `torch` CPU build
- `marker-pdf`
- `surya-ocr`

The local environment directory `.venv-ocr/` is ignored and should be recreated if needed.

Recommended repo improvement:

- add a documented bootstrap script for OCR
- add a repeatable extraction command for PDF / scan inputs

## اصطلاحات نموذج البيانات

Registry entries should keep these in sync:

- `status`
- `raw_file`
- `text_file`
- `markdown_outputs`
- `duplicate_keys.content_sha256` when relevant
- provenance and notes when acquisition/extraction choices matter

## فلسفة المشروع

- prefer real source-backed artifacts over more planning
- keep provenance explicit
- keep raw, cleaned text, and synthesized markdown separate
- optimize final Markdown for agent readability, not book facsimile layout
- prefer small verified increments over bulk ingestion

## إذا لم يكن لك إلا عشر دقائق

Do this in order:

1. inspect `data/registry/sources.json`
2. inspect existing mutanabbi raw files
3. produce one cleaned text excerpt
4. update registry
5. run `python3 scripts/registry_tool.py lint`

That will create the highest-value continuation from the current state.
