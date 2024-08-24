إكمال القيم المفقودة
============================

.. currentmodule:: sklearn.impute

لأسباب مختلفة، تحتوي العديد من مجموعات البيانات الواقعية على قيم مفقودة، والتي غالبًا ما تكون مشفرة كمساحات فارغة أو NaN أو أي رموز أخرى. ومع ذلك، لا تتوافق هذه المجموعات مع خوارزميات scikit-learn التي تفترض أن جميع القيم في المصفوفة رقمية، وأن لها معنى. تتمثل إحدى الاستراتيجيات الأساسية لاستخدام مجموعات البيانات غير المكتملة في التخلص من الصفوف و/أو الأعمدة بالكامل التي تحتوي على قيم مفقودة. ومع ذلك، يأتي ذلك مقابل فقدان البيانات التي قد تكون ذات قيمة (على الرغم من عدم اكتمالها). تتمثل الاستراتيجية الأفضل في إكمال القيم المفقودة، أي استنتاجها من الجزء المعروف من البيانات. راجع مدخل المسرد على :term:`imputation`.

إكمال أحادي المتغير مقابل متعدد المتغيرات
======================================

هناك نوع واحد من خوارزميات الإكمال وهو أحادي المتغير، والذي يكمل القيم في البعد i-th لميزة باستخدام القيم غير المفقودة فقط في ذلك البعد المميز (على سبيل المثال: class:`SimpleImputer`). على النقيض من ذلك، تستخدم خوارزميات الإكمال متعددة المتغيرات مجموعة الميزات المتاحة بالكامل لتقدير القيم المفقودة (على سبيل المثال: class:`IterativeImputer`).

.. _single_imputer:

إكمال ميزة أحادية المتغير
=============================

توفر فئة class:`SimpleImputer` استراتيجيات أساسية لإكمال القيم المفقودة. يمكن إكمال القيم المفقودة باستخدام قيمة ثابتة مقدمة، أو باستخدام الإحصاءات (المتوسط أو الوسيط أو الأكثر تكرارًا) لكل عمود توجد فيه القيم المفقودة. تسمح هذه الفئة أيضًا بمخططات ترميز القيم المفقودة المختلفة.

توضح القطعة التالية كيفية استبدال القيم المفقودة، المشفرة كـ ``np.nan``، باستخدام متوسط قيمة الأعمدة (المحور 0) التي تحتوي على القيم المفقودة::

    >>> import numpy as np
    >>> from sklearn.impute import SimpleImputer
    >>> imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    >>> imp.fit([[1, 2], [np.nan, 3], [7, 6]])
    SimpleImputer()
    >>> X = [[np.nan, 2], [6, np.nan], [7, 6]]
    >>> print(imp.transform(X))
    [[4.          2.        ]
     [6.          3.666...]
     [7.          6.        ]]

تدعم فئة class:`SimpleImputer` أيضًا المصفوفات المبعثرة::

    >>> import scipy.sparse as sp
    >>> X = sp.csc_matrix([[1, 2], [0, -1], [8, 4]])
    >>> imp = SimpleImputer(missing_values=-1, strategy='mean')
    >>> imp.fit(X)
    SimpleImputer(missing_values=-1)
    >>> X_test = sp.csc_matrix([[-1, 2], [6, -1], [7, 6]])
    >>> print(imp.transform(X_test).toarray())
    [[3. 2.]
     [6. 3.]
     [7. 6.]]

لاحظ أن هذا التنسيق لا يُقصد به استخدامه لتخزين القيم المفقودة ضمنيًا في المصفوفة لأنه سيكثفها في وقت التحويل. يجب استخدام القيم المفقودة المشفرة بواسطة 0 مع الإدخال الكثيف.

