يسلط هذا الفصل الضوء على بعض المطبات الشائعة والأنماط المضادة التي تحدث عند استخدام scikit-learn. ويقدم أمثلة على ما **لا** يجب فعله، إلى جانب مثال صحيح مقابل.

المعالجة المسبقة غير المتسقة
==========================

يوفر scikit-learn مكتبة من :ref: `data-transforms` ، والتي قد تنظف (راجع: ref: `preprocessing`)، تقلل (راجع: ref: `data_reduction`)، توسع (راجع: ref: `kernel_approximation`) أو توليد (راجع: ref: `feature_extraction`) تمثيلات الميزات. إذا تم استخدام هذه التحويلات على البيانات عند تدريب نموذج، فيجب أيضًا استخدامها في مجموعات البيانات اللاحقة، سواء كانت بيانات الاختبار أو البيانات في نظام الإنتاج. وإلا، فستتغير مساحة الميزة، ولن يتمكن النموذج من الأداء بشكل فعال.

بالنسبة للمثال التالي، دعنا نقوم بإنشاء مجموعة بيانات اصطناعية بميزة واحدة::

    >>> from sklearn.datasets import make_regression
    >>> from sklearn.model_selection import train_test_split

    >>> random_state = 42
    >>> X, y = make_regression(random_state=random_state, n_features=1, noise=1)
    >>> X_train, X_test, y_train, y_test = train_test_split(
    ...     X, y, test_size=0.4, random_state=random_state)

**خطأ**

تم تحجيم مجموعة البيانات التدريبية، ولكن ليس مجموعة الاختبار، لذا فإن أداء النموذج على مجموعة بيانات الاختبار أسوأ من المتوقع::

    >>> from sklearn.metrics import mean_squared_error
    >>> from sklearn.linear_model import LinearRegression
    >>> from sklearn.preprocessing import StandardScaler

    >>> scaler = StandardScaler()
    >>> X_train_transformed = scaler.fit_transform(X_train)
    >>> model = LinearRegression().fit(X_train_transformed, y_train)
    >>> mean_squared_error(y_test, model.predict(X_test))
    62.80...

**صحيح**

بدلاً من تمرير `X_test` غير المحول إلى `predict`، يجب علينا تحويل بيانات الاختبار، بنفس الطريقة التي حولنا بها بيانات التدريب::

    >>> X_test_transformed = scaler.transform(X_test)
    >>> mean_squared_error(y_test, model.predict(X_test_transformed))
    0.90...

بدلاً من ذلك، نوصي باستخدام: class: `Pipeline <sklearn.pipeline.Pipeline>`، مما يسهل تسلسل التحولات مع المحكمين، ويقلل من احتمال نسيان التحول::

    >>> from sklearn.pipeline import make_pipeline

    >>> model = make_pipeline(StandardScaler(), LinearRegression())
    >>> model.fit(X_train, y_train)
    Pipeline(steps=[('standardscaler', StandardScaler()),
                    ('linearregression', LinearRegression())])
    >>> mean_squared_error(y_test, model.predict(X_test))
    0.90...

كما تساعد خطوط الأنابيب في تجنب أحد المطبات الشائعة: تسرب بيانات الاختبار إلى بيانات التدريب.

.. _data_leakage:

تسرب البيانات
============

يحدث تسرب البيانات عندما يتم استخدام معلومات لن تكون متاحة في وقت التنبؤ عند بناء النموذج. يؤدي هذا إلى تقديرات أداء متفائلة للغاية، على سبيل المثال من: ref: `cross-validation <cross_validation>`، وبالتالي ضعف الأداء عندما يتم استخدام النموذج على بيانات جديدة بالفعل، على سبيل المثال أثناء الإنتاج.

السبب الشائع هو عدم الحفاظ على مجموعات البيانات الفرعية للاختبار والتدريب منفصلة. لا ينبغي أبدًا استخدام بيانات الاختبار لاتخاذ خيارات بشأن النموذج. **القاعدة العامة هي عدم استدعاء** `fit` **على بيانات الاختبار**. على الرغم من أن هذا قد يبدو واضحًا، إلا أنه من السهل تفويته في بعض الحالات، على سبيل المثال عند تطبيق خطوات المعالجة المسبقة معينة.

