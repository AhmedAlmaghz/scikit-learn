خطوط الأنابيب ومقدّرات المُركّبات
==================================

لإنشاء مُقدّر مُركّب، يتم عادةً دمج المحوّلات مع محوّلات أخرى أو مع مُتنبّئات
(مثل المُصنّفات أو المُرتّبات). أكثر الأدوات شيوعًا المُستخدمة لتأليف المُقدّرات هي
خط الأنابيب. تتطلّب خطوط الأنابيب أن تكون جميع الخطوات باستثناء الأخيرة مُحوّلًا.
يمكن أن تكون الخطوة الأخيرة أي شيء، مُحوّل أو مُتنبّئ أو مُقدّر تجميع قد يكون أو لا
يكون لديه طريقة ".predict(...)" . يُعرّض خط الأنابيب جميع الطرق التي يوفّرها المُقدّر
الأخير: إذا وفّرت الخطوة الأخيرة طريقة "transform"، فسيكون لخط الأنابيب طريقة
"transform" ويتصرّف مثل المُحوّل. إذا وفّرت الخطوة الأخيرة طريقة "predict"، فسيكشف
خط الأنابيب عن تلك الطريقة، وبالنسبة لبيانات "X"، يستخدم جميع الخطوات باستثناء
الأخيرة لتحويل البيانات، ثم يُمرّر تلك البيانات المُحوّلة إلى طريقة "predict"
للخطوة الأخيرة من خط الأنابيب. غالبًا ما تُستخدم فئة "Pipeline" بالاقتران مع
"ColumnTransformer" أو "FeatureUnion" الذي يُدمج ناتج المحوّلات في مساحة مُميّزة
مُركّبة.

خط الأنابيب: تسلسل المُقدّرات
=============================

يمكن استخدام "Pipeline" لتسلسل مُقدّرات مُتعدّدة في مُقدّر واحد. هذا مفيد لأن
هناك غالبًا تسلسل ثابت من الخطوات في معالجة البيانات، على سبيل المثال اختيار
السمات، التطبيع والتصنيف. يخدم خط الأنابيب أغراضًا مُتعدّدة هنا:

الراحة والتغليف
    تحتاج فقط إلى استدعاء "fit" و "predict" مرة واحدة على بياناتك لتناسب تسلسلًا
    كاملًا من المُقدّرات.
اختيار المُعاملات المُشتركة
    يمكنك البحث الشبكي على مُعاملات جميع المُقدّرات في خط الأنابيب في نفس الوقت.
السلامة
    تُساعد خطوط الأنابيب على تجنّب تسريب الإحصاءات من بيانات الاختبار إلى النموذج
    المُدرّب في التصديق المُتقاطع، عن طريق ضمان استخدام نفس العينات لتدريب
    المُحوّلات والمُتنبّئات.

يجب أن تكون جميع المُقدّرات في خط الأنابيب، باستثناء الأخير، مُحوّلات (أي يجب أن
يكون لديها طريقة "transform"). قد يكون المُقدّر الأخير أي نوع (مُحوّل، مُصنّف،
إلخ).

.. note::

    إن استدعاء "fit" على خط الأنابيب هو نفسه استدعاء "fit" على كل مُقدّر بدوره،
    ويُحوّل الإدخال ويمرّره إلى الخطوة التالية. لدي خط الأنابيب جميع الطرق التي
    يمتلكها المُقدّر الأخير في خط الأنابيب، أي إذا كان المُقدّر الأخير مُصنّفًا،
    فيمكن استخدام "Pipeline" كمُصنّف. إذا كان المُقدّر الأخير مُحوّلًا، فسيصبح
    خط الأنابيب كذلك.

الاستخدام
-----

بناء خط أنابيب
................

