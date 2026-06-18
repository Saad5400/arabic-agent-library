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

- 26 total source entries
- categories covered: dictionary, rhetoric, grammar-style, reference, poetry
- 26 sources are currently `synthesized`
- 0 sources remain `candidate`
- 0 sources remain `queued`
- 191 final Markdown packs, excluding `data/markdown/_template.md`
- 108 text artifacts under `data/text/`, excluding `.gitkeep`
- 73 raw artifacts under `data/raw/`, excluding `.gitkeep`

### أحدث إنجاز مصدري بعد الإغلاق المرحلي

وُسِّع `معجم مقاييس اللغة` لابن فارس بدفعة معجمية سادسة كبيرة غير مكررة من شاهد Internet Archive الكبير نفسه `20220809_Makaislugha`: استُخرجت الأوراق/OBJECTs 556-655، أي 100 ورقة إضافية متصلة تلي نطاق 456-555 مباشرة، وتختم قطاعًا واسعًا من الشين ثم تغطي الصاد والضاد والطاء والظاء وافتتاح العين. الخام الكبير المعتمد محفوظ سابقًا في `data/raw/dict-maqayis-al-lugha.ia-djvu.xml` بحجم 33,729,915 bytes مع DjVuTXT وscandata؛ وأُنتج OCR وسيط جديد `data/text/dict-maqayis-al-lugha-leaves-556-655-ocr-extract.txt` حجمه 377,705 bytes / نحو 210,812 حرفًا، وtext عملي جديد `data/text/dict-maqayis-al-lugha-leaves-556-655-writing-selection.txt`، ثم النص الجامع المعتمد `data/text/dict-maqayis-al-lugha-leaves-56-655-writing-selection.txt`. أضيفت خمس حزم Markdown عريضة: `data/markdown/dict-maqayis-al-lugha-shin-sad-raising-support-conflict-and-resistance.md`، و`data/markdown/dict-maqayis-al-lugha-sad-firmness-polish-aim-and-color.md`، و`data/markdown/dict-maqayis-al-lugha-document-truth-patience-joining-and-loss.md`، و`data/markdown/dict-maqayis-al-lugha-narrowness-harm-magnitude-measure-and-purity.md`، و`data/markdown/dict-maqayis-al-lugha-folding-nature-path-injustice-and-evidence.md`. صار مجموع تغطية `مقاييس اللغة` نحو 600 ورقة وتسعًا وعشرين حزمة، وهو مناسب لقاعدة ~ملف لكل 20 صفحة/ورقة.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

وُسِّع `الصحاح تاج اللغة وصحاح العربية` للجوهري بدفعة معجمية سابعة كبيرة غير مكررة من شاهد Internet Archive الكبير نفسه `civ-7220`: استُخرجت الأوراق/OBJECTs 740-859، أي 120 ورقة إضافية متصلة تلي نطاق 620-739 مباشرة، من تتمة حرف العين وافتتاح حرف الغين. الخام الكبير المعتمد محفوظ سابقًا في `data/raw/dict-al-sihah-al-jawhari.ia-djvu.xml` بحجم 47,839,854 bytes مع DjVuTXT وscandata؛ وأُنتج OCR وسيط جديد `data/text/dict-al-sihah-al-jawhari-leaves-740-859-ocr-extract.txt` حجمه 568,572 bytes، وtext عملي جديد `data/text/dict-al-sihah-al-jawhari-leaves-740-859-writing-selection.txt`، ثم النص الجامع المعتمد `data/text/dict-al-sihah-al-jawhari-leaves-20-859-writing-selection.txt`. أضيفت ست حزم Markdown عريضة: `data/markdown/dict-al-sihah-al-jawhari-adad-adl-udhr-and-responsibility.md`، و`data/markdown/dict-al-sihah-al-jawhari-arabicization-presentation-and-opposition.md`، و`data/markdown/dict-al-sihah-al-jawhari-urf-irq-hardship-and-cohesion.md`، و`data/markdown/dict-al-sihah-al-jawhari-support-consequence-reason-and-work.md`، و`data/markdown/dict-al-sihah-al-jawhari-covenant-return-benefit-and-defect.md`، و`data/markdown/dict-al-sihah-al-jawhari-ghadaq-strangeness-severity-and-obscurity.md`. صار مجموع تغطية `الصحاح` نحو 840 ورقة واثنتين وأربعين حزمة، وهو مناسب لقاعدة ~ملف لكل 20 صفحة/ورقة.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

وُسِّع `شرح شذور الذهب في معرفة كلام العرب` لابن هشام بدفعة نحوية/أسلوبية رابعة كبيرة غير مكررة من شاهد Internet Archive الكبير نفسه `hm4337`: استُخرجت الأوراق/OBJECTs 330-404، أي نحو 75 ورقة إضافية متصلة تلي نطاق 230-329 وقبل الفهارس العامة، وتغطي تتمة عمل الفعل، والأسماء التي تعمل عمل الفعل، والمصدر واسم الفاعل وصيغ المبالغة والصفة المشبهة، واسم الفعل، وأفعال التعجب، والتنازع، والتوابع، وموانع الصرف، والعدد. الخام الكبير المعتمد محفوظ سابقًا في `data/raw/grammar-style-sharh-shudhur-al-dhahab.ia-djvu.xml` بحجم 13,933,142 bytes مع DjVuTXT وscandata؛ وأُنتج OCR وسيط جديد `data/text/grammar-style-sharh-shudhur-al-dhahab-leaves-330-404-ocr-extract.txt` حجمه 218,938 bytes، وtext عملي جديد `data/text/grammar-style-sharh-shudhur-al-dhahab-leaves-330-404-writing-foundations.txt`، ثم النص الجامع المعتمد `data/text/grammar-style-sharh-shudhur-al-dhahab-leaves-30-404-writing-foundations.txt`. أضيفت أربع حزم Markdown عريضة: `data/markdown/grammar-style-sharh-shudhur-al-dhahab-action-nouns-and-working-descriptions.md`، و`data/markdown/grammar-style-sharh-shudhur-al-dhahab-verb-nouns-exclamation-and-tanazu.md`، و`data/markdown/grammar-style-sharh-shudhur-al-dhahab-tawabi-paragraph-control.md`، و`data/markdown/grammar-style-sharh-shudhur-al-dhahab-diptotes-and-number-editing.md`. صار مجموع تغطية `شرح شذور الذهب` نحو 375 ورقة وتسع عشرة حزمة، وهو مناسب لقاعدة ~ملف لكل 20 صفحة/ورقة.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

