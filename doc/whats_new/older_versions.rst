.. include:: _contributors.rst

.. currentmodule:: sklearn

==============
الإصدارات القديمة
==============

.. _changes_0_12.1:

الإصدار 0.12.1
===============

**8 أكتوبر 2012**

إصدار 0.12.1 هو إصدار إصلاح الأخطاء ولا يحتوي على ميزات إضافية، ولكنه بدلاً من ذلك مجموعة من إصلاحات الأخطاء

سجل التغييرات
----------

- تحسين الاستقرار العددي في التضمين الطيفي بواسطة `Gael Varoquaux`_

- Doctest في نظام التشغيل Windows 64 بت بواسطة `Gael Varoquaux`_

- إصلاحات التوثيق لشبكة مطاطية بواسطة `Andreas Müller`_ و`Alexandre Gramfort`_

- السلوك الصحيح مع صفائف NumPy ذات الترتيب الحصري بواسطة `Gael Varoquaux`_

- اجعل GridSearchCV يعمل مع مصفوفة متقطعة غير CSR بواسطة `Lars Buitinck`_

- إصلاح الحوسبة المتوازية في MDS بواسطة `Gael Varoquaux`_

- إصلاح دعم Unicode في محول الكلمات إلى أرقام بواسطة `Andreas Müller`_

- إصلاح MinCovDet الذي يتسبب في حدوث خطأ مع X.shape = (3، 1) بواسطة: user: `Virgile Fritsch <VirgileFritsch>`

- إصلاح الاستنساخ من كائنات SGD بواسطة `Peter Prettenhofer`_

- استقرار GMM بواسطة: user: `Virgile Fritsch <VirgileFritsch>`

الأشخاص
------

* 14 `Peter Prettenhofer`_
* 12 `Gael Varoquaux`_
* 10 `Andreas Müller`_
* 5 `Lars Buitinck`_
* 3: user: `Virgile Fritsch <VirgileFritsch>`
* 1 `Alexandre Gramfort`_
* 1 `Gilles Louppe`_
* 1 `Mathieu Blondel`_

.. _changes_0_12:

الإصدار 0.12
============

**4 سبتمبر 2012**

سجل التغييرات
---------

- تحسينات سرعة مختلفة في وحدة :ref: `<tree>`، بواسطة `Gilles Louppe`_.

- :class: `~ensemble.GradientBoostingRegressor` و: class: `~ensemble.GradientBoostingClassifier` الآن يدعمان الاستخلاص الفرعي للميزات عبر حجة "max_features"، بواسطة `Peter Prettenhofer`_.

- تمت إضافة دالة هابر وخسارة الكمية إلى: class: `~ensemble.GradientBoostingRegressor`، بواسطة `Peter Prettenhofer`_.

- :ref: `<tree>` و: ref: `<forest>` الآن يدعمان مشكلات التصنيف والانحدار متعددة الإخراج، بواسطة `Gilles Louppe`_.

- تمت الإضافة: class: `~preprocessing.LabelEncoder`، فئة أداة بسيطة لتطبيع التسميات أو تحويل التسميات غير الرقمية، بواسطة `Mathieu Blondel`_.

- تمت الإضافة: ref: `<sgd>`، بواسطة `Mathieu Blondel`_.

- تمت الإضافة: ref: `<multidimensional_scaling>`، بواسطة Nelle Varoquaux.

- محمل تنسيق ملف SVMlight يكتشف الآن الملفات المضغوطة (gzip/bzip2) ويقوم بفك ضغطها أثناء التنقل، بواسطة `Lars Buitinck`_.

- محول تنسيق ملف SVMlight يحافظ الآن على قيم النقطة العائمة ذات الدقة المزدوجة، بواسطة `Olivier Grisel`_.

- تمت إضافة إطار عمل اختبار مشترك لجميع التقديرات، بواسطة `Andreas Müller`_.

- رسائل خطأ مفهومة للمقدّرات التي لا تقبل الإدخال المتقطع بواسطة `Gael Varoquaux`_

- تسريع في التجميع الهرمي بواسطة `Gael Varoquaux`_. على وجه الخصوص، يدعم بناء الشجرة الآن التوقف المبكر. هذا مفيد عندما يكون عدد المجموعات ليس صغيرًا مقارنة بعدد العينات.

- أضف MultiTaskLasso وMultiTaskElasticNet لاختيار الميزات المشتركة، بواسطة `Alexandre Gramfort`_.

- تمت إضافة `metrics.auc_score` و: func: `metrics.average_precision_score` بواسطة `Andreas Müller`_.

- تحسين دعم المصفوفة المتقطعة في وحدة: ref: `<feature_selection>` بواسطة `Andreas Müller`_.

- محلل n-gram المستند إلى حدود الكلمات الجديد لوحدة: ref: `<text_feature_extraction>` بواسطة: user: `@kernc <kernc>`.

- إصلاح خطأ في التجميع الطيفي الذي أدى إلى حدوث مجموعات ذات نقطة واحدة بواسطة `Andreas Müller`_.

- في: class: `~feature_extraction.text.CountVectorizer`، تمت إضافة خيار لتجاهل الكلمات غير المتكررة، "min_df" بواسطة `Andreas Müller`_.

- أضف دعمًا لأهداف متعددة في بعض النماذج الخطية (ElasticNet وLasso وOrthogonalMatchingPursuit) بواسطة `Vlad Niculae`_ و`Alexandre Gramfort`_.

- الإصلاحات في دالة التهديف `decomposition.ProbabilisticPCA` بواسطة Wei Li.

- إصلاح حساب أهمية الميزة في: ref: `<gradient_boosting>`.

ملخص التغييرات في واجهة برمجة التطبيقات
-------------------

- اختفت الحزمة القديمة "scikits.learn"؛ يجب أن يستورد كل التعليمات البرمجية من "sklearn" بدلاً من ذلك، والتي تم تقديمها في 0.9.

- في: func: `metrics.roc_curve`، يتم الآن إرجاع مصفوفة "thresholds" مع عكس ترتيبها، للحفاظ على اتساقها مع ترتيب "fpr" و"tpr" المرتجعة.

- في كائنات "hmm"، مثل "hmm.GaussianHMM" و"hmm.MultinomialHMM"، يجب تمرير جميع المعلمات إلى الكائن عند تهيئته وليس من خلال "fit". الآن "fit" سيقبل فقط بيانات الإدخال كمعلمة.

- بالنسبة لجميع فئات SVM، تم إصلاح سلوك "gamma" المعيب. في السابق، تم حساب قيمة "gamma" الافتراضية فقط في المرة الأولى التي تم فيها استدعاء "fit" ثم تم تخزينها. يتم الآن إعادة حسابها في كل استدعاء لـ "fit".

- جميع الفئات "Base" هي الآن فئات مجردة بحيث لا يمكن إنشاء مثيل منها.

- :func: `cluster.ward_tree` الآن يعيد أيضًا مصفوفة الأب. هذا ضروري للتوقف المبكر، في هذه الحالة لا يتم بناء الشجرة بالكامل.

- في: class: `~feature_extraction.text.CountVectorizer`، تم دمج معلمات "min_n" و"max_n" في معلمة "n_gram_range" للسماح بالبحث الشبكي لكليهما في نفس الوقت.

- في: class: `~feature_extraction.text.CountVectorizer`، يتم الآن تجاهل الكلمات التي تظهر في وثيقة واحدة فقط بشكل افتراضي. لتكرار السلوك السابق، قم بتعيين "min_df=1".

- إصلاح عدم اتساق واجهة برمجة التطبيقات: :meth: `linear_model.SGDClassifier.predict_proba` الآن يعيد مصفوفة ثنائية الأبعاد عند التهيئة على فئتين.

- إصلاح عدم اتساق واجهة برمجة التطبيقات: :meth: `discriminant_analysis.QuadraticDiscriminantAnalysis.decision_function` و:meth: `discriminant_analysis.LinearDiscriminantAnalysis.decision_function` الآن يعيدان مصفوفات أحادية البعد عند التهيئة على فئتين.

