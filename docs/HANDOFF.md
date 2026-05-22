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
- 7 sources are currently `synthesized`
- 4 sources remain `candidate`
- 2 sources remain `queued`

### أحدث إنجاز بنيوي مهم

المستودع لم يعد في مرحلة إثبات المسار فقط؛ بل دخل مرحلة **مراجعة الأساس المنتج نفسه**. في آخر مراجعة كبيرة جُمعت حزم `مختار الصحاح` و`الكتاب` المتفرقة في ملفين جامعَين، وصارت مخرجات المصادر التأسيسية أوضح وأقل تفتيتًا، مع تحديث السجل والخطة الرئيسية تبعًا لذلك.

### مثالان مرجعيان مكتملان داخل طبقة الأساس

Source ids:

- `dict-mukhtar-al-sihah`
- `grammar-style-kitab`

Representative artifacts:

- `data/markdown/dict-mukhtar-al-sihah-complete-writing-foundations.md`
- `data/markdown/grammar-style-kitab-complete-writing-foundations.md`

What this now proves:

- registry -> raw -> text -> markdown works across multiple source families, not once only
- the project can both ingest new material and later rebalance file granularity for usability
- the foundation layers (dictionary + grammar/style) are materially stronger than the early handoff state

### مصدر شعري له مسار مكتمل فعلاً

Source id: `poetry-diwan-al-mutanabbi`

Artifacts already present locally:

- `data/raw/poetry-diwan-al-mutanabbi.ia.pdf`
- `data/raw/poetry-diwan-al-mutanabbi.ia-djvu.txt`
- `data/text/poetry-mutanabbi-ambition-opening.txt`
- `data/markdown/poetry-mutanabbi-ambition-and-voice.md`

Interpretation:

- acquisition, cleanup, and synthesis have all happened for this source
- poetry is no longer merely downloaded raw material

## ملفات لا غنى عنها

### ابدأ بهذه الملفات

- `docs/MASTER_EXECUTION_CHECKLIST.md`
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

1. start `reference-adab-al-katib` in line with `docs/MASTER_EXECUTION_CHECKLIST.md`
2. acquire a materially large raw batch from a real digital witness (not a tiny excerpt)
3. build one cleaned text artifact under `data/text/`
4. synthesize one appropriately broad Markdown output, ثم تحديث السجل

Why this is the best next step:

- the checklist’s first audit step for dictionary/grammar foundations has now been advanced
- the project should move next to the first unfinished reference source instead of looping on the same foundation files
- `أدب الكاتب` fits the user’s goal of practical, source-grounded guidance for fusha writing better than another cosmetic reshuffle

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
