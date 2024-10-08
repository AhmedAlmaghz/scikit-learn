خارطة الطريق
================

الغرض من هذه الوثيقة
------------------------
هذه الوثيقة قائمة بالتوجهات العامة التي يهتم المساهمون الأساسيون برؤيتها مطورة في سكيت-ليرن. إن إدراج بند ما هنا لا يعد بأي حال من الأحوال وعدًا بتنفيذه، حيث إن الموارد محدودة. بل هو إشارة إلى أن المساعدة في هذا الموضوع موضع ترحيب.

بيان الغرض: سكيت-ليرن في عام 2018
------------------------------------------
بعد أحد عشر عامًا من ظهور سكيت-ليرن، تغير الكثير في عالم تعلم الآلة. تشمل التغييرات الرئيسية ما يلي:

* الأدوات الحسابية: استغلال وحدات معالجة الرسوميات، وأطر البرمجة الموزعة مثل Scala/Spark، وما إلى ذلك.
* المكتبات عالية المستوى في بايثون للتجريب ومعالجة البيانات وإدارتها: Jupyter notebook، وCython، وPandas، وDask، وNumba، إلخ.
* التغييرات في تركيز أبحاث تعلم الآلة: تطبيقات الذكاء الاصطناعي (حيث يكون هيكل الإدخال هو المفتاح) مع التعلم العميق، وتعلم التمثيل، والتعلم التعزيزي، ونقل المجال، وما إلى ذلك.

هناك تغيير أكثر دقة على مدى العقد الماضي، وهو أنه بسبب تغير الاهتمامات في مجال تعلم الآلة، من المحتمل أن يساهم طلاب الدكتوراه في مجال تعلم الآلة في مشاريع مثل PyTorch وDask، أكثر من سكيت-ليرن، لذا فإن مجموعة المساهمين لدينا مختلفة جدًا عما كانت عليه منذ عقد مضى.

لا يزال سكيت-ليرن شائعًا جدًا في الممارسة العملية لتجربة تقنيات تعلم الآلة الكنسية، خاصة لتطبيقات العلوم التجريبية وعلوم البيانات. الكثير مما نقدمه الآن ناضج جدًا. ولكن يمكن أن يكون مكلفًا للصيانة، وبالتالي لا يمكننا تضمين التنفيذ الجديد التعسفي. ومع ذلك، فإن سكيت-ليرن ضروري أيضًا لتحديد إطار عمل API لتطوير مكونات تعلم الآلة القابلة للتشغيل البيني خارج المكتبة الأساسية.

**لذلك تتمثل أهدافنا الرئيسية في هذا العصر فيما يلي**:

* الاستمرار في صيانة مجموعة عالية الجودة وموثقة جيدًا من الأدوات الكنسية لمعالجة البيانات وتعلم الآلة ضمن النطاق الحالي (أي البيانات المستطيلة التي لا تتغير بشكل كبير مع ترتيب الأعمدة والصفوف؛ التنبؤ بالأهداف ذات البنية البسيطة)
* تحسين سهولة تطوير المستخدمين للمكونات الخارجية ونشرها
* تحسين قابلية التشغيل البيني مع أدوات علوم البيانات الحديثة (مثل Pandas وDask) والبنى التحتية (مثل المعالجة الموزعة)

يمكن العثور على العديد من الأهداف الأكثر تفصيلاً تحت علامة "API tag" في متتبع القضايا.

الأهداف المعمارية/العامة
-----------------------------
ترقم القائمة ليس كإشارة إلى ترتيب الأولويات، ولكن لتسهيل الإشارة إلى نقاط محددة. يرجى إضافة إدخالات جديدة في الأسفل فقط. لاحظ أن الإدخالات المشطوبة مكتملة، ونحاول تحديث الوثيقة أثناء عملنا على هذه القضايا.