على الرغم من أنه يجب أن تتلقى كل من مجموعات البيانات الفرعية للتدريب والاختبار نفس تحويل المعالجة المسبقة (كما هو موضح في القسم السابق)، إلا أنه من المهم أن يتم تعلم هذه التحولات فقط من بيانات التدريب. على سبيل المثال، إذا كان لديك خطوة تطبيع تقسم فيها بالقيمة المتوسطة، فيجب أن يكون المتوسط هو متوسط ​​مجموعة البيانات الفرعية للتدريب، **وليس** متوسط ​​جميع البيانات. إذا تم تضمين مجموعة البيانات الفرعية للاختبار في حساب المتوسط، فإن المعلومات من مجموعة البيانات الفرعية للاختبار تؤثر على النموذج.

كيفية تجنب تسرب البيانات
-------------------------

فيما يلي بعض النصائح لتجنب تسرب البيانات:

* قم دائمًا بتقسيم البيانات إلى مجموعات فرعية للتدريب والاختبار أولاً، خاصة قبل أي خطوات للمعالجة المسبقة.
* لا تضمن أبدًا بيانات الاختبار عند استخدام طرق `fit` و` fit_transform`. يمكن أن يؤدي استخدام جميع البيانات، على سبيل المثال، `fit (X)`، إلى درجات متفائلة للغاية.

  على العكس من ذلك، يجب استخدام طريقة "التحويل" في كل من المجموعات الفرعية للتدريب والاختبار نظرًا لأنه يجب تطبيق نفس المعالجة المسبقة على جميع البيانات. يمكن تحقيق ذلك عن طريق استخدام `fit_transform` على المجموعة الفرعية للتدريب و` transform` على المجموعة الفرعية للاختبار.
* تعد خط أنابيب scikit-learn: ref: `pipeline` طريقة رائعة لمنع تسرب البيانات حيث تضمن إجراء الطريقة المناسبة على مجموعة البيانات الفرعية الصحيحة. تعد الأنابيب مثالية للاستخدام في وظائف الضبط والضبط باستخدام الضبط.

يرد أدناه مثال على تسرب البيانات أثناء المعالجة المسبقة.

تسرب البيانات أثناء المعالجة المسبقة
----------------------------------

.. note::
    نختار هنا توضيح تسرب البيانات باستخدام خطوة اختيار الميزة. ومع ذلك، فإن خطر التسرب هذا مناسب مع جميع التحولات تقريبًا في scikit-learn، بما في ذلك (ولكن لا تقتصر على)
    : class: `~sklearn.preprocessing.StandardScaler`،
    : class: `~sklearn.impute.SimpleImputer`، و
    : class: `~sklearn.decomposition.PCA`.

يتوفر عدد من: ref: `feature_selection` الوظائف في scikit-learn. يمكنهم المساعدة في إزالة الميزات غير ذات الصلة والزائدة والضجيج، بالإضافة إلى تحسين وقت بناء النموذج وأدائه. كما هو الحال مع أي نوع آخر من المعالجة المسبقة، يجب أن يستخدم اختيار الميزة **فقط** بيانات التدريب. سيؤدي تضمين بيانات الاختبار في اختيار الميزة إلى تحيز نموذجك بشكل متفائل.

لتوضيح ذلك، سنقوم بإنشاء مشكلة تصنيف ثنائي مع 10000 ميزة تم إنشاؤها بشكل عشوائي::

    >>> import numpy as np
    >>> n_samples، n_features، n_classes = 200، 10000، 2
    >>> rng = np.random.RandomState (42)
    >>> X = rng.standard_normal ((n_samples، n_features))
    >>> y = rng.choice (n_classes، n_samples)

**خطأ**