- يتم الآن تخزين شبكة ألفا المستخدمة لتناسب: class: `~linear_model.LassoCV` و: class: `~linear_model.ElasticNetCV` في السمة "alphas_" بدلاً من تجاوز معلمة init "alphas".

- تخزن النماذج الخطية عند تقدير ألفا بواسطة التحقق من صحة متقاطعة القيمة المقدرة في السمة "alpha_" بدلاً من مجرد "alpha" أو "best_alpha".

- :class: `~ensemble.GradientBoostingClassifier` الآن يدعم: meth: `~ensemble.GradientBoostingClassifier.staged_predict_proba`، و: meth: `~ensemble.GradientBoostingClassifier.staged_predict`.

- `svm.sparse.SVC` وفئات SVM المتقطعة الأخرى أصبحت قديمة الآن. جميع الفئات في وحدة: ref: `<svm>` الآن تختار تلقائيًا التمثيل المتقطع أو الكثيف بناءً على الإدخال.

- تفسر جميع خوارزميات التجميع الآن المصفوفة "X" المقدمة إلى "fit" على أنها بيانات إدخال، على وجه الخصوص: class: `~cluster.SpectralClustering` و: class: `~cluster.AffinityPropagation` التي كانت تتوقع سابقًا مصفوفات التشابه.

- بالنسبة لخوارزميات التجميع التي تأخذ عدد المجموعات المرغوب كمعلمة، يُطلق على هذه المعلمة الآن "n_clusters".

الأشخاص
------
* 267 `Andreas Müller`_
* 94 `Gilles Louppe`_
* 89 `Gael Varoquaux`_
* 79 `Peter Prettenhofer`_
* 60 `Mathieu Blondel`_
* 57 `Alexandre Gramfort`_
* 52 `Vlad Niculae`_
* 45 `Lars Buitinck`_
* 44 Nelle Varoquaux
* 37 `Jaques Grobler`_
* 30 Alexis Mignon
* 30 Immanuel Bayer
* 27 `Olivier Grisel`_
* 16 Subhodeep Moitra
* 13 Yannick Schwartz
* 12: user: `@kernc <kernc>`
* 11: user: `Virgile Fritsch <VirgileFritsch>`
* 9 Daniel Duckworth
* 9 `Fabian Pedregosa`_
* 9 `Robert Layton`_
* 8 John Benediktsson
* 7 Marko Burjek
* 5 `Nicolas Pinto`_
* 4 Alexandre Abraham
* 4 `Jake Vanderplas`_
* 3 `Brian Holt`_
* 3 `Edouard Duchesnay`_
* 3 Florian Hoenig
* 3 flyingimmidev
* 2 Francois Savard
* 2 Hannes Schulz
* 2 Peter Welinder
* 2 `Yaroslav Halchenko`_
* 2 Wei Li
* 1 Alex Companioni
* 1 Brandyn A. White
* 1 Bussonnier Matthias
* 1 Charles-Pierre Astolfi
* 1 Dan O'Huiginn
* 1 David Cournapeau
* 1 Keith Goodman
* 1 Ludwig Schwardt
* 1 Olivier Hervieu
* 1 Sergio Medina
* 1 Shiqiao Du
* 1 Tim Sheerman-Chase
* 1 buguen

.. _changes_0_11:

الإصدار 0.11
**7 مايو 2012**

سجل التغييرات
----------------

أبرز التغييرات
................

- أشجار الانحدار المعززة بالتدرج (: ref: `gradient_boosting`)
  للتصنيف والانحدار من قبل `Peter Prettenhofer`_
  و `Scott White`_.

- محمل ميزات بسيط يعتمد على القاموس مع دعم للمتغيرات الفئوية
  (: class: ~ feature_extraction.DictVectorizer) من قبل `Lars Buitinck`_.

- تمت إضافة معامل ارتباط Matthews (: func: `metrics.matthews_corrcoef`)
  وخيارات المتوسط الكلي والجزئي إلى
  : func: ~ metrics.precision_score`، : func: `metrics.recall_score` و
  : func: ~ metrics.f1_score` من قبل `Satrajit Ghosh`_.

- : ref: `out_of_bag` من خطأ التعميم لـ : ref: `ensemble`
  من قبل `Andreas Müller`_.

- النماذج الخطية المتناثرة العشوائية لاختيار الميزات، من قبل `Alexandre Gramfort`_ و `Gael Varoquaux`_

- : ref: `label_propagation` للتعلم شبه المُشرف، من قبل Clay
  Woolam. **ملاحظة** لا يزال واجهة برمجة التطبيقات شبه المُشرف قيد التقدم
  وقد يتغير.

- تمت إضافة BIC/AIC اختيار النموذج إلى : ref: `gmm` الكلاسيكي ووحدة نمطية
  وحدد واجهة برمجة التطبيقات مع بقية scikit-learn، من قبل `Bertrand Thirion`_

- تمت إضافة `sklearn.cross_validation.StratifiedShuffleSplit`، وهو
  `sklearn.cross_validation.ShuffleSplit` مع تقسيمات متوازنة،
  من قبل Yannick Schwartz.

- تم إضافة : class: ~ sklearn.neighbors.NearestCentroid` classifier، إلى جانب
  معلمة "shrink_threshold"، والتي تنفذ **تصنيف النقاط المركزية المنكمشة**، من قبل `Robert Layton`_.

التغييرات الأخرى
..................

- تم دمج التنفيذ الكثيف والمُبعثر لـ : ref: `sgd` module وتم
  عرض أنواع امتدادات المنفعة لمجموعات البيانات التسلسلية "seq_dataset"
  ومتجهات الأوزان "weight_vector"
  من قبل `Peter Prettenhofer`_.

- تمت إضافة "partial_fit" (دعم التعلم عبر الإنترنت/الميني باتش) و
  "warm_start" إلى : ref: `sgd` module من قبل `Mathieu Blondel`_.

- تم دمج التنفيذ الكثيف والمُبعثر لـ : ref: `svm` classes و
  : class: ~ linear_model.LogisticRegression` من قبل `Lars Buitinck`_.

- يمكن الآن استخدام المتنبئين كخوارزمية تقدير أساسية في : ref: `multiclass`
  module من قبل `Mathieu Blondel`_.

- تمت إضافة خيار "n_jobs" إلى : func: `metrics.pairwise_distances`
  و : func: `metrics.pairwise.pairwise_kernels` للحساب المتوازي،
  من قبل `Mathieu Blondel`_.

- يمكن الآن تشغيل : ref: `k_means` بشكل متوازٍ، باستخدام حجة "n_jobs"
  إما إلى : ref: `k_means` أو : class: `cluster.KMeans`، من قبل `Robert Layton`_.

- تم تحسين : ref: `cross_validation` و : ref: `grid_search` الوثائق
  وتم تقديم دالة المساعدة الجديدة `cross_validation.train_test_split`
  من قبل `Olivier Grisel`_