يتم بناء خط الأنابيب باستخدام قائمة من أزواج "(key, value)"، حيث "key" هو سلسلة
تحتوي على الاسم الذي تريد منحه لهذه الخطوة و "value" هو كائن المُقدّر::

    >>> from sklearn.pipeline import Pipeline
    >>> from sklearn.svm import SVC
    >>> from sklearn.decomposition import PCA
    >>> estimators = [('reduce_dim', PCA()), ('clf', SVC())]
    >>> pipe = Pipeline(estimators)
    >>> pipe
    Pipeline(steps=[('reduce_dim', PCA()), ('clf', SVC())])

الوصول إلى خطوات خط الأنابيب
.....................

يتم تخزين مُقدّرات خط الأنابيب على شكل قائمة في سمة "steps". يمكن استخراج
خط أنابيب فرعي باستخدام ترميز الشرائح المُستخدم عادةً لتسلسلات Python مثل
القوائم أو السلاسل (على الرغم من السماح فقط بخطوة واحدة). هذا مُفيد لأداء بعض
التحويلات فقط (أو عكسها)::

    >>> pipe[:1]
    Pipeline(steps=[('reduce_dim', PCA())])
    >>> pipe[-1:]
    Pipeline(steps=[('clf', SVC())])

الوصول إلى خطوة حسب الاسم أو الموضع
  يمكن أيضًا الوصول إلى خطوة مُحدّدة عن طريق الفهرسة (بـ "[idx]") في خط الأنابيب::

      >>> pipe.steps[0]
      ('reduce_dim', PCA())
      >>> pipe[0]
      PCA()
      >>> pipe['reduce_dim']
      PCA()

  تتيح سمة "named_steps" لخط الأنابيب الوصول إلى الخطوات حسب الاسم مع اكتمال التبويب
  في البيئات التفاعلية::

      >>> pipe.named_steps.reduce_dim is pipe['reduce_dim']
      True

تتبّع أسماء الميزات في خط أنابيب
............................

لتمكين فحص النموذج، لدى "Pipeline" طريقة "get_feature_names_out()"، تمامًا مثل
جميع المُحوّلات. يمكنك استخدام تقطيع خط الأنابيب للحصول على أسماء الميزات التي
تدخل كل خطوة::

    >>> from sklearn.datasets import load_iris
    >>> from sklearn.linear_model import LogisticRegression
    >>> from sklearn.feature_selection import SelectKBest
    >>> iris = load_iris()
    >>> pipe = Pipeline(steps=[
    ...    ('select', SelectKBest(k=2)),
    ...    ('clf', LogisticRegression())])
    >>> pipe.fit(iris.data, iris.target)
    Pipeline(steps=[('select', SelectKBest(...)), ('clf', LogisticRegression(...))])
    >>> pipe[:-1].get_feature_names_out()
    array(['x2', 'x3'], ...)

تخصيص أسماء الميزات
  يمكنك أيضًا توفير أسماء ميزات مُخصّصة للبيانات المُدخلة باستخدام "get_feature_names_out"::

      >>> pipe[:-1].get_feature_names_out(iris.feature_names)
      array(['petal length (cm)', 'petal width (cm)'], ...)

الوصول إلى المُعاملات المُتعرّشة
...........................

من الشائع ضبط مُعاملات مُقدّر ضمن خط أنابيب. لذلك، فإن هذا المُعامِل مُتعرّش
لأنه ينتمي إلى خطوة فرعية مُحدّدة. يمكن الوصول إلى مُعاملات المُقدّرات في خط
الأنابيب باستخدام بناء الجملة "<estimator> __ <parameter>" ::

    >>> pipe = Pipeline(steps=[("reduce_dim", PCA()), ("clf", SVC())])
    >>> pipe.set_params(clf__C=10)
    Pipeline(steps=[('reduce_dim', PCA()), ('clf', SVC(C=10))])