تدعم فئة class:`SimpleImputer` أيضًا البيانات الفئوية الممثلة كقيم سلسلة أو فئات Pandas عند استخدام استراتيجية "most_frequent" أو "constant"::

    >>> import pandas as pd
    >>> df = pd.DataFrame([["a", "x"],
    ...                    [np.nan, "y"],
    ...                    ["a", np.nan],
    ...                    ["b", "y"]], dtype="category")
    ...
    >>> imp = SimpleImputer(strategy="most_frequent")
    >>> print(imp.fit_transform(df))
    [['a' 'x']
     ['a' 'y']
     ['a' 'y']
     ['b' 'y']]

للحصول على مثال آخر على الاستخدام، راجع: ref:`sphx_glr_auto_examples_impute_plot_missing_values.py`.

.. _iterative_imputer:

إكمال ميزة متعددة المتغيرات
===============================

هناك نهج أكثر تطوراً هو استخدام فئة class:`IterativeImputer`، والتي تقوم بتصميم كل ميزة بالقيم المفقودة كدالة للميزات الأخرى، ويتم استخدام هذا التقدير للإكمال. يقوم بذلك بطريقة دورية متكررة: في كل خطوة، يتم تعيين عمود ميزة كإخراج y ويتم التعامل مع أعمدة الميزات الأخرى على أنها مدخلات X. يتم ضبط مرجع على (X، y) للقيم y المعروفة. بعد ذلك، يتم استخدام المرجع للتنبؤ بالقيم المفقودة من y. يتم ذلك لكل ميزة بطريقة تكرارية، ثم يتم تكرارها لـ max_iter جولات الإكمال. يتم إرجاع نتائج جولة الإكمال الأخيرة.

.. note::

   لا يزال هذا المرجع **تجريبيًا** الآن: قد تتغير معلمات الافتراض أو تفاصيل السلوك دون أي دورة تقاعد. سيساعد حل المشكلات التالية في تثبيت class:`IterativeImputer`: معايير التقارب (:issue:`14338`)، والمراجع الافتراضية (:issue:`13286`)، واستخدام حالة التعشيش العشوائي (:issue:`15611`). لاستخدامه، يجب عليك استيراد "enable_iterative_imputer" بشكل صريح.

::

    >>> import numpy as np
    >>> from sklearn.experimental import enable_iterative_imputer
    >>> from sklearn.impute import IterativeImputer
    >>> imp = IterativeImputer(max_iter=10, random_state=0)
    >>> imp.fit([[1, 2], [3, 6], [4, 8], [np.nan, 3], [7, np.nan]])
    IterativeImputer(random_state=0)
    >>> X_test = [[np.nan, 2], [6, np.nan], [np.nan, 6]]
    >>> # يتعلم النموذج أن الميزة الثانية ضعف الأولى
    >>> print(np.round(imp.transform(X_test)))
    [[ 1.  2.]
     [ 6. 12.]
     [ 3.  6.]]

يمكن استخدام كل من class:`SimpleImputer` و class:`IterativeImputer` في خط أنابيب كطريقة لبناء مرجع مركب يدعم الإكمال.
راجع: ref:`sphx_glr_auto_examples_impute_plot_missing_values.py`.

مرونة IterativeImputer
-------------------------------

هناك العديد من حزم الإكمال الراسخة في نظام R البيئي لعلوم البيانات: أميليا، mi، الفئران، missForest، إلخ. تعد missForest شائعة، وتتضح أنها مثال محدد لخوارزميات الإكمال التسلسلية المختلفة التي يمكن تنفيذها جميعًا باستخدام class:`IterativeImputer` عن طريق تمرير مراجعات مختلفة للتنبؤ بقيم الميزات المفقودة. في حالة missForest، يكون هذا المرجع عبارة عن Random Forest.
راجع: ref:`sphx_glr_auto_examples_impute_plot_iterative_imputer_variants_comparison.py`.


.. _multiple_imputation:

الإكمال المتعدد مقابل الإكمال الفردي
------------------------------