- تم تغيير علامة الأعضاء "coef_" و "intercept_" في : class: ~ svm.SVC`
  من أجل الاتساق مع "decision_function"؛ بالنسبة لـ "kernel==linear"،
  تم إصلاح "coef_" في حالة one-vs-one، من قبل `Andreas Müller`_.

- تحسينات الأداء للانحدار Ridge المتقاطع مع ترك واحد، وخاصةً لحالة
  "n_samples > n_features"، في : class: ~ linear_model.RidgeCV، من قبل Reuben Fletcher-Costin.

- إعادة هيكلة وتبسيط واجهة برمجة التطبيقات : ref: `text_feature_extraction`
  وإصلاح خطأ قد يتسبب في قيمة IDF سالبة،
  من قبل `Olivier Grisel`_.

- تمت إزالة خيار تشذيب الشعاع في وحدة نمطية `_BaseHMM` لأنه
  من الصعب تحويله إلى Cython. إذا كنت مهتمًا بالمساهمة في إصدار Cython،
  فيمكنك استخدام إصدار Python في تاريخ Git كمرجع.

- تدعم الفئات في : ref: `neighbors` الآن متري مينكوفسكي التعسفي لعمليات البحث عن أقرب جار.
  يمكن تحديد المقياس من خلال وسيط "p".

ملخص التغييرات في واجهة برمجة التطبيقات
------------------------------------

- `covariance.EllipticEnvelop` أصبح الآن قديمًا.
  يرجى استخدام : class: ~ covariance.EllipticEnvelope بدلاً من ذلك.

- تمت إزالة "NeighborsClassifier" و "NeighborsRegressor" في الوحدة النمطية
  : ref: `neighbors`. استخدم الفئات : class: ~ neighbors.KNeighborsClassifier`،
  : class: ~ neighbors.RadiusNeighborsClassifier`، : class: ~ neighbors.KNeighborsRegressor`
  و/أو : class: ~ neighbors.RadiusNeighborsRegressor` بدلاً من ذلك.

- أصبحت الفئات المُبعثرة في الوحدة النمطية : ref: `sgd` قديمة الآن.

- في `mixture.GMM`، `mixture.DPGMM` و `mixture.VBGMM`،
  يجب تمرير المعلمات إلى كائن عند تهيئته وليس من خلال
  "fit". الآن "fit" سيقبل فقط البيانات كمعلمة إدخال.

- أصبحت الطرق "rvs" و "decode" في وحدة نمطية `GMM` قديمة الآن.
  يجب استخدام "sample" و "score" أو "predict" بدلاً من ذلك.

- أصبحت الخاصية "scores_" و "pvalues_" في كائنات اختيار الميزات أحادية المتغير قديمة الآن.
  يجب استخدام "scores_" أو "pvalues_" بدلاً من ذلك.

- في : class: ~ linear_model.LogisticRegression`، : class: ~ svm.LinearSVC`،
  : class: ~ svm.SVC` و : class: ~ svm.NuSVC`، أصبحت معلمة "class_weight"
  الآن معلمة تهيئة، وليست معلمة لضبط النموذج. يجعل هذا الأمر ممكنًا
  البحث الشبكي عبر هذه المعلمة.

- الآن "data" في LFW دائمًا على شكل "n_samples، n_features" ليكون
  متسقًا مع مجموعة بيانات وجوه Olivetti. استخدم الخاصية "images" و
  "pairs" للوصول إلى الأشكال الصورية الطبيعية بدلاً من ذلك.

- في : class: ~ svm.LinearSVC`، تغير معنى معلمة "multi_class".
  الخيارات الآن هي "ovr" و "crammer_singer"، مع
  "ovr" كخيار افتراضي. لا يغير هذا السلوك الافتراضي ولكنه
  من المفترض أن يكون أقل إرباكًا.

- أصبحت فئة `feature_selection.text.Vectorizer` قديمة واستبدلت
  بـ `feature_selection.text.TfidfVectorizer`.

- تمت إزالة البنية المُعششة للمُهيئ/المُحلل لاستخراج ميزات النص. كل هذه الميزات
  يتم الآن تمريرها مباشرةً كوسيطات مسطحة لبناء
  `feature_selection.text.TfidfVectorizer` و
  `feature_selection.text.CountVectorizer`، وعلى وجه التحديد الوسيطات التالية
  يتم استخدامها الآن:

- يمكن أن يكون "analyzer" "word" أو "char" للتبديل بين مخطط التحليل الافتراضي،
  أو استخدام دالة Python قابلة للاستدعاء (كما كان من قبل).

- تم تقديم "tokenizer" و "preprocessor" لجعل تخصيص هذه الخطوات
  ممكنًا مع واجهة برمجة التطبيقات الجديدة.

- يتحكم "input" بشكل صريح في كيفية تفسير التسلسل الذي تم تمريره إلى
  "fit" و "predict": أسماء الملفات، أو كائنات الملفات، أو السلاسل (البايتات أو
  يونيكود) مباشرةً.

- ترميز الأحرف صارم بشكل افتراضي.

- يتم الآن تخزين القاموس، سواء تم ضبطه أم لا، في
  خاصية "vocabulary_" ليكون متسقًا مع اتفاقيات المشروع.

- تستمد فئة `feature_selection.text.TfidfVectorizer` الآن مباشرةً
  من `feature_selection.text.CountVectorizer` لجعل البحث الشبكي
  بسيطًا.

- أصبحت الطرق "rvs" في وحدة نمطية `_BaseHMM` قديمة الآن.
  يجب استخدام "sample" بدلاً من ذلك.

- تمت إزالة خيار تشذيب الشعاع في وحدة نمطية `_BaseHMM` لأنه
  من الصعب تحويله إلى Cython. إذا كنت مهتمًا، فيمكنك الاطلاع على
  رموز التاريخ باستخدام Git.

- يدعم محمل تنسيق SVMlight الآن الملفات ذات المؤشرات العمودية المستندة إلى الصفر والواحد،
  حيث أن كلا النوعين موجود "في البرية".

- أصبحت وسيطات الفئة : class: ~ model_selection.ShuffleSplit` الآن متسقة مع
  : class: ~ model_selection.StratifiedShuffleSplit`. أصبحت وسيطات "test_fraction" و
  "train_fraction" قديمة وتمت إعادة تسميتها إلى "test_size" و
  "train_size" ويمكن أن تقبل كلاً من "float" و "int".

