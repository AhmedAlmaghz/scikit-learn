:ref: المشاريع ذات الصلة
تشجع المشاريع التي تنفذ واجهة برمجة تطبيقات Scikit-learn على استخدام قالب Scikit-learn-contrib، والذي يسهل اتباع أفضل الممارسات في اختبار وتوثيق التقديرات. كما تقبل منظمة Scikit-learn-contrib على GitHub المساهمات عالية الجودة للمستودعات المتوافقة مع هذا القالب.

فيما يلي قائمة بالمشاريع الشقيقة، والتمديدات، والحزم الخاصة بمجالات محددة:

التعاون مع الأطر الأخرى وتحسينها
-------------------------------------------

تتكيف هذه الأدوات مع Scikit-learn لاستخدامها مع التقنيات الأخرى، أو تعزز وظائف تقديرات Scikit-learn بطريقة أخرى.

**تنسيقات البيانات**

- sklearn_pandas: جسر لأنابيب Scikit-learn وأطر بيانات Pandas مع محولات مخصصة.

- sklearn_xarray: يوفر التوافق بين تقديرات Scikit-learn وهياكل بيانات Xarray.

**التعلم الآلي التلقائي**

- auto-sklearn: مجموعة أدوات للتعلم الآلي التلقائي، ويمكن استخدامها كبديل لتقدير Scikit-learn.

- autoviml: أداة لبناء عدة نماذج للتعلم الآلي تلقائيًا باستخدام سطر واحد من الكود. تم تصميمها كطريقة أسرع لاستخدام نماذج Scikit-learn دون الحاجة إلى معالجة البيانات مسبقًا.

- TPOT: مجموعة أدوات للتعلم الآلي التلقائي تقوم بتحسين سلسلة من مشغلات Scikit-learn لتصميم خط أنابيب للتعلم الآلي، بما في ذلك معالجات مسبقة للبيانات والميزات بالإضافة إلى التقديرات. ويمكن استخدامه كبديل لتقدير Scikit-learn.

- Featuretools: إطار عمل لأداء الهندسة التلقائية للميزات. يمكن استخدامه لتحويل مجموعات البيانات الزمنية والعلائقية إلى مصفوفات ميزات للتعلم الآلي.

- Neuraxle: مكتبة لبناء خطوط أنابيب منظمة، توفر التجريدات الصحيحة لتسهيل البحث والتطوير ونشر تطبيقات التعلم الآلي. وهي متوافقة مع أطر عمل التعلم العميق وواجهة برمجة تطبيقات Scikit-learn، ويمكنها بث الدفعات المصغرة واستخدام نقاط التفتيش للبيانات وبناء خطوط أنابيب متطورة، وتسلسل النماذج باستخدام برامج حفظ مخصصة لكل خطوة.

- EvalML: مكتبة للتعلم الآلي التلقائي تقوم ببناء وتحسين وتقييم خطوط أنابيب التعلم الآلي باستخدام دالات الهدف الخاصة بالمجال. تدمج عدة مكتبات نمذجة تحت واجهة برمجة تطبيقات واحدة، وتستخدم الأشياء التي تنشئها EvalML واجهة برمجة تطبيقات متوافقة مع Scikit-learn.

**أطر عمل التجارب وتسجيل النماذج**

- MLFlow: منصة مفتوحة المصدر لإدارة دورة حياة التعلم الآلي، بما في ذلك التجارب وإمكانية التكرار والنشر، بالإضافة إلى سجل مركزي للنماذج.

- Neptune: مخزن بيانات لممارسات MLOps، تم بناؤه للفرق التي تجري العديد من التجارب. يوفر مكانًا واحدًا لتسجيل وتخزين وعرض وتنظيم ومقارنة واستعلام جميع بيانات إنشاء النماذج الخاصة بك.

- Sacred: أداة لمساعدتك في تكوين التجارب وتنظيمها وتسجيلها وتكرارها.

- Scikit-Learn Laboratory: غلاف سطر الأوامر حول Scikit-learn، مما يسهل تشغيل تجارب التعلم الآلي باستخدام عدة متعلمين ومجموعات ميزات كبيرة.

**فحص النماذج والتصور**

- dtreeviz: مكتبة Python لتصور شجرة القرار وتفسير النموذج.

- eli5: مكتبة لتصحيح/فحص نماذج التعلم الآلي وتفسير تنبؤاتها.