متى يهم الأمر؟
  هذا مهم بشكل خاص للبحث الشبكي::

      >>> from sklearn.model_selection import GridSearchCV
      >>> param_grid = dict(reduce_dim__n_components=[2, 5, 10],
      ...                   clf__C=[0.1, 10, 100])
      >>> grid_search = GridSearchCV(pipe, param_grid=param_grid)

  قد يتم أيضًا استبدال الخطوات الفردية كمُعاملات، ويمكن تجاهل الخطوات غير النهائية
  عن طريق تعيينها على "passthrough"::

      >>> param_grid = dict(reduce_dim=['passthrough', PCA(5), PCA(10)],
      ...                   clf=[SVC(), LogisticRegression()],
      ...                   clf__C=[0.1, 10, 100])
      >>> grid_search = GridSearchCV(pipe, param_grid=param_grid)

  .. seealso::

    * :ref:`composite_grid_search`

الأمثلة
........

* :ref:`sphx_glr_auto_examples_feature_selection_plot_feature_selection_pipeline.py`
* :ref:`sphx_glr_auto_examples_model_selection_plot_grid_search_text_feature_extraction.py`
* :ref:`sphx_glr_auto_examples_compose_plot_digits_pipe.py`
* :ref:`sphx_glr_auto_examples_miscellaneous_plot_kernel_approximation.py`
* :ref:`sphx_glr_auto_examples_svm_plot_svm_anova.py`
* :ref:`sphx_glr_auto_examples_compose_plot_compare_reduction.py`
* :ref:`sphx_glr_auto_examples_miscellaneous_plot_pipeline_display.py`

ذاكرة التخزين المؤقت للمُحوّلات: تجنّب الحساب المُتكرّر
-------------------------------------------------

قد يكون ضبط المُحوّلات مُكلفًا من الناحية الحسابية. باستخدام مُعامله "memory" المُعيّن،
سيقوم "Pipeline" بتخزين كل مُحوّل في الذاكرة بعد استدعاء "fit".
يتم استخدام هذه الميزة لتجنّب حساب المُحوّلات المُلائمة ضمن خط أنابيب إذا كانت
المُعاملات وبيانات الإدخال مُتطابقة. مثال نموذجي هو حالة البحث الشبكي حيث
يمكن ملاءمة المُحوّلات مرة واحدة فقط وإعادة استخدامها لكل تكوين. لن يتم تخزين
الخطوة الأخيرة مطلقًا، حتى إذا كانت مُحوّل.

يتم استخدام مُعامِل "memory" لتخزين المُحوّلات في الذاكرة. يمكن أن يكون "memory"
إما سلسلة تحتوي على الدليل الذي سيتم فيه تخزين المُحوّلات المؤقتة أو كائن
"joblib.Memory".

.. dropdown:: الآثار الجانبية لتخزين المُحوّلات المؤقتة
  :color: warning

  بدون تمكين التخزين المؤقت، يمكن فحص مثيل المُحوّل الأصلي كما هو مُبيّن أدناه::

      >>> from sklearn.datasets import load_digits
      >>> X_digits, y_digits = load_digits(return_X_y=True)
      >>> pca1 = PCA(n_components=10)
      >>> svm1 = SVC()
      >>> pipe = Pipeline([('reduce_dim', pca1), ('clf', svm1)])
      >>> pipe.fit(X_digits, y_digits)
      Pipeline(steps=[('reduce_dim', PCA(n_components=10)), ('clf', SVC())])
      >>> # يمكن فحص مثيل PCA مباشرةً
      >>> pca1.components_.shape
      (10, 64)

  يؤدي تمكين التخزين المؤقت إلى تشغيل نسخة من المُحوّلات قبل الضبط. لذلك، لا
  يمكن فحص مثيل المُحوّل المُعطى لخط الأنابيب مباشرةً. في المثال التالي، سيؤدّي
  الوصول إلى مثيل "PCA" إلى رفع "AttributeError" نظرًا لأن "pca2" سيكون مُحوّلًا
  غير مُلائم. بدلاً من ذلك، استخدم سمة "named_steps" لفحص المُقدّرات ضمن
  خط الأنابيب::

      >>> cachedir = mkdtemp()
      >>> pca2 = PCA(n_components=10)
      >>> svm2 = SVC()
      >>> cached_pipe = Pipeline([('reduce_dim', pca2), ('clf', svm2)],
      ...                        memory=cachedir)
      >>> cached_pipe.fit(X_digits, y_digits)
      Pipeline(memory=...,
               steps=[('reduce_dim', PCA(n_components=10)), ('clf', SVC())])
      >>> cached_pipe.named_steps['reduce_dim'].components_.shape
      (10, 64)
      >>> # إزالة دليل التخزين المؤقت
      >>> rmtree(cachedir)