- أصبحت وسيطات الفئة `Bootstrap` الآن متسقة مع
  : class: ~ model_selection.StratifiedShuffleSplit`. أصبحت وسيطات "n_test" و
  "n_train" قديمة وتمت إعادة تسميتها إلى "test_size" و
  "train_size" ويمكن أن تقبل كلاً من "float" و "int".

- تمت إضافة وسيط "p" إلى الفئات في : ref: `neighbors` لتحديد
  متري مينكوفسكي التعسفي لعمليات البحث عن أقرب جار.

المساهمون
----------

* 282  `Andreas Müller`_
* 239  `Peter Prettenhofer`_
* 198  `Gael Varoquaux`_
* 129  `Olivier Grisel`_
* 114  `Mathieu Blondel`_
* 103  Clay Woolam
*  96  `Lars Buitinck`_
*  88  `Jaques Grobler`_
*  82  `Alexandre Gramfort`_
*  50  `Bertrand Thirion`_
*  42  `Robert Layton`_
*  28  flyingimmidev
*  26  `Jake Vanderplas`_
*  26  Shiqiao Du
*  21  `Satrajit Ghosh`_
*  17  `David Marek`_
*  17  `Gilles Louppe`_
*  14  `Vlad Niculae`_
*  11  Yannick Schwartz
*  10  `Fabian Pedregosa`_
*   9  fcostin
*   7  Nick Wilson
*   5  Adrien Gaidon
*   5  `Nicolas Pinto`_
*   4  `David Warde-Farley`_
*   5  Nelle Varoquaux
*   5  Emmanuelle Gouillart
*   3  Joonas Sillanpää
*   3  Paolo Losi
*   2  Charles McCarthy
*   2  Roy Hyunjin Han
*   2  Scott White
*   2  ibayer
*   1  Brandyn White
*   1  Carlos Scheidegger
*   1  Claire Revillet
*   1  Conrad Lee
*   1  `Edouard Duchesnay`_
*   1  Jan Hendrik Metzen
*   1  Meng Xinfan
*   1  `Rob Zinkov`_
*   1  Shiqiao
*   1  Udi Weinsberg
*   1  Virgile Fritsch
*   1  Xinfan Meng
*   1  Yaroslav Halchenko
*   1  jansoe
*   1  Leon Palafox
**11 يناير 2012**

سجل التغييرات
----------------

- تم التخلي عن التوافق مع بايثون 2.5؛ حيث أصبحت أقل نسخة بايثون مطلوبة لاستخدام سكايت-ليرن هي 2.6.

- :ref: تم إضافة تقدير `sparse_inverse_covariance` باستخدام Graph Lasso، مع مُقدِّر مُعاير مُتقاطع مرتبط، بواسطة `Gael Varoquaux`_.

- إضافة نموذج جديد :ref:`Tree <tree>` بواسطة `Brian Holt`_، `Peter Prettenhofer`_، `Satrajit Ghosh`_ و`Gilles Louppe`_. يأتي النموذج مع توثيق وأمثلة كاملة.

- إصلاح خطأ في وحدة RFE بواسطة `Gilles Louppe`_ (المشكلة #378).

- إصلاح تسرب في الذاكرة في وحدة :ref:`svm` بواسطة `Brian Holt`_ (المشكلة #367).

- جعل الاختبارات أسرع بواسطة `Fabian Pedregosa`_ وآخرون.

- إضافة معيار تقييم تحليل التجميع Silhouette Coefficient كـ :func:`~sklearn.metrics.silhouette_score` بواسطة Robert Layton.

- إصلاح خطأ في :ref:`k_means` في معالجة معامل ``n_init``: كان يتم تشغيل خوارزمية التجميع ``n_init`` مرة، ولكن كان يتم الاحتفاظ بالحل الأخير بدلاً من الحل الأفضل بواسطة `Olivier Grisel`_.

- إعادة تنظيم طفيفة في وحدة :ref:`sgd`؛ دمج طرق التنبؤ الكثيفة والمتفرقة؛ تحسين أداء وقت الاختبار عن طريق تحويل معلمات النموذج إلى مصفوفات على الطريقة فورتان بعد التجهيز (فقط متعددة الفئات).

- إضافة معيار Mutual Information المُعدل كـ :func:`~sklearn.metrics.adjusted_mutual_info_score` بواسطة Robert Layton.

- النماذج مثل SVC/SVR/LinearSVC/LogisticRegression من libsvm/liblinear تدعم الآن تحجيم معامل C المنتظم حسب عدد العينات بواسطة `Alexandre Gramfort`_.

- إضافة نموذج جديد :ref:`Ensemble Methods <ensemble>` بواسطة `Gilles Louppe`_ و`Brian Holt`_. يأتي النموذج مع خوارزمية الغابة العشوائية وطريقة الأشجار الإضافية، بالإضافة إلى التوثيق والأمثلة.

- :ref:`outlier_detection`: اكتشاف القيم الشاذة والبيانات الجديدة، بواسطة :user:`Virgile Fritsch <VirgileFritsch>`.

- :ref:`kernel_approximation`: تحويل لتنفيذ تقريب النواة للـ SGD السريع على النواة غير الخطية بواسطة `Andreas Müller`_.

- إصلاح خطأ بسبب تبديل الذرات في :ref:`OMP` بواسطة `Vlad Niculae`_.

- :ref:`SparseCoder` بواسطة `Vlad Niculae`_.

- تحسينات أداء :ref:`mini_batch_kmeans` بواسطة `Olivier Grisel`_.

- إضافة دعم المصفوفات المتناثرة في :ref:`k_means` بواسطة `Mathieu Blondel`_.

- تحسين التوثيق للمطورين ولوحدة :mod:`sklearn.utils` بواسطة `Jake Vanderplas`_.

- تحميل مجموعة بيانات 20newsgroups المُجهزّة :func:`~sklearn.datasets.fetch_20newsgroups_vectorized` بواسطة `Mathieu Blondel`_.

- :ref:`multiclass` بواسطة `Lars Buitinck`_.

- إضافة مرافق للحساب السريع للمتوسط والانحراف المعياري للمصفوفات المتناثرة بواسطة `Mathieu Blondel`_.

- جعل :func:`~sklearn.preprocessing.scale` و`sklearn.preprocessing.Scaler` تعمل على المصفوفات المتناثرة بواسطة `Olivier Grisel`_

- أهمية الخصائص باستخدام أشجار القرار و/أو غابة الأشجار، بواسطة `Gilles Louppe`_.

- التنفيذ المتوازي لغابة الأشجار المُعشاة بواسطة `Gilles Louppe`_.

- يمكن لـ `sklearn.cross_validation.ShuffleSplit` أن تُعَيِّن عينات فرعية لمجموعات التدريب والاختبار بواسطة `Olivier Grisel`_.

- إصلاح أخطاء في بناء التوثيق بواسطة `Andreas Müller`_.

ملخص التغييرات في واجهة برمجة التطبيقات
------------------------------------

فيما يلي تعليمات ترحيل التعليمات البرمجية عند الترقية من إصدار سكايت-ليرن 0.9:

- كان لبعض المُقدِّرات التي قد تكتب فوق إدخالاتها لتوفير الذاكرة معلمات ``overwrite_``؛ تم استبدالها بمعلمات ``copy_`` بمعنى عكسي تمامًا.

  يؤثر هذا بشكل خاص على بعض المُقدِّرات في :mod:`~sklearn.linear_model`. لا يزال السلوك الافتراضي هو نسخ كل شيء يتم تمريره.

- لم يعد مُحمِّل مجموعة بيانات SVMlight :func:`~sklearn.datasets.load_svmlight_file` يدعم تحميل ملفين في نفس الوقت؛ استخدم ``load_svmlight_files`` بدلاً من ذلك. أيضًا، تم إزالة معامل (غير المستخدم) ``buffer_mb``.

- تستخدم المُقدِّرات المتناثرة في وحدة :ref:`sgd` متجه المعلمات الكثيفة ``coef_`` بدلاً من ``sparse_coef_``. هذا يحسن بشكل كبير أداء وقت الاختبار.

- تحتوي وحدة :ref:`covariance` الآن على مُقدِّر قوي لتغاير البيانات، وهو مُقدِّر Minimum Covariance Determinant.

- تمت إعادة تنظيم مقاييس تقييم التجميع في :mod:`~sklearn.metrics.cluster` ولكن التغييرات متوافقة مع الإصدارات السابقة. تم نقلها إلى `metrics.cluster.supervised`، جنبًا إلى جنب مع `metrics.cluster.unsupervised` التي تحتوي على معيار Silhouette Coefficient.

- الآن، تعمل دالة ``permutation_test_score`` بنفس طريقة ``cross_val_score`` (أي تستخدم متوسط الدرجات عبر الطيات).

- تستخدم مولدات التحقق من الصحة المتقاطع الآن مؤشرات رقمية (``indices=True``) بشكل افتراضي بدلاً من الأقنعة المنطقية. هذا يجعلها أكثر بداهة عند استخدامها مع بيانات المصفوفات المتناثرة.

- تم دمج الدوال المستخدمة للترميز المتناثر، ``sparse_encode`` و``sparse_encode_parallel``، في :func:`~sklearn.decomposition.sparse_encode``، وتم نقل أشكال المصفوفات للاتساق مع إعداد عاملي المصفوفات، بدلاً من إعداد الانحدار.

- إصلاح خطأ في التعامل مع ملفات SVMlight/LibSVM؛ يجب إعادة إنشاء الملفات التي تم إنشاؤها باستخدام :func:`~sklearn.datasets.dump_svmlight_file` (يجب أن تستمر في العمل، ولكنها تحتوي عن طريق الخطأ على عمود إضافي واحد من الأصفار مُسبقة الإلحاق).

- تم استبدال فئة ``BaseDictionaryLearning`` بـ ``SparseCodingMixin``.

- تمت إعادة تسمية `sklearn.utils.extmath.fast_svd` إلى :func:`~sklearn.utils.extmath.randomized_svd` وأصبح الإفراط في أخذ العينات الافتراضي الآن ثابتًا عند 10 متجهات عشوائية إضافية بدلاً من مضاعفة عدد المكونات التي سيتم استخراجها. يتبع السلوك الجديد الورقة المرجعية.

المساهمون
---------

ساهم الأشخاص التالية أسماؤهم في سكايت-ليرن منذ الإصدار الأخير:

* 246  `Andreas Müller`_
* 242  `Olivier Grisel`_
* 220  `Gilles Louppe`_
* 183  `Brian Holt`_
* 166  `Gael Varoquaux`_
* 144  `Lars Buitinck`_
*  73  `Vlad Niculae`_
*  65  `Peter Prettenhofer`_
*  64  `Fabian Pedregosa`_
*  60  Robert Layton
*  55  `Mathieu Blondel`_
*  52  `Jake Vanderplas`_
*  44  Noel Dawe
*  38  `Alexandre Gramfort`_
*  24  :user:`Virgile Fritsch <VirgileFritsch>`
*  23  `Satrajit Ghosh`_
*   3  Jan Hendrik Metzen
*   3  Kenneth C. Arnold
*   3  Shiqiao Du
*   3  Tim Sheerman-Chase
*   3  `Yaroslav Halchenko`_
*   2  Bala Subrahmanyam Varanasi
*   2  DraXus
*   2  Michael Eickenberg
*   1  Bogdan Trach
*   1  Félix-Antoine Fortin
*   1  Juan Manuel Caicedo Carvajal
*   1  Nelle Varoquaux
*   1  `Nicolas Pinto`_
*   1  Tiziano Zito
*   1  Xinfan Meng

.. _changes_0_9:

الإصدار 0.9
**21 سبتمبر 2011**

تم إصدار scikit-learn 0.9 في سبتمبر 2011، بعد ثلاثة أشهر من إصدار 0.8، ويشمل الوحدات النمطية الجديدة: :ref:`manifold`، :ref:`dirichlet_process`، بالإضافة إلى العديد من الخوارزميات الجديدة وتحسينات التوثيق.

يشمل هذا الإصدار أيضًا عمل تعلم القاموس الذي طوره `فلاد نيكولاي`_ كجزء من برنامج `Google Summer of Code <https://developers.google.com/open-source/gsoc>`_.

.. |banner1| image:: ../auto_examples/manifold/images/thumb/sphx_glr_plot_compare_methods_thumb.png
   :target: ../auto_examples/manifold/plot_compare_methods.html

.. |banner2| image:: ../auto_examples/linear_model/images/thumb/sphx_glr_plot_omp_thumb.png
   :target: ../auto_examples/linear_model/plot_omp.html

.. |banner3| image:: ../auto_examples/decomposition/images/thumb/sph0_glr_plot_kernel_pca_thumb.png
   :target: ../auto_examples/decomposition/plot_kernel_pca.html

.. |center-div| raw:: html

    <div style="text-align: center; margin: 0px 0 -5px 0;">

.. |end-div| raw:: html

    </div>

|center-div| |banner2| |banner1| |banner3| |end-div|

سجل التغييرات
---------

- وحدة نمطية جديدة :ref:`manifold` بواسطة `جيك فانديربلاس`_ و `فابيان بيدراجوسا`_.

- نموذج مزيج غاوسي لعملية ديريتشليت الجديدة :ref:`Dirichlet Process <dirichlet_process>` بواسطة `ألكسندر باسوس`_

- إعادة تنظيم وحدة نمطية :ref:`neighbors` بواسطة `جيك فانديربلاس`_: إعادة تنظيم عامة، ودعم المصفوفات المبعثرة في الإدخال، وتحسينات في السرعة والتوثيق. راجع القسم التالي للحصول على قائمة كاملة بتغييرات واجهة برمجة التطبيقات.

- تحسينات على وحدة نمطية :ref:`feature_selection` بواسطة `جيلز لوب`_: إعادة تنظيم فئات RFE، وإعادة كتابة التوثيق، وزيادة الكفاءة وتغييرات طفيفة على واجهة برمجة التطبيقات.

- :ref:`SparsePCA` بواسطة `فلاد نيكولاي`_، `غايل فارو`_ و `ألكسندر جرامفورت`_

- طباعة مُقدِّر الآن يتصرف بشكل مستقل عن البنى ومعماريات الإصدارات المختلفة من بايثون بفضل :user:`جان كوسايفي <JeanKossaifi>`.

- :ref:`محمل بتنسيق libsvm/svmlight <libsvm_loader>` بواسطة `ماثيو بلونديل`_ و `لارس بوتينيك`_

- تحسينات التوثيق: مصغرات في معرض الأمثلة بواسطة `فابيان بيدراجوسا`_.

- إصلاحات أخطاء مهمة في وحدة نمطية :ref:`svm` (segfaults، الأداء السيئ) بواسطة `فابيان بيدراجوسا`_.

- تمت الإضافة :ref:`multinomial_naive_bayes` و :ref:`bernoulli_naive_bayes` بواسطة `لارس بوتينيك`_

- عمليات تحسين استخراج ميزات النص بواسطة لارس بوتينيك

- اختيار الميزات باستخدام اختبار مربع كاي (:func:`feature_selection.chi2`) بواسطة `لارس بوتينيك`_.

- إعادة تنظيم وحدة نمطية :ref:`sample_generators` بواسطة `جيلز لوب`_

- :ref:`multiclass` بواسطة `ماثيو بلونديل`_

- إعادة كتابة شجرة الكرة بواسطة `جيك فانديربلاس`_

- تنفيذ خوارزمية :ref:`dbscan` بواسطة روبرت لايتون

- التنبؤ والتحويل باستخدام K-means بواسطة روبرت لايتون

- إعادة تنظيم وحدة معالجة مسبقة بواسطة `أوليفييه جريسيل`_

- Mean shift أسرع بواسطة كونراد لي

- إضافة "Bootstrap" جديدة، :ref:`ShuffleSplit` وتحسينات مختلفة أخرى في مخططات التحقق من الصحة المتقاطعة بواسطة `أوليفييه جريسيل`_ و `غايل فارو`_

- مؤشرات تقييم التجميع Adjusted Rand index و V-Measure بواسطة `أوليفييه جريسيل`_

- تمت الإضافة :class:`Orthogonal Matching Pursuit <linear_model.OrthogonalMatchingPursuit>` بواسطة `فلاد نيكولاي`_

- تمت الإضافة 2D-patch مستخرج المرافق في وحدة نمطية :ref:`feature_extraction` بواسطة `فلاد نيكولاي`_

- تنفيذ :class:`~linear_model.LassoLarsCV` (محلول Lasso المعبر عن طريق التحقق من صحة Lasso باستخدام خوارزمية Lars) و :class:`~linear_model.LassoLarsIC` (تحديد نماذج BIC/AIC في Lars) بواسطة `غايل فارو`_ و `ألكسندر جرامفورت`_

- تحسينات قابلية التوسع في :func:`metrics.roc_curve` بواسطة أوليفييه هيرفييو

- مساعدات المسافة :func:`metrics.pairwise_distances` و :func:`metrics.pairwise.pairwise_kernels` بواسطة روبرت لايتون

- :class:`Mini-Batch K-Means <cluster.MiniBatchKMeans>` بواسطة نيل فارو وكيتر وبيتر بريتنهوفر.

- خدمات mldata بواسطة بيترو بيركس.

- :ref:`olivetti_faces_dataset` بواسطة `ديفيد وارد فارلي`_.

ملخص تغييرات واجهة برمجة التطبيقات
-------------------

فيما يلي تعليمات ترحيل التعليمات البرمجية عند الترقية من إصدار scikit-learn 0.8:

- تمت إعادة تسمية حزمة "scikits.learn" إلى "sklearn". لا يزال هناك حزمة "scikits.learn" مستخدمة كاسم مستعار للتوافق مع الإصدارات السابقة.

يجب على المشاريع التابعة للطرف الثالث التي تعتمد على scikit-learn 0.9+ ترقية قاعدة التعليمات البرمجية الخاصة بها. على سبيل المثال، في Linux / MacOSX، قم ببساطة بتشغيل (قم بعمل نسخة احتياطية أولاً!) ::

    find -name "*.py" | xargs sed -i 's/\bscikits.learn\b/sklearn/g'

- لم تعد المُقَدِّرات تقبل معلمات النموذج كحجج "fit": بدلاً من ذلك، يجب تمرير جميع المعلمات فقط كحجج للمنشئ أو باستخدام طريقة "set_params" العامة الموروثة من :class:`~base.BaseEstimator`.