وُسِّع `الصحاح تاج اللغة وصحاح العربية` للجوهري بدفعة معجمية سادسة كبيرة غير مكررة من شاهد Internet Archive الكبير نفسه `civ-7220`: استُخرجت الأوراق/OBJECTs 620-739، أي 120 ورقة إضافية متصلة تلي نطاق 500-619 مباشرة، من أواخر الشين، وحرف الصاد، وحرف الضاد، وحرف الطاء، وحرف الظاء، وافتتاح حرف العين حتى مادة عدا. الخام الكبير المعتمد محفوظ سابقًا في `data/raw/dict-al-sihah-al-jawhari.ia-djvu.xml` بحجم 47,839,854 bytes مع DjVuTXT وscandata؛ وأُنتج OCR وسيط جديد `data/text/dict-al-sihah-al-jawhari-leaves-620-739-ocr-extract.txt` حجمه 552,080 bytes، وtext عملي جديد `data/text/dict-al-sihah-al-jawhari-leaves-620-739-writing-selection.txt`، ثم النص الجامع المعتمد `data/text/dict-al-sihah-al-jawhari-leaves-20-739-writing-selection.txt`. أضيفت ست حزم Markdown عريضة: `data/markdown/dict-al-sihah-al-jawhari-shura-sabr-and-sidq-foundations.md`، و`data/markdown/dict-al-sihah-al-jawhari-saraa-salat-sawab-and-isaba.md`، و`data/markdown/dict-al-sihah-al-jawhari-dafw-dafr-and-tadmin.md`، و`data/markdown/dict-al-sihah-al-jawhari-tabaa-taste-path-and-fit.md`، و`data/markdown/dict-al-sihah-al-jawhari-atwar-tawah-and-transition.md`، و`data/markdown/dict-al-sihah-al-jawhari-zama-zulm-atiq-and-udwan.md`. صار مجموع تغطية `الصحاح` نحو 720 ورقة وستًا وثلاثين حزمة، وهو مناسب لقاعدة ~ملف لكل 20 صفحة/ورقة.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

وُسِّع `القاموس المحيط` للفيروزآبادي بدفعة معجمية جديدة غير مكررة من شاهد Internet Archive/Shamela الكبير نفسه `2315Htm`: استُخرج باب الجيم من نحو (1/178) إلى قبل باب الحاء نحو (1/211)، أي قرابة 34 صفحة مطبوعة من HTML الخام الكبير `data/raw/dict-al-qamus-al-muhit-shamela.html` المحفوظ سابقًا بحجم 9,197,314 bytes. أُنتج cleaned range جديد `data/text/dict-al-qamus-al-muhit-shamela-bab-al-jim-ocr-cleaned.txt` حجمه 205,853 bytes، واختيار عملي `data/text/dict-al-qamus-al-muhit-bab-al-jim-writing-selection.txt`، ثم نص جامع مع باب الباء `data/text/dict-al-qamus-al-muhit-bab-al-ba-jim-writing-selection.txt`. أضيفت حزمتا Markdown عريضتان: `data/markdown/dict-al-qamus-al-muhit-jim-appearance-path-and-mixture.md` و`data/markdown/dict-al-qamus-al-muhit-jim-motion-sound-and-maturity.md`. صار مجموع `القاموس المحيط` نحو 156 صفحة مطبوعة من بابي الباء والجيم، ومع الطبقة الأولى نحو 184-204 صفحة عملية وتسع حزم، وهو مناسب لقاعدة ~ملف لكل 20 صفحة.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

وُسِّع `معجم مقاييس اللغة` لابن فارس بدفعة معجمية رابعة كبيرة من شاهد Internet Archive الكبير نفسه `20220809_Makaislugha`: استُخرجت الأوراق/OBJECTs 356-455، أي 100 ورقة إضافية متصلة من ختام الخاء، وكتاب الدال، وكتاب الذال، وافتتاح كتاب الراء. الخام الكبير المعتمد محفوظ سابقًا في `data/raw/dict-maqayis-al-lugha.ia-djvu.xml` بحجم 33,729,915 bytes مع DjVuTXT وscandata؛ وأُنتج OCR وسيط جديد `data/text/dict-maqayis-al-lugha-leaves-356-455-ocr-extract.txt` حجمه 396,047 bytes / 220,033 حرفًا، وtext عملي جديد `data/text/dict-maqayis-al-lugha-leaves-356-455-writing-selection.txt`، ثم النص الجامع المعتمد `data/text/dict-maqayis-al-lugha-leaves-56-455-writing-selection.txt`. أضيفت خمس حزم Markdown عريضة: `data/markdown/dict-maqayis-al-lugha-kha-to-dal-confusion-pushing-and-calling.md`، و`data/markdown/dict-maqayis-al-lugha-nearness-proof-slipping-and-hidden-flaw.md`، و`data/markdown/dict-maqayis-al-lugha-dhal-to-ra-humility-intellect-and-loss.md`، و`data/markdown/dict-maqayis-al-lugha-rasl-rasm-rifq-composition-and-symbol.md`، و`data/markdown/dict-maqayis-al-lugha-narration-adornment-binding-and-return.md`. صار مجموع تغطية `مقاييس اللغة` نحو 400 ورقة وتسع عشرة حزمة، وهو مناسب لقاعدة ~ملف لكل 20 صفحة/ورقة.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

وُسِّع `الصحاح تاج اللغة وصحاح العربية` للجوهري بدفعة معجمية خامسة كبيرة من شاهد Internet Archive الكبير نفسه `civ-7220`: استُخرجت الأوراق/OBJECTs 500-619، أي 120 ورقة إضافية متصلة من أواخر الزاي، وقطاع واسع من حرف السين، وبدايات حرف الشين حتى مواد الشهادة والشهرة. الخام الكبير المعتمد محفوظ سابقًا في `data/raw/dict-al-sihah-al-jawhari.ia-djvu.xml` بحجم 47,839,854 bytes مع DjVuTXT وscandata؛ وأُنتج OCR وسيط جديد `data/text/dict-al-sihah-al-jawhari-leaves-500-619-ocr-extract.txt` حجمه 564,860 bytes / 318,165 حرفًا، وtext عملي جديد `data/text/dict-al-sihah-al-jawhari-leaves-500-619-writing-selection.txt`، ثم النص الجامع المعتمد `data/text/dict-al-sihah-al-jawhari-leaves-20-619-writing-selection.txt`. أضيفت ست حزم Markdown عريضة: `data/markdown/dict-al-sihah-al-jawhari-zuhd-zawal-question-and-request.md`، و`data/markdown/dict-al-sihah-al-jawhari-sabk-sijil-sijal-and-sadad.md`، و`data/markdown/dict-al-sihah-al-jawhari-say-sam-sumuk-and-reputation.md`، و`data/markdown/dict-al-sihah-al-jawhari-tashabbuth-branches-and-dispersal.md`، و`data/markdown/dict-al-sihah-al-jawhari-desire-brilliance-and-shihab.md`، و`data/markdown/dict-al-sihah-al-jawhari-testimony-witness-fame-and-observation.md`. صار مجموع تغطية `الصحاح` نحو 600 ورقة وثلاثين حزمة، وهو مناسب لقاعدة ~ملف لكل 20 صفحة/ورقة.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

