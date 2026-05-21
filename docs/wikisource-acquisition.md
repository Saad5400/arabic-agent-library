# جلب مواد ويكي مصدر العربية بطريقة قابلة للتكرار

هذا الدليل يشرح استعمال `scripts/fetch_wikisource.py` لجلب النص الخام من صفحات ويكي مصدر العربية مع ترويسة provenance صريحة ومعالجة مهذبة لأخطاء `429 Too Many Requests`.

## لماذا أضيف هذا المسار؟

في هذه المرحلة يعتمد المشروع على مصادر تأسيسية كثيرة من ويكي مصدر، وخصوصًا المعاجم وكتب النحو والمرجعيات الأسلوبية. لكن الجلب اليدوي المباشر يتعثر بسهولة بسبب:

- غياب مكتبة `requests` في البيئة الدنيا
- تكرار أخطاء rate limiting من واجهة MediaWiki API
- الحاجة إلى حفظ النص الخام مع عنوان الصفحة والرابط القانوني ووقت الجلب و`sha256`

لذلك أضيف هذا السكربت ليكون خطوة اقتناء أولية قبل التنظيف والتركيب.

## أمثلة سريعة

### 1) جلب مصدر مسجل في السجل

```bash
python3 scripts/fetch_wikisource.py --source-id dict-lisan-al-arab
```

النتيجة الافتراضية تكون في:

- `data/raw/dict-lisan-al-arab.wikitext.txt`

### 2) جلب صفحة بعينها بعنوانها الصريح

```bash
python3 scripts/fetch_wikisource.py \
  --title "لسان العرب/بين-" \
  --output data/raw/lisan-bayn-page.wikitext.txt
```

### 3) الطباعة إلى stdout بدل الكتابة

```bash
python3 scripts/fetch_wikisource.py --title "القاموس المحيط" --stdout
```

## ما الذي يحفظه الملف الخام؟

كل ملف ناتج يبدأ بترويسة قصيرة تتضمن:

- `requested_title`
- `canonical_title`
- `canonical_url`
- `source_id` إن وُجد
- `fetched_at_utc`
- `page_id`
- `revision_id`
- `content_sha256`

ثم يلي ذلك **wikitext الخام** كما أعادته واجهة ويكي مصدر، من غير تنظيف تحريري.

## سلوك التباطؤ وإعادة المحاولة

السكربت يستعمل:

- `User-Agent` صريحًا
- إعادة محاولة تلقائية
- backoff تصاعديًا عند `429`
- احترام `Retry-After` إن أعادته الخدمة

الخيارات المفيدة:

```bash
--max-retries 6
--base-sleep 4
--timeout 30
```

إذا كانت الخدمة تتشدد مؤقتًا، زد `--base-sleep` أو خفف عدد الطلبات في الجلسة الواحدة.

## كيف يدخل في سير العمل العام؟

1. جلب الخام من ويكي مصدر إلى `data/raw/`
2. إنشاء ملف نصي منظف أو مقتطف منظم في `data/text/`
3. تركيب حزمة وكيل غنية في `data/markdown/`
4. تحديث `data/registry/sources.json`
5. تشغيل:

```bash
python3 scripts/registry_tool.py lint
python3 scripts/registry_tool.py check-duplicates
```

## ملاحظة مهمة

هذا السكربت **لا** ينظف النص ولا يبني الحزمة النهائية. وظيفته أن يثبت طبقة الاقتناء الخام بطريقة قابلة للتكرار، حتى لا نضيع وقتًا متكررًا في تجاوز rate limiting أو في إعادة حفظ provenance يدويًا.
