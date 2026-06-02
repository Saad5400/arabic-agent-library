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

### أحدث إنجاز مصدري بعد الإغلاق المرحلي

وُسِّع الأساس النحوي/الأسلوبي داخل `الخصائص` بدفعة كبيرة جديدة من ويكي مصدر لا تكرر دفعاته السابقة: 12 صفحة فعلية عن اختلاف اللغات وحجيتها، أصل اللغة، إجماع أهل العربية، انتقال اللسان، اجتماع اللغات، تعارض السماع والقياس، المخالف للجمهور، تركب اللغات، وتلاقي اللغة. حُفظ الخام في `data/raw/grammar-style-khasais-lughat-samaa-qiyas-batch.wikitext.txt` بحجم 136,667 bytes ونحو 13,968 كلمة عربية، أي قرابة 40–47 صفحة رقمية. نُظم في `data/text/grammar-style-khasais-lughat-samaa-qiyas-foundations.txt`، وأُنتجت حزمتا Markdown: `data/markdown/grammar-style-khasais-language-variation-and-usage-authority.md` و`data/markdown/grammar-style-khasais-samaa-qiyas-and-apparent-exceptions.md`. هذا تقدم grammar/style foundation ويعالج أخطاء عملية للوكيل: التخطئة المتسرعة، القياس على الشاذ، وبناء الاشتقاق من تشابه لفظي عابر.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

وُسِّعت طبقة `تاج العروس` مرة أخرى بدفعة معجمية متصلة من الأوراق/OBJECTs 456-498 من شاهد Internet Archive نفسه، لا من فهرس ولا من wikitext صغير. أُنتج لها OCR وسيط `data/text/dict-taj-al-arus-leaves-456-498-ocr-extract.txt` وملف اختيار عملي `data/text/dict-taj-al-arus-leaves-456-498-foundational-selection.txt`، ثم جُمعت الدفعات 370-412 و413-455 و456-498 في النص المعتمد الجديد `data/text/dict-taj-al-arus-leaves-370-498-foundational-selection.txt`. أضيفت حزمتا Markdown جديدتان: `data/markdown/dict-taj-al-arus-old-inheritance-denial-and-clear-paths.md` و`data/markdown/dict-taj-al-arus-stripping-clarity-and-separate-remnants.md`. صار `dict-taj-al-arus` يغطي نحو 129 ورقة مصدرية وست حزم، وهو متناسب مع قاعدة ~ملف لكل 20 صفحة/ورقة.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

وُسِّع الأساس النحوي/الأسلوبي داخل `الكتاب` بدفعة كبيرة من `الجزء الرابع` الكامل على ويكي مصدر، لا من باب صغير منفرد. حُفظ الخام في `data/raw/grammar-style-kitab-part-four.wikitext.txt` بحجم يقارب 199 كيلوبايت، ونُظم في `data/text/grammar-style-kitab-part-four-ibtida-nida-istithna-damair-foundations.txt`. أُنتجت ثلاث حزم Markdown متوسطة الغنى: `data/markdown/grammar-style-kitab-part-four-ibtida-inna-and-kam.md`، و`data/markdown/grammar-style-kitab-part-four-nida-nudba-and-address.md`، و`data/markdown/grammar-style-kitab-part-four-negation-exception-pronouns.md`. تغطي هذه الدفعة نحو 60 صفحة مصدرية رقمية تقديرية من مباحث الابتداء، والحروف الخمسة، وكم، والنداء والندبة، والنفي والاستثناء، والضمائر والاستفهام، ولذلك يبررها التقسيم إلى ثلاث حزم تحت قاعدة ~ملف لكل 20 صفحة.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

وُسِّعت طبقة `تاج العروس` بدفعة معجمية جديدة متصلة من الأوراق/OBJECTs 413-455 من شاهد Internet Archive نفسه، لا من فهرس ولا من wikitext صغير. أُنتج لها OCR وسيط `data/text/dict-taj-al-arus-leaves-413-455-ocr-extract.txt` وملف اختيار عملي `data/text/dict-taj-al-arus-leaves-413-455-foundational-selection.txt`، ثم جُمعت الدفعتان 370-412 و413-455 في النص المعتمد الجديد `data/text/dict-taj-al-arus-leaves-370-455-foundational-selection.txt`. أضيفت حزمتا Markdown جديدتان: `data/markdown/dict-taj-al-arus-cooling-distance-and-message-paths.md` و`data/markdown/dict-taj-al-arus-place-stagnation-and-erasure.md`. صار `dict-taj-al-arus` يغطي نحو 86 ورقة مصدرية وأربع حزم، وهو متناسب مع قاعدة ~ملف لكل 20 صفحة.

### أحدث إنجاز بنيوي مهم

