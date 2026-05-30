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

- 14 total source entries
- categories covered: dictionary, rhetoric, grammar-style, reference, poetry
- 14 sources are currently `synthesized`
- 0 sources remain `candidate`
- 0 sources remain `queued`

### أحدث إنجاز بنيوي مهم

أضيف `dict-taj-al-arus` كمصدر معجمي رابع synthesized بدل بقاء raw شاهد Internet Archive غير مسجل. استُخدم الشاهد الكبير `taga07_202001` المحفوظ محليًا (`data/raw/dict-taj-al-arus.ia.pdf`، و`data/raw/dict-taj-al-arus.ia-djvu.txt`، و`data/raw/dict-taj-al-arus.ia-djvu.xml`، و`data/raw/dict-taj-al-arus.ia-scandata.xml`) لا ملفات wikitext الصغيرة ولا فهرسًا. استُخرج نطاق متصل من DjVuXML عبر الأوراق/OBJECTs 370-412، أي نحو 43 ورقة مصدرية من محتوى معجمي حقيقي، ثم صيغ منه ملف OCR وسيط وملف اختيار عملي محافظ، وتحوّل إلى حزمتين Markdown: واحدة عن الأبد/الأحد/الأكيد/الأمد، والثانية عن الأيد/أبجد/لا بد/التبدد/البرد. وبذلك صارت كل المصادر المسجلة حاليًا في السجل synthesized، وأصبحت الخطوة التالية حسب `docs/MASTER_EXECUTION_CHECKLIST.md` هي مراجعة الجودة النهائية على المشروع كله.

### أمثلة مرجعية مكتملة يمكن القياس عليها

Source ids:

- `dict-mukhtar-al-sihah`
- `dict-taj-al-arus`
- `grammar-style-kitab`
- `reference-adab-al-katib`
- `reference-al-bayan-wa-al-tabyin`

Representative artifacts:

- `data/markdown/dict-mukhtar-al-sihah-complete-writing-foundations.md`
- `data/markdown/dict-taj-al-arus-time-unity-and-confirmed-commitment.md`
- `data/markdown/grammar-style-kitab-complete-writing-foundations.md`
- `data/markdown/reference-adab-al-katib-lexical-corrections-and-precision.md`
- `data/markdown/reference-al-bayan-wa-al-tabyin-channels-of-bayan-and-meaning.md`
- `data/markdown/rhetoric-dalail-al-ijaz-nazm-and-relational-meaning.md`

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
- the rhetoric layer is now fully synthesized across its two registered sources
- the broader poetry layer is now synthesized across its three registered diwans
- no comprehensive automated test suite yet
- no packaging / release process

## الخطوة التالية المقترحة

Best next concrete task:

1. execute phase 6 in `docs/MASTER_EXECUTION_CHECKLIST.md`: final project-wide quality review
2. audit every `synthesized` source for existing raw/text/markdown paths and source-page/Markdown-count proportionality
3. normalize stale registry notes and handoff/readme counts where they drift from reality
4. run both registry validations and update the checklist boxes only when the audit is actually complete

Why this is the best next step:

- all currently registered sources are now synthesized
- the last run added a real dictionary foundation increment from `تاج العروس`, so repeating another small same-source slice immediately would risk source-churn rather than final consolidation
- the master checklist's next unchecked item is explicitly the final quality review

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
3. start phase 6 final quality review in checklist order
4. update registry/checklist/readme/handoff together only when facts are verified
5. run `python3 scripts/registry_tool.py lint` and `python3 scripts/registry_tool.py check-duplicates`

That will create the highest-value continuation from the current state.