الأمثلة
........

* :ref:`sphx_glr_auto_examples_compose_plot_compare_reduction.py`

تحويل الهدف في الانحدار
يحوّل :class:`~sklearn.compose.TransformedTargetRegressor` الأهداف ``y`` قبل ضبط نموذج الانحدار. يتم إعادة تعيين التوقعات إلى المجال الأصلي عن طريق تحويل عكسي. يأخذ كحجة المنحنى الذي سيتم استخدامه للتنبؤ، والمحول الذي سيتم تطبيقه على متغير الهدف::

>>> استيراد numpy كالن
>>> من sklearn.datasets استيراد fetch_california_housing
>>> من sklearn.compose استيراد TransformedTargetRegressor
>>> من sklearn.preprocessing استيراد QuantileTransformer
>>> من sklearn.linear_model استيراد LinearRegression
>>> من sklearn.model_selection استيراد train_test_split
>>> X، y = fetch_california_housing(return_X_y=True)
>>> X، y = X [: 2000:،:]، y [: 2000] # حدد جزءًا من البيانات
>>> المحول = QuantileTransformer(output_distribution='normal')
>>> المنحنى = LinearRegression()
>>> regr = TransformedTargetRegressor(المنحنى = المنحنى،
... المحول = المحول)
>>> X_train، X_test، y_train، y_test = train_test_split(X، y، random_state=0)
>>> regr.fit(X_train، y_train)
TransformedTargetRegressor (...)
>>> طباعة ('R2 score: {0:.2f}'.format(regr.score(X_test، y_test)))
R2 score: 0.61
>>> raw_target_regr = LinearRegression().fit(X_train، y_train)
>>> طباعة ('R2 score: {0:.2f}'.format(raw_target_regr.score(X_test، y_test)))
R2 score: 0.59

بالنسبة للتحويلات البسيطة، بدلاً من كائن Transformer، يمكن تمرير زوج من الدالات التي تحدد التحويل ورسمها العكسي::

>>> def func(x):
... return np.log(x)
>>> def inverse_func(x):
... return np.exp(x)

بعد ذلك، يتم إنشاء الكائن على النحو التالي::

>>> regr = TransformedTargetRegressor(المنحنى = المنحنى،
... func = func،
... inverse_func = inverse_func)
>>> regr.fit(X_train، y_train)
TransformedTargetRegressor (...)
>>> طباعة ('R2 score: {0:.2f}'.format(regr.score(X_test، y_test)))
R2 score: 0.51

بشكل افتراضي، يتم التحقق من الدالات المقدمة في كل عملية ضبط لكونها عكس بعضها البعض. ومع ذلك، من الممكن تجاوز هذا التحقق عن طريق تعيين ``check_inverse`` إلى ``False``::

>>> def inverse_func(x):
... return x
>>> regr = TransformedTargetRegressor(المنحنى = المنحنى،
... func = func،
... inverse_func = inverse_func،
... check_inverse = False)
>>> regr.fit(X_train، y_train)
TransformedTargetRegressor (...)
>>> طباعة ('R2 score: {0:.2f}'.format(regr.score(X_test، y_test)))
R2 score: -1.57

.. note::

يمكن تشغيل التحويل عن طريق تعيين إما ``transformer`` أو
زوج من الدوال ``func`` و ``inverse_func``. ومع ذلك، فإن تعيين كلا الخيارين سيرفع خطأ.

.. rubric:: أمثلة

* :ref: 'sphx_glr_auto_examples_compose_plot_transformed_target.py'