1. تحسين التعامل مع أطر بيانات بانداس

   * توثيق التعامل الحالي
   * مشكلة إعادة ترتيب الأعمدة: :issue:`7242`
   * تجنب التحويل غير الضروري إلى ndarray |ss| :issue:`12147` |se|
   * إعادة أطر البيانات من المحولات :issue:`5523`
   * الحصول على أطر البيانات من محملات مجموعات البيانات |ss| :issue:`10733` |se|،
     |ss| :issue:`13902` |se|
   * Sparse غير مدرج حاليًا |ss| :issue:`12800` |se|

2. تحسين التعامل مع الميزات الفئوية

   * يجب أن تكون النماذج القائمة على الشجرة قادرة على التعامل مع الميزات المستمرة والفئوية على حد سواء: :issue:`12866` و |ss| :issue:`15550` |se|.
   * |ss| في محملات مجموعات البيانات :issue:`13902` |se|
   * كمحولات عامة لاستخدامها مع ColumnTransforms (مثل الترميز الترتيبي الذي يشرف عليه الارتباط مع متغير الهدف) :issue:`5853`،
     :issue:`11805`
   * التعامل مع الخلطات من الميزات الفئوية والمستمرة

3. تحسين التعامل مع البيانات المفقودة

   * التأكد من أن الميتا-مقدّرات متساهلة تجاه البيانات المفقودة،
     |ss| :issue:`15319` |se|
   * معالجات غير تافهة |ss| :issue:`11977`، :issue:`12852` |se|
   * المتعلمون الذين يتعاملون مباشرة مع البيانات المفقودة |ss| :issue:`13911` |se|
   * مولد عينات البتر لجعل أجزاء من مجموعة البيانات مفقودة
     :issue:`6284`

4. وثائق أكثر تعليمية

   * أضيفت المزيد والمزيد من الخيارات إلى سكيت-ليرن. ونتيجة لذلك، فإن الوثائق مزدحمة، مما يجعل من الصعب على المبتدئين الحصول على الصورة الكبيرة. يمكن القيام ببعض العمل في ترتيب المعلومات حسب الأولوية.

5. تمرير المعلومات التي ليست (X، y): خصائص العينة

   * نحتاج إلى القدرة على تمرير أوزان العينات إلى المسجلين في التحقق من صحة البيانات.
   * يجب أن تكون لدينا طرق قياسية/عامة لتمرير الخصائص الخاصة بالعينة في الميتا-مقدّرات. :issue:`4497` :issue:`7646`

6. تمرير المعلومات التي ليست (X، y): خصائص الميزة

   * يجب أن تكون أسماء الميزات أو الأوصاف متاحة بشكل مثالي للتناسب، على سبيل المثال. :issue:`6425` :issue:`6424`
   * يجب ألا تحتاج المعالجة لكل ميزة (على سبيل المثال، "هل هذا ترتيب/ترتيب/نص باللغة الإنجليزية؟") أيضًا إلى توفيرها لمُنشئي المُقدّر، ولكن يجب أن تكون متاحة كبيانات وصفية بجانب X. :issue:`8480`

7. تمرير المعلومات التي ليست (X، y): معلومات الهدف

   * لدينا مشاكل في الحصول على المجموعة الكاملة من الفئات لجميع المكونات عندما تكون البيانات مقسمة/معينة. :issue:`6231` :issue:`8100`
   * لا توجد طريقة للتعامل مع مزيج من الأهداف الفئوية والمستمرة.

8. تسهيل الأمر على المستخدمين الخارجيين لكتابة مكونات متوافقة مع سكيت-ليرن

   * فحوصات المُقدّر الأكثر مرونة التي لا يتم تحديدها بواسطة اسم المُقدّر
     |ss| :issue:`6599` |se| :issue:`6715`
   * مثال على كيفية تطوير مُقدّر أو ميتا-مُقدّر،
     |ss| :issue:`14582` |se|
   * تشغيل أكثر اكتفاءًا ذاتيًا لـ scikit-learn-contrib أو مورد مماثل

9. دعم إعادة أخذ العينات وتقليل العينات

   * السماح بالاستعانة بعينات فرعية من الفئات الرئيسية (في خط أنابيب؟) :issue:`3855`
   * تنفيذ الغابات العشوائية مع إعادة أخذ العينات :issue:`13227`