وُسِّع `شرح شذور الذهب في معرفة كلام العرب` لابن هشام بدفعة نحوية/أسلوبية كبيرة من شاهد Internet Archive الكبير نفسه `hm4337`: استُخرجت الأوراق/OBJECTs 130-229، أي 100 ورقة إضافية متصلة تلي نطاق الأوراق 30-129 السابق. الخام الكبير المعتمد محفوظ سابقًا في `data/raw/grammar-style-sharh-shudhur-al-dhahab.ia-djvu.xml` بحجم 13,933,142 bytes مع DjVuTXT وscandata؛ وأُنتج OCR وسيط جديد `data/text/grammar-style-sharh-shudhur-al-dhahab-leaves-130-229-ocr-extract.txt` حجمه 299,196 bytes، وtext عملي جديد `data/text/grammar-style-sharh-shudhur-al-dhahab-leaves-130-229-writing-foundations.txt`، ثم النص الجامع المعتمد `data/text/grammar-style-sharh-shudhur-al-dhahab-leaves-30-229-writing-foundations.txt`. أضيفت خمس حزم Markdown عريضة: `data/markdown/grammar-style-sharh-shudhur-al-dhahab-definiteness-praise-and-reference.md`، و`data/markdown/grammar-style-sharh-shudhur-al-dhahab-agent-passive-and-agreement.md`، و`data/markdown/grammar-style-sharh-shudhur-al-dhahab-mubtada-predicate-and-nawasikh.md`، و`data/markdown/grammar-style-sharh-shudhur-al-dhahab-objects-ishtighal-and-absolute-object.md`، و`data/markdown/grammar-style-sharh-shudhur-al-dhahab-cause-comitative-and-hal.md`. صار مجموع تغطية `شرح شذور الذهب` نحو 200 ورقة وعشر حزم، وهو مناسب لقاعدة ~ملف لكل 20 صفحة/ورقة.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

وُسِّع `القاموس المحيط` للفيروزآبادي بدفعة معجمية كبيرة من شاهد Internet Archive/Shamela `2315Htm`: حُفظ ZIP خام `data/raw/dict-al-qamus-al-muhit-shamela-html.zip` بحجم 2,067,930 bytes واستُخرج HTML UTF-8 `data/raw/dict-al-qamus-al-muhit-shamela.html` بحجم 9,197,314 bytes. استُخرج باب الباء كاملًا تقريبًا من نحو (1/57) إلى قبل باب الجيم نحو (1/178)، أي قرابة 122 صفحة مطبوعة، في `data/text/dict-al-qamus-al-muhit-shamela-bab-al-ba-ocr-cleaned.txt` حجمه 794,526 bytes، ثم صيغ اختيار عملي `data/text/dict-al-qamus-al-muhit-bab-al-ba-writing-selection.txt` من 18 محورًا. أضيفت ست حزم Markdown عريضة: `data/markdown/dict-al-qamus-al-muhit-adab-irb-and-lexical-method.md`، و`data/markdown/dict-al-qamus-al-muhit-return-readiness-and-mobilization.md`، و`data/markdown/dict-al-qamus-al-muhit-calculation-sufficiency-and-veils.md`، و`data/markdown/dict-al-qamus-al-muhit-seeking-dominance-and-nearness.md`، و`data/markdown/dict-al-qamus-al-muhit-writing-monitoring-lineage-and-reproach.md`، و`data/markdown/dict-al-qamus-al-muhit-truth-obligation-and-recommendation.md`. صار مجموع `القاموس المحيط` سبع حزم تغطي الطبقة الأولى وباب الباء الواسع، وهو مناسب تقريبًا لقاعدة ~ملف لكل 20 صفحة.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

وُسِّع `معجم مقاييس اللغة` لابن فارس بدفعة معجمية ثالثة كبيرة من شاهد Internet Archive الكبير نفسه `20220809_Makaislugha`: استُخرجت الأوراق/OBJECTs 256-355، أي 100 ورقة إضافية من تتمة الحاء إلى أوائل الخاء. raw الشاهد الكبير محفوظ سابقًا في `data/raw/dict-maqayis-al-lugha.ia-djvu.xml` بحجم 33,729,915 bytes مع DjVuTXT وscandata؛ وأُنتج OCR وسيط جديد `data/text/dict-maqayis-al-lugha-leaves-256-355-ocr-extract.txt` حجمه 384,711 bytes / 213,789 حرفًا، وtext عملي `data/text/dict-maqayis-al-lugha-leaves-256-355-writing-selection.txt`، ثم النص الجامع المعتمد `data/text/dict-maqayis-al-lugha-leaves-56-355-writing-selection.txt`. أضيفت خمس حزم Markdown عريضة: `data/markdown/dict-maqayis-al-lugha-haq-hall-hajj-guarded-boundaries.md`، و`data/markdown/dict-maqayis-al-lugha-hasr-hifz-hukm-hilm-hamd.md`، و`data/markdown/dict-maqayis-al-lugha-haml-hawl-hayat-habl-hajar.md`، و`data/markdown/dict-maqayis-al-lugha-kha-beginnings-deception-loss-humility-dispute.md`، و`data/markdown/dict-maqayis-al-lugha-kha-completion-purity-succession-goodness.md`. صار مجموع تغطية `مقاييس اللغة` نحو 300 ورقة وأربع عشرة حزمة، وهو مناسب لقاعدة ~ملف لكل 20 صفحة/ورقة.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

وُسِّع `الصحاح تاج اللغة وصحاح العربية` للجوهري بدفعة معجمية رابعة كبيرة من شاهد Internet Archive الكبير نفسه `civ-7220`: استُخرجت الأوراق/OBJECTs 380-499، أي 120 ورقة إضافية من أواخر الدال، وحرف الذال، وقطاع واسع من الراء حتى أوائل الزاي. raw الشاهد الكبير محفوظ سابقًا في `data/raw/dict-al-sihah-al-jawhari.ia-djvu.xml` بحجم 47,839,854 bytes مع DjVuTXT وscandata؛ وأُنتج OCR وسيط جديد `data/text/dict-al-sihah-al-jawhari-leaves-380-499-ocr-extract.txt` حجمه 567,404 bytes، وtext عملي `data/text/dict-al-sihah-al-jawhari-leaves-380-499-writing-selection.txt`، ثم النص الجامع المعتمد `data/text/dict-al-sihah-al-jawhari-leaves-20-499-writing-selection.txt`. أضيفت ست حزم Markdown: `data/markdown/dict-al-sihah-al-jawhari-extraction-signification-and-softness.md`، و`data/markdown/dict-al-sihah-al-jawhari-calamity-cunning-darkness-and-turning.md`، و`data/markdown/dict-al-sihah-al-jawhari-sharpness-means-and-ethical-bonds.md`، و`data/markdown/dict-al-sihah-al-jawhari-linking-returning-refutation-and-breadth.md`، و`data/markdown/dict-al-sihah-al-jawhari-value-provision-guidance-and-consent.md`، و`data/markdown/dict-al-sihah-al-jawhari-patching-composition-narration-and-control.md`. صار مجموع تغطية `الصحاح` نحو 480 ورقة وأربعًا وعشرين حزمة، وهو مناسب لقاعدة ~ملف لكل 20 صفحة/ورقة.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