.. _feature_union:

FeatureUnion: مساحات الميزات المركبة
======================================

.. currentmodule:: sklearn.pipeline

:class: 'FeatureUnion' يجمع بين العديد من كائنات المحول في محول جديد
يضم إخراجها. يأخذ :class: 'FeatureUnion' قائمة من كائنات المحول. أثناء الضبط،
يتم ضبط كل منها على البيانات بشكل مستقل. يتم تطبيق المحولات بالتوازي،
ويتم ضم مصفوفات الميزات التي ينتجونها جنبًا إلى جنب في مصفوفة أكبر.

عندما تريد تطبيق تحويلات مختلفة على كل حقل من البيانات،
راجع فئة :class: '~sklearn.compose.ColumnTransformer' ذات الصلة
(راجع: ref: 'دليل المستخدم <column_transformer>`__).

:class: 'FeatureUnion' يخدم نفس الأغراض مثل :class: 'Pipeline' -
الراحة والتقدير المشترك للمؤشرات والتحقق من صحتها.

يمكن الجمع بين :class: 'FeatureUnion' و :class: 'Pipeline' ل
إنشاء نماذج معقدة.

(ليس لدى :class: 'FeatureUnion' طريقة للتحقق مما إذا كان محولان
قد ينتجان ميزات متطابقة. فهو ينتج اتحادًا فقط عندما تكون مجموعات الميزات غير متداخلة،
والتأكد من أنها كذلك هو مسؤولية المتصل.)


الاستخدام
-----

يتم بناء :class: 'FeatureUnion' باستخدام قائمة من أزواج ``(key، value)``،
حيث ``key`` هو الاسم الذي تريد إعطاءه لتحويل معين
(سلسلة تعسفية؛ فهو يعمل فقط كمعرف)
و ``value`` هو كائن مقدر::

>>> من sklearn.pipeline استيراد FeatureUnion
>>> من sklearn.decomposition استيراد PCA
>>> من sklearn.decomposition استيراد KernelPCA
>>> المقدرات = [('pca الخطي'، PCA())، ('kernel_pca'، KernelPCA())]
>>> مجتمعة = FeatureUnion(المقدرات)
>>> مجتمعة
FeatureUnion(قائمة المحول = [('pca الخطي'، PCA())،
('kernel_pca'، KernelPCA())])

مثل خطوط الأنابيب، لدى اتحادات الميزات بناء مختصر يسمى
:func: 'make_union' الذي لا يتطلب تسمية صريحة للمكونات.


مثل "خط الأنابيب"، يمكن استبدال الخطوات الفردية باستخدام "set_params"،
ويتم تجاهلها عن طريق تعيينها على "drop"::

>>> مجتمعة.set_params(kernel_pca='drop')
FeatureUnion(قائمة المحول = [('pca الخطي'، PCA())،
('kernel_pca'، 'drop')])

.. rubric:: أمثلة

* :ref: 'sphx_glr_auto_examples_compose_plot_feature_union.py'


.. _column_transformer:

ColumnTransformer للبيانات غير المتجانسة
تحتوي العديد من مجموعات البيانات على سمات من أنواع مختلفة، مثل النصوص والأعداد العشرية والتواريخ، حيث يتطلب كل نوع من السمات خطوات معالجة أو استخراج سمات منفصلة. وغالبًا ما يكون من الأسهل معالجة البيانات قبل تطبيق أساليب التعلم في سكيت-ليرن، على سبيل المثال باستخدام بانداس.

قد تكون معالجة بياناتك قبل تمريرها إلى سكيت-ليرن مشكلة لأحد الأسباب التالية:

1. يؤدي دمج الإحصاءات من بيانات الاختبار في معالجات ما قبل المعالجة إلى جعل درجات الضبط غير موثوقة (تُعرف باسم "تسرب البيانات")، على سبيل المثال في حالة معايرات أو استكمال القيم المفقودة.
2. قد ترغب في تضمين معلمات معالجات ما قبل المعالجة في بحث عن المعلمات.

تساعد class ~ sklearn.compose.ColumnTransformer في إجراء تحويلات مختلفة لأعمدة مختلفة من البيانات، داخل class ~ sklearn.pipeline.Pipeline التي تكون آمنة من تسرب البيانات والتي يمكن معلمتها. تعمل class ~ sklearn.compose.ColumnTransformer على المصفوفات والمصفوفات المبعثرة، وبيانات الإطار من بانداس.

يمكن تطبيق تحويل مختلف على كل عمود، مثل المعالجة المسبقة أو طريقة استخراج ميزات محددة:

بالنسبة لهذه البيانات، قد نرغب في ترميز عمود "المدينة" كمتغير فئوي باستخدام class ~ sklearn.preprocessing.OneHotEncoder ولكن تطبيق class ~ sklearn.feature_extraction.text.CountVectorizer على عمود "العنوان". نظرًا لأننا قد نستخدم طرق استخراج ميزات متعددة على نفس العمود، فإننا نعطي كل محول اسماً فريداً، مثل "city_category" و"title_bow". يتم تجاهل أعمدة التصنيف المتبقية بشكل افتراضي (remainder='drop'):

في المثال أعلاه، يتوقع class ~ sklearn.feature_extraction.text.CountVectorizer مصفوفة أحادية البعد كإدخال، وبالتالي تم تحديد الأعمدة كسلسلة ("العنوان"). ومع ذلك، فإن class ~ sklearn.preprocessing.OneHotEncoder، مثل معظم المحولات الأخرى، يتوقع بيانات ثنائية الأبعاد، لذلك في هذه الحالة، يلزم تحديد العمود كقائمة من السلاسل (["المدينة"]).

وبصرف النظر عن قيمة قياسية أو قائمة فردية، يمكن تحديد اختيار العمود كقائمة من عدة عناصر، أو مصفوفة من الأعداد الصحيحة، أو شريحة، أو قناع منطقي، أو باستخدام: func ~ sklearn.compose.make_column_selector. يتم استخدام: func ~ sklearn.compose.make_column_selector لاختيار الأعمدة استنادًا إلى نوع البيانات أو اسم العمود:

يمكن أن تشير السلاسل إلى أعمدة إذا كان الإدخال عبارة عن إطار بيانات، ويتم تفسير الأعداد الصحيحة دائمًا على أنها أعمدة موضعية.

يمكننا الاحتفاظ بأعمدة التصنيف المتبقية عن طريق تعيين "remainder='passthrough'". يتم إضافة القيم إلى نهاية التحول:

يمكن تعيين معلمة "remainder" إلى محدد مواقع معلومات لتحويل أعمدة التصنيف المتبقية. يتم إضافة القيم المحولة إلى نهاية التحول:

يمكن الإشارة إلى الأعمدة بواسطة السلاسل إذا كان الإدخال عبارة عن إطار بيانات، ويتم تفسير الأعداد الصحيحة دائمًا على أنها أعمدة موضعية.

يمكن عرض المحولات باستخدام تمثيل HTML عند عرضها في دفتر ملاحظات Jupyter. وهذا مفيد لتشخيص أو تصور خط أنابيب به العديد من المحولات. يتم تنشيط هذا التصور بشكل افتراضي:

يمكن إلغاء تنشيطه عن طريق تعيين خيار "العرض" في: func ~ sklearn.set_config إلى "النص":

يمكن الاطلاع على مثال على إخراج HTML في قسم "تمثيل HTML لخط الأنابيب" من: ref: sphx_glr_auto_examples_compose_plot_column_transformer_mixed_types.py. كبديل، يمكن كتابة HTML في ملف باستخدام: func ~ sklearn.utils.estimator_html_repr:

.. rubric:: الأمثلة

* : ref: sphx_glr_auto_examples_compose_plot_column_transformer.py
* : ref: sphx_glr_auto_examples_compose_plot_column_transformer_mixed_types.py