أُنجزت مراجعة الجودة النهائية للمشروع كله، ووُثقت في `docs/FINAL_QUALITY_REVIEW.md`. راجعت المراجعة كل entries بحالة `synthesized` في `data/registry/sources.json` واحدًا واحدًا، وتحققت من وجود raw/text/markdown، ومن عدم وجود Markdown غير مسجل أو إحالات Markdown مفقودة، ومن أن عدد الحزم لكل مصدر مناسب لحجم الشريحة المصدرية تقريبًا. بناءً على ذلك أُغلقت مرحلة 6 في `docs/MASTER_EXECUTION_CHECKLIST.md`: كل المصادر الأربعة عشر المسجلة حاليًا synthesized، ولا توجد candidate أو queued، والإغلاق هنا مرحلي للمصادر المسجلة لا ادعاء بأنه تم تمثيل كل كتاب كاملًا.

### آخر دفعة مصدرية كبيرة قبل المراجعة

أضيف `dict-taj-al-arus` كمصدر معجمي رابع synthesized بدل بقاء raw شاهد Internet Archive غير مسجل. استُخدم الشاهد الكبير `taga07_202001` المحفوظ محليًا (`data/raw/dict-taj-al-arus.ia.pdf`، و`data/raw/dict-taj-al-arus.ia-djvu.txt`، و`data/raw/dict-taj-al-arus.ia-djvu.xml`، و`data/raw/dict-taj-al-arus.ia-scandata.xml`) لا ملفات wikitext الصغيرة ولا فهرسًا. استُخرج نطاق متصل من DjVuXML عبر الأوراق/OBJECTs 370-412، أي نحو 43 ورقة مصدرية من محتوى معجمي حقيقي، ثم صيغ منه ملف OCR وسيط وملف اختيار عملي محافظ، وتحوّل إلى حزمتين Markdown: واحدة عن الأبد/الأحد/الأكيد/الأمد، والثانية عن الأيد/أبجد/لا بد/التبدد/البرد. وبذلك صارت كل المصادر المسجلة حاليًا في السجل synthesized.

### أمثلة مرجعية مكتملة يمكن القياس عليها

Source ids:

- `dict-mukhtar-al-sihah`
- `dict-taj-al-arus`
- `grammar-style-kitab`
- `reference-adab-al-katib`
- `reference-al-bayan-wa-al-tabyin`

Representative artifacts:

- `data/markdown/dict-mukhtar-al-sihah-complete-writing-foundations.md`
- `data/markdown/dict-taj-al-arus-old-inheritance-denial-and-clear-paths.md`
- `data/markdown/dict-taj-al-arus-stripping-clarity-and-separate-remnants.md`
- `data/markdown/grammar-style-khasais-language-variation-and-usage-authority.md`
- `data/markdown/grammar-style-khasais-samaa-qiyas-and-apparent-exceptions.md`
- `data/markdown/grammar-style-kitab-part-four-ibtida-inna-and-kam.md`
- `data/markdown/grammar-style-kitab-part-four-negation-exception-pronouns.md`
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

### ما يزال محتاجًا إلى استكمال لاحقًا

- OCR/bootstrap is not yet formalized into repo scripts, لكن لا تجعل ذلك أولوية إلا إذا خدم دفعة مصدرية كبيرة جديدة.
- لا توجد بعد حزمة إصدار أو packaging للمكتبة؛ المشروع في هذه المرحلة corpus مرجعي لا مكتبة برمجية منشورة.
- التغطية داخل كل كتاب أو ديوان ما تزال جزئية في معظم المصادر، وإن كان مسار raw/text/markdown مكتملًا لكل مصدر مسجل.
- أي نقص لاحق ينبغي أن يُعالج بإضافة نطاقات مصدرية كبيرة لا بتعديلات تجميلية صغيرة.

## الخطوة التالية المقترحة

Best next concrete task:

1. إذا كان المطلوب استمرار التوسيع، فأضف مصدرًا أو نطاقًا جديدًا كبيرًا وفق ترتيب يحدده `docs/MASTER_EXECUTION_CHECKLIST.md` بعد مرحلة الإغلاق، لا تعد إلى تلميع الحزم الحالية إلا عند ظهور خلل محدد. آخر توسيع كان نحويًا/أسلوبيًا في `الخصائص`، لذلك يُفضّل أن تكون الدفعة التالية معجمية كبيرة غير ملاصقة مباشرة أو مرجعية/بلاغية واسعة إذا اقتضى التخطيط، حتى لا يتكرر العمل على المصدر نفسه مباشرة.
2. اجعل أي توسعة لاحقة raw/text/markdown كاملة في نفس الدفعة، مع تحديث السجل والمذكرة.
3. حافظ على قاعدة الحجم: نحو ملف Markdown واحد لكل ~20 صفحة/ورقة، مع تجنب تفتيت المصدر الصغير.
4. شغّل فحصي السجل بعد أي تغيير.

Why this is the best next step:

- المراجعة النهائية أغلقت Phase 6 للمصادر المسجلة حاليًا.
- إعادة صياغة الحزم الحالية بلا مصدر جديد ستكون أقرب إلى churn تجميلي.
- القيمة التالية ستكون في توسيع corpus بمادة كبيرة جديدة أو في معالجة خلل موثق إن ظهر.

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