وُسِّع `لسان العرب` بدفعة معجمية جديدة من متن ويكي مصدر الحقيقي لا من صفحة الفهرس: جُمعت خمس صفحات فعلية من التاء والحاء (`تا-تبع`، `تبك-`، `حاء-`، `حبل -`، `حثلم-`) في raw واحد `data/raw/dict-lisan-al-arab-ta-ha-cluster-writing-foundations.wikitext.txt` حجمه 1,224,148 bytes / 670,388 حرفًا. استُخرج text عملي `data/text/dict-lisan-al-arab-ta-ha-cluster-foundational-roots.txt` من 20 جذرًا يخدم البحث والتوثيق والحجاج والسبك والحكم (`تبع`، `حجب`، `حسب`، `حدث`، `حجج`، `حبل`، `حصل`، `حفل`، `حلل`، `حمل`، `حول`، `حال`، `حجم`، `حزم`، `حسم`، `حكم`، `حلم`، `حسن`، `حصن`، `حنن`). أضيفت وحدة عريضة واحدة إلى الملف الموحد `data/markdown/dict-lisan-al-arab-complete-writing-foundations.md` بدل إنشاء ملفات صغيرة؛ فالدفعة قليلة الصفحات عددًا لكنها كبيرة الحجم وغنية الجذور، والإبقاء على Markdown واحد لهذا المصدر يراعي قاعدة عدم التفتيت. هذا العمل يؤكد مرة أخرى أن `data/raw/dict-lisan-al-arab.wikitext.txt` القديم فهرس فقط، وأن التوسعات المعتمدة الآن مبنية على محتوى معجمي حقيقي.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

وُسِّع `معجم مقاييس اللغة` لابن فارس بدفعة معجمية ثانية كبيرة غير مكررة: استُخرج نطاق متصل جديد من شاهد Internet Archive الكبير `20220809_Makaislugha` نفسه، الأوراق/OBJECTs 156-255، أي 100 ورقة إضافية من أواخر الباء، وكتاب التاء، وكتاب الثاء، وبداية كتاب الجيم حتى افتتاح الحاء. raw الشاهد الكبير محفوظ في `data/raw/dict-maqayis-al-lugha.ia-djvu.xml` بحجم 33,729,915 bytes مع DjVuTXT وscandata؛ أُنتج OCR وسيط جديد `data/text/dict-maqayis-al-lugha-leaves-156-255-ocr-extract.txt` بحجم 380,254 bytes، ثم text عملي جامع للأوراق 56-255 في `data/text/dict-maqayis-al-lugha-leaves-56-255-writing-selection.txt`. أضيفت خمس حزم Markdown: `data/markdown/dict-maqayis-al-lugha-late-ba-distance-partition-and-disclosure.md`، و`data/markdown/dict-maqayis-al-lugha-ta-completion-following-and-return.md`، و`data/markdown/dict-maqayis-al-lugha-tha-density-weight-penetration-and-fixity.md`، و`data/markdown/dict-maqayis-al-lugha-jim-roots-injury-acquisition-and-recompense.md`، و`data/markdown/dict-maqayis-al-lugha-jim-collection-clarity-generosity-and-boundary.md`. صار مجموع تغطية `مقاييس اللغة` نحو 200 ورقة وتسع حزم، وهو مناسب لقاعدة ~ملف لكل 20 صفحة/ورقة.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

وُسِّع `الصحاح تاج اللغة وصحاح العربية` للجوهري بدفعة معجمية ثالثة كبيرة غير مكررة بعد دفعة `شرح شذور الذهب`: استُخرج نطاق متصل جديد من شاهد Internet Archive الكبير `civ-7220` نفسه، الأوراق/OBJECTs 260-379، أي 120 ورقة مصدرية إضافية من تتمة الحاء، وحرف الخاء، وبداية حرف الدال. raw الشاهد الكبير محفوظ في `data/raw/dict-al-sihah-al-jawhari.ia-djvu.xml` بحجم 47,839,854 bytes مع DjVuTXT وscandata؛ أُنتج OCR وسيط جديد `data/text/dict-al-sihah-al-jawhari-leaves-260-379-ocr-extract.txt` بحجم نحو 554 كيلوبايت، وtext عملي `data/text/dict-al-sihah-al-jawhari-leaves-260-379-writing-selection.txt`، ثم النص الجامع المعتمد `data/text/dict-al-sihah-al-jawhari-leaves-20-379-writing-selection.txt`. أضيفت ست حزم Markdown: `data/markdown/dict-al-sihah-al-jawhari-right-judgment-preservation-and-solution.md`، و`data/markdown/dict-al-sihah-al-jawhari-protection-zeal-state-and-life.md`، و`data/markdown/dict-al-sihah-al-jawhari-hidden-news-ending-and-abandonment.md`، و`data/markdown/dict-al-sihah-al-jawhari-order-roughness-restraint-and-hiddenness.md`، و`data/markdown/dict-al-sihah-al-jawhari-difference-friendship-choice-and-goodness.md`، و`data/markdown/dict-al-sihah-al-jawhari-persistence-movement-refutation-and-intrusion.md`. صار مجموع تغطية `الصحاح` نحو 360 ورقة وثماني عشرة حزمة، وهو مناسب لقاعدة ~ملف لكل 20 صفحة/ورقة.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

أضيف `شرح شذور الذهب في معرفة كلام العرب` لابن هشام كمصدر نحوي/أسلوبي تأسيسي جديد غير مكرر بعد توسعة `الصحاح` المعجمية: حُفظ شاهد Internet Archive الكبير `hm4337` في `data/raw/grammar-style-sharh-shudhur-al-dhahab.ia-djvu.txt` بحجم 1,517,945 bytes، و`data/raw/grammar-style-sharh-shudhur-al-dhahab.ia-djvu.xml` بحجم 13,933,142 bytes، و`data/raw/grammar-style-sharh-shudhur-al-dhahab.ia-scandata.xml`. استُخرج نطاق واسع من الأوراق/OBJECTs 30-129، أي نحو 100 ورقة مصدرية رقمية من أوائل متن الشرح، في `data/text/grammar-style-sharh-shudhur-al-dhahab-leaves-30-129-ocr-extract.txt`، ثم صيغ text عملي محافظ في `data/text/grammar-style-sharh-shudhur-al-dhahab-leaves-30-129-writing-foundations.txt`. أُنتجت خمس حزم Markdown: `data/markdown/grammar-style-sharh-shudhur-al-dhahab-word-classes-and-writing-diagnosis.md`، و`data/markdown/grammar-style-sharh-shudhur-al-dhahab-verb-tests-tense-and-command.md`، و`data/markdown/grammar-style-sharh-shudhur-al-dhahab-particles-linking-and-meaning-relations.md`، و`data/markdown/grammar-style-sharh-shudhur-al-dhahab-irab-agency-and-ambiguity-control.md`، و`data/markdown/grammar-style-sharh-shudhur-al-dhahab-bina-pronouns-and-reference.md`. هذه دفعة grammar/style foundations واسعة من مصدر جديد، وخمس الحزم مبررة لأن النطاق 100 ورقة وتجنبت تفتيت أبواب صغيرة.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