يؤدي استخدام جميع البيانات لأداء اختيار الميزة إلى الحصول على درجة دقة أعلى بكثير من الفرصة، على الرغم من أن أهدافنا عشوائية تمامًا. تعني هذه العشوائية أن "X" و"y" مستقلان، وبالتالي نتوقع أن تكون الدقة حوالي 0.5. ومع ذلك، نظرًا لأن خطوة اختيار الميزة "ترى" بيانات الاختبار، فإن النموذج لديه ميزة غير عادلة. في المثال غير الصحيح أدناه، نستخدم أولاً جميع البيانات لاختيار الميزة ثم نقسم البيانات إلى مجموعات فرعية للتدريب والاختبار لتناسب النموذج. النتيجة هي درجة دقة أعلى بكثير من المتوقع::

    >>> from sklearn.model_selection import train_test_split
    >>> from sklearn.feature_selection import SelectKBest
    >>> from sklearn.ensemble import GradientBoostingClassifier
    >>> from sklearn.metrics import accuracy_score

    >>> # معالجة مسبقة غير صحيحة: يتم تحويل البيانات بالكامل
    >>> X_selected = SelectKBest (k=25).fit_transform (X، y)

    >>> X_train، X_test، y_train، y_test = train_test_split (
    ...     X_selected، y، random_state=42)
    >>> gbc = GradientBoostingClassifier (random_state=1)
    >>> gbc.fit (X_train، y_train)
    GradientBoostingClassifier (random_state=1)

    >>> y_pred = gbc.predict (X_test)
    >>> accuracy_score (y_test، y_pred)
    0.76

**صحيح**

لمنع تسرب البيانات، من الجيد تقسيم بياناتك إلى مجموعات فرعية للتدريب والاختبار **أولاً**. يمكن بعد ذلك إجراء اختيار الميزة باستخدام مجموعة البيانات التدريبية فقط. لاحظ أنه كلما استخدمنا `fit` أو `fit_transform`، فإننا نستخدم مجموعة البيانات التدريبية فقط. النتيجة الآن هي ما نتوقعه للبيانات، بالقرب من الفرصة::

    >>> X_train، X_test، y_train، y_test = train_test_split (
    ...     X، y، random_state=42)
    >>> select = SelectKBest (k=25)
    >>> X_train_selected = select.fit_transform (X_train، y_train)

    >>> gbc = GradientBoostingClassifier (random_state=1)
    >>> gbc.fit (X_train_selected، y_train)
    GradientBoostingClassifier (random_state=1)

    >>> X_test_selected = select.transform (X_test)
    >>> y_pred = gbc.predict (X_test_selected)
    >>> accuracy_score (y_test، y_pred)
    0.46

نوصي هنا مرة أخرى باستخدام: class: `~sklearn.pipeline.Pipeline` لربط اختيار الميزة ومقدّرات النموذج معًا. تضمن الأنابيب استخدام بيانات التدريب فقط عند إجراء `fit` واستخدام بيانات الاختبار فقط لحساب درجة الدقة::

    >>> from sklearn.pipeline import make_pipeline
    >>> X_train، X_test، y_train، y_test = train_test_split (
    ...     X، y، random_state=42)
    >>> pipeline = make_pipeline (SelectKBest (k=25)،
    ...                          GradientBoostingClassifier (random_state=1))
    >>> pipeline.fit (X_train، y_train)
    Pipeline (steps = [('selectkbest'، SelectKBest (k=25))،
    ...                    ('gradientboostingclassifier'،
    ...                     GradientBoostingClassifier (random_state=1))])

    >>> y_pred = pipeline.predict (X_test)
    >>> accuracy_score (y_test، y_pred)
    0.46

يمكن أيضًا تغذية الأنابيب في دالة التحقق من صحة متقاطعة مثل: func: `~sklearn.model_selection.cross_val_score`. مرة أخرى، تضمن الأنابيب استخدام مجموعة البيانات الفرعية الصحيحة والمناسب الصحيح أثناء التجهيز والتنبؤ::

    >>> from sklearn.model_selection import cross_val_score
    >>> scores = cross_val_score (pipeline، X، y)
    >>> print (f "Mean accuracy: {scores.mean (): .2f} +/- {scores.std (): .2f}")
    متوسط ​​الدقة: 0.46 +/- 0.07


.. _randomness:

التحكم في العشوائية
بعض كائنات scikit-learn عشوائية بطبيعتها. وعادة ما تكون هذه الكائنات هي أدوات تقدير (مثل :class: ~ sklearn.ensemble.RandomForestClassifier) و splitters التحقق من صحة التعابر (مثل :class: ~ sklearn.model_selection.KFold). يتم التحكم في عشوائية هذه الكائنات من خلال معلمة 'random_state' الخاصة بها، كما هو موضح في: مصطلح: 'مسرد المصطلحات <random_state>`. يوسع هذا القسم إدخال المسرد، ويصف الممارسات الجيدة والمزالق الشائعة فيما يتعلق بهذا المعلمة الدقيقة.

.. ملاحظة:: ملخص التوصية

    للحصول على أقصى قدر من المتانة لنتائج التحقق من صحة التعابر، قم بتمرير حالات 'RandomState' عند إنشاء أدوات التقدير، أو اترك 'random_state' إلى 'None'. يعد تمرير الأعداد الصحيحة إلى splitters التحقق من صحة التعابر هو الخيار الأكثر أمانًا وعادة ما يكون مفضلًا؛ قد يكون تمرير حالات 'RandomState' إلى splitters مفيدًا في بعض الأحيان لتحقيق حالات استخدام محددة جدًا.
    لكل من أدوات التقدير وsplitters، يؤدي تمرير عدد صحيح مقابل تمرير مثيل (أو 'None') إلى اختلافات دقيقة ولكنها مهمة، خاصةً لإجراءات التحقق من صحة التعابر. هذه الاختلافات مهمة لفهمها عند الإبلاغ عن النتائج.

    للحصول على نتائج قابلة للتكرار عبر عمليات التنفيذ، قم بإزالة أي استخدام لـ 'random_state = None'.

استخدام 'None' أو حالات 'RandomState'، والمكالمات المتكررة إلى 'fit' و'split'
--------------------------------------------------------------------------------

تحدد معلمة 'random_state' ما إذا كانت الاستدعاءات المتعددة لـ: مصطلح: 'fit' (لأدوات التقدير) أو إلى: مصطلح: 'split' (لـ CV splitters) ستنتج نفس النتائج، وفقًا لهذه القواعد:

- إذا تم تمرير عدد صحيح، فإن استدعاء 'fit' أو 'split' عدة مرات ينتج دائمًا نفس النتائج.
- إذا تم تمرير 'None' أو مثيل 'RandomState': فإن 'fit' و'split' سينتجان نتائج مختلفة في كل مرة يتم استدعاؤها فيها، وستستكشف سلسلة الاستدعاءات جميع مصادر الإنتروبيا. 'None' هي القيمة الافتراضية لجميع معلمات 'random_state'.

نوضح هنا هذه القواعد لكل من أدوات التقدير وCV splitters.

