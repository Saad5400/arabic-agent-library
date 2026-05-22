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
- 9 sources are currently `synthesized`
- 2 sources remain `candidate`
- 2 sources remain `queued`

### أحدث إنجاز بنيوي مهم

اكتملت الآن طبقة المراجع العامة كلها، لا بمصدر واحد معزول، بل بثلاثة شهود فعلية في السجل. بعد دفعة `أدب الكاتب` الواسعة، أُنجزت كذلك أول دفعة عملية من `البيان والتبيين` اعتمادًا على شاهد Internet Archive (`al-Jahiz`) عبر اقتناء خام كبير يشمل OCR النصي وملفي `scandata.xml` و`djvu.xml` مع PDF، ثم استخراج نطاق متصل من الجزء الأول يمتد تقريبًا على 40 صفحة مصدرية (101–140) تُعرّف البيان، وتشرح قنوات الدلالة، وتنتقل إلى الإيجاز، ومراعاة السامع، وضبط عيوب الأداء. نُظمت الدفعة في ملف text عملي وحزمتين Markdown متناسبتين مع قاعدة نحو ملف واحد لكل عشرين صفحة. وبذلك صارت المراجع الثلاثة (`كتاب الصناعتين` و`أدب الكاتب` و`البيان والتبيين`) كلُّها في حالة `synthesized` فعلية.

### أمثلة مرجعية مكتملة يمكن القياس عليها

Source ids:

- `dict-mukhtar-al-sihah`
- `grammar-style-kitab`
- `reference-adab-al-katib`
- `reference-al-bayan-wa-al-tabyin`

Representative artifacts:

- `data/markdown/dict-mukhtar-al-sihah-complete-writing-foundations.md`
- `data/markdown/grammar-style-kitab-complete-writing-foundations.md`
- `data/markdown/reference-adab-al-katib-lexical-corrections-and-precision.md`
- `data/markdown/reference-al-bayan-wa-al-tabyin-channels-of-bayan-and-meaning.md`

What this now proves:

- registry -> raw -> text -> markdown works across multiple source families, not once only
- the project can both ingest new material and later rebalance file granularity for usability
- the foundation layers (dictionary + grammar/style) are materially stronger than the early handoff state
- the reference layer is now fully synthesized across its three registered sources, not stuck at one or two examples only

### مصدر شعري له مسار مكتمل فعلاً

Source id: `poetry-diwan-al-mutanabbi`

Artifacts already present locally:

- `data/raw/poetry-diwan-al-mutanabbi.ia.pdf`
- `data/raw/poetry-diwan-al-mutanabbi.ia-djvu.txt`
- `data/text/poetry-diwan-al-mutanabbi-selected-poems.txt`
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
- multiple synthesized examples across dictionary, grammar/style, reference, and poetry layers
- completed mutanabbi raw/text/markdown path as proof that the poetry layer is reachable, even if still incomplete overall

### ما يزال محتاجًا إلى استكمال

- OCR/bootstrap is not yet formalized into repo scripts
- the next unfinished checklist source is now `دلائل الإعجاز` at the rhetoric layer
- the broader poetry layer is still incomplete because `أبي تمام` and `البحتري` remain queued
- no comprehensive automated test suite yet
- no packaging / release process

## الخطوة التالية المقترحة

Best next concrete task:

1. start `rhetoric-dalail-al-ijaz` in line with `docs/MASTER_EXECUTION_CHECKLIST.md`
2. acquire a materially large raw batch from a real digital witness or a broad digital text witness (not a tiny excerpt)
3. build one cleaned text artifact under `data/text/`
4. synthesize one or more appropriately broad Markdown outputs under the ~1 file per 20 pages rule, ثم تحديث السجل

Why this is the best next step:

- the checklist order has now moved cleanly from the completed reference layer into the first unfinished rhetoric source before returning to poetry
- repeating minor expansions on `البيان والتبيين` immediately would violate the anti-repeat rule after a substantive 40-page batch already landed
- `دلائل الإعجاز` is the clearest next source for beginning the rhetoric layer on top of the now-stronger dictionary, grammar, and reference foundations

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
- prefer broad verified source batches over tiny polished slices

## إذا لم يكن لك إلا عشر دقائق

Do this in order:

1. inspect `docs/MASTER_EXECUTION_CHECKLIST.md`
2. inspect `data/registry/sources.json`
3. start the next unfinished source in checklist order (`rhetoric-dalail-al-ijaz`)
4. update registry and checklist together
5. run `python3 scripts/registry_tool.py lint`

That will create the highest-value continuation from the current state.