في مجتمع الإحصاء، من الشائع إجراء عمليات إكمال متعددة، مما يؤدي إلى إنشاء، على سبيل المثال، عمليات إكمال m منفصلة لمصفوفة ميزة واحدة. يتم بعد ذلك إدخال كل من هذه الإكمال m في خط أنابيب التحليل اللاحق (على سبيل المثال، هندسة الميزات، التجميع، الانحدار، التصنيف). تسمح نتائج التحليل m النهائية (على سبيل المثال، أخطاء التحقق من الصحة المحجوزة) لعالم البيانات بفهم كيفية اختلاف النتائج التحليلية كنتيجة لعدم اليقين المتأصل الذي تسببه القيم المفقودة. يُطلق على الممارسة المذكورة أعلاه اسم الإكمال المتعدد.

استلهمت عملية تنفيذنا لـ class:`IterativeImputer` من حزمة R MICE (الإكمال متعدد المتغيرات بواسطة المعادلات المتسلسلة) [1]_، ولكنها تختلف عنها من خلال إرجاع إكمال واحد بدلاً من عمليات الإكمال المتعددة. ومع ذلك، يمكن أيضًا استخدام class:`IterativeImputer` للإكمال المتعدد عن طريق تطبيقه بشكل متكرر على نفس مجموعة البيانات باستخدام بذور عشوائية مختلفة عند sample_posterior=True``. راجع [2]_، الفصل 4 لمزيد من المناقشة حول الإكمال المتعدد مقابل الإكمال الفردي.

لا يزال من المشكلات المفتوحة مدى فائدة الإكمال الفردي مقابل الإكمال المتعدد في سياق التنبؤ والتصنيف عندما لا يكون المستخدم مهتمًا بقياس عدم اليقين بسبب القيم المفقودة.

لاحظ أن استدعاء طريقة "التحويل" لـ class:`IterativeImputer` غير مسموح بتغيير عدد العينات. لذلك لا يمكن تحقيق عمليات الإكمال المتعددة من خلال استدعاء واحد لـ "التحويل".

مراجع
----------

.. [1] `ستيف فان بويرين، كارين جرووثويس-أودشورن (2011). "الفئران: الإكمال متعدد المتغيرات بواسطة المعادلات المتسلسلة في R". مجلة البرمجيات الإحصائية 45: 1-67. <https://www.jstatsoft.org/article/view/v045i03>`_

.. [2] رودريك جيه إيه ليتل ودونالد بي روبين (1986). "التحليل الإحصائي باستخدام البيانات المفقودة". جون وايلي وأولاده، نيويورك، نيويورك، الولايات المتحدة الأمريكية.

.. _knnimpute:

إكمال أقرب جيران
============================

توفر فئة class:`KNNImputer` الإكمال لملء القيم المفقودة باستخدام نهج k-Nearest Neighbors. بشكل افتراضي، يتم استخدام مسافة يوكليديانية التي تدعم القيم المفقودة، :func:`~sklearn.metrics.pairwise.nan_euclidean_distances`، للعثور على أقرب الجيران. يتم إكمال كل ميزة مفقودة باستخدام القيم من أقرب الجيران n_neighbors التي تحتوي على قيمة للميزة. يتم حساب متوسط ميزة الجيران بالتساوي أو مرجح حسب المسافة إلى كل جار. إذا كان لدى عينة أكثر من ميزة مفقودة، فيمكن أن يكون لدى الجيران لهذه العينة جيران مختلفون اعتمادًا على الميزة المحددة التي يتم إكمالها. عندما يكون عدد الجيران المتاحين أقل من n_neighbors ولا توجد مسافات محددة لمجموعة التدريب، يتم استخدام متوسط مجموعة التدريب لهذه الميزة أثناء الإكمال. إذا كان هناك جار واحد على الأقل بمسافة محددة، فسيتم استخدام المتوسط المرجح أو غير المرجح لباقي الجيران أثناء الإكمال. إذا كانت الميزة مفقودة دائمًا في التدريب، فسيتم إزالتها أثناء التحويل. لمزيد من المعلومات حول المنهجية، راجع ref. [OL2001]_.