وُسِّع `الصحاح تاج اللغة وصحاح العربية` للجوهري بدفعة معجمية ثانية كبيرة غير مكررة بعد دفعة `شرح درة الغواص`: استُخرج نطاق متصل جديد من شاهد Internet Archive الكبير `civ-7220` نفسه، الأوراق/OBJECTs 140-259، أي 120 ورقة مصدرية إضافية من آخر التاء، وحرف الثاء، وكتلة واسعة من الجيم، وبداية الحاء حتى الحضور والحاضرة. raw الشاهد الكبير كان محفوظًا في `data/raw/dict-al-sihah-al-jawhari.ia-djvu.xml` بحجم 47,839,854 bytes مع DjVuTXT وscandata؛ أُنتج OCR وسيط جديد `data/text/dict-al-sihah-al-jawhari-leaves-140-259-ocr-extract.txt` بحجم نحو 541 كيلوبايت، وtext عملي `data/text/dict-al-sihah-al-jawhari-leaves-140-259-writing-selection.txt`، ثم النص الجامع المعتمد `data/text/dict-al-sihah-al-jawhari-leaves-20-259-writing-selection.txt`. أضيفت ست حزم Markdown: `data/markdown/dict-al-sihah-al-jawhari-fixity-number-and-rank.md`، و`data/markdown/dict-al-sihah-al-jawhari-repair-nature-roots-and-cutting.md`، و`data/markdown/dict-al-sihah-al-jawhari-flow-parts-testing-and-sufficiency.md`، و`data/markdown/dict-al-sihah-al-jawhari-roughness-clarity-endurance-and-dignity.md`، و`data/markdown/dict-al-sihah-al-jawhari-collection-classification-effort-and-ignorance.md`، و`data/markdown/dict-al-sihah-al-jawhari-answer-quality-justice-limits-and-presence.md`. صار مجموع تغطية `الصحاح` نحو 240 ورقة واثنتي عشرة حزمة، وهو مناسب لقاعدة ~ملف لكل 20 صفحة/ورقة.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

أضيف `شرح درة الغواص في أوهام الخواص` للخفاجي على درة الحريري كمصدر نحوي/أسلوبي وتصحيحي جديد غير مكرر بعد دفعة `الصحاح` المعجمية: حُفظ شاهد Internet Archive/Shamela HTML الكبير `4616Htm` في `data/raw/grammar-style-sharh-durrat-al-ghawwas-html.zip` بحجم 278,678 bytes، واستُخرج منه `data/raw/grammar-style-sharh-durrat-al-ghawwas.html` بحجم نحو 783,800 حرف، ثم نُظف كاملًا في `data/text/grammar-style-sharh-durrat-al-ghawwas-complete-cleaned.txt`. اختير نطاق المسائل [1]-[25] في `data/text/grammar-style-sharh-durrat-al-ghawwas-issues-1-25-writing-selection.txt`، من `سائر` إلى التعجب من الألوان والعاهات، ويقابل تقريبًا صفحات 46-159، أي نحو 114 صفحة مصدرية. أُنتجت ست حزم Markdown: `data/markdown/grammar-style-sharh-durrat-al-ghawwas-quantity-sequence-and-time.md`، و`data/markdown/grammar-style-sharh-durrat-al-ghawwas-comparison-eligibility-and-diminution.md`، و`data/markdown/grammar-style-sharh-durrat-al-ghawwas-night-motion-fixed-usage-and-adverbs.md`، و`data/markdown/grammar-style-sharh-durrat-al-ghawwas-naming-transitivity-attribution-and-sending.md`، و`data/markdown/grammar-style-sharh-durrat-al-ghawwas-warning-place-and-color-forms.md`، و`data/markdown/grammar-style-sharh-durrat-al-ghawwas-coordination-hal-raja-and-exclamation.md`. هذه دفعة grammar/style foundations واسعة لتصحيح أوهام الخواص في الألفاظ والتراكيب، وست الحزم مبررة لأن النطاق نحو 114 صفحة وتجنبت تفتيت المسائل إلى ملفات صغيرة.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

أضيف `الصحاح تاج اللغة وصحاح العربية` للجوهري كمصدر معجمي تأسيسي جديد غير مكرر بعد دفعة `الجمل في النحو` النحوية: حُفظ شاهد Internet Archive الكبير `civ-7220` في `data/raw/dict-al-sihah-al-jawhari.ia-djvu.txt` بحجم 6,023,564 bytes، و`data/raw/dict-al-sihah-al-jawhari.ia-djvu.xml` بحجم 47,839,854 bytes، و`data/raw/dict-al-sihah-al-jawhari.ia-scandata.xml`. استُخرج نطاق OCR واسع من الأوراق/OBJECTs 20-139 في `data/text/dict-al-sihah-al-jawhari-leaves-20-139-ocr-extract.txt`، ثم صيغ text عملي محافظ في `data/text/dict-al-sihah-al-jawhari-leaves-20-139-writing-selection.txt`، أي 120 ورقة مصدرية من افتتاح حرف الألف وبداية حرف الباء. أُنتجت ست حزم Markdown: `data/markdown/dict-al-sihah-al-jawhari-motion-origin-and-adab.md`، و`data/markdown/dict-al-sihah-al-jawhari-security-familiarity-and-community.md`، و`data/markdown/dict-al-sihah-al-jawhari-particles-linking-and-warning.md`، و`data/markdown/dict-al-sihah-al-jawhari-initiative-substitution-and-clearance.md`، و`data/markdown/dict-al-sihah-al-jawhari-expansion-invalidity-interiority-and-settlement.md`، و`data/markdown/dict-al-sihah-al-jawhari-morphology-attribution-and-witness-limits.md`. هذه دفعة dictionary foundations واسعة من مصدر جديد، لا تكرار لدفعة `الجمل`؛ ست الحزم مبررة لأن النطاق 120 ورقة وتجنبت تفتيت الجذور إلى ملفات صغيرة.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

أضيف `الجمل في النحو` كمصدر نحوي/أسلوبي تأسيسي جديد غير مكرر بعد دفعة `شرح قطر الندى`: جُمعت ثماني عشرة صفحة فعلية من ويكي مصدر في raw واحد `data/raw/grammar-style-al-jumal-fi-al-nahw-core-pages.wikitext.txt` حجمه 311,736 bytes وفيه نحو 25,181 تتابعًا عربيًا، تشمل المقدمة ووجوه الرفع والنصب والجزم والخفض وأبواب الحروف (`الألفات`، `التاءات`، `الواوات`، `اللامات`، `الباءات`، `الفاءات`، `النونات`، `الياءات`، `الهاءات`، و`لا`) وفصلي `أم/أو` و`رويد`. أُنتج النص العملي المحافظ `data/text/grammar-style-al-jumal-fi-al-nahw-core-pages-writing-foundations.txt`، ثم ثلاث حزم Markdown: `data/markdown/grammar-style-al-jumal-irab-map-and-case-governance.md`، و`data/markdown/grammar-style-al-jumal-particles-linking-and-meaning.md`، و`data/markdown/grammar-style-al-jumal-variant-readings-choice-and-editorial-judgment.md`. هذه دفعة grammar/style foundations واسعة من مصدر جديد لا تعيد تفصيل أبواب قطر الندى؛ تقديرها نحو 70-90 صفحة مكافئة، وثلاث الحزم مبررة تحت قاعدة ~ملف لكل 20 صفحة.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