- sklearn-evaluation: جعل تقييم نموذج التعلم الآلي سهلاً: الرسوم البيانية والجداول والتقارير HTML وتتبع التجارب وتحليل Jupyter notebook. التحليل المرئي، واختيار النموذج، والتقييم، والتشخيص.

- yellowbrick: مجموعة من أدوات التصور المخصصة لـ Matplotlib لتقديرات Scikit-learn لدعم التحليل المرئي للميزات، واختيار النماذج، والتقييم، والتشخيص.

**اختيار النماذج**

- scikit-optimize: مكتبة لتقليل وظائف الصناديق السوداء الباهظة الثمن والمليئة بالضجيج. تقوم بتنفيذ عدة طرق للتحسين القائم على النماذج، وتشمل استبدالًا لـ GridSearchCV أو RandomizedSearchCV لإجراء بحث معلمات مع عبور التحقق باستخدام أي من هذه الاستراتيجيات.

- sklearn-deap: استخدام الخوارزميات التطورية بدلاً من البحث الشبكي في Scikit-learn.

**تصدير النماذج للإنتاج**

- sklearn-onnx: تسلسل العديد من خطوط أنابيب Scikit-learn إلى ONNX للتبادل والتنبؤ.

- skops.io: نموذج استمرارية أكثر أمانًا من pickle، يمكن استخدامه بدلاً من pickle في معظم الحالات الشائعة.

- sklearn2pmml: تسلسل مجموعة متنوعة واسعة من محولات ومقدّرات Scikit-learn إلى PMML بمساعدة مكتبة JPMML-SkLearn.

- sklearn-porter: ترجمة نماذج Scikit-learn المدربة إلى C وJava وJavaScript ولغات أخرى.

- m2cgen: مكتبة خفيفة الوزن تسمح بترجمة نماذج التعلم الآلي المدربة، بما في ذلك العديد من تقديرات Scikit-learn، إلى كود أصلي لـ C وJava وGo وR وPHP وDart وHaskell وRust ولغات برمجة أخرى.

- treelite: يقوم بتجميع نماذج المجموعة المستندة إلى الشجرة إلى كود C لتقليل زمن التنبؤ.

- micromlgen: تجلب MicroML خوارزميات التعلم الآلي إلى المتحكمات الدقيقة. يدعم العديد من مصنفات Scikit-learn عن طريق ترجمتها إلى كود C.

- emlearn: ينفذ تقديرات Scikit-learn في C99 للأجهزة المدمجة والمتحكمات الدقيقة. يدعم عدة نماذج للتصنيف والانحدار واكتشاف العلامات الخارجية.

**معدل إنتاج النماذج**

- Intel(R) Extension for scikit-learn: على أجهزة Intel(R) عالية الأداء بشكل أساسي، يقوم بتسريع بعض نماذج Scikit-learn لكل من التدريب والاستدلال في ظل ظروف معينة. يتم الحفاظ على هذا المشروع بواسطة Intel(R)، ولا يشارك القائمون على صيانة Scikit-learn في تطوير هذا المشروع. كما تجدر الإشارة إلى أنه في بعض الحالات، قد يؤدي استخدام الأدوات والتقديرات الموجودة في "scikit-learn-intelex" إلى نتائج مختلفة عن تلك الموجودة في "scikit-learn" نفسه. إذا واجهت مشكلات أثناء استخدام هذا المشروع، تأكد من الإبلاغ عن المشكلات المحتملة في مستودعاتها الخاصة.

مقدّرات ومهام أخرى
بالتأكيد! فيما يلي ترجمة للنص المحدد من ReStructuredText إلى اللغة العربية:

ليس كل شيء ينتمي أو ناضج بما يكفي لمشروع scikit-learn الأساسي. فيما يلي بعض المشاريع التي توفر واجهات مماثلة لـ scikit-learn لخوارزميات التعلم الإضافية والبنى التحتية والمهام.

**السلاسل الزمنية والتنبؤ**

- `Darts <https://unit8co.github.io/darts/>`_ : مكتبة بايثون للتنبؤ والكشف عن الانحرافات في السلاسل الزمنية. تحتوي على مجموعة متنوعة من النماذج، من الكلاسيكيات مثل ARIMA إلى الشبكات العصبية العميقة. يمكن استخدام جميع نماذج التنبؤ بنفس الطريقة، باستخدام وظائف fit() وpredict() ، المشابهة لـ scikit-learn.