10. واجهات أفضل للتطوير التفاعلي

   * |ss| __repr__ وتصورات HTML للمُقدّرات
     :issue:`6323` و :pr:`14180` |se|.
   * تضمين أدوات التخطيط، وليس فقط كأمثلة. :issue:`9173`

11. أدوات محسنة لتشخيص النماذج والاستدلال الأساسي

   * |ss| بدائل لتنفيذ أهمية الميزة، :issue:`13146` |se|
   * طرق أفضل للتعامل مع مجموعات التحقق عند التجهيز
   * طرق أفضل للعثور على العتبات / إنشاء قواعد القرار :issue:`8614`

12. أدوات أفضل لاختيار فرط المعلمات مع المُقدّرات الاستقرائية

   * لا ينطبق البحث الشبكي والتحقق من صحة البيانات على معظم مهام التجميع. يعد الاختيار القائم على الاستقرار أكثر ملاءمة.

13. دعم أفضل لبناء خطوط الأنابيب يدويًا وتلقائيًا

   * طريقة أسهل لبناء خطوط أنابيب ومعلمات بحث معقدة
     :issue:`7608` :issue:`5082` :issue:`8243`
   * توفير نطاقات البحث للمُقدّرات الشائعة؟؟
   * راجع `searchgrid <https://searchgrid.readthedocs.io/en/latest/>`_

14. تحسين تتبع التجهيز

   * لا يعد الوضع المفصل وديًا جدًا، ويجب أن يستخدم مكتبة تسجيل قياسية
     :issue:`6929`، :issue:`78`
   * من شأن الاستدعاءات أو نظام مماثل أن يسهل التسجيل والتوقف المبكر

15. التوزيع المتوازي

   * قبول البيانات المتوافقة مع ``__array_function__``

16. طريقة للمضي قدمًا في المزيد من خارج النواة

    * تمكن Dask من الحساب خارج النواة بسهولة. في حين أن نموذج Dask ربما لا يمكن تكييفه مع جميع خوارزميات التعلم الآلي، فإن معظم التعلم الآلي يتم على بيانات أصغر من ETL، وبالتالي يمكننا ربما التكيف مع النطاق الكبير جدًا مع دعم جزء فقط من الأنماط.

17. دعم العمل مع النماذج المُدربة مسبقًا

   * "تجميد" المُقدّر. على وجه الخصوص، من المستحيل حاليًا استنساخ "CalibratedClassifierCV" مع prefit. :issue:`8370`. :issue:`6451`

18. التسلسل/فك التسلسل المتوافق مع الإصدارات السابقة لبعض المُقدّرات

   * حاليًا، يتسبب التسلسل (مع pickle) في حدوث أخطاء عبر الإصدارات. في حين أنه قد لا نتمكن من التغلب على القيود الأخرى لـ pickle re security، فسيكون من الرائع تقديم الأمان عبر الإصدارات بدءًا من الإصدار 1.0. ملاحظة: يعتقد غاييل وأوليفييه أن هذا يمكن أن يسبب عبئًا ثقيلًا على الصيانة ويجب علينا إدارة المقايضات. بديل ممكن مقدم في النقطة التالية.

19. وثائق وأدوات لإدارة دورة حياة النموذج

   * توثيق الممارسات الجيدة لنشر النماذج ودورة حياتها: قبل نشر نموذج: لقطة لنسخ رموز الإصدارات (numpy، scipy، scikit-learn، مستودع التعليمات البرمجية المخصصة)، وسيناريو التدريب واسم مستعار حول كيفية استرداد بيانات التدريب التاريخية + لقطة من مجموعة التحقق الصغيرة + لقطة من التوقعات (احتمالات التنبؤ لمصنفات)
     على مجموعة التحقق تلك.
   * توثيق الأدوات وجعل من السهل إدارة ترقية إصدارات scikit-learn:

     * حاول تحميل pickle القديم، إذا نجح، استخدم لقطة تنبؤات مجموعة التحقق للكشف عن أن النموذج المسلسل لا يزال يتصرف بنفس الطريقة؛
     * إذا لم ينجح joblib.load / pickle.load، استخدم سيناريو التدريب المُسيطر على الإصدارات + مجموعة التدريب التاريخية لإعادة تدريب النموذج واستخدم لقطة تنبؤات مجموعة التحقق للتأكيد على أنه من الممكن استعادة الأداء التنبئي السابق: إذا لم يكن الأمر كذلك، فمن المحتمل أن يكون هناك خطأ في scikit-learn يحتاج إلى الإبلاغ عنه.