توضح القطعة التالية كيفية استبدال القيم المفقودة، المشفرة كـ ``np.nan``، باستخدام متوسط قيمة الميزة لأقرب جارين للعينات التي تحتوي على قيم مفقودة::

    >>> import numpy as np
    >>> from sklearn.impute import KNNImputer
    >>> nan = np.nan
    >>> X = [[1, 2, nan], [3, 4, 3], [nan, 6, 5], [8, 8, 7]]
    >>> imputer = KNNImputer(n_neighbors=2, weights="uniform")
    >>> imputer.fit_transform(X)
    array([[1. , 2. , 4. ],
           [3. , 4. , 3. ],
           [5.5, 6. , 5. ],
           [8. , 8. , 7. ]])

للحصول على مثال آخر على الاستخدام، راجع: ref:`sphx_glr_auto_examples_impute_plot_missing_values.py`.

.. rubric:: References

.. [OL2001] `أولغا ترويانسكايا، مايكل كانتور، جافين شيرلوك، بات براون، تريفور هاستي، روبرت تيبشيران، ديفيد بوتستين وروس ب. ألتمان، أساليب تقدير القيمة المفقودة لمصفوفات الدنا الدقيقة، BIOINFORMATICS المجلد 17 رقم 6، 2001 الصفحات 520-525. <https://academic.oup.com/bioinformatics/article/17/6/520/272365>`_

الحفاظ على عدد الميزات ثابتًا
=======================================

بشكل افتراضي، ستتخلص برامج إكمال scikit-learn من الميزات الفارغة تمامًا، أي أعمدة تحتوي فقط على قيم مفقودة. على سبيل المثال::

  >>> imputer = SimpleImputer()
  >>> X = np.array([[np.nan، 1]، [np.nan، 2]، [np.nan، 3]])
  >>> imputer.fit_transform(X)
  array([[1.]
         [2.]
         [3.]])

تم إسقاط الميزة الأولى في X التي تحتوي فقط على قيم np.nan بعد الإكمال. بينما لن تساعد هذه الميزة في الإعداد التنبئي، فإن إسقاط الأعمدة سيغير شكل X والذي قد يكون مشكلة عند استخدام برامج الإكمال في خط أنابيب التعلم الآلي الأكثر تعقيدًا. يوفر معلمة keep_empty_features خيار الاحتفاظ بالميزات الفارغة عن طريق الإكمال بقيم ثابتة. في معظم الحالات، تكون هذه القيمة الثابتة صفرًا::

  >>> imputer.set_params(keep_empty_features=True)
  SimpleImputer(keep_empty_features=True)
  >>> imputer.fit_transform(X)
  array([[0.، 1.]
         [0.، 2.]
         [0.، 3.]])

.. _missing_indicator:

وضع علامة على القيم المكتملة
محول :class:`MissingIndicator` مفيد لتحويل مجموعة بيانات إلى مصفوفة ثنائية مقابلة تشير إلى وجود قيم مفقودة في مجموعة البيانات. وهذا التحول مفيد بالاقتران مع الاستيفاء. عند استخدام الاستيفاء، فإن الحفاظ على المعلومات حول القيم التي كانت مفقودة يمكن أن يكون مفيدًا. لاحظ أن كلاً من :class:`SimpleImputer` و :class:`IterativeImputer` لهما معلمة منطقية ``add_indicator`` (القيمة الافتراضية هي ``False``) والتي عند تعيينها إلى ``True`` توفر طريقة ملائمة لدمج إخراج محول :class:`MissingIndicator` مع إخراج المستوفي.