أضيف `شرح قطر الندى وبل الصدى` كمصدر نحوي/أسلوبي تأسيسي جديد غير مكرر بعد دفعة `معجم مقاييس اللغة` المعجمية: حُفظ شاهد Internet Archive الكبير `AAlexandrina-007066` في `data/raw/grammar-style-sharh-qatr-al-nada.ia-djvu.txt` بحجم 1,408,058 bytes، و`data/raw/grammar-style-sharh-qatr-al-nada.ia-djvu.xml` بحجم 11,743,422 bytes، و`data/raw/grammar-style-sharh-qatr-al-nada.ia-scandata.xml`. استُخرج نطاق OCR واسع من الأوراق/OBJECTs 40-139 في `data/text/grammar-style-sharh-qatr-al-nada-leaves-40-139-ocr-extract.txt`، ثم صيغ text عملي من الأوراق 50-139 في `data/text/grammar-style-sharh-qatr-al-nada-leaves-50-139-writing-foundations.txt`، أي نحو 90 ورقة مصدرية رقمية. أُنتجت أربع حزم Markdown: `data/markdown/grammar-style-sharh-qatr-al-nada-word-classes-verb-and-particle-tests.md`، و`data/markdown/grammar-style-sharh-qatr-al-nada-five-nouns-plurals-and-five-verbs.md`، و`data/markdown/grammar-style-sharh-qatr-al-nada-mudari-nasb-jazm-and-condition.md`، و`data/markdown/grammar-style-sharh-qatr-al-nada-reference-definiteness-and-linking.md`. هذه دفعة grammar/style foundations واسعة من مصدر جديد، لا تكرار لدفعة ابن فارس؛ أربع الحزم مبررة لأن النطاق يقارب 90 ورقة وتجنبت تفتيت كل أداة أو باب صغير.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

أضيف `معجم مقاييس اللغة` لابن فارس كمصدر معجمي تأسيسي جديد غير مكرر بعد الدفعة النحوية في `شرح ابن عقيل`: حُفظ شاهد Internet Archive الكبير `20220809_Makaislugha` في `data/raw/dict-maqayis-al-lugha.ia-djvu.txt` بحجم 4,309,722 bytes، و`data/raw/dict-maqayis-al-lugha.ia-djvu.xml` بحجم 33,729,915 bytes، و`data/raw/dict-maqayis-al-lugha.ia-scandata.xml`. استُخرج نطاق متصل من DjVuXML عبر الأوراق/OBJECTs 56-155، أي نحو 100 ورقة مصدرية من افتتاح منهج ابن فارس وباب الهمزة وأوائل الباء، في OCR وسيط `data/text/dict-maqayis-al-lugha-leaves-56-155-ocr-extract.txt`، ثم صيغ text عملي `data/text/dict-maqayis-al-lugha-leaves-56-155-foundational-selection.txt`. أُنتجت أربع حزم Markdown: `data/markdown/dict-maqayis-al-lugha-roots-method-and-lexical-judgment.md`، و`data/markdown/dict-maqayis-al-lugha-time-effect-trust-and-adab.md`، و`data/markdown/dict-maqayis-al-lugha-taking-starting-substitution-and-invalidity.md`، و`data/markdown/dict-maqayis-al-lugha-dissemination-insight-building-and-reaching.md`. هذه دفعة dictionary foundations واسعة من مصدر جديد، لا تكرار لدفعة `شرح ابن عقيل`؛ أربع الحزم مبررة لأن النطاق يقارب 100 ورقة وتجنبت تفتيت الجذور إلى ملفات صغيرة.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

أضيف `شرح ابن عقيل على ألفية ابن مالك` كمصدر نحوي/أسلوبي تأسيسي جديد غير مكرر: جُمعت صفحات المجلد الأول الست المتاحة على ويكي مصدر (`الكلام وما يتألف منه`، `المعرب والمبني`، `النكرة والمعرفة`، `العلم`، `اسم الإشارة`، `الموصول`) في raw واحد `data/raw/grammar-style-sharh-ibn-aqil-volume-one-core-topics.wikitext.txt` حجمه 390,597 bytes، أي دفعة عريضة لا باب صغيرًا منفردًا. أُنتج النص العملي المنظف `data/text/grammar-style-sharh-ibn-aqil-volume-one-core-topics-foundations.txt` مع إبقاء ترتيب الأبواب وحدود التنظيف، ثم صيغت أربع حزم Markdown: `data/markdown/grammar-style-sharh-ibn-aqil-kalam-word-classes-and-sentence-minimum.md`، و`data/markdown/grammar-style-sharh-ibn-aqil-irab-bina-and-inflection-checks.md`، و`data/markdown/grammar-style-sharh-ibn-aqil-definiteness-pronouns-and-reference.md`، و`data/markdown/grammar-style-sharh-ibn-aqil-proper-nouns-demonstratives-and-relative-links.md`. تقدير الدفعة نحو 80-110 صفحات مكافئة، وأربع الحزم مبررة تحت قاعدة ~ملف لكل 20 صفحة لأنها تغطي بنية الكلام والإعراب والضمائر والربط، لا تفتيتًا ميكروسكوبيًا لموضع واحد.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

أضيف `إصلاح المنطق` لابن السكيت كمصدر نحوي/أسلوبي عملي جديد غير مكرر: حُفظت صفحة ويكي مصدر العربية الكاملة في raw واحد `data/raw/reference-islah-al-mantiq-complete.wikitext.txt` حجمه 902,857 bytes ونحو 79,205 تتابعات عربية، أي شاهد كامل كبير لا صفحة صغيرة ولا فهرسًا. أُنتج النص العملي المنظف `data/text/grammar-style-islah-al-mantiq-complete-cleaned.txt` بحجم 903,203 bytes مع إبقاء بنية الأبواب والتنبيه إلى أنه ليس تحقيقًا طباعيًا جديدًا. صيغت ثلاث حزم Markdown من اختيار عريض يقارب 60 صفحة ذات كثافة تحريرية عالية: `data/markdown/grammar-style-islah-al-mantiq-public-error-corrections.md`، و`data/markdown/grammar-style-islah-al-mantiq-verbs-forms-and-number.md`، و`data/markdown/grammar-style-islah-al-mantiq-idioms-and-semantic-distinctions.md`. الشاهد الكامل يقدَّر بنحو 190-230 صفحة مكافئة؛ لكن هذه الدفعة أنتجت ثلاث حزم فقط لأنها تمثل طبقة أولى عريضة من أبواب التصحيح والصيغ والعدد والأمثال، لا تفتيتًا ميكروسكوبيًا لكل باب.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