20. يجب أن يتوافق كل شيء في سكيت-ليرن على الأرجح مع عقد API الخاص بنا.
    لا نزال في طور اتخاذ القرارات بشأن بعض هذه القضايا ذات الصلة.

   * `Pipeline <pipeline.Pipeline>` و`FeatureUnion` تعديل معلمات الإدخال الخاصة بهم في التجهيز. يتطلب إصلاح هذا التأكد من أن لدينا فهمًا جيدًا لحالات الاستخدام الخاصة بهم للتأكد من الحفاظ على جميع الوظائف الحالية. :issue:`8157` :issue:`7382`

21. (اختياري) تحسين مجموعة الاختبارات الشائعة في سكيت-ليرن للتأكد من أن (على الأقل للنماذج المستخدمة بشكل متكرر) تنبؤات مستقرة عبر الإصدارات (للمناقشة)؛

   * توسيع الوثائق لذكر كيفية نشر النماذج في بيئات خالية من بايثون، على سبيل المثال `ONNX <https://github.com/onnx/sklearn-onnx>`_.
     واستخدام أفضل الممارسات المذكورة أعلاه لتقييم الاتساق التنبئي بين وظائف التنبؤ في scikit-learn وONNX على مجموعة التحقق.
   * توثيق الممارسات الجيدة للكشف عن الانحراف في التوزيع الزمني للنموذج المنشور والممارسات الجيدة لإعادة التدريب على البيانات الجديدة دون التسبب في حدوث تراجعات كبيرة في الأداء التنبئي.

الأهداف المحددة للبرنامج الفرعي
-------------------------

:mod:`sklearn.ensemble`

* |ss| تنفيذ التكديس، :issue:`11047` |se|

:mod:`sklearn.cluster`

* متغيرات kmeans للمسافات غير الإقليدية، إذا تمكنا من إظهار هذه الفوائد التي تتجاوز التجميع الهرمي.

:mod:`sklearn.model_selection`

* |ss| التسجيل متعدد المقاييس بطيء :issue:`9326` |se|
* ربما نريد أن نتمكن من الحصول على أكثر من مقاييس متعددة
* التعامل مع حالات التوقف العشوائية في قواطع CV هو تصميم فقير ويتناقض مع التحقق من صحة معلمات مماثلة في المُقدّرات،
     `SLEP011 <https://github.com/scikit-learn/enhancement_proposals/pull/24>`_
* استغلال البدء الدافئ وخوارزميات المسار بحيث يمكن الوصول إلى فوائد كائنات `EstimatorCV`
     عبر `GridSearchCV` واستخدامها في خطوط الأنابيب.
     :issue:`1626`
* يجب أن يكون من الممكن استبدال التحقق من صحة البيانات بتقديرات OOB كلما تم استخدام مكرر التحقق من صحة البيانات.
* يجب تجنب الحسابات المكررة في خطوط الأنابيب (ذات صلة بالنقطة أعلاه) راجع `dask-ml
     <https://ml.dask.org/hyper-parameter-search.html#avoid-repeated-work>`_

:mod:`sklearn.neighbors`

* |ss| القدرة على استبدال تنفيذ nearest neighbors المخصص/التقريبي/المحسوب مسبقًا لدينا في جميع/معظم السياقات التي تستخدم فيها nearest neighbors للتعلم. :issue:`10463` |se|

:mod:`sklearn.pipeline`

* مشكلات الأداء مع `Pipeline.memory`
* راجع "يجب أن يتوافق كل شيء في سكيت-ليرن مع عقد API الخاص بنا" أعلاه