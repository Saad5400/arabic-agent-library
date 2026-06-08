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

- 23 total source entries
- categories covered: dictionary, rhetoric, grammar-style, reference, poetry
- 23 sources are currently `synthesized`
- 0 sources remain `candidate`
- 0 sources remain `queued`

### أحدث إنجاز مصدري بعد الإغلاق المرحلي

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
- `grammar-style-kitab`
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

1. إذا كان المطلوب استمرار التوسيع، فأضف مصدرًا أو نطاقًا جديدًا كبيرًا وفق ترتيب يحدده `docs/MASTER_EXECUTION_CHECKLIST.md` بعد مرحلة الإغلاق، لا تعد إلى تلميع الحزم الحالية إلا عند ظهور خلل محدد. آخر توسيع كان نحويًا/أسلوبيًا في `الجمل في النحو` عبر ثماني عشرة صفحة ويكي مصدرية ونحو 70-90 صفحة مكافئة، لذلك يُفضّل أن تكون الدفعة التالية من مصدر آخر أو نطاق كبير لاحق غير مكرر، لا إعادة تفصيل أبواب `الجمل` نفسها، مع تجنب تكرار العمل مباشرة على نطاقات `تاج العروس` 370-541 أو أوراق `كتاب الصناعتين` 120-179 أو `أدب الكاتب` 65-140 أو `أساس البلاغة` الجزأين 1-2 أو اختيار `المقتضب` الحالي أو حزم `إصلاح المنطق` و`شرح ابن عقيل` و`معجم مقاييس اللغة` و`شرح قطر الندى` و`الجمل في النحو` الأخيرة.
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