أضيف `المصباح المنير في غريب الشرح الكبير` للفيومي كمصدر معجمي تأسيسي جديد غير مكرر: جُمعت صفحات كتب الحروف الثمانية والعشرين كاملة من ويكي مصدر، من `كتاب الألف` إلى `كتاب الياء`، في raw واحد `data/raw/dict-al-misbah-al-munir-complete-letter-books.wikitext.txt` حجمه 3,522,238 bytes، أي مادة أكبر بكثير من صفحة أو جذر صغير. استُخرج اختيار عملي واسع `data/text/dict-al-misbah-al-munir-complete-letter-books-writing-selection.txt` من 43 مدخلًا يخدم البيان والدلالة، والتحقق والثبوت، والحكم والقصد، والكتابة والنقل، والفصل والوصل، والوصف والتخصيص والمقدار. أُنتجت ست حزم Markdown: `data/markdown/dict-al-misbah-al-munir-clarity-disclosure-and-signification.md`، و`data/markdown/dict-al-misbah-al-munir-verification-truth-and-reliable-knowledge.md`، و`data/markdown/dict-al-misbah-al-munir-judgment-intent-command-and-fairness.md`، و`data/markdown/dict-al-misbah-al-munir-writing-speech-transmission-and-attribution.md`، و`data/markdown/dict-al-misbah-al-munir-connection-separation-order-and-distance.md`، و`data/markdown/dict-al-misbah-al-munir-description-specificity-measure-and-quality.md`. تقدير الدفعة نحو 220-300 صفحة مكافئة؛ لذلك ست حزم عريضة مبررة مع تجنب تفتيت الجذور إلى ملفات صغيرة. هذه دفعة dictionary foundations جديدة لا تكرر دفعة `المقتضب` السابقة لأنها تعود إلى الأساس المعجمي والدلالي بعد توسيع النحو/الأسلوب.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

أضيف `فقه اللغة وسر العربية` للثعالبي كمصدر مرجعي/لغوي تأسيسي جديد غير مكرر: جُمعت صفحة المقدمة وثلاثون بابًا فعليًا من ويكي مصدر في raw واحد `data/raw/reference-fiqh-al-lugha-wa-sirr-al-arabiyya-complete.wikitext.txt` حجمه 620,358 bytes ونحو 45,833 كلمة/تتابع عربي، أي مادة أكبر بكثير من صفحة أو باب صغير. استُخرج text عملي منظف `data/text/reference-fiqh-al-lugha-wa-sirr-al-arabiyya-complete-cleaned.txt` حجمه 601,145 bytes ونحو 44,330 كلمة/تتابع عربي، وأُنتجت خمس حزم Markdown: `data/markdown/reference-fiqh-al-lugha-taxonomy-boundaries-and-naming.md`، و`data/markdown/reference-fiqh-al-lugha-body-description-and-action.md`، و`data/markdown/reference-fiqh-al-lugha-sounds-groups-and-crowds.md`، و`data/markdown/reference-fiqh-al-lugha-clothing-food-and-tools.md`، و`data/markdown/reference-fiqh-al-lugha-weather-water-and-land.md`. تقدير حجم الدفعة نحو 120-150 صفحة مكافئة؛ لذلك خمس حزم عريضة مبررة تحت قاعدة ~ملف لكل 20 صفحة مع تجنب تفتيت زائد. هذه دفعة reference/foundation لغوية لا تكرر دفعة `أساس البلاغة` السابقة لأنها تنتقل من الجذر المعجمي البلاغي إلى الحقول الدلالية والتسمية والتصنيف الطبيعي والعملي.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

أضيف `أساس البلاغة` للزمخشري كمصدر معجمي/بلاغي تأسيسي جديد غير مكرر: جُمعت صفحتا ويكي مصدر الكاملتان `أساس البلاغة - الجزء الأول` و`أساس البلاغة - الجزء الثاني` في raw واحد `data/raw/dict-asas-al-balagha-parts-one-two.wikitext.txt` حجمه 351,727 bytes ونحو 33,952 كلمة عربية، أي مادة أكبر بكثير من جذر أو صفحة صغيرة. استُخرج text عملي `data/text/dict-asas-al-balagha-parts-one-two-writing-foundations.txt` من 28 جذرًا مختارًا، وأُنتجت أربع حزم Markdown: `data/markdown/dict-asas-al-balagha-bayan-balagha-and-visible-meaning.md`، و`data/markdown/dict-asas-al-balagha-trust-fixity-and-verification.md`، و`data/markdown/dict-asas-al-balagha-composition-origin-building-and-completion.md`، و`data/markdown/dict-asas-al-balagha-relation-distance-following-and-flow.md`. تقدير حجم الدفعة نحو 90-110 صفحة مكافئة؛ لذلك أربع حزم متوسطة الغنى مبررة تحت قاعدة ~ملف لكل 20 صفحة مع تجنب تفتيت زائد. هذه دفعة dictionary foundations جديدة لا تكرر توسعة `أدب الكاتب` السابقة.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

وُسِّع `أدب الكاتب` بدفعة مرجعية كبيرة غير مكررة من شاهد Internet Archive نفسه: حُفظ raw بنيوي جديد `data/raw/reference-adab-al-katib.ia-djvu.xml` بحجم يتجاوز 7.5 ميغابايت، واستُخرج نطاق متصل من OBJECTs/leaves 65-140، أي نحو 76 ورقة مصدرية رقمية من تتمة `كتاب المعرفة` وبداية `أبواب الفروق`. هذه ليست صفحة صغيرة ولا إعادة تلخيص للافتتاح السابق، بل نطاق واسع يغطي أسماء الرجال وأصولها، والسماء والنجوم والنبات، وإناث الحيوان وجموعه، وصفات الخيل وعيوبها وشياتها، وعيوب الإنسان، وفروق الإنسان والحيوان والطعام والمجالس. أُنتج OCR وسيط `data/text/reference-adab-al-katib-leaves-65-140-ocr-extract.txt` وملف عملي `data/text/reference-adab-al-katib-leaves-65-140-names-stars-creatures-furuq-foundations.txt`، وأضيفت أربع حزم Markdown: `data/markdown/reference-adab-al-katib-names-origins-and-natural-taxonomies.md`، و`data/markdown/reference-adab-al-katib-animals-horses-and-described-form.md`، و`data/markdown/reference-adab-al-katib-human-defects-and-ethical-description.md`، و`data/markdown/reference-adab-al-katib-furuq-human-animal-food-and-social-scenes.md`. صار `reference-adab-al-katib` يغطي نحو 133 صفحة/ورقة عملية عبر سبع حزم، وهو متناسب مع قاعدة ~ملف لكل 20 صفحة. هذه دفعة reference material واسعة، وليست تكرارًا للتوسعة المعجمية السابقة في `تاج العروس`.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