عادةً ما يتم استخدام ``NaN`` كمساحة حجز للقيم المفقودة. ومع ذلك، فإنه يجبر نوع البيانات على أن يكون float. تسمح المعلمة ``missing_values`` بتحديد مساحة حجز أخرى مثل integer. في المثال التالي، سنستخدم ``-1`` كقيم مفقودة::

  >>> from sklearn.impute import MissingIndicator
  >>> X = np.array([[-1, -1, 1, 3],
  ...               [4, -1, 0, -1],
  ...               [8, -1, 1, 0]])
  >>> indicator = MissingIndicator(missing_values=-1)
  >>> mask_missing_values_only = indicator.fit_transform(X)
  >>> mask_missing_values_only
  array([[ True,  True, False],
         [False,  True,  True],
         [False,  True, False]])

يستخدم معلمة ``features`` لاختيار الميزات التي يتم بناء القناع لها. بشكل افتراضي، يكون ``'missing-only'`` الذي يعيد قناع المستوفي للميزات التي تحتوي على قيم مفقودة في وقت ``fit``::

  >>> indicator.features_
  array([0, 1, 3])

يمكن تعيين معلمة ``features`` إلى ``'all'`` لإرجاع جميع الميزات سواء احتوت على قيم مفقودة أم لا::

  >>> indicator = MissingIndicator(missing_values=-1, features="all")
  >>> mask_all = indicator.fit_transform(X)
  >>> mask_all
  array([[ True,  True, False, False],
         [False,  True, False,  True],
         [False,  True, False, False]])
  >>> indicator.features_
  array([0, 1, 2, 3])

عند استخدام :class:`MissingIndicator` في :class:`~sklearn.pipeline.Pipeline`، تأكد من استخدام :class:`~sklearn.pipeline.FeatureUnion` أو :class:`~sklearn.compose.ColumnTransformer` لإضافة ميزات المؤشر إلى الميزات العادية. أولاً، نحصل على مجموعة بيانات `iris`، ونضيف بعض القيم المفقودة إليها.

  >>> from sklearn.datasets import load_iris
  >>> from sklearn.impute import SimpleImputer, MissingIndicator
  >>> from sklearn.model_selection import train_test_split
  >>> from sklearn.pipeline import FeatureUnion, make_pipeline
  >>> from sklearn.tree import DecisionTreeClassifier
  >>> X, y = load_iris(return_X_y=True)
  >>> mask = np.random.randint(0, 2, size=X.shape).astype(bool)
  >>> X[mask] = np.nan
  >>> X_train, X_test, y_train, _ = train_test_split(X, y, test_size=100,
  ...                                                random_state=0)

الآن نقوم بإنشاء :class:`~sklearn.pipeline.FeatureUnion`. سيتم استيفاء جميع الميزات باستخدام :class:`SimpleImputer`، وذلك لتمكين المصنفات من العمل مع هذه البيانات. بالإضافة إلى ذلك، فإنه يضيف المتغيرات المؤشر من :class:`MissingIndicator`.

  >>> transformer = FeatureUnion(
  ...     transformer_list=[
  ...         ('features', SimpleImputer(strategy='mean')),
  ...         ('indicators', MissingIndicator())])
  >>> transformer = transformer.fit(X_train, y_train)
  >>> results = transformer.transform(X_test)
  >>> results.shape
  (100, 8)

بالطبع، لا يمكننا استخدام المحول للتنبؤ. يجب أن نلف هذا في :class:`~sklearn.pipeline.Pipeline` مع مصنف (على سبيل المثال، :class:`~sklearn.tree.DecisionTreeClassifier`) ليكون قادرًا على إجراء تنبؤات.

  >>> clf = make_pipeline(transformer, DecisionTreeClassifier())
  >>> clf = clf.fit(X_train, y_train)
  >>> results = clf.predict(X_test)
  >>> results.shape
  (100,)

المقدرات التي تتعامل مع قيم NaN
==============================

تم تصميم بعض المقدرات للتعامل مع قيم NaN بدون معالجة مسبقة.
فيما يلي قائمة بهذه المقدرات، مصنفة حسب النوع
(عنقود، مرجع، مصنف، تحويل):

.. allow_nan_estimators::