- `sktime <https://github.com/alan-turing-institute/sktime>`_ : صندوق أدوات متوافق مع scikit-learn للتعلم الآلي مع السلاسل الزمنية بما في ذلك تصنيف/انحدار السلاسل الزمنية والتنبؤ (الإشراف/لوحة).

- `skforecast <https://github.com/JoaquinAmatRodrigo/skforecast>`_ : مكتبة بايثون تسهل استخدام منقحات scikit-learn كمتنبئين متعدد الخطوات. كما أنه يعمل مع أي منقح متوافق مع واجهة برمجة تطبيقات scikit-learn.

- `tslearn <https://github.com/tslearn-team/tslearn>`_ : مكتبة تعلم آلي للسلاسل الزمنية توفر أدوات للتحضير واستخراج الميزات، بالإضافة إلى نماذج مخصصة للتجميع والتصنيف والانحدار.

**تعزيز التدرج (الشجرة)**

ملاحظة: لدى scikit-learn معززات التدرج الحديثة الخاصة بها: :class:`~sklearn.ensemble.HistGradientBoostingClassifier` و:class:`~sklearn.ensemble.HistGradientBoostingRegressor`.

- `XGBoost <https://github.com/dmlc/xgboost>`_ : XGBoost هي مكتبة معززة للتوزيع التدريجي مصممة لتكون فعالة ومرنة وقابلة للتنقل.

- `LightGBM <https://lightgbm.readthedocs.io>`_ : LightGBM هو إطار عمل لتعزيز التدرج يستخدم خوارزميات التعلم الشجري. تم تصميمه لتوزيع وكفاءة.

**التعلم المنظم**

- `HMMLearn <https://github.com/hmmlearn/hmmlearn>`_ : تنفيذ نماذج ماركوف المخفية التي كانت في السابق جزءًا من scikit-learn.

- `PyStruct <https://pystruct.github.io>`_ : حقول ماركوف الشرطية العامة والتنبؤ المنظم.

- `pomegranate <https://github.com/jmschrei/pomegranate>`_ : النمذجة الاحتمالية للبايثون، مع التركيز على نماذج ماركوف المخفية.

- `sklearn-crfsuite <https://github.com/TeamHG-Memex/sklearn-crfsuite>`_ : حقول ماركوف الشرطية الخطية (`CRFsuite <http://www.chokkan.org/software/crfsuite/>`_ wrapper with sklearn-like API).

**الشبكات العصبية العميقة، إلخ.**

- `skorch <https://github.com/dnouri/skorch>`_ : مكتبة شبكات عصبية متوافقة مع scikit-learn والتي تغلف PyTorch.

- `scikeras <https://github.com/adriangb/scikeras>`_ : يوفر غلافًا حول Keras للواجهة مع scikit-learn. SciKeras هو الخلف لـ `tf.keras.wrappers.scikit_learn`.

**التعلم الاتحادي**

- `Flower <https://flower.dev/>`_ : إطار عمل تعلم اتحادي ودود مع نهج موحد يمكنه الاتحاد مع أي حمل عمل، وأي إطار عمل للتعلم الآلي، وأي لغة برمجة.

**التعلم الآلي لحماية الخصوصية**

- `Concrete ML <https://github.com/zama-ai/concrete-ml/>`_ : إطار عمل للتعلم الآلي لحماية الخصوصية مبني على `Concrete <https://github.com/zama-ai/concrete>`_ ، مع ارتباطات بإطارات عمل التعلم الآلي التقليدية، بفضل التشفير المتجانس تمامًا. واجهات برمجة التطبيقات الخاصة بما يسمى النماذج المدمجة في Concrete ML قريبة جدًا من واجهات برمجة تطبيقات scikit-learn.

**نطاق واسع**

- `mlxtend <https://github.com/rasbt/mlxtend>`_ : يتضمن عددًا من المقدرات الإضافية بالإضافة إلى برامج مساعدة لتصور النماذج.

- `scikit-lego <https://github.com/koaning/scikit-lego>`_ : عدد من المحولات والمقاييس والنماذج المتوافقة مع scikit-learn، مع التركيز على حل مهام الصناعة العملية.

**الانحدار والتصنيف الآخر**