وُسِّع `تاج العروس` بدفعة معجمية رابعة متصلة من الأوراق/OBJECTs 499-541 من شاهد Internet Archive نفسه، أي نحو 43 ورقة حتى آخر DjVuXML. هذه ليست صفحة wikitext صغيرة ولا فهرسًا؛ بل محتوى معجمي حقيقي يغطي الجسد والجعد والجلد والجمد والجند والجود والجهد والجيد. أُنتج OCR وسيط `data/text/dict-taj-al-arus-leaves-499-541-ocr-extract.txt` وملف اختيار عملي `data/text/dict-taj-al-arus-leaves-499-541-foundational-selection.txt`، ثم جُمعت الدفعات 370-412 و413-455 و456-498 و499-541 في النص المعتمد الجديد `data/text/dict-taj-al-arus-leaves-370-541-foundational-selection.txt`. أضيفت حزمتا Markdown جديدتان: `data/markdown/dict-taj-al-arus-body-form-firmness-and-frozen-limits.md` و`data/markdown/dict-taj-al-arus-cohorts-generosity-effort-and-fine-placement.md`. صار `dict-taj-al-arus` يغطي نحو 172 ورقة مصدرية وثماني حزم، وهو متناسب مع قاعدة ~ملف لكل 20 صفحة/ورقة. هذه دفعة dictionary foundations واسعة، وليست تكرارًا للتوسعة المرجعية السابقة في `كتاب الصناعتين`.

### إنجاز مصدري سابق بعد الإغلاق المرحلي

وُسِّع `كتاب الصناعتين` بدفعة مرجعية كبيرة غير مكررة: حُفظت خامات DjVuXML وscandata من Internet Archive إلى جانب DjVuTXT القديم، ثم استُخرج نطاق متصل من الأوراق/OBJECTs 120-179، أي نحو 60 ورقة مصدرية، عن حسن السبك وجودة الرصف، والإيجاز والحذف والإطناب المقبول، والأخذ من السابقين والزيادة الحسنة والتقصير. أُنتج OCR وسيط في `data/text/reference-sinaatayn-leaves-120-179-sabk-ijaz-akhdh-ocr.txt`، وملف اختيار عملي في `data/text/reference-sinaatayn-leaves-120-179-sabk-ijaz-akhdh-foundations.txt`، وثلاث حزم Markdown جديدة: `data/markdown/reference-sinaatayn-sabk-and-word-placement.md`، و`data/markdown/reference-sinaatayn-ijaz-itnab-and-sufficient-brevity.md`، و`data/markdown/reference-sinaatayn-akhdh-source-use-and-good-addition.md`. هذه دفعة reference material واسعة تحت قاعدة ~ملف لكل 20 صفحة، وليست تكرارًا للتوسعة النحوية السابقة في `الخصائص`.

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
- `dict-asas-al-balagha`
- `dict-maqayis-al-lugha`
- `dict-al-sihah-al-jawhari`
- `grammar-style-kitab`
- `grammar-style-sharh-shudhur-al-dhahab`
- `reference-adab-al-katib`
- `reference-al-bayan-wa-al-tabyin`

Representative artifacts:

- `data/markdown/dict-mukhtar-al-sihah-complete-writing-foundations.md`
- `data/markdown/dict-taj-al-arus-body-form-firmness-and-frozen-limits.md`
- `data/markdown/dict-taj-al-arus-cohorts-generosity-effort-and-fine-placement.md`
- `data/markdown/dict-asas-al-balagha-bayan-balagha-and-visible-meaning.md`
- `data/markdown/dict-asas-al-balagha-composition-origin-building-and-completion.md`
- `data/markdown/dict-maqayis-al-lugha-roots-method-and-lexical-judgment.md`
- `data/markdown/dict-maqayis-al-lugha-time-effect-trust-and-adab.md`
- `data/markdown/dict-al-sihah-al-jawhari-motion-origin-and-adab.md`
- `data/markdown/dict-al-sihah-al-jawhari-expansion-invalidity-interiority-and-settlement.md`
- `data/markdown/dict-taj-al-arus-old-inheritance-denial-and-clear-paths.md`
- `data/markdown/dict-taj-al-arus-stripping-clarity-and-separate-remnants.md`
- `data/markdown/reference-sinaatayn-sabk-and-word-placement.md`
- `data/markdown/reference-sinaatayn-ijaz-itnab-and-sufficient-brevity.md`
- `data/markdown/reference-sinaatayn-akhdh-source-use-and-good-addition.md`
- `data/markdown/reference-adab-al-katib-names-origins-and-natural-taxonomies.md`
- `data/markdown/reference-adab-al-katib-furuq-human-animal-food-and-social-scenes.md`
- `data/markdown/grammar-style-khasais-language-variation-and-usage-authority.md`
- `data/markdown/grammar-style-khasais-samaa-qiyas-and-apparent-exceptions.md`
- `data/markdown/grammar-style-kitab-part-four-ibtida-inna-and-kam.md`
- `data/markdown/grammar-style-kitab-part-four-negation-exception-pronouns.md`
- `data/markdown/grammar-style-sharh-ibn-aqil-kalam-word-classes-and-sentence-minimum.md`
- `data/markdown/grammar-style-sharh-ibn-aqil-irab-bina-and-inflection-checks.md`
- `data/markdown/grammar-style-sharh-qatr-al-nada-mudari-nasb-jazm-and-condition.md`
- `data/markdown/grammar-style-sharh-qatr-al-nada-reference-definiteness-and-linking.md`
- `data/markdown/grammar-style-sharh-shudhur-al-dhahab-irab-agency-and-ambiguity-control.md`
- `data/markdown/grammar-style-sharh-shudhur-al-dhahab-bina-pronouns-and-reference.md`
- `data/markdown/grammar-style-al-jumal-irab-map-and-case-governance.md`
- `data/markdown/grammar-style-al-jumal-particles-linking-and-meaning.md`
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

1. إذا كان المطلوب استمرار التوسيع، فأضف مصدرًا أو نطاقًا جديدًا كبيرًا وفق ترتيب يحدده `docs/MASTER_EXECUTION_CHECKLIST.md` بعد مرحلة الإغلاق، لا تعد إلى تلميع الحزم الحالية إلا عند ظهور خلل محدد. آخر توسيع كان معجميًا داخل `معجم مقاييس اللغة` عبر شاهد IA `20220809_Makaislugha` والأوراق/OBJECTs 556-655؛ لذلك يُفضّل أن تكون الدفعة التالية من مصدر آخر أو نطاق كبير غير مكرر، أو امتداد بعيد/ضروري لا يعيد تفصيل هذا النطاق. تجنب أيضًا إعادة تفصيل باب الباء/الجيم/الحاء من `القاموس المحيط`، ونطاقات `الصحاح` 20-859، وعنقود `لسان العرب` الحالي، وأوراق `معجم مقاييس اللغة` 56-555، ونطاقات `تاج العروس` 370-541، وأوراق `كتاب الصناعتين` 120-179، و`أدب الكاتب` 65-140، و`أساس البلاغة` الجزأين 1-2، واختيار `المقتضب` الحالي، وحزم `إصلاح المنطق` و`شرح ابن عقيل` و`شرح قطر الندى` و`الجمل في النحو` و`شرح شذور الذهب` 30-404.
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