يمكن لبعض المُقَدِّرات أن تقبل حجج الكلمات الرئيسية على "fit" ولكن هذا يقتصر على القيم المعتمدة على البيانات (على سبيل المثال، مصفوفة غرام أو مصفوفة تشابه محسوبة مسبقًا من مصفوفة البيانات "X".

- تمت إعادة تسمية حزمة "cross_val" إلى "cross_validation" على الرغم من وجود حزمة "cross_val" مستخدمة كاسم مستعار للتوافق مع الإصدارات السابقة.

يجب على المشاريع التابعة للطرف الثالث التي تعتمد على scikit-learn 0.9+ ترقية قاعدة التعليمات البرمجية الخاصة بها. على سبيل المثال، في Linux / MacOSX، قم ببساطة بتشغيل (قم بعمل نسخة احتياطية أولاً!) ::

    find -name "*.py" | xargs sed -i 's/\bcross_val\b/cross_validation/g'

- يُتوقع الآن أن يقبل وسيط "score_func" لوظيفة "sklearn.cross_validation.cross_val_score" وسيطي "y_test" و "y_predicted" فقط لمهمتي التصنيف والتنبؤ، أو "X_test" للمُقَدِّرات غير الخاضعة للإشراف.

- يتم تعيين وسيط "gamma" لخوارزميات آلات المتجهات الداعمة إلى "1 / n_features" بشكل افتراضي، بدلاً من "1 / n_samples".

- تم وضع علامة "sklearn.hmm" على أنها يتيمة: سيتم إزالتها من scikit-learn في الإصدار 0.11 ما لم يتقدم شخص ما للمساهمة في التوثيق والأمثلة وإصلاح مشكلات الاستقرار العددي الكامنة.

- تم تحويل "sklearn.neighbors" إلى وحدة فرعية. تم وضع علامة "التصنيف" و "NeighborsRegressor" على أنهما مهملان. تم تقسيم وظائفهما بين خمس فئات جديدة: "NearestNeighbors" للبحث عن الجيران غير الخاضع للإشراف، و "KNeighborsClassifier" و "RadiusNeighborsClassifier" لمشكلات التصنيف الخاضعة للإشراف، و "KNeighborsRegressor" و "RadiusNeighborsRegressor" لمشكلات التنبؤ الخاضعة للإشراف.

- تم نقل "sklearn.ball_tree.BallTree" إلى "sklearn.neighbors.BallTree". سيؤدي استخدام السابق إلى ظهور تحذير.

- تمت إعادة تسمية "sklearn.linear_model.LARS()" والفئات ذات الصلة (LassoLARS، LassoLARSCV، إلخ) إلى "sklearn.linear_model.Lars()".

- تحتوي جميع مقاييس المسافة والنوى في "sklearn.metrics.pairwise" الآن على وسيط "Y"، والذي يكون افتراضيًا "None". إذا لم يتم منحها، تكون النتيجة هي المسافة (أو تشابه النواة) بين كل عينة في "Y". إذا تم منحها، تكون النتيجة هي المسافة المزدوجة (أو تشابه النواة) بين العينات في "X" إلى "Y".

- تمت إعادة تسمية "sklearn.metrics.pairwise.l1_distance" إلى "manhattan_distance"، وهي تعيد بشكل افتراضي المسافة المزدوجة. للحصول على المسافة المكونة، قم بتعيين وسيط "sum_over_features" إلى "False".

سيتم إزالة أسماء حزم التوافق مع الإصدارات السابقة والوظائف والفئات المهمَلة الأخرى في الإصدار 0.11.

الأشخاص
------

38 شخصًا ساهموا في هذا الإصدار.

- 387  `فلاد نيكولاي`_
- 320  `أوليفييه جريسيل`_
- 192  `لارس بوتينيك`_
- 179  `غايل فارو`_
- 168  `فابيان بيدراجوسا`_ (`INRIA`_، `Parietal Team`_)
- 127  `جيك فانديربلاس`_
- 120  `ماثيو بلونديل`_
- 85  `ألكسندر باسوس`_
- 67  `ألكسندر جرامفورت`_
- 57  `بيتر بريتنهوفر`_
- 56  `جيلز لوب`_
- 42  روبرت لايتون
- 38  نيل فارو
- 32  :user:`جان كوسايفي <JeanKossaifi>`
- 30  كونراد لي
- 22  بيترو بيركس
- 18  آندي
- 17  ديفيد وارد فارلي
- 12  برايان هولت
- 11  روبرت
- 8  أميت أيدس
- 8  :user:`فيرجيل فيريتش <VirgileFritsch>`
- 7  `ياروسلاف هالتشنكو`_
- 6  سالفاتوري ماسيكيا
- 5  باولو لوسي
- 4  فينسنت شوت
- 3  أليكسيس ميتيريو
- 3  براين سيلفيرثورن
- 3  `أندرياس مولر`_
- 2  مينوو جيك لي
- 1  إيمانويل جوييار
- 1  كيث جودمان
- 1  لوكاس وايمان
- 1  `نيكولاس بينتو`_
- 1  ثويس (راي) جونز
- 1  تيم شيرمان تشيس

.. _changes_0_8:

الإصدار 0.8
===========

**11 مايو 2011**

تم إصدار scikit-learn 0.8 في مايو 2011، بعد شهر واحد من أول "مهرجان برمجة" `scikit-learn <https://github.com/scikit-learn/scikit-learn/wiki/Upcoming-events>`_ دولي، ويتميز بتضمين وحدات نمطية مهمة: :ref:`hierarchical_clustering`، :ref:`cross_decomposition`، :ref:`NMF`، ودعم مبدئي لـ Python 3، بالإضافة إلى تحسينات وإصلاحات أخطاء مهمة.

سجل التغييرات
---------

تم تقديم العديد من الوحدات النمطية الجديدة خلال هذا الإصدار:

- وحدة نمطية جديدة :ref:`hierarchical_clustering` بواسطة فينسنت ميشيل، `بيرتراند ثيريون`_، `ألكسندر جرامفورت`_ و `غايل فارو`_.

- تنفيذ :ref:`kernel_pca` بواسطة `ماثيو بلونديل`_

- :ref:`labeled_faces_in_the_wild_dataset` بواسطة `أوليفييه جريسيل`_.

- وحدة نمطية جديدة :ref:`cross_decomposition` بواسطة `إدوارد دوشيسناي`_.

- وحدة نمطية :ref:`NMF` بواسطة `فلاد نيكولاي`_

- تنفيذ خوارزمية :ref:`oracle_approximating_shrinkage` بواسطة :user:`فيرجيل فيريتش <VirgileFritsch>` في وحدة نمطية :ref:`covariance`.

استفادت بعض الوحدات النمطية الأخرى من تحسينات أو عمليات تنظيف مهمة.

- دعم مبدئي لـ Python 3: البناء والاستيراد بشكل نظيف، وبعض الوحدات النمطية قابلة للاستخدام بينما تعاني وحدات أخرى من فشل الاختبارات بواسطة `فابيان بيدراجوسا`_.

- يمكن الآن استخدام :class:`~decomposition.PCA` من كائن Pipeline بواسطة `أوليفييه جريسيل`_.

- دليل :ref:`performance-howto` بواسطة `أوليفييه جريسيل`_.

- إصلاحات لتسرب الذاكرة في ارتباطات libsvm، وشجرة BallTree أكثر أمانًا لـ 64 بت بواسطة لارس بوتينيك.

- إصلاح الأخطاء وأسلوب الكود في خوارزمية :ref:`k_means` بواسطة جان شلوتر.

- إضافة سمة "converged" إلى نماذج المزج الغاوسي بواسطة فينسنت شوت.

- تم تنفيذ "transform"، "predict_log_proba" في :class:`~discriminant_analysis.LinearDiscriminantAnalysis` بواسطة `ماثيو بلونديل`_.

- إعادة تنظيم وحدة نمطية :ref:`svm` وإصلاح الأخطاء بواسطة `فابيان بيدراجوسا`_، `غايل فارو`_ و أميت أيدس.

- إعادة تنظيم وحدة نمطية SGD (إزالة ازدواجية التعليمات البرمجية، وتحسين تسمية المتغيرات)، وإضافة واجهة لوزن العينة بواسطة `بيتر بريتنهوفر`_.

- تغليف شجرة BallTree باستخدام Cython بواسطة ثويس (راي) جونز.

- تمت الإضافة وظيفة :func:`svm.l1_min_c` بواسطة باولو لوسي.

- تصحيحات الأخطاء الإملائية، وأسلوب التوثيق، وما إلى ذلك بواسطة `ياروسلاف هالتشنكو`_، `غايل فارو`_، `أوليفييه جريسيل`_، يان ماليت، `نيكولاس بينتو`_، لارس بوتينيك و `فابيان بيدراجوسا`_.

الأشخاص
-------

الأشخاص الذين جعلوا هذا الإصدار ممكنًا مسبوقًا بعدد الالتزامات:

- 159  `أوليفييه جريسيل`_
- 96  `غايل فارو`_
- 96  `فلاد نيكولاي`_
- 94  `فابيان بيدراجوسا`_
- 36  `ألكسندر جرامفورت`_
- 32  باولو لوسي
- 31  `إدوارد دوشيسناي`_
- 30  `ماثيو بلونديل`_
- 25  `بيتر بريتنهوفر`_
- 22  `نيكولاس بينتو`_
- 11  :user:`فيرجيل فيريتش <VirgileFritsch>`
-  7  لارس بوتينيك
-  6  فينسنت ميشيل
-  5  `بيرتراند ثيريون`_
-
فيما يلي ترجمة للنص المكتوب بتنسيق ReStructuredText إلى اللغة العربية:

===========

**2 مارس 2011**

تم إصدار scikit-learn 0.7 في مارس 2011، بعد حوالي ثلاثة أشهر من إصدار 0.6. ويتميز هذا الإصدار بتحسينات في السرعة في الخوارزميات الموجودة مثل k-Nearest Neighbors وخوارزمية K-Means، وبإدراج خوارزمية فعالة لحساب حل Ridge Generalized Cross Validation. وعلى عكس الإصدار السابق، لم يتم إضافة أي وحدات نمطية جديدة إلى هذا الإصدار.

سجل التغييرات
---------

- تحسينات في الأداء لنمذجة المزج الغاوسي [Jan Schlüter].

- تنفيذ خوارزمية فعالة للتحقق من صحة Ridge باستخدام طريقة Leave-One-Out Cross-Validated في :class:`~linear_model.RidgeCV` [`Mathieu Blondel`_]

- معالجة أفضل للخطية في :func:`linear_model.lars_path` [`Alexandre Gramfort`_ و`Fabian Pedregosa`_].

- إصلاحات لترتيب liblinear للعلامات وإشارة المعاملات [Dan Yamins، Paolo Losi، `Mathieu Blondel`_ و`Fabian Pedregosa`_].

- تحسينات في الأداء لخوارزمية Nearest Neighbors في المساحات عالية الأبعاد [`Fabian Pedregosa`_].

- تحسينات في الأداء لـ :class:`~cluster.KMeans` [`Gael Varoquaux`_ و`James Bergstra`_].

- فحوصات السلامة للفئات المستندة إلى SVM [`Mathieu Blondel`_].

- إعادة تصميم `neighbors.NeighborsClassifier` و :func:`neighbors.kneighbors_graph`: إضافة خوارزميات مختلفة لبحث k-Nearest Neighbor وتنفيذ خوارزمية أكثر استقرارًا لإيجاد أوزان مركز الثقل. كما تمت إضافة بعض وثائق المطورين لهذه الوحدة النمطية، راجع `notes_neighbors <https://github.com/scikit-learn/scikit-learn/wiki/Neighbors-working-notes>`_ لمزيد من المعلومات [`Fabian Pedregosa`_].

- تحسينات في التوثيق: إضافة `pca.RandomizedPCA` و :class:`~linear_model.LogisticRegression` إلى المرجع الفصلي. كما تمت إضافة مراجع للمصفوفات المستخدمة في التجميع وإصلاحات أخرى [`Gael Varoquaux`_، `Fabian Pedregosa`_، `Mathieu Blondel`_، `Olivier Grisel`_، Virgile Fritsch، Emmanuelle Gouillart]

- ربط الدالة decision_function في الفئات التي تستخدم liblinear_، والمتغيرات الكثيفة والمبعثرة، مثل :class:`~svm.LinearSVC` أو :class:`~linear_model.LogisticRegression` [`Fabian Pedregosa`_].

- تحسينات في الأداء وAPI لـ :func:`metrics.pairwise.euclidean_distances` و لـ `pca.RandomizedPCA` [`James Bergstra`_].

- إصلاح مشكلات التجميع تحت NetBSD [Kamel Ibn Hassen Derouiche]

- السماح بتسلسلات الإدخال بأطوال مختلفة في `hmm.GaussianHMM` [`Ron Weiss`_].

- إصلاح خلل في الانتشار العاطفي الناجم عن الفهرسة غير الصحيحة [Xinfan Meng]

الأشخاص
------

الأشخاص الذين جعلوا هذا الإصدار ممكنًا يسبقهم عدد الالتزامات:

- 85  `Fabian Pedregosa`_
- 67  `Mathieu Blondel`_
- 20  `Alexandre Gramfort`_
- 19  `James Bergstra`_
- 14  Dan Yamins
- 13  `Olivier Grisel`_
- 12  `Gael Varoquaux`_
- 4  `Edouard Duchesnay`_
- 4  `Ron Weiss`_
- 2  Satrajit Ghosh
- 2  Vincent Dubourg
- 1  Emmanuelle Gouillart
- 1  Kamel Ibn Hassen Derouiche
- 1  Paolo Losi
- 1  VirgileFritsch
- 1  `Yaroslav Halchenko`_
- 1  Xinfan Meng

.. _changes_0_6:

الإصدار 0.6
===========

**21 ديسمبر 2010**

تم إصدار scikit-learn 0.6 في ديسمبر 2010. ويتميز بإدراج عدة وحدات نمطية جديدة وإعادة تسمية الوحدات القديمة بشكل عام. كما يتميز أيضًا بإدراج أمثلة جديدة، بما في ذلك التطبيقات على مجموعات البيانات الواقعية.

سجل التغييرات
---------

- وحدة نمطية جديدة للانحدار التدريجي العشوائي <https://scikit-learn.org/stable/modules/sgd.html>`_ بواسطة Peter Prettenhofer. تأتي الوحدة النمطية مع توثيق كامل وأمثلة.

- تحسين وحدة SVM: تم تقليل استهلاك الذاكرة بنسبة 50%، وتم إضافة طريقة لحساب أوزان الفئات تلقائيًا، وإمكانية تعيين أوزان للعينات (راجع :ref:`sphx_glr_auto_examples_svm_plot_weighted_samples.py` لمثال).

- وحدة نمطية جديدة :ref:`gaussian_process` بواسطة Vincent Dubourg. تحتوي هذه الوحدة النمطية أيضًا على توثيق رائع وبعض الأمثلة الرائعة. راجع example_gaussian_process_plot_gp_regression.py أو example_gaussian_process_plot_gp_probabilistic_classification_after_regression.py لمشاهدة ما يمكن القيام به.

- أصبح من الممكن الآن استخدام Liblinear's Multi-class SVC (خيار multi_class في :class:`~svm.LinearSVC`)

- ميزات جديدة وتحسينات في الأداء لاستخراج ميزات النص.

- تحسين دعم المصفوفات المبعثرة، في الفئات الرئيسية (:class:`~model_selection.GridSearchCV`) كما في الوحدات النمطية sklearn.svm.sparse وsklearn.linear_model.sparse.

- العديد من الأمثلة الرائعة وقسم جديد يستخدم مجموعات بيانات واقعية. تشمل هذه الأمثلة: :ref:`sphx_glr_auto_examples_applications_plot_face_recognition.py`، :ref:`sphx_glr_auto_examples_applications_plot_species_distribution_modeling.py`، :ref:`sphx_glr_auto_examples_applications_wikipedia_principal_eigenvector.py` وغيرها.

- خوارزمية :ref:`least_angle_regression` أسرع. إنها الآن أسرع مرتين من إصدار R في أسوأ الحالات وأسرع 10 مرات في بعض الحالات.

- خوارزمية الانحدار المنسق أسرع. على وجه الخصوص، فإن إصدار المسار الكامل من lasso (:func:`linear_model.lasso_path`) أسرع من الإصدار السابق بأكثر من 200 مرة.

- أصبح من الممكن الآن الحصول على تقديرات الاحتمالية من نموذج :class:`~linear_model.LogisticRegression`.

- إعادة تسمية الوحدة النمطية: تمت إعادة تسمية وحدة glm النمطية إلى linear_model، وتمت إضافة وحدة gmm النمطية إلى المزيج العام، وتمت إضافة وحدة sgd النمطية إلى linear_model.

- العديد من إصلاحات الأخطاء وتحسينات التوثيق.

الأشخاص
------

الأشخاص الذين جعلوا هذا الإصدار ممكنًا يسبقهم عدد الالتزامات:

* 207  `Olivier Grisel`_

* 167 `Fabian Pedregosa`_

* 97 `Peter Prettenhofer`_

* 68 `Alexandre Gramfort`_

* 59  `Mathieu Blondel`_

* 55  `Gael Varoquaux`_

* 33  Vincent Dubourg

* 21  `Ron Weiss`_

* 9  Bertrand Thirion

* 3  `Alexandre Passos`_

* 3  Anne-Laure Fouque

* 2  Ronan Amicel

* 1 `Christian Osendorfer`_

.. _changes_0_5:

الإصدار 0.5
===========

**11 أكتوبر 2010**

سجل التغييرات
---------

فئات جديدة
-----------

- دعم المصفوفات المبعثرة في بعض مصنفات الوحدات النمطية "svm" و"linear_model" (راجع `svm.sparse.SVC`، `svm.sparse.SVR`، `svm.sparse.LinearSVC`، `linear_model.sparse.Lasso`، `linear_model.sparse.ElasticNet`)

- فئة :class:`~pipeline.Pipeline` جديدة لدمج مصادر مختلفة.

- روتينات إزالة الميزات المتكررة في وحدة :ref:`feature_selection` النمطية.

- إضافة فئات مختلفة قادرة على التحقق من الصحة المتقاطعة في وحدة linear_model النمطية (:class:`~linear_model.LassoCV`، :class:`~linear_model.ElasticNetCV`، إلخ).

- تنفيذ جديد أكثر كفاءة لخوارزمية LARS. كما تم تنفيذ متغير Lasso للخوارزمية. راجع :class:`~linear_model.lars_path`، :class:`~linear_model.Lars` و :class:`~linear_model.LassoLars`.

- وحدة نمطية جديدة للنماذج المخفية لهار ماركوف (راجع الفئات `hmm.GaussianHMM`، `hmm.MultinomialHMM`، `hmm.GMMHMM`)

- وحدة نمطية جديدة لاستخراج الميزات (راجع :ref:`class reference <feature_extraction_ref>`)

- خوارزمية FastICA جديدة في الوحدة النمطية sklearn.fastica

التوثيق
-------------

- تحسين التوثيق للعديد من الوحدات النمطية، مع فصل التوثيق السردي عن المرجع الفصلي. على سبيل المثال، راجع "توثيق وحدة نمطية SVM <https://scikit-learn.org/stable/modules/svm.html>`_ و "المرجع الفصلي الكامل <https://scikit-learn.org/stable/modules/classes.html>`_.

الإصلاحات
-----

- تغييرات API: الالتزام بأسماء المتغيرات لـ PEP-8، وإعطاء أسماء أكثر دلالة.

- إصلاحات لوحدة نمطية SVM لتشغيلها في سياق الذاكرة المشتركة (multiprocessing).

- أصبح من الممكن مرة أخرى إنشاء ملفات Latex (وبالتالي PDF) من وثائق Sphinx.

الأمثلة
--------

- أمثلة جديدة باستخدام بعض مجموعات بيانات mlcomp: ``sphx_glr_auto_examples_mlcomp_sparse_document_classification.py`` (تمت الإزالة منذ ذلك الحين) و:ref:`sphx_glr_auto_examples_text_plot_document_classification_20newsgroups.py`

- العديد من الأمثلة الأخرى. `راجع هنا <https://scikit-learn.org/stable/auto_examples/index.html>`_ للحصول على القائمة الكاملة للأمثلة.

التبعيات الخارجية
---------------------

- Joblib هو الآن اعتماد لهذا الحزمة، على الرغم من أنها تأتي مع (sklearn.externals.joblib).

الوحدات النمطية المحذوفة
---------------

- تمت إزالة وحدة ANN (الشبكات العصبية الاصطناعية) من التوزيع. يجب على المستخدمين الذين يرغبون في هذا النوع من الخوارزميات الاطلاع على pybrain.

متفرقات
----

- موضوع Sphinx جديد لصفحة الويب.

المؤلفون
-------

فيما يلي قائمة بالمؤلفين لهذا الإصدار، يسبقها عدد الالتزامات:

* 262  Fabian Pedregosa
* 240  Gael Varoquaux
* 149  Alexandre Gramfort
* 116  Olivier Grisel
*  40  Vincent Michel
*  38  Ron Weiss
*  23  Matthieu Perrot
*  10  Bertrand Thirion
*   7  Yaroslav Halchenko
*   9  VirgileFritsch
*   6  Edouard Duchesnay
*   4  Mathieu Blondel
*   1  Ariel Rokem
*   1  Matthieu Brucher

الإصدار 0.4
===========

**26 أغسطس 2010**

سجل التغييرات
---------

تشمل التغييرات الرئيسية في هذا الإصدار ما يلي:

- إعادة تصميم خوارزمية Coordinate Descent (Lasso، ElasticNet) وتحسينات في السرعة (أسرع حوالي 100 مرة).

- إعادة تصميم Coordinate Descent (وإصلاح الأخطاء) للاتساق مع حزمة R's GLMNET.

- وحدة نمطية جديدة للقياسات.

- وحدة نمطية جديدة GMM مقدمة من Ron Weiss.

- تنفيذ خوارزمية LARS (بدون متغير Lasso في الوقت الحالي).

- إعادة تصميم وحدة feature_selection النمطية.

- الهجرة إلى GIT كنظام تحكم في الإصدار.

- إزالة وحدة attrselect النمطية القديمة.

- إعادة تسمية الامتدادات المجمعة الخاصة (تمت إضافة علامة Underscore).

- إزالة التعليمات البرمجية القديمة غير المدعومة.

- تحسينات التوثيق (توثيق Docstring و RST).

- تحسين نظام البناء للارتباط الاختياري مع MKL. أيضًا، قم بتوفير تنفيذ BLAS خفيف في حالة عدم العثور على BLAS على مستوى النظام.

- العديد من الأمثلة الجديدة.

- إصلاحات أخطاء عديدة...

المؤلفون
-------

قائمة المؤلفين لهذا الإصدار (يسبقها عدد الالتزامات):

* 143  Fabian Pedregosa
* 35  Alexandre Gramfort
* 34  Olivier Grisel
* 11  Gael Varoquaux
*  5  Yaroslav Halchenko
*  2  Vincent Michel
*  1  Chris Filo Gorgolewski

الإصدارات السابقة
================

تضمنت الإصدارات السابقة مساهمات من Fred Mailhot، وDavid Cooke، وDavid Huard، وDave Morrill، وEd Schofield، وTravis Oliphant، وPearu Peterson.