- `ML-Ensemble <https://mlens.readthedocs.io/>`_ : التعلم التجميعي المعمم (التكديس، المزج، subsemble، التجميعات العميقة، إلخ).

- `lightning <https://github.com/scikit-learn-contrib/lightning>`_ : محلات النماذج الخطية السريعة ذات الحالة الفنية (SDCA، AdaGrad، SVRG، SAG، إلخ...).

- `py-earth <https://github.com/scikit-learn-contrib/py-earth>`_ : الانحدار متعدد المتغيرات للسبل التكيفية.

- `gplearn <https://github.com/trevorstephens/gplearn>`_ : البرمجة الوراثية للمهام الانحدار الرمزية.

- `scikit-multilearn <https://github.com/scikit-multilearn/scikit-multilearn>`_ : التصنيف متعدد التصنيفات مع التركيز على التلاعب في مساحة التسمية.

- `seglearn <https://github.com/dmbee/seglearn>`_ : التعلم التسلسلي والتعلم التسلسلي باستخدام التجزئة النافذة المنزلقة.

- `fastFM <https://github.com/ibayer/fastFM>`_ : تنفيذ عامل التصفية السريع المتوافق مع scikit-learn

**التحليل والتجميع**

- `lda <https://github.com/lda-project/lda/>`_ : تنفيذ سريع لتخصيص ديريتشليت الكامن في Cython والذي يستخدم `Gibbs sampling <https://en.wikipedia.org/wiki/Gibbs_sampling>`_ لأخذ العينات من التوزيع الاحتمالي الحقيقي. (يستخدم تنفيذ scikit-learn :class:`~sklearn.decomposition.LatentDirichletAllocation` `التفكير المتغير <https://en.wikipedia.org/wiki/Variational_Bayesian_methods>`_ لأخذ العينات من تقريب قابل للتعقب لتوزيع الموضوع اللاحق.)

- `kmodes <https://github.com/nicodv/kmodes>`_ : خوارزمية k-modes clustering للبيانات الفئوية، وعدد من تنوعاتها.

- `hdbscan <https://github.com/scikit-learn-contrib/hdbscan>`_ : خوارزميات HDBSCAN وRobust Single Linkage clustering للتجميع متغير الكثافة المتين. اعتبارًا من إصدار scikit-learn 1.3.0، هناك :class:`~sklearn.cluster.HDBSCAN`.

- `spherecluster <https://github.com/clara-labs/spherecluster>`_ : إجراءات التجميع الكروي K-means ومزيج von Mises Fisher للبيانات الموجودة على hypersphere الوحدة.

**معالجة مسبقة**

- `categorical-encoding <https://github.com/scikit-learn-contrib/categorical-encoding>`_ : مكتبة من encoders الفئوية المتوافقة مع sklearn. اعتبارًا من إصدار scikit-learn 1.3.0، هناك :class:`~sklearn.preprocessing.TargetEncoder`.

- `imbalanced-learn <https://github.com/scikit-learn-contrib/imbalanced-learn>`_ : طرق مختلفة لأسفل وأخذ عينات من مجموعات البيانات.

- `Feature-engine <https://github.com/solegalli/feature_engine>`_ : مكتبة من المحولات المتوافقة مع sklearn لملء البيانات المفقودة، والترميز الفئوي، وتحويل المتغيرات، والتقسيم، ومعالجة القيم الشاذة، والمزيد. تسمح Feature-engine بتطبيق خطوات المعالجة المسبقة على مجموعات متغيرة مختارة وهي متوافقة تمامًا مع خط أنابيب Scikit-learn.

**تحليل البيانات الطوبولوجية**

- `giotto-tda <https://github.com/giotto-ai/giotto-tda>`_ : مكتبة لتحليل البيانات الطوبولوجية تهدف إلى توفير واجهة برمجة تطبيقات متوافقة مع scikit-learn. فهو يوفر أدوات لتحويل إدخالات البيانات (سحب النقاط، والرسوم البيانية، والسلاسل الزمنية، والصور) إلى أشكال مناسبة لحسابات الملخصات الطوبولوجية، ومكونات مخصصة لاستخراج مجموعات من الميزات ذات الأصل الطوبولوجي، والتي يمكن استخدامها جنبًا إلى جنب مع طرق استخراج الميزات الأخرى في scikit-learn.

التعلم الإحصائي مع بايثون
--------------------------
حزم أخرى مفيدة لتحليل البيانات والتعلم الآلي.

