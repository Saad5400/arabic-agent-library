# مواصفة التخزين المعجمي في SQLite

## الهدف

إضافة طبقة تخزين أساسية سريعة وقابلة للتوسعة للمداخل المعجمية العربية داخل المشروع، بحيث تكون:

- SQLite هو مصدر الحقيقة الأساسي
- الحقول الأصلية محفوظة كما هي
- الحقول normalized محفوظة بجانبها لتحسين البحث
- التصدير إلى JSON/JSONL/CSV يتم بسكربت منفصل
- البحث يتم بسكربت منفصل يدعم exact + normalized + FTS + fuzzy matching

## الملفات المضافة

- `data/registry/lexicon.schema.sql`
- `scripts/arabic_normalization.py`
- `scripts/lexicon_sqlite.py`
- `scripts/export_lexicon_sqlite.py`
- `scripts/search_lexicon_sqlite.py`

## لماذا SQLite هنا؟

لأن المشروع يتحرك نحو معاجم كاملة لا مقتطفات صغيرة فقط، فنحتاج إلى:

- فهرسة سريعة
- فلترة حسب المصدر والجذر والصفحات
- دعم FTS5 محليًا من دون خدمة خارجية
- سهولة التصدير لاحقًا إلى JSON أو CSV أو JSONL
- ملف واحد سهل النسخ والنسخ الاحتياطي والمراجعة

## الجداول الأساسية

### 1) `sources`

نسخة عملية من بيانات `data/registry/sources.json` داخل القاعدة، لتسهيل الربط بين المداخل والمعجم المصدر.

حقول مهمة:

- `id`
- `title`
- `title_normalized`
- `author`
- `author_normalized`
- `category`
- `registry_json`

### 2) `lexicon_entries`

هذا هو جدول المداخل المعجمية نفسه.

حقول مهمة:

- `source_id`
- `source_entry_id`
- `headword`
- `headword_normalized`
- `root`
- `root_normalized`
- `entry_text`
- `entry_text_normalized`
- `definition_summary`
- `definition_summary_normalized`
- `usage_notes`
- `usage_notes_normalized`
- `examples_json`
- `metadata_json`
- `provenance_json`
- `page_start`
- `page_end`
- `section_ref`
- `content_sha256`

## التطبيع `normalized`

التطبيع المعتمد الآن يركز على تحسين الاسترجاع، لا على إعادة كتابة النص الأصلي. لذلك تبقى الحقول الأصلية محفوظة أيضًا.

أهم التحويلات الحالية:

- إزالة التشكيل والعلامات الملحقة
- توحيد: `أ/إ/آ/ٱ -> ا`
- توحيد: `ى -> ي`
- توحيد: `ة -> ه`
- توحيد: `ؤ -> و`
- توحيد: `ئ -> ي`
- إزالة التطويل `ـ`
- تسوية المسافات وبعض علامات الترقيم

يمكن تعديل هذا لاحقًا إذا ظهر أن بعض المعاجم تحتاج سياسة أخرى، لكن هذه البداية مناسبة للبحث العملي.

## طبقات البحث

### 1) exact normalized

يبحث في:

- `headword_normalized`
- `root_normalized`

### 2) substring normalized

يفيد عندما يكتب المستخدم جزءًا من المدخل أو جزءًا من تعريفه.

### 3) FTS5 prefix search

يبحث داخل:

- headword
- root
- definition summary
- entry text

مع دعم prefix matching لاسترجاع نتائج أوسع وأسرع.

### 4) fuzzy fallback

عند وجود فرق بسيط في كتابة الكلمة، يستعمل السكربت `difflib.SequenceMatcher` على الحقول normalized، خصوصًا:

- `headword_normalized`
- `root_normalized`

وهذا يحقق المطلوب: "جيب أقرب النتائج حتى لو فيه شوي اختلاف بكلمة البحث".

## صيغة الإدخال الحالية للمداخل

سكربت `scripts/lexicon_sqlite.py import-json` يقبل:

- JSON array
- JSONL
- أو كائنًا بالشكل:

```json
{
  "entries": [
    {
      "source_id": "dict-lisan-al-arab",
      "source_entry_id": "qwl-001",
      "headword": "قول",
      "root": "ق و ل",
      "entry_text": "النص الكامل للمدخل...",
      "definition_summary": "ملخص قصير",
      "usage_notes": "ملاحظات استعمال",
      "examples": ["مثال 1", "مثال 2"],
      "metadata": {"volume": 1},
      "provenance": {"page_url": "..."},
      "page_start": 10,
      "page_end": 11,
      "section_ref": "باب القاف"
    }
  ]
}
```

الحقول الإلزامية حاليًا:

- `source_id`
- `headword`
- `entry_text`

إذا لم يُمرَّر `source_entry_id` فإن السكربت يشتق معرفًا ثابتًا من هوية المدخل الأساسية (`source_id` + `headword_normalized` + `root_normalized` + الصفحات + `section_ref`) بدل اشتقاقه من النص الكامل، حتى يبقى upsert مستقرًا عندما يتحسن نص المدخل أو يُراجع لاحقًا.

## أوامر العمل

### 1) إنشاء القاعدة

```bash
python3 scripts/lexicon_sqlite.py init
```

### 2) مزامنة جدول المصادر من السجل

```bash
python3 scripts/lexicon_sqlite.py sync-sources
```

### 3) استيراد مداخل من JSON/JSONL

```bash
python3 scripts/lexicon_sqlite.py import-json --input path/to/entries.jsonl
```

### 4) البحث

```bash
python3 scripts/search_lexicon_sqlite.py "القول"
python3 scripts/search_lexicon_sqlite.py "الاقوال" --format json
python3 scripts/search_lexicon_sqlite.py "قيل" --source-id dict-lisan-al-arab
```

### 5) التصدير

```bash
python3 scripts/export_lexicon_sqlite.py --output exports/lexicon.json --pretty
python3 scripts/export_lexicon_sqlite.py --output exports/lexicon.jsonl
python3 scripts/export_lexicon_sqlite.py --output exports/lexicon.csv --source-id dict-lisan-al-arab
```

## ما لم يُنفذ بعد

هذه الدفعة تضيف البنية التشغيلية، لكنها لا تنفذ بعد ingest كاملًا من معجم كامل إلى القاعدة. ما يزال مطلوبًا لاحقًا:

- اختيار المعجم الكامل التالي
- تصميم extractor خاص ببنية ذلك المصدر
- تعبئة القاعدة بمداخل فعلية واسعة
- اختبار جودة التطبيع على ألفاظ عربية أكثر
- تحسين ranking إذا ظهرت احتياجات أدق

## مبدأ العمل من الآن

- SQLite = المصدر الأساسي للبيانات المعجمية المنظمة
- JSON/JSONL/CSV = صيغ تصدير أو تبادل
- المداخل الأصلية لا تُفقد
- normalized fields تبنى دائمًا تلقائيًا مع الاستيراد
- البحث القريب/fuzzy جزء أساسي من المسار، لا إضافة ثانوية