.. ملاحظة::
    نظرًا لأن تمرير 'random_state = None' يعادل تمرير مثيل 'RandomState' العالمي من 'numpy' ('random_state = np.random.mtrand._rand`)، فلن نذكر صراحةً 'None' هنا. كل ما ينطبق على الحالات ينطبق أيضًا على استخدام 'None'.

أدوات التقدير
..........

يعني تمرير الحالات أن استدعاء 'fit' عدة مرات لن ينتج نفس النتائج، حتى إذا تم ضبط أداة التقدير على نفس البيانات وبنفس المعلمات فائقة الدقة::

    >>> from sklearn.linear_model import SGDClassifier
    >>> from sklearn.datasets import make_classification
    >>> import numpy as np

    >>> rng = np.random.RandomState(0)
    >>> X, y = make_classification(n_features=5, random_state=rng)
    >>> sgd = SGDClassifier(random_state=rng)

    >>> sgd.fit(X, y).coef_
    array([[ 8.85418642,  4.79084103, -3.13077794,  8.11915045, -0.56479934]])

    >>> sgd.fit(X, y).coef_
    array([[ 6.70814003,  5.25291366, -7.55212743,  5.18197458,  1.37845099]])

يمكننا أن نرى من المقتطف أعلاه أن الاستدعاءات المتكررة لـ 'sgd.fit' أنتجت نماذج مختلفة، حتى إذا كانت البيانات هي نفسها. ويرجع ذلك إلى أن مولد الأرقام العشوائية (RNG) لأداة التقدير يتم استهلاكه (أي تغييره) عند استدعاء 'fit'، وسيتم استخدام هذا RNG المتحول في الاستدعاءات اللاحقة لـ 'fit'. بالإضافة إلى ذلك، يتم مشاركة كائن 'rng' عبر جميع الكائنات التي تستخدمه، وكنتيجة لذلك، تصبح هذه الكائنات مترابطة إلى حد ما. على سبيل المثال، ستؤثر أداتان تقديريتان تشتركان في نفس مثيل 'RandomState' على بعضهما البعض، كما سنرى لاحقًا عند مناقشة الاستنساخ. هذه النقطة مهمة يجب مراعاتها عند تصحيح الأخطاء.

إذا كنا قد مررنا عددًا صحيحًا إلى معلمة 'random_state' لأداة التقدير: class: ~ sklearn.linear_model.SGDClassifier، لكنا حصلنا على نفس النماذج، وبالتالي نفس الدرجات في كل مرة. عندما نمرر عددًا صحيحًا، يتم استخدام نفس RNG عبر جميع الاستدعاءات لـ 'fit'. ما يحدث داخليًا هو أنه على الرغم من استهلاك RNG عند استدعاء 'fit'، إلا أنه يتم إعادة تعيينه دائمًا إلى حالته الأصلية في بداية 'fit'.

CV splitters
............

لدى CV splitters العشوائية سلوك مماثل عند تمرير مثيل 'RandomState'؛ يؤدي استدعاء 'split' عدة مرات إلى تقسيمات بيانات مختلفة::

    >>> from sklearn.model_selection import KFold
    >>> import numpy as np

    >>> X = y = np.arange(10)
    >>> rng = np.random.RandomState(0)
    >>> cv = KFold(n_splits=2, shuffle=True, random_state=rng)

    >>> for train, test in cv.split(X, y):
    ... print(train, test)
    [0 3 5 6 7] [1 2 4 8 9]
    [1 2 4 8 9] [0 3 5 6 7]

    >>> for train, test in cv.split(X, y):
    ... print(train, test)
    [0 4 6 7 8] [1 2 3 5 9]
    [1 2 3 5 9] [0 4 6 7 8]

يمكننا أن نرى أن التقسيمات مختلفة بدءًا من المرة الثانية التي يتم فيها استدعاء 'split'. قد يؤدي ذلك إلى نتائج غير متوقعة إذا كنت تقارن أداء أدوات تقدير متعددة عن طريق استدعاء 'split' عدة مرات، كما سنرى في القسم التالي.

المزالق الدقيقة والتعقيدات
------------------------------

على الرغم من أن القواعد التي تحكم معلمة 'random_state' تبدو بسيطة، إلا أن لها بعض الآثار الدقيقة. في بعض الحالات، قد يؤدي ذلك حتى إلى استنتاجات خاطئة.

أدوات التقدير
..........

**أنواع مختلفة من 'random_state' تؤدي إلى إجراءات تحقق من صحة التعابر المختلفة**

وفقًا لنوع معلمة 'random_state'، ستتصرف أدوات التقدير بشكل مختلف، خاصة في إجراءات التحقق من صحة التعابر. ضع في اعتبارك المقتطف التالي::

    >>> from sklearn.ensemble import RandomForestClassifier
    >>> from sklearn.datasets import make_classification
    >>> from sklearn.model_selection import cross_val_score
    >>> import numpy as np

    >>> X, y = make_classification(random_state=0)

    >>> rf_123 = RandomForestClassifier(random_state=123)
    >>> cross_val_score(rf_123, X, y)
    array([0.85, 0.95, 0.95, 0.9 , 0.9 ])

    >>> rf_inst = RandomForestClassifier(random_state=np.random.RandomState(0))
    >>> cross_val_score(rf_inst, X, y)
    array([0.9 , 0.95, 0.95, 0.9 , 0.9 ])

يمكننا أن نرى أن الدرجات المتحقق من صحتها عبر التعابر لـ 'rf_123' و'rf_inst' مختلفة، كما هو متوقع حيث لم نقم بتمرير نفس معلمة 'random_state'. ومع ذلك، فإن الاختلاف بين هذه الدرجات أكثر دقة مما يبدو، و**إجراءات التحقق من صحة التعابر التي تم تنفيذها بواسطة** :func: ~ sklearn.model_selection.cross_val_score **تختلف بشكل كبير في كل حالة**:

- نظرًا لأنه تم تمرير عدد صحيح إلى 'rf_123'، فإن كل استدعاء لـ 'fit' يستخدم نفس RNG: وهذا يعني أن جميع الخصائص العشوائية لأداة تقدير الغابة العشوائية ستكون هي نفسها لكل من طيات إجراء التحقق من صحة التعابر الخمسة. على وجه الخصوص، ستكون المجموعة الفرعية من الميزات (التي تم اختيارها بشكل عشوائي) لأداة التقدير هي نفسها عبر جميع الطيات.
- نظرًا لأنه تم تمرير مثيل 'RandomState' إلى 'rf_inst'، فإن كل استدعاء لـ 'fit' يبدأ من RNG مختلف. ونتيجة لذلك، ستكون المجموعة الفرعية العشوائية من الميزات مختلفة لكل طية.

على الرغم من أن وجود RNG ثابت لأداة التقدير عبر الطيات ليس خطأ في حد ذاته، إلا أننا نريد عادةً نتائج التحقق من صحة التعابر التي تكون قوية فيما يتعلق بعشوائية أداة التقدير. ونتيجة لذلك، قد يكون تمرير مثيل بدلاً من عدد صحيح مفضلًا، حيث سيسمح ذلك بتغيير RNG لأداة التقدير لكل طية.

.. ملاحظة::
    هنا، سيستخدم: func: ~ sklearn.model_selection.cross_val_score أداة تقسيم التحقق من صحة التعابر غير العشوائية (كما هو الافتراضي)، لذا سيتم تقييم كلا الأداة على نفس التقسيمات. لا يتعلق هذا القسم بالتنوع في التقسيمات. أيضًا، سواء قمنا بتمرير عدد صحيح أو مثيل إلى: func: ~ sklearn.datasets.make_classification ليس ذي صلة بغرض التوضيح: ما يهم هو ما نمرره إلى أداة تقدير RandomForestClassifier.

.. dropdown:: الاستنساخ

    التأثير الجانبي الدقيق الآخر لتمرير حالات 'RandomState' هو كيفية عمل: func: ~ sklearn.base.clone::

        >>> from sklearn import clone
        >>> from sklearn.ensemble import RandomForestClassifier
        >>> import numpy as np

        >>> rng = np.random.RandomState(0)
        >>> a = RandomForestClassifier(random_state=rng)
        >>> b = clone(a)

    نظرًا لأنه تم تمرير مثيل 'RandomState' إلى 'a'، فإن 'a' و'b' ليسا استنساخًا بالمعنى الدقيق للكلمة، ولكنهما استنساخًا بالمعنى الإحصائي: ستظل 'a' و'b' نموذجين مختلفين، حتى عند استدعاء 'fit (X، y)' على نفس البيانات. علاوة على ذلك، ستؤثر 'a' و'b' على بعضهما البعض لأنهما يتشاركان نفس RNG الداخلي: سيستهلك استدعاء 'a.fit' RNG لـ 'b'، وسيستهلك استدعاء 'b.fit' RNG لـ 'a'، لأنهما نفس الشيء. هذه النقطة صحيحة لأي أدوات تقدير تشترك في معلمة 'random_state'؛ إنه ليس خاصًا بالاستنساخ.

    إذا تم تمرير عدد صحيح، فإن 'a' و'b' سيكونان استنساخًا دقيقًا ولن يؤثرا على بعضهما البعض.

    .. تحذير::
        على الرغم من أن: func: ~ sklearn.base.clone نادرًا ما يتم استخدامه في شفرة المستخدم، إلا أنه يتم استدعاؤه بشكل مكثف في جميع أنحاء قاعدة التعليمات البرمجية لـ scikit-learn: على وجه الخصوص، تقوم معظم أدوات التقدير الفوقية التي تقبل أدوات التقدير غير المنضبطة باستدعاء: func: ~ sklearn.base.clone داخليًا (: class: ~ sklearn.model_selection.GridSearchCV،: class: ~ sklearn.ensemble.StackingClassifier،: class: ~ sklearn.calibration.CalibratedClassifierCV، إلخ).


CV splitters
............

عند تمرير مثيل 'RandomState'، ينتج CV splitters تقسيمات مختلفة في كل مرة يتم فيها استدعاء 'split'. عند مقارنة أدوات التقدير المختلفة، يمكن أن يؤدي ذلك إلى المبالغة في تقدير تباين الفرق في الأداء بين أدوات التقدير::

    >>> from sklearn.naive_bayes import GaussianNB
    >>> from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    >>> from sklearn.datasets import make_classification
    >>> from sklearn.model_selection import KFold
    >>> from sklearn.model_selection import cross_val_score
    >>> import numpy as np

    >>> rng = np.random.RandomState(0)
    >>> X, y = make_classification(random_state=rng)
    >>> cv = KFold(shuffle=True, random_state=rng)
    >>> lda = LinearDiscriminantAnalysis()
    >>> nb = GaussianNB()

    >>> for est in (lda, nb):
    ... print(cross_val_score(est, X, y, cv=cv))
    [0.8 0.75 0.75 0.7 0.85]
    [0.85 0.95 0.95 0.85 0.95]


سيكون من الخطأ مقارنة أداء أداة تقدير: class: ~ sklearn.discriminant_analysis.LinearDiscriminantAnalysis مباشرةً مقابل أداة تقدير: class: ~ sklearn.naive_bayes.GaussianNB **على كل طية**؛ **التقسيمات التي يتم تقييم أدوات التقدير عليها مختلفة**. في الواقع، سيقوم: func: ~ sklearn.model_selection.cross_val_score داخليًا باستدعاء 'cv.split' على نفس مثيل: class: ~ sklearn.model_selection.KFold، ولكن ستكون التقسيمات مختلفة في كل مرة. ينطبق هذا أيضًا على أي أداة تقوم باختيار النماذج عبر التحقق من صحة التعابر، مثل: class: ~ sklearn.model_selection.GridSearchCV و: class: ~ sklearn.model_selection.RandomizedSearchCV: لا يمكن مقارنة الدرجات عبر الطيات المختلفة عبر استدعاءات 'search.fit' المختلفة، نظرًا لأنه سيتم استدعاء 'cv.split' عدة مرات. ومع ذلك، ضمن استدعاء 'search.fit' واحد، تكون المقارنة عبر الطيات ممكنة نظرًا لأن أداة البحث تستدعي 'cv.split' مرة واحدة فقط.

للحصول على نتائج قابلة للمقارنة عبر الطيات في جميع السيناريوهات، يجب تمرير عدد صحيح إلى أداة تقسيم التحقق من صحة التعابر: 'cv = KFold(shuffle=True، random_state=0)'.

.. ملاحظة::
    على الرغم من أن المقارنة عبر الطيات غير مستحسنة مع حالات 'RandomState'، إلا أنه يمكن للمرء أن يتوقع أن تسمح الدرجات المتوسطة باستنتاج ما إذا كانت إحدى أدوات التقدير أفضل من الأخرى، طالما تم استخدام عدد كافٍ من الطيات والبيانات.

.. ملاحظة::
    ما يهم في هذا المثال هو ما تم تمريره إلى: class: ~ sklearn.model_selection.KFold. سواء قمنا بتمرير مثيل 'RandomState' أو عدد صحيح إلى: func: ~ sklearn.datasets.make_classification ليس ذي صلة بغرض التوضيح. أيضًا، لا تعد أداة تقدير: class: ~ sklearn.discriminant_analysis.LinearDiscriminantAnalysis ولا أداة تقدير: class: ~ sklearn.naive_bayes.GaussianNB أدوات تقدير عشوائية.

التوصيات العامة
الحصول على نتائج قابلة للتكرار عبر عمليات التنفيذ المتعددة
.................................................................

من أجل الحصول على نتائج قابلة للتكرار (أي ثابتة) عبر عمليات تنفيذ البرنامج المتعددة، يجب علينا إزالة جميع الاستخدامات لـ `` random_state=None ``، والتي هي القيمة الافتراضية. الطريقة الموصى بها هي إعلان متغير `` rng `` في أعلى البرنامج، وتمريره إلى أي كائن يقبل معلمة `` random_state ``::

    >>> from sklearn.ensemble import RandomForestClassifier
    >>> from sklearn.datasets import make_classification
    >>> from sklearn.model_selection import train_test_split
    >>> import numpy as np

    >>> rng = np.random.RandomState(0)
    >>> X, y = make_classification(random_state=rng)
    >>> rf = RandomForestClassifier(random_state=rng)
    >>> X_train, X_test, y_train, y_test = train_test_split(X, y,
    ...                                                     random_state=rng)
    >>> rf.fit(X_train, y_train).score(X_test, y_test)
    0.84

الآن، نضمن أن نتيجة هذا البرنامج النصي ستكون دائمًا 0.84، بغض النظر عن عدد المرات التي نقوم بتشغيلها فيها. تغيير متغير `` rng `` العالمي إلى قيمة مختلفة يجب أن يؤثر على النتائج، كما هو متوقع.

من الممكن أيضًا إعلان متغير `` rng `` كعدد صحيح. ومع ذلك، فقد يؤدي ذلك إلى نتائج أقل متانة للتحقق من صحة التعبر، كما سنرى في القسم التالي.

.. note::
    لا نوصي بتعيين البذرة العالمية لـ NumPy عن طريق استدعاء `` np.random.seed(0) ``. راجع `هنا <https://stackoverflow.com/questions/5836335/consistently-create-same-random-numpy-array/5837352#comment6712034_5837352>`_ للمناقشة.

متانة نتائج التحقق من صحة التعبر
.........................................

عندما نقيم أداء مقدر عشوائي من خلال التحقق من صحة التعبر، نريد التأكد من أن المقدر يمكنه تقديم تنبؤات دقيقة لبيانات جديدة، ولكننا نريد أيضًا التأكد من أن المقدر متين فيما يتعلق بالتهيئة العشوائية. على سبيل المثال، نود أن تكون تهيئة الأوزان العشوائية لـ :class: `~ sklearn.linear_model.SGDClassifier` جيدة باستمرار عبر جميع الطيات: وإلا، فعند تدريب هذا المقدر على بيانات جديدة، قد لا نكون محظوظين وقد تؤدي التهيئة العشوائية إلى أداء سيئ. وبالمثل، نريد أن تكون الغابة العشوائية متينة فيما يتعلق بمجموعة الميزات التي يتم اختيارها بشكل عشوائي والتي سيستخدمها كل شجرة.

لهذه الأسباب، من الأفضل تقييم أداء التحقق من صحة التعبر عن طريق السماح للمقدر باستخدام RNG مختلف في كل طية. يتم ذلك عن طريق تمرير مثيل `` RandomState `` (أو `` None ``) إلى تهيئة المقدر.

عندما نمرر عددًا صحيحًا، سيستخدم المقدر نفس RNG في كل طية: إذا كان أداء المقدر جيدًا (أو سيئًا)، كما تم تقييمه بواسطة CV، فقد يكون ذلك ببساطة لأننا كنا محظوظين (أو غير محظوظين) مع تلك البذرة المحددة. يؤدي تمرير المثيلات إلى نتائج CV أكثر متانة، ويجعل المقارنة بين الخوارزميات المختلفة أكثر عدلاً. كما يساعد في الحد من الرغبة في معاملة RNG المقدر كمعلمة يمكن ضبطها.

سواء قمنا بتمرير مثيلات `` RandomState `` أو أعداد صحيحة إلى برامج تقسيم CV، لا يؤثر على المتانة، طالما تم استدعاء `` split `` مرة واحدة فقط. عندما يتم استدعاء `` split `` عدة مرات، لم يعد من الممكن إجراء مقارنات بين الطيات. نتيجة لذلك، فإن تمرير الأعداد الصحيحة إلى برامج تقسيم CV أكثر أمانًا عادةً ويغطي معظم حالات الاستخدام.