- `Pandas <https://pandas.pydata.org/>`_ : أدوات للعمل مع البيانات غير المتجانسة والعمودية، والاستعلامات العلائقية، والسلاسل الزمنية والإحصاءات الأساسية.

- `statsmodels <https://www.statsmodels.org>`_ : تقدير وتحليل النماذج الإحصائية. يركز أكثر على الاختبارات الإحصائية وأقل على التنبؤ من scikit-learn.

- `PyMC <https://www.pymc.io/>`_ : النماذج الإحصائية الباييسية وخوارزميات التجهيز.

- `Seaborn <https://stanford.edu/~mwaskom/software/seaborn/>`_ : مكتبة عرض مستندة إلى matplotlib. يوفر واجهة عالية المستوى لرسم الرسومات الإحصائية الجذابة.

- `scikit-survival <https://scikit-survival.readthedocs.io/>`_ : مكتبة لتنفيذ النماذج للتعلم من بيانات وقت الحدث الخاضعة للرقابة (يطلق عليها أيضًا تحليل البقاء). النماذج متوافقة تمامًا مع scikit-learn.

حزم محرك التوصية
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `implicit <https://github.com/benfred/implicit>`_ ، مكتبة لمجموعات التعليقات غير المباشرة.

- `lightfm <https://github.com/lyst/lightfm>`_ : تنفيذ Python/Cython لنظام التوصية الهجين.

- `OpenRec <https://github.com/ylongqi/openrec>`_ : خوارزميات التوصية المستوحاة من الشبكات العصبية القائمة على TensorFlow.

- `Surprise Lib <https://surpriselib.com/>`_ : مكتبة لمجموعات التعليقات المباشرة.

الحزم المحددة المجال
~~~~~~~~~~~~~~~~~~~~~~~~

- `scikit-network <https://scikit-network.readthedocs.io/>`_ : التعلم الآلي على الرسوم البيانية.

- `scikit-image <https://scikit-image.org/>`_ : معالجة الصور والرؤية الحاسوبية في بايثون.

- `Natural language toolkit (nltk) <https://www.nltk.org/>`_ : معالجة اللغة الطبيعية وبعض التعلم الآلي.

- `gensim <https://radimrehurek.com/gensim/>`_ : مكتبة لوضع نماذج الموضوعات وفهرسة الوثائق واسترجاع التشابه.

- `NiLearn <https://nilearn.github.io/>`_ : التعلم الآلي للتصوير العصبي.

- `AstroML <https://www.astroml.org/>`_ : التعلم الآلي لعلم الفلك.

ترجمات وثائق scikit-learn
------------------------------------------

الغرض من الترجمة هو تسهيل القراءة والفهم بلغات أخرى غير اللغة الإنجليزية. تهدف إلى مساعدة الأشخاص الذين لا يفهمون اللغة الإنجليزية أو لديهم شكوك بشأن تفسيرها. بالإضافة إلى ذلك، يفضل بعض الأشخاص قراءة الوثائق بلغتهم الأم، ولكن يرجى ملاحظة أن الوثائق الرسمية الوحيدة هي الوثائق باللغة الإنجليزية [#f1]_.

هذه الجهود الترجمية هي مبادرات مجتمعية وليس لدينا أي سيطرة عليها.
إذا كنت تريد المساهمة أو الإبلاغ عن مشكلة في الترجمة، يرجى الاتصال بمؤلفي الترجمة.
ترتبط بعض الترجمات المتوفرة هنا لتحسين نشرها وتعزيز جهود المجتمع.

- `الترجمة الصينية <https://sklearn.apachecn.org/>`_
  (`source <https://github.com/apachecn/sklearn-doc-zh>`__)
- `الترجمة الفارسية <https://sklearn.ir/>`_
  (`source <https://github.com/mehrdad-dev/scikit-learn>`__)
- `الترجمة الإسبانية <https://qu4nt.github.io/sklearn-doc-es/>`_
  (`source <https://github.com/qu4nt/sklearn-doc-es>`__)
- `الترجمة الكورية <https://panda5176.github.io/scikit-learn-korean/>`_
  (`source <https://github.com/panda5176/scikit-learn-korean>`__)


.. rubric:: Footnotes

.. [#f1] following `linux documentation Disclaimer
   <https://www.kernel.org/doc/html/latest/translations/index.html#disclaimer>`__