معالجة البيانات الأولية
==================

توفر حزمة ``sklearn.preprocessing`` العديد من وظائف المنفعة الشائعة وفئات المحول لتغيير متجهات الميزات الأولية إلى تمثيل أكثر ملاءمة للمقدّرات النهائية.

بشكل عام، يستفيد العديد من خوارزميات التعلم، مثل النماذج الخطية، من توحيد مجموعة البيانات
(راجع: ref:`sphx_glr_auto_examples_preprocessing_plot_scaling_importance.py`).
إذا كانت هناك بعض القيم الشاذة في المجموعة، فقد يكون استخدام المقيّمين المتينين أو محولات أخرى أكثر ملاءمة. يتم تسليط الضوء على سلوك المقاييس والمحولات والمطبعين المختلفين على مجموعة بيانات تحتوي على قيم شاذة هامشية في
:ref:`sphx_glr_auto_examples_preprocessing_plot_all_scaling.py`.


توحيد البيانات، أو إزالة المتوسط وتقييم التباين
=====================================================

**توحيد** مجموعات البيانات هو **متطلب شائع للعديد من
مقدرات التعلم الآلي** المطبقة في scikit-learn؛ فقد لا تعمل بشكل جيد إذا لم تكن الميزات الفردية أكثر أو أقل تشابهاً مع البيانات العادية الموزعة بشكل طبيعي: غاوسي مع **صفر متوسط وانحراف معياري واحد**.

في الممارسة العملية، غالبًا ما نتجاهل شكل التوزيع ونحول البيانات فقط لمركزها عن طريق إزالة القيمة المتوسطة لكل ميزة، ثم قياسها عن طريق قسمة الميزات غير الثابتة على انحرافها المعياري.

على سبيل المثال، قد تفترض العديد من العناصر المستخدمة في الدالة الهدف
لخوارزمية التعلم (مثل نواة RBF لآلات المتجهات الداعمة أو المنظمين l1 وl2 للنماذج الخطية) أن جميع الميزات تتمحور حول الصفر أو لها تباين بنفس الترتيب. إذا كان لميزة ما تباين أكبر بعدة أوامر من الحجم من الآخرين، فقد تهيمن على الدالة الهدف وتجعل المقدر غير قادر على التعلم بشكل صحيح من الميزات الأخرى كما هو متوقع.


توفر الوحدة النمطية :mod:`~sklearn.preprocessing` فئة
:class:`StandardScaler` ، والتي تعد طريقة سريعة وسهلة لأداء العملية التالية على مجموعة بيانات تشبه المصفوفة::

  >>> from sklearn import preprocessing
  >>> import numpy as np
  >>> X_train = np.array([[ 1., -1.,  2.],
  ...                     [ 2.,  0.,  0.],
  ...                     [ 0.,  1., -1.]])
  >>> scaler = preprocessing.StandardScaler().fit(X_train)
  >>> scaler
  StandardScaler()

  >>> scaler.mean_
  array([1. ..., 0. ..., 0.33...])

  >>> scaler.scale_
  array([0.81..., 0.81..., 1.24...])

  >>> X_scaled = scaler.transform(X_train)
  >>> X_scaled
  array([[ 0.  ..., -1.22...,  1.33...],
         [ 1.22...,  0.  ..., -0.26...],
         [-1.22...,  1.22..., -1.06...]])

..
        >>> import numpy as np
        >>> print_options = np.get_printoptions()
        >>> np.set_printoptions(suppress=True)

تكون للبيانات المُدرجة صفر متوسط وانحراف معياري واحد::

  >>> X_scaled.mean(axis=0)
  array([0., 0., 0.])

  >>> X_scaled.std(axis=0)
  array([1., 1., 1.])

..    >>> print_options = np.set_printoptions(print_options)

تنفذ هذه الفئة واجهة برمجة التطبيقات "المحول" (Transformer API) لحساب المتوسط والانحراف المعياري لمجموعة تدريب بحيث يمكن إعادة تطبيق نفس التحويل لاحقًا على مجموعة الاختبار. وبالتالي، فإن هذه الفئة مناسبة
للاستخدام في الخطوات الأولى من :class:`~sklearn.pipeline.Pipeline`::

  >>> from sklearn.datasets import make_classification
  >>> from sklearn.linear_model import LogisticRegression
  >>> from sklearn.model_selection import train_test_split
  >>> from sklearn.pipeline import make_pipeline
  >>> from sklearn.preprocessing import StandardScaler

  >>> X, y = make_classification(random_state=42)
  >>> X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
  >>> pipe = make_pipeline(StandardScaler(), LogisticRegression())
  >>> pipe.fit(X_train, y_train)  # تطبيق التوحيد على بيانات التدريب
  Pipeline(steps=[('standardscaler', StandardScaler()),
                  ('logisticregression', LogisticRegression())])

  >>> pipe.score(X_test, y_test)  # تطبيق التوحيد على بيانات الاختبار، دون تسريب بيانات التدريب.
  0.96

من الممكن تعطيل التمركيز أو التقييم عن طريق تمرير إما
``with_mean=False`` أو ``with_std=False`` إلى منشئ
:class:`StandardScaler`.


تقييم الميزات إلى نطاق
---------------------------

يتمثل التوحيد البديل في تقييم الميزات بحيث
تقع ضمن نطاق قيمة دنيا وقصوى معين، وغالبًا ما يكون بين الصفر والواحد،
أو بحيث يتم تقييم القيمة المطلقة القصوى لكل ميزة إلى الحجم الوحيد.
يمكن تحقيق ذلك باستخدام :class:`MinMaxScaler` أو :class:`MaxAbsScaler`،
على التوالي.

ويشمل الدافع لاستخدام هذا التقييم المرونة تجاه الانحرافات المعيارية الصغيرة جدًا للميزات والحفاظ على الإدخالات الصفرية في البيانات المتناثرة.

فيما يلي مثال على تقييم مصفوفة بيانات تجريبية إلى النطاق ``[0، 1]``::

  >>> X_train = np.array([[ 1., -1.,  2.],
  ...                     [ 2.,  0.,  0.],
  ...                     [ 0.,  1., -1.]])
  ...
  >>> min_max_scaler = preprocessing.MinMaxScaler()
  >>> X_train_minmax = min_max_scaler.fit_transform(X_train)
  >>> X_train_minmax
  array([[0.5       , 0.        , 1.        ],
         [1.        , 0.5       , 0.33333333],
         [0.        , 1.        , 0.        ]])

يمكن بعد ذلك تطبيق نفس مثيل المحول على بعض بيانات الاختبار الجديدة
غير المرئية أثناء مكالمة التثبيت: سيتم تطبيق نفس عمليات التقييم والتحويل
للحفاظ على الاتساق مع التحويل الذي تم إجراؤه على بيانات التدريب::

  >>> X_test = np.array([[-3., -1.,  4.]])
  >>> X_test_minmax = min_max_scaler.transform(X_test)
  >>> X_test_minmax
  array([[-1.5       ,  0.        ,  1.66666667]])

من الممكن فحص سمات المقيّم لمعرفة الطبيعة الدقيقة
للتحويل الذي تم تعلمه على بيانات التدريب::

  >>> min_max_scaler.scale_
  array([0.5       , 0.5       , 0.33...])

  >>> min_max_scaler.min_
  array([0.        , 0.5       , 0.33...])

إذا تم إعطاء :class:`MinMaxScaler` نطاق ميزة صريح ``(min، max)`` فإن
الصيغة الكاملة هي::

    X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))

    X_scaled = X_std * (max - min) + min

يعمل :class:`MaxAbsScaler` بطريقة مشابهة جدًا، ولكنه يقيّم بحيث تقع بيانات التدريب ضمن النطاق ``[-1، 1]`` عن طريق القسمة على القيمة القصوى القصوى في كل ميزة. القصد منه هو للبيانات
التي تتمحور بالفعل حول الصفر أو البيانات المتناثرة.

فيما يلي كيفية استخدام بيانات اللعب من المثال السابق مع هذا المقيّم::

  >>> X_train = np.array([[ 1., -1.,  2.],
  ...                     [ 2.,  0.,  0.],
  ...                     [ 0.,  1., -1.]])
  ...
  >>> max_abs_scaler = preprocessing.MaxAbsScaler()
  >>> X_train_maxabs = max_abs_scaler.fit_transform(X_train)
  >>> X_train_maxabs
  array([[ 0.5, -1. ,  1. ],
         [ 1. ,  0. ,  0. ],
         [ 0. ,  1. , -0.5]])
  >>> X_test = np.array([[ -3., -1.,  4.]])
  >>> X_test_maxabs = max_abs_scaler.transform(X_test)
  >>> X_test_maxabs
  array([[-1.5, -1. ,  2. ]])
  >>> max_abs_scaler.scale_
  array([2.,  1.,  2.])


تقييم البيانات المتناثرة
-------------------

قد يؤدي تركز البيانات المتناثرة إلى تدمير بنية التبعثر في البيانات، وبالتالي نادرًا ما يكون إجراءً منطقيًا. ومع ذلك، قد يكون من المنطقي تقييم الإدخالات المتناثرة، خاصة إذا كانت الميزات على مقاييس مختلفة.

تم تصميم :class:`MaxAbsScaler` خصيصًا لتقييم
البيانات المتناثرة، وهي الطريقة الموصى بها للقيام بذلك.
ومع ذلك، يمكن لـ :class:`StandardScaler` قبول المصفوفات "scipy.sparse"
كإدخال، طالما يتم تمرير ``with_mean=False`` بشكل صريح
إلى المنشئ. وإلا، فسيتم إلقاء ``ValueError`` لأن التمركيز الصامت سيكسر التبعثر وقد يؤدي إلى تعطل التنفيذ عن طريق تخصيص كميات مفرطة من الذاكرة عن غير قصد. لا يمكن لـ :class:`RobustScaler` التلاؤم مع الإدخالات المتناثرة، ولكن يمكنك استخدام
طريقة "التحويل" على الإدخالات المتناثرة.

لاحظ أن المقاييس تقبل تنسيقات الصفوف المتناثرة والعمود المتناثر (راجع ``scipy.sparse.csr_matrix`` و
``scipy.sparse.csc_matrix``). سيتم **تحويل أي إدخال متناثر آخر إلى
تمثيل الصفوف المتناثرة**. لتجنب عمليات نسخ الذاكرة غير الضرورية، يوصى باختيار تمثيل CSR أو CSC أعلى.

أخيرًا، إذا كان من المتوقع أن تكون البيانات المركزة صغيرة بما يكفي، فإن التحويل الصريح للإدخال إلى مصفوفة باستخدام طريقة "toarray" للمصفوفات المتناثرة هو خيار آخر.


تقييم البيانات بالقيم الشاذة
--------------------------

إذا كانت بياناتك تحتوي على العديد من القيم الشاذة، فمن المحتمل ألا يعمل التقييم باستخدام المتوسط والانحراف المعياري للبيانات بشكل جيد. في هذه الحالات، يمكنك استخدام
:class:`RobustScaler` كبديل جاهز للاستخدام بدلاً من ذلك. فهو يستخدم
تقديرات أكثر متانة لمركز ونطاق بياناتك.


.. dropdown:: المراجع

  تتوفر مناقشة أخرى حول أهمية مركز البيانات وتقييمها في هذا الدليل: `هل يجب أن أطبّع/أوحّد/أعيد تصعيد البيانات؟
  <http://www.faqs.org/faqs/ai-faq/neural-nets/part2/section-16.html>`_

.. dropdown:: التقييم مقابل التبييض

  في بعض الأحيان، لا يكفي مركز الميزات وتقييمها بشكل مستقل، حيث يمكن أن يفترض نموذج أسفل البئر أيضًا بعض الافتراضات
حول الاستقلال الخطي للميزات.

  لمعالجة هذه المشكلة، يمكنك استخدام :class:`~sklearn.decomposition.PCA` مع
``whiten=True`` لإزالة الارتباط الخطي عبر الميزات بشكل أكبر.


.. _kernel_centering:

مركز مصفوفات النواة
-------------------------

إذا كان لديك مصفوفة نواة لنواة :math:`K` تقوم بحساب ناتج القسمة
في مساحة الميزة (محددة ضمنيًا) بواسطة دالة
:math:`\phi(\cdot)`، فيمكن لـ :class:`KernelCenterer` تحويل مصفوفة النواة
بحيث تحتوي على نواتج القسمة في مساحة الميزة المحددة بواسطة :math:`\phi`
تليها إزالة المتوسط في تلك المساحة. وبعبارة أخرى،
:class:`KernelCenterer` يحسب مصفوفة غرام المركزية المرتبطة بنواة إيجابية شبه محددة :math:`K`.

.. dropdown:: الصيغة الرياضية

  يمكننا إلقاء نظرة على الصيغة الرياضية الآن بعد أن حصلنا على الحدس. دع :math:`K` تكون مصفوفة نواة الشكل `(n_samples، n_samples)`
محسوب من :math:`X`، مصفوفة بيانات الشكل `(n_samples، n_features)`،
خلال الخطوة `fit`. يتم تعريف :math:`K` بواسطة

  .. math::
    K(X، X) = \phi(X) . \phi(X)^{T}

  :math:`\phi(X)` عبارة عن رسم خريطة لـ :math:`X` إلى فضاء هيلبرت. يتم تعريف النواة المركزية :math:`\tilde{K}` على النحو التالي:

  .. math::
    \tilde{K}(X، X) = \tilde{\phi}(X) . \tilde{\phi}(X)^{T}

  حيث :math:`\tilde{\phi}(X)` ينتج عن مركز :math:`\phi(X)` في
فضاء هيلبرت.

  وبالتالي، يمكن حساب :math:`\tilde{K}` عن طريق رسم خريطة لـ :math:`X` باستخدام
الدالة :math:`\phi(\cdot)` ومركز البيانات في هذا الفضاء الجديد. ومع ذلك،
غالبًا ما يتم استخدام النواة لأنها تسمح ببعض الحسابات الجبرية التي
تتجنب حساب هذا التخطيط بشكل صريح باستخدام :math:`\phi(\cdot)`. في الواقع، يمكن إجراء التركيز بشكل ضمني كما هو موضح في الملحق ب في [Scholkopf1998]_:

  .. math::
    \tilde{K} = K - 1_{\text{n}_{samples}} K - K 1_{\text{n}_{samples}} + 1_{\text{n}_{samples}} K 1_{\text{n}_{samples}}

  :math:`1_{\text{n}_{samples}}` عبارة عن مصفوفة من الشكل `(n_samples، n_samples)` حيث
تكون جميع الإدخالات مساوية لـ :math:`\frac{1}{\text{n}_{samples}}`. في
خطوة `التحويل`، تصبح النواة :math:`K_{test}(X، Y)` المحددة على النحو التالي:

  .. math::
    K_{test}(X، Y) = \phi(Y) . \phi(X)^{T}

  :math:`Y` هي مجموعة بيانات الاختبار الشكل `(n_samples_test، n_features)` وبالتالي
:math:`K_{test}` من الشكل `(n_samples_test، n_samples)`. في هذه الحالة،
يتم إجراء التركيز :math:`K_{test}` على النحو التالي:

  .. math::
    \tilde{K}_{test}(X، Y) = K_{test} - 1'_{\text{n}_{samples}} K - K_{test} 1_{\text{n}_{samples}} + 1'_{\text{n}_{samples}} K 1_{\text{n}_{samples}}

  :math:`1'_{\text{n}_{samples}}` عبارة عن مصفوفة الشكل
`(n_samples_test، n_samples)` حيث تكون جميع الإدخالات مساوية لـ
:math:`\frac{1}{\text{n}_{samples}}`.

  .. rubric:: المراجع

  .. [Scholkopf1998] B. Schölkopf، A. Smola، and K.R. Müller،
    `"Nonlinear component analysis as a kernel eigenvalue problem."
    <https://www.mlpack.org/papers/kpca.pdf>`_
    الحساب العصبي 10.5 (1998): 1299-1319.

.. _preprocessing_transformer:

التحويل غير الخطي
يوجد نوعان من التحولات المتاحة: تحويلات الكميات وتحويلات القوة. يعتمد كل من تحويلات الكميات وتحويلات القوة على التحولات الأحادية الاتجاه للخصائص، وبالتالي الحفاظ على ترتيب القيم على طول كل خاصية.

تضع تحويلات الكميات جميع الخصائص في نفس التوزيع المرغوب بناءً على الصيغة: G^{-1}(F(X)) حيث F هي دالة التوزيع التراكمي للخاصية وG^{-1} هي دالة الكمية <https://en.wikipedia.org/wiki/Quantile_function> للتوزيع المخرج المرغوب G. تستخدم هذه الصيغة الحقيقتين التاليتين: (1) إذا كانت X متغيرًا عشوائيًا له دالة توزيع تراكمية مستمرة F، فإن F(X) لها توزيع منتظم على [0،1]؛ (2) إذا كان U متغيرًا عشوائيًا بتوزيع منتظم على [0،1]، فإن G^{-1}(U) له توزيع G. من خلال إجراء تحويل مرتبي، يقوم تحويل الكمية بتنعيم التوزيعات غير المعتادة والتأثر بقيم الشواذ بدرجة أقل من طرق التدرج. ومع ذلك، فإنه يشوه الارتباطات والمسافات داخل الخصائص وفيما بينها.

تحويلات القوة هي عائلة من التحولات المعلمية التي تهدف إلى رسم خريطة للبيانات من أي توزيع إلى أقرب توزيع غاوسي ممكن.

رسم الخرائط إلى توزيع منتظم
--------------------------

توفر QuantileTransformer تحويلًا غير معلمي لرسم خريطة للبيانات إلى توزيع منتظم مع قيم بين 0 و1::

  >>> from sklearn.datasets import load_iris
  >>> from sklearn.model_selection import train_test_split
  >>> X, y = load_iris(return_X_y=True)
  >>> X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
  >>> quantile_transformer = preprocessing.QuantileTransformer(random_state=0)
  >>> X_train_trans = quantile_transformer.fit_transform(X_train)
  >>> X_test_trans = quantile_transformer.transform(X_test)
  >>> np.percentile(X_train[:, 0], [0, 25, 50, 75, 100]) # doctest: +SKIP
  array([ 4.3,  5.1,  5.8,  6.5,  7.9])

تتوافق هذه الميزة مع طول الكأس بالسم. بمجرد تطبيق تحويل الكمية، تقترب هذه المعالم بشكل وثيق من النسب المئوية المحددة مسبقًا::

  >>> np.percentile(X_train_trans[:, 0], [0, 25, 50, 75, 100])
  ... # doctest: +SKIP
  array([ 0.00... ,  0.24...,  0.49...,  0.73...,  0.99... ])

يمكن التأكد من ذلك على مجموعة اختبار مستقلة مع ملاحظات مماثلة::

  >>> np.percentile(X_test[:, 0], [0, 25, 50, 75, 100])
  ... # doctest: +SKIP
  array([ 4.4  ,  5.125,  5.75 ,  6.175,  7.3  ])
  >>> np.percentile(X_test_trans[:, 0], [0, 25, 50, 75, 100])
  ... # doctest: +SKIP
  array([ 0.01...,  0.25...,  0.46...,  0.60... ,  0.94...])

رسم الخرائط إلى توزيع غاوسي
--------------------------

في العديد من سيناريوهات النمذجة، يكون التوزيع الطبيعي للخصائص في مجموعة بيانات أمرًا مرغوبًا. تحويلات القوة هي عائلة من التحولات الأحادية الاتجاه المعلمية التي تهدف إلى رسم خريطة للبيانات من أي توزيع إلى أقرب توزيع غاوسي ممكن من أجل تثبيت التباين وتقليل اللاتناظر.

يوفر PowerTransformer حاليًا تحويلين من هذا القبيل للقوة، وهما تحويل ييو-جونسون وتحويل بوكس-كوكس.

.. dropdown:: تحويل ييو-جونسون

  .. math::
      x_i^{(\lambda)} =
      \begin{cases}
      [(x_i + 1)^\lambda - 1] / \lambda & \text{if } \lambda \neq 0, x_i \geq 0, \\[8pt]
      \ln{(x_i + 1)} & \text{if } \lambda = 0, x_i \geq 0 \\[8pt]
      -[(-x_i + 1)^{2 - \lambda} - 1] / (2 - \lambda) & \text{if } \lambda \neq 2, x_i < 0, \\[8pt]
      - \ln (- x_i + 1) & \text{if } \lambda = 2, x_i < 0
      \end{cases}

.. dropdown:: تحويل بوكس-كوكس

  .. math::
      x_i^{(\lambda)} =
      \begin{cases}
      \dfrac{x_i^\lambda - 1}{\lambda} & \text{if } \lambda \neq 0, \\[8pt]
      \ln{(x_i)} & \text{if } \lambda = 0,
      \end{cases}

  يمكن تطبيق Box-Cox فقط على البيانات الموجبة الصارمة. في كلتا الطريقتين، يتم تحديد التحول بواسطة المعلمة λ، والتي يتم تحديدها من خلال تقدير الإمكان الأقصى. فيما يلي مثال على استخدام Box-Cox لرسم خريطة لعينات تم رسمها من توزيع لوجاريتمي إلى توزيع طبيعي::

    >>> pt = preprocessing.PowerTransformer(method='box-cox', standardize=False)
    >>> X_lognormal = np.random.RandomState(616).lognormal(size=(3, 3))
    >>> X_lognormal
    array([[1.28..., 1.18..., 0.84...],
          [0.94..., 1.60..., 0.38...],
          [1.35..., 0.21..., 1.09...]])
    >>> pt.fit_transform(X_lognormal)
    array([[ 0.49...,  0.17..., -0.15...],
          [-0.05...,  0.58..., -0.57...],
          [ 0.69..., -0.84...,  0.10...]])

  في حين أن المثال أعلاه يحدد خيار "standardize" إلى "False"، سيقوم PowerTransformer بتطبيع التباين المتوسط والصفر على الإخراج المحول بشكل افتراضي.


فيما يلي أمثلة على Box-Cox وYeo-Johnson المطبقة على توزيعات احتمالية مختلفة. لاحظ أنه عند تطبيقها على توزيعات معينة، تحقق تحويلات القوة نتائج شبيهة بالتوزيع الغاوسي جدًا، ولكنها غير فعالة مع توزيعات أخرى. وهذا يسلط الضوء على أهمية تصور البيانات قبل وبعد التحول.

.. figure:: ../auto_examples/preprocessing/images/sphx_glr_plot_map_data_to_normal_001.png
   :target: ../auto_examples/preprocessing/plot_map_data_to_normal.html
   :align: center
   :scale: 100

من الممكن أيضًا رسم خريطة للبيانات إلى توزيع طبيعي باستخدام QuantileTransformer عن طريق تعيين "output_distribution='normal'". باستخدام المثال السابق مع مجموعة بيانات Iris::

  >>> quantile_transformer = preprocessing.QuantileTransformer(
  ...     output_distribution='normal', random_state=0)
  >>> X_trans = quantile_transformer.fit_transform(X)
  >>> quantile_transformer.quantiles_
  array([[4.3, 2. , 1. , 0.1],
         [4.4, 2.2, 1.1, 0.1],
         [4.4, 2.2, 1.2, 0.1],
         ...,
         [7.7, 4.1, 6.7, 2.5],
         [7.7, 4.2, 6.7, 2.5],
         [7.9, 4.4, 6.9, 2.5]])

وهكذا، يصبح الوسيط للإدخال متوسط الإخراج، الذي يتم مركزه عند 0. يتم قص التوزيع الطبيعي بحيث لا تصبح القيمة الدنيا والقصوى للإدخال - والتي تتوافق مع الكميات 1e-7 و1 - 1e-7 على التوالي - لانهائية في ظل التحول.

.. _preprocessing_normalization:

التطبيع
=============

**التطبيع** هي عملية **تحجيم العينات الفردية بحيث يكون لها معيار الوحدة**. يمكن أن تكون هذه العملية مفيدة إذا كنت تخطط لاستخدام نموذج رباعي مثل المنتج النقطي أو أي نواة أخرى لقياس تشابه أي زوج من العينات.

يعد هذا الافتراض هو الأساس لنموذج مساحة المتجه <https://en.wikipedia.org/wiki/Vector_Space_Model> المستخدم غالبًا في سياقات تصنيف النصوص وتجميعها.

توفر الدالة normalize طريقة سريعة وسهلة لأداء هذه العملية على مجموعة بيانات واحدة تشبه المصفوفة، باستخدام معايير "l1" أو "l2" أو "max"::

  >>> X = [[ 1., -1.,  2.],
  ...      [ 2.,  0.,  0.],
  ...      [ 0.,  1., -1.]]
  >>> X_normalized = preprocessing.normalize(X, norm='l2')

  >>> X_normalized
  array([[ 0.40..., -0.40...,  0.81...],
         [ 1.  ...,  0.  ...,  0.  ...],
         [ 0.  ...,  0.70..., -0.70...]])

يوفر وحدة "preprocessing" أيضًا فئة فائدة Normalizer التي تنفذ نفس العملية باستخدام واجهة برمجة تطبيقات المحول (على الرغم من أن طريقة "fit" عديمة الفائدة في هذه الحالة: تكون الفئة عديمة الحالة نظرًا لأن هذه العملية تعامل العينات بشكل مستقل).

لذلك، فإن هذه الفئة مناسبة للاستخدام في الخطوات الأولى من خط أنابيب: class: ~sklearn.pipeline.Pipeline::

  >>> normalizer = preprocessing.Normalizer().fit(X)  # fit does nothing
  >>> normalizer
  Normalizer()


يمكن بعد ذلك استخدام مثيل المحول على متجهات العينة كما هو الحال مع أي محول::

  >>> normalizer.transform(X)
  array([[ 0.40..., -0.40...,  0.81...],
         [ 1.  ...,  0.  ...,  0.  ...],
         [ 0.  ...,  0.70..., -0.70...]])

  >>> normalizer.transform([[-1.,  1., 0.]])
  array([[-0.70...,  0.70...,  0.  ...]])


ملاحظة: التطبيع L2 معروف أيضًا باسم المعالجة المسبقة للإشارة المكانية.

.. dropdown:: الإدخال المتناثر

  يقبل normalize وNormalizer **كل من المصفوفات الكثيفة المتشابهة والمصفوفات المتناثرة من scipy.sparse كإدخال**.

  بالنسبة للإدخال المتناثر، يتم **تحويل البيانات إلى تمثيل الصفوف المتناثرة المضغوطة** (راجع scipy.sparse.csr_matrix) قبل إدخالها إلى روتين Cython فعال. لتجنب عمليات نسخ الذاكرة غير الضرورية، يُنصح باختيار تمثيل CSR أعلى.

.. _preprocessing_categorical_features:

ترميز الميزات الفئوية
غالباً ما تكون الخصائص غير معطاة على شكل قيم مستمرة ولكنها تصنيفية. على سبيل المثال، يمكن أن تكون لشخص خصائص مثل ["ذكر"، "أنثى"]، أو ["من أوروبا"، "من الولايات المتحدة"، "من آسيا"]، أو ["يستخدم فايرفوكس"، "يستخدم كروم"، "يستخدم سفاري"، "يستخدم إنترنت إكسبلورر"]. يمكن ترميز مثل هذه الخصائص بكفاءة على شكل أعداد صحيحة، على سبيل المثال، يمكن التعبير عن ["ذكر"، "من الولايات المتحدة"، "يستخدم إنترنت إكسبلورر"] على شكل [0, 1, 3] في حين يمكن التعبير عن ["أنثى"، "من آسيا"، "يستخدم كروم"] على شكل [1, 2, 1].

لتحويل الخصائص التصنيفية إلى رموز أعداد صحيحة، يمكننا استخدام التصنيف OrdinalEncoder. يحول هذا التقدير كل خاصية تصنيفية إلى خاصية جديدة واحدة من الأعداد الصحيحة (من 0 إلى n_categories - 1).

على سبيل المثال:

>>> enc = preprocessing.OrdinalEncoder()
>>> X = [['male', 'from US', 'uses Safari'], ['female', 'from Europe', 'uses Firefox']]
>>> enc.fit(X)
OrdinalEncoder()
>>> enc.transform([['female', 'from US', 'uses Safari']])
array([[0., 1., 1.]])

ومع ذلك، لا يمكن استخدام تمثيل الأعداد الصحيحة هذا مباشرة مع جميع تقديرات scikit-learn، لأنها تتوقع إدخال قيم مستمرة، وستفسر الفئات على أنها مرتبة، وهو ما لا يكون مرغوباً في كثير من الأحيان (أي أن مجموعة المتصفحات تم ترتيبها بشكل تعسفي).

بشكل افتراضي، سوف يقوم التصنيف OrdinalEncoder أيضًا بنقل القيم المفقودة التي يتم الإشارة إليها بـ np.nan.

على سبيل المثال:

>>> enc = preprocessing.OrdinalEncoder()
>>> X = [['male'], ['female'], [np.nan], ['female']]
>>> enc.fit_transform(X)
array([[ 1.],
       [ 0.],
       [nan],
       [ 0.]])

يوفر التصنيف OrdinalEncoder معامل encoded_missing_value لترميز القيم المفقودة دون الحاجة إلى إنشاء خط أنابيب واستخدام التصنيف sklearn.impute.SimpleImputer.

على سبيل المثال:

>>> enc = preprocessing.OrdinalEncoder(encoded_missing_value=-1)
>>> X = [['male'], ['female'], [np.nan], ['female']]
>>> enc.fit_transform(X)
array([[ 1.],
       [ 0.],
       [-1.],
       [ 0.]])

تعادل المعالجة المذكورة أعلاه خط الأنابيب التالي:

>>> from sklearn.pipeline import Pipeline
>>> from sklearn.impute import SimpleImputer
>>> enc = Pipeline(steps=[
...     ("encoder", preprocessing.OrdinalEncoder()),
...     ("imputer", SimpleImputer(strategy="constant", fill_value=-1)),
... ])
>>> enc.fit_transform(X)
array([[ 1.],
       [ 0.],
       [-1.],
       [ 0.]])

هناك إمكانية أخرى لتحويل الخصائص التصنيفية إلى خصائص يمكن استخدامها مع تقديرات scikit-learn وهي استخدام ترميز one-of-K، المعروف أيضًا باسم one-hot أو dummy encoding.

يمكن الحصول على هذا النوع من الترميز باستخدام التصنيف OneHotEncoder، والذي يحول كل خاصية تصنيفية تحتوي على n_categories من القيم المحتملة إلى n_categories من الخصائص الثنائية، حيث تكون إحدى هذه الخصائص تساوي 1، وكل الخصائص الأخرى تساوي 0.

استمرارًا للمثال المذكور أعلاه:

>>> enc = preprocessing.OneHotEncoder()
>>> X = [['male', 'from US', 'uses Safari'], ['female', 'from Europe', 'uses Firefox']]
>>> enc.fit(X)
OneHotEncoder()
>>> enc.transform([['female', 'from US', 'uses Safari'],
...                ['male', 'from Europe', 'uses Safari']]).toarray()
array([[1., 0., 0., 1., 0., 1.],
       [0., 1., 1., 0., 0., 1.]])

بشكل افتراضي، يتم استنتاج القيم التي يمكن أن تأخذها كل خاصية تلقائيًا من مجموعة البيانات ويمكن العثور عليها في خاصية categories_.

على سبيل المثال:

>>> enc.categories_
[array(['female', 'male'], dtype=object), array(['from Europe', 'from US'], dtype=object), array(['uses Firefox', 'uses Safari'], dtype=object)]

من الممكن تحديد هذا بشكل صريح باستخدام معامل categories. هناك نوعان اجتماعيان، وأربع قارات محتملة، وأربعة متصفحات ويب في مجموعة البيانات الخاصة بنا:

>>> genders = ['female', 'male']
>>> locations = ['from Africa', 'from Asia', 'from Europe', 'from US']
>>> browsers = ['uses Chrome', 'uses Firefox', 'uses IE', 'uses Safari']
>>> enc = preprocessing.OneHotEncoder(categories=[genders, locations, browsers])
>>> # لاحظ أنه توجد قيم تصنيفية مفقودة للخاصية الثانية والثالثة
>>> X = [['male', 'from US', 'uses Safari'], ['female', 'from Europe', 'uses Firefox']]
>>> enc.fit(X)
OneHotEncoder(categories=[['female', 'male'],
                          ['from Africa', 'from Asia', 'from Europe',
                           'from US'],
                          ['uses Chrome', 'uses Firefox', 'uses IE',
                           'uses Safari']])
>>> enc.transform([['female', 'from Asia', 'uses Chrome']]).toarray()
array([[1., 0., 0., 1., 0., 0., 1., 0., 0., 0.]])

إذا كان هناك احتمال أن تحتوي بيانات التدريب على خصائص تصنيفية مفقودة، فقد يكون من الأفضل تحديد handle_unknown='infrequent_if_exist' بدلاً من تعيين categories يدويًا كما هو موضح أعلاه. عندما يتم تحديد handle_unknown='infrequent_if_exist' ويتم مواجهة فئات غير معروفة أثناء التحويل، فلن يتم رفع أي خطأ ولكن سيتم اعتبار الأعمدة المشفرة one-hot الناتجة عن هذه الخاصية كلها أصفار أو فئة نادرة إذا تم تمكينها. (يتم دعم handle_unknown='infrequent_if_exist' فقط لترميز one-hot).

على سبيل المثال:

>>> enc = preprocessing.OneHotEncoder(handle_unknown='infrequent_if_exist')
>>> X = [['male', 'from US', 'uses Safari'], ['female', 'from Europe', 'uses Firefox']]
>>> enc.fit(X)
OneHotEncoder(handle_unknown='infrequent_if_exist')
>>> enc.transform([['female', 'from Asia', 'uses Chrome']]).toarray()
array([[1., 0., 0., 0., 0., 0.]])

من الممكن أيضًا ترميز كل عمود إلى n_categories - 1 من الأعمدة بدلاً من n_categories من الأعمدة باستخدام معامل drop. يسمح هذا المعامل للمستخدم بتحديد فئة لكل خاصية ليتم إسقاطها. وهذا مفيد لتجنب التلازم في مصفوفة الإدخال في بعض التصنيفات. تعد هذه الوظيفة مفيدة، على سبيل المثال، عند استخدام الانحدار غير المنتظم (LinearRegression)، حيث قد يتسبب التلازم في عدم إمكانية عكس مصفوفة القيم الذاتية.

على سبيل المثال:

>>> X = [['male', 'from US', 'uses Safari'],
...      ['female', 'from Europe', 'uses Firefox']]
>>> drop_enc = preprocessing.OneHotEncoder(drop='first').fit(X)
>>> drop_enc.categories_
[array(['female', 'male'], dtype=object), array(['from Europe', 'from US'], dtype=object),
 array(['uses Firefox', 'uses Safari'], dtype=object)]
>>> drop_enc.transform(X).toarray()
array([[1., 1., 1.],
       [0., 0., 0.]])

قد يرغب المرء في إسقاط أحد العمودين فقط للخصائص التي تحتوي على فئتين. في هذه الحالة، يمكنك تعيين معامل drop='if_binary'.

على سبيل المثال:

>>> X = [['male', 'US', 'Safari'],
...      ['female', 'Europe', 'Firefox'],
...      ['female', 'Asia', 'Chrome']]
>>> drop_enc = preprocessing.OneHotEncoder(drop='if_binary').fit(X)
>>> drop_enc.categories_
[array(['female', 'male'], dtype=object), array(['Asia', 'Europe', 'US'], dtype=object),
 array(['Chrome', 'Firefox', 'Safari'], dtype=object)]
>>> drop_enc.transform(X).toarray()
array([[1., 0., 0., 1., 0., 0., 1.],
       [0., 0., 1., 0., 0., 1., 0.],
       [0., 1., 0., 0., 1., 0., 0.]])

في مصفوفة X المحولة، العمود الأول هو ترميز الخاصية بالفئات "ذكر"/"أنثى"، في حين أن الأعمدة الستة المتبقية هي ترميز الخاصيتين اللتين تحتوي كل منهما على 3 فئات.

عندما يكون handle_unknown='ignore' و drop ليس None، يتم ترميز الفئات غير المعروفة على أنها كلها أصفار:

>>> drop_enc = preprocessing.OneHotEncoder(drop='first',
...                                        handle_unknown='ignore').fit(X)
>>> X_test = [['unknown', 'America', 'IE']]
>>> drop_enc.transform(X_test).toarray()
array([[0., 0., 0., 0., 0.]])

جميع الفئات في X_test غير معروفة أثناء التحويل وسيتم تعيينها إلى كلها أصفار. وهذا يعني أن الفئات غير المعروفة سيكون لها نفس الترميز مثل الفئة التي تم إسقاطها. سيقوم الأسلوب OneHotEncoder.inverse_transform بتعيين كل الأصفار إلى الفئة التي تم إسقاطها إذا تم إسقاط فئة، وإلى None إذا لم يتم إسقاط فئة:

>>> drop_enc = preprocessing.OneHotEncoder(drop='if_binary', sparse_output=False,
...                                        handle_unknown='ignore').fit(X)
>>> X_test = [['unknown', 'America', 'IE']]
>>> X_trans = drop_enc.transform(X_test)
>>> X_trans
array([[0., 0., 0., 0., 0., 0., 0.]])
>>> drop_enc.inverse_transform(X_trans)
array([['female', None, None]], dtype=object)

يدعم التصنيف OneHotEncoder الخصائص التصنيفية بالقيم المفقودة من خلال اعتبار القيم المفقودة فئة إضافية:

>>> X = [['male', 'Safari'],
...      ['female', None],
...      [np.nan, 'Firefox']]
>>> enc = preprocessing.OneHotEncoder(handle_unknown='error').fit(X)
>>> enc.categories_
[array(['female', 'male', nan], dtype=object),
 array(['Firefox', 'Safari', None], dtype=object)]
>>> enc.transform(X).toarray()
array([[0., 1., 0., 0., 1., 0.],
       [1., 0., 0., 0., 0., 1.],
       [0., 0., 1., 1., 0., 0.]])

إذا كانت الخاصية تحتوي على كل من np.nan و None، فسيتم اعتبارهما فئتين منفصلتين:

>>> X = [['Safari'], [None], [np.nan], ['Firefox']]
>>> enc = preprocessing.OneHotEncoder(handle_unknown='error').fit(X)
>>> enc.categories_
[array(['Firefox', 'Safari', None, nan], dtype=object)]
>>> enc.transform(X).toarray()
array([[0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.],
       [1., 0., 0., 0.]])

راجع قسم dict_feature_extraction للاطلاع على الخصائص التصنيفية الممثلة على شكل قاموس، وليس على شكل قيم فردية.

الفئات النادرة
يدعم كل من :class:`OneHotEncoder` و :class:`OrdinalEncoder` تجميع الفئات غير المتكررة في مخرج واحد لكل خاصية. والمعياران اللذان يمكنان من جمع الفئات غير المتكررة هما `min_frequency` و `max_categories`.

1. `min_frequency` إما أن يكون عددًا صحيحًا أكبر من أو يساوي 1، أو عددًا عشريًا في الفترة `(0.0, 1.0)`. إذا كان `min_frequency` عددًا صحيحًا، فسيتم اعتبار الفئات التي لها عدد حالات أقل من `min_frequency` غير متكررة. إذا كان `min_frequency` عددًا عشريًا، فسيتم اعتبار الفئات التي لها عدد حالات أقل من هذا الجزء من العدد الإجمالي للعينات غير متكررة. والقيمة الافتراضية هي 1، مما يعني أن كل فئة يتم ترميزها بشكل منفصل.

2. `max_categories` إما أن تكون `None` أو أي عدد صحيح أكبر من 1. يحدد هذا المعيار حدًا أعلى لعدد الميزات الإخراجية لكل ميزة إدخال. يشمل `max_categories` الميزة التي تجمع الفئات غير المتكررة.

في المثال التالي باستخدام :class:`OrdinalEncoder`، تعتبر الفئتان `'dog'` و `'snake'` غير متكررتين::

   >>> X = np.array([['dog'] * 5 + ['cat'] * 20 + ['rabbit'] * 10 +
   ...               ['snake'] * 3], dtype=object).T
   >>> enc = preprocessing.OrdinalEncoder(min_frequency=6).fit(X)
   >>> enc.infrequent_categories_
   [array(['dog', 'snake'], dtype=object)]
   >>> enc.transform(np.array([['dog'], ['cat'], ['rabbit'], ['snake']]))
   array([[2.],
          [0.],
          [1.],
          [2.]])

لا يأخذ `max_categories` في :class:`OrdinalEncoder` في الاعتبار الفئات المفقودة أو غير المعروفة. يؤدي تعيين `unknown_value` أو `encoded_missing_value` إلى عدد صحيح إلى زيادة عدد الرموز العددية الفريدة بواحد لكل منهما. يمكن أن يؤدي ذلك إلى ما يصل إلى `max_categories + 2` رموز عددية. في المثال التالي، تعتبر "a" و "d" غير متكررتين ويتم تجميعهما معًا في فئة واحدة، و"b" و "c" هما فئتان منفصلتان، ويتم ترميز القيم غير المعروفة على أنها 3 والقيم المفقودة على أنها 4.

  >>> X_train = np.array(
  ...     [["a"] * 5 + ["b"] * 20 + ["c"] * 10 + ["d"] * 3 + [np.nan]],
  ...     dtype=object).T
  >>> enc = preprocessing.OrdinalEncoder(
  ...     handle_unknown="use_encoded_value", unknown_value=3,
  ...     max_categories=3, encoded_missing_value=4)
  >>> _ = enc.fit(X_train)
  >>> X_test = np.array([["a"], ["b"], ["c"], ["d"], ["e"], [np.nan]], dtype=object)
  >>> enc.transform(X_test)
  array([[2.],
         [0.],
         [1.],
         [2.],
         [3.],
         [4.]])

وبالمثل، يمكن تكوين :class:`OneHotEncoder` ليقوم بتجميع الفئات غير المتكررة::

   >>> enc = preprocessing.OneHotEncoder(min_frequency=6, sparse_output=False).fit(X)
   >>> enc.infrequent_categories_
   [array(['dog', 'snake'], dtype=object)]
   >>> enc.transform(np.array([['dog'], ['cat'], ['rabbit'], ['snake']]))
   array([[0., 0., 1.],
          [1., 0., 0.],
          [0., 1., 0.],
          [0., 0., 1.]])

عن طريق تعيين handle_unknown إلى `'infrequent_if_exist'`، سيتم اعتبار الفئات غير المعروفة غير متكررة::

   >>> enc = preprocessing.OneHotEncoder(
   ...    handle_unknown='infrequent_if_exist', sparse_output=False, min_frequency=6)
   >>> enc = enc.fit(X)
   >>> enc.transform(np.array([['dragon']]))
   array([[0., 0., 1.]])

يستخدم :meth:`OneHotEncoder.get_feature_names_out` كلمة 'infrequent' كاسم للفئة غير المتكررة::

   >>> enc.get_feature_names_out()
   array(['x0_cat', 'x0_rabbit', 'x0_infrequent_sklearn'], dtype=object)

عندما يتم تعيين `'handle_unknown'` إلى `'infrequent_if_exist'` وتتم مواجهة فئة غير معروفة في التحول:

1. إذا لم يتم تكوين دعم الفئة غير المتكررة أو لم تكن هناك فئة غير متكررة أثناء التدريب، فستكون الأعمدة المشفرة بنظام one-hot الناتجة عن هذه الميزة جميعها أصفار. في التحول العكسي، سيتم تمثيل الفئة غير المعروفة بـ `None`.

2. إذا كانت هناك فئة غير متكررة أثناء التدريب، فسيتم اعتبار الفئة غير المعروفة غير متكررة. في التحول العكسي، سيتم استخدام 'infrequent_sklearn' لتمثيل الفئة غير المتكررة.

يمكن أيضًا تكوين الفئات غير المتكررة باستخدام `max_categories`. في المثال التالي، نقوم بتعيين `max_categories=2` للحد من عدد الميزات في الإخراج. سيؤدي هذا إلى اعتبار جميع الفئات باستثناء فئة `'cat'` على أنها غير متكررة، مما يؤدي إلى ميزتين، واحدة لـ `'cat'` والأخرى للفئات غير المتكررة - والتي هي جميع الفئات الأخرى::

   >>> enc = preprocessing.OneHotEncoder(max_categories=2, sparse_output=False)
   >>> enc = enc.fit(X)
   >>> enc.transform([['dog'], ['cat'], ['rabbit'], ['snake']])
   array([[0., 1.],
          [1., 0.],
          [0., 1.],
          [0., 1.]])

إذا كانت لكل من `max_categories` و `min_frequency` قيم غير افتراضية، فسيتم اختيار الفئات بناءً على `min_frequency` أولاً ويتم الاحتفاظ بـ `max_categories` من الفئات. في المثال التالي، يعتبر `min_frequency=4` أن `snake` فقط غير متكرر، ولكن `max_categories=3`، يجبر `dog` أيضًا على أن يكون غير متكرر::

   >>> enc = preprocessing.OneHotEncoder(min_frequency=4, max_categories=3, sparse_output=False)
   >>> enc = enc.fit(X)
   >>> enc.transform([['dog'], ['cat'], ['rabbit'], ['snake']])
   array([[0., 0., 1.],
          [1., 0., 0.],
          [0., 1., 0.],
          [0., 0., 1.]])

إذا كانت هناك فئات غير متكررة لها نفس عدد الحالات عند حد `max_categories`، فسيتم أخذ أول `max_categories` بناءً على الترتيب المعجمي. في المثال التالي، تحتوي "b" و "c" و "d" على نفس عدد الحالات، ومع `max_categories=2`، تعتبر "b" و "c" غير متكررتين لأنهما لهما ترتيب معجمي أعلى.

   >>> X = np.asarray([["a"] * 20 + ["b"] * 10 + ["c"] * 10 + ["d"] * 10], dtype=object).T
   >>> enc = preprocessing.OneHotEncoder(max_categories=3).fit(X)
   >>> enc.infrequent_categories_
   [array(['b', 'c'], dtype=object)]

.. _target_encoder:

مشفّر الهدف
--------------

.. currentmodule:: sklearn.preprocessing

يستخدم :class:`TargetEncoder` متوسط الهدف المشروط على الميزة الفئوية لتشفير الفئات غير المرتبة، أي الفئات الاسمية [PAR]_ [MIC]_. يعتبر نظام الترميز هذا مفيدًا مع الميزات الفئوية ذات التكرار العالي، حيث يؤدي الترميز one-hot إلى تضخيم مساحة الميزة، مما يجعلها أكثر تكلفة لنموذج المصب لمعالجتها. ومن الأمثلة الكلاسيكية على الفئات ذات التكرار العالي الفئات المستندة إلى الموقع مثل الرمز البريدي أو المنطقة.

.. dropdown:: أهداف التصنيف الثنائي

  بالنسبة لهدف التصنيف الثنائي، يكون الترميز الهدف على النحو التالي:

  .. math::
      S_i = \lambda_i\frac{n_{iY}}{n_i} + (1 - \lambda_i)\frac{n_Y}{n}

  حيث :math:`S_i` هو الترميز للفئة :math:`i`، :math:`n_{iY}` هو
  عدد الملاحظات مع :math:`Y=1` والفئة :math:`i`، :math:`n_i` هو
  عدد الملاحظات مع الفئة :math:`i`، :math:`n_Y` هو
  عدد الملاحظات مع :math:`Y=1`، :math:`n` هو
  عدد الملاحظات، و:math:`\lambda_i` هو عامل انكماش للفئة :math:`i`. يتم إعطاء عامل الانكماش على النحو التالي:

  .. math::
      \lambda_i = \frac{n_i}{m + n_i}

  حيث :math:`m` هو عامل التمهيد، والذي يتحكم فيه معلمة `smooth`
  في :class:`TargetEncoder`. ستعطي عوامل التمهيد الكبيرة وزنًا أكبر للمتوسط العالمي. عندما يكون `smooth="auto"`، يتم حساب عامل التمهيد كتقدير Bayes إحصائي: :math:`m=\sigma_i^2/\tau^2`، حيث
  :math:`\sigma_i^2` هو تباين `y` مع الفئة :math:`i` و
  :math:`\tau^2` هو التباين العالمي لـ `y`.

.. dropdown:: أهداف التصنيف متعدد الفئات

  بالنسبة لأهداف التصنيف متعدد الفئات، فإن الصيغة مماثلة للتصنيف الثنائي:

  .. math::
      S_{ij} = \lambda_i\frac{n_{iY_j}}{n_i} + (1 - \lambda_i)\frac{n_{Y_j}}{n}

  حيث :math:`S_{ij}` هو الترميز للفئة :math:`i` والصنف :math:`j`،
  :math:`n_{iY_j}` هو عدد الملاحظات مع :math:`Y=j` والفئة
  :math:`i`، :math:`n_i` هو عدد الملاحظات مع الفئة :math:`i`،
  :math:`n_{Y_j}` هو عدد الملاحظات مع :math:`Y=j`، :math:`n` هو
  عدد الملاحظات، و:math:`\lambda_i` هو عامل انكماش للفئة :math:`i`.

.. dropdown:: الأهداف المستمرة

  بالنسبة للأهداف المستمرة، فإن الصيغة مماثلة للتصنيف الثنائي:

  .. math::
      S_i = \lambda_i\frac{\sum_{k\in L_i}Y_k}{n_i} + (1 - \lambda_i)\frac{\sum_{k=1}^{n}Y_k}{n}

  حيث :math:`L_i` هي مجموعة الملاحظات مع الفئة :math:`i` و
  :math:`n_i` هو عدد الملاحظات مع الفئة :math:`i`.


يعتمد :meth:`~TargetEncoder.fit_transform` داخليًا على مخطط :term:`cross fitting`
لمنع تسرب معلومات الهدف إلى تمثيل وقت التدريب، خاصة بالنسبة للمتغيرات الفئوية عالية التكرار غير المعلوماتية، والمساعدة في منع النموذج المصب من الإفراط في ملاءمة الارتباطات الزائفة. لاحظ أنه نتيجة لذلك، فإن `fit(X, y).transform(X)` لا يساوي
`fit_transform(X, y)`. في :meth:`~TargetEncoder.fit_transform`، يتم تقسيم بيانات التدريب إلى *k* طيات (يحددها معلمة `cv`) ويتم ترميز كل طية باستخدام الترميزات التي تم تعلمها باستخدام الطيات الأخرى *k-1*. يوضح الرسم البياني التالي مخطط :term:`cross fitting` في
:meth:`~TargetEncoder.fit_transform` مع `cv=5` الافتراضي:

.. image:: ../images/target_encoder_cross_validation.svg
   :width: 600
   :align: center

يتعلم :meth:`~TargetEncoder.fit_transform` أيضًا ترميز "البيانات الكاملة" باستخدام
مجموعة التدريب بأكملها. لا يتم استخدام هذا أبدًا في
:meth:`~TargetEncoder.fit_transform` ولكنه يتم حفظه في السمة `encodings_`،
للاستخدام عند استدعاء :meth:`~TargetEncoder.transform`. لاحظ أن الترميزات التي تم تعلمها لكل طية أثناء مخطط :term:`cross fitting` لا يتم حفظها في سمة.

لا تستخدم طريقة :meth:`~TargetEncoder.fit` أي مخططات :term:`cross fitting` ويتعلم ترميزًا واحدًا على مجموعة التدريب بأكملها، والذي يتم استخدامه لترميز الفئات في :meth:`~TargetEncoder.transform`.
هذا الترميز هو نفسه ترميز "البيانات الكاملة" الذي تم تعلمه في :meth:`~TargetEncoder.fit_transform`.

.. note::
  يعتبر :class:`TargetEncoder` القيم المفقودة، مثل `np.nan` أو `None`،
  كفئة أخرى ويقوم بترميزها مثل أي فئة أخرى. يتم ترميز الفئات
  التي لم يتم رؤيتها أثناء `fit` بمتوسط الهدف، أي
  `target_mean_`.

.. rubric:: أمثلة

* :ref:`sphx_glr_auto_examples_preprocessing_plot_target_encoder.py`
* :ref:`sphx_glr_auto_examples_preprocessing_plot_target_encoder_cross_val.py`

.. rubric:: مراجع

.. [MIC] :doi:`Micci-Barreca, Daniele. "A preprocessing scheme for high-cardinality
    categorical attributes in classification and prediction problems"
    SIGKDD Explor. Newsl. 3, 1 (July 2001), 27-32. <10.1145/507533.507538>`

.. [PAR] :doi:`Pargent, F., Pfisterer, F., Thomas, J. et al. "Regularized target
    encoding outperforms traditional methods in supervised machine learning with
    high cardinality features" Comput Stat 37, 2671-2692 (2022)
    <10.1007/s00180-022-01207-6>`

.. _preprocessing_discretization:

التقسيم
التجزئة (المعروفة أيضًا باسم التكميم أو التصنيف) هي طريقة لتقسيم الخصائص المستمرة إلى قيم منفصلة. قد تستفيد بعض مجموعات البيانات ذات الخصائص المستمرة من التجزئة، لأن التجزئة يمكن أن تحول مجموعة البيانات ذات السمات المستمرة إلى مجموعة بيانات ذات سمات اسمية فقط.

يمكن أن تجعل الميزات المنفصلة المشفرة بنظام one-hot النموذج أكثر تعبيرًا، مع الحفاظ على إمكانية تفسيره. على سبيل المثال، يمكن أن يؤدي المعالجة المسبقة باستخدام أداة تجزئة إلى تقديم عدم خطية إلى النماذج الخطية. للحصول على إمكانيات أكثر تقدمًا، خاصة تلك الملساء، راجع: ref: generating_polynomial_features أدناه.

تجزئة ك-بينز
---------------------

يقسم: class: KBinsDiscretizer الميزات إلى "ك" حاويات::

  >>> X = np.array([[-3، 5، 15]،
  ...               [0، 6، 14]،
  ...               [6، 3، 11]])
  >>> est = preprocessing.KBinsDiscretizer(n_bins = [3، 2، 2]، encode = 'ordinal').fit (X)

بشكل افتراضي، يكون الإخراج مشفرًا بنظام one-hot في مصفوفة متفرقة
(راجع: ref: preprocessing_categorical_features)
ويمكن تكوينه باستخدام معلمة "الترميز".
بالنسبة لكل ميزة، يتم حساب حواف الحاوية أثناء "التناسب" ومع عدد الحاويات، فهي تحدد الفترات. وبالتالي، بالنسبة للمثال الحالي، يتم تحديد هذه الفترات على النحو التالي:

- الميزة 1: :math:`{[-\infty، -1)، [-1، 2)، [2، \ infty)}`
- الميزة 2: :math:`{[-\infty، 5)، [5، \ infty)}`
- الميزة 3: :math:`{[-\infty، 14)، [14، \ infty)}`

بناءً على فترات الحاوية هذه، يتم تحويل "س" على النحو التالي::

  >>> est.transform (X)                      # doctest: +SKIP
  array([[ 0.، 1.، 1.،]
         [ 1.، 1.، 1.]
         [ 2.، 0.، 0.]])

تحتوي مجموعة البيانات الناتجة على سمات ترتيبية يمكن استخدامها بشكل أكبر
في: class: sklearn.pipeline.Pipeline.

التجزئة مشابهة لبناء مخططات توزيع التواتر للبيانات المستمرة.
ومع ذلك، تركز مخططات توزيع التواتر على عد الميزات التي تقع في حاويات معينة، في حين تركز التجزئة على تعيين قيم الميزات لهذه الحاويات.

ينفذ: class: KBinsDiscretizer استراتيجيات التصنيف المختلفة، والتي يمكن
تحديدها باستخدام معلمة "الإستراتيجية". تستخدم إستراتيجية "الموحدة"
حاويات ذات عرض ثابت. تستخدم إستراتيجية "الكميات" قيم الكميات للحصول على
حاويات مأهولة بالتساوي في كل ميزة. تحدد إستراتيجية "kmeans" الحاويات بناءً
على إجراء التجميع k-means الذي يتم إجراؤه على كل ميزة بشكل مستقل.

كن على علم بأنه يمكنك تحديد حاويات مخصصة عن طريق تمرير دالة قابلة للاستدعاء تحدد
إستراتيجية التجزئة إلى: class: sklearn.preprocessing.FunctionTransformer.
على سبيل المثال، يمكننا استخدام دالة Pandas: func: pandas.cut::

  >>> import pandas as pd
  >>> import numpy as np
  >>> from sklearn import preprocessing
  >>>
  >>> bins = [0، 1، 13، 20، 60، np.inf]
  >>> labels = ['infant'، 'kid'، 'teen'، 'adult'، 'senior citizen']
  >>> المحول = preprocessing.FunctionTransformer (
  ...     pd.cut، kw_args = {'bins': bins، 'labels': labels، 'retbins': False}
  ... )
  >>> X = np.array ([0.2، 2، 15، 25، 97])
  >>> المحول. fit_transform (X)
  ['infant'، 'kid'، 'teen'، 'adult'، 'senior citizen']
  الفئات (5، كائن): ['infant' <'kid' <'teen' <'adult' <'senior citizen']

.. rubric :: أمثلة

* : ref: sphx_glr_auto_examples_preprocessing_plot_discretization.py`
* : ref: sphx_glr_auto_examples_preprocessing_plot_discretization_classification.py`
* : ref: sphx_glr_auto_examples_preprocessing_plot_discretization_strategies.py`

.. _preprocessing_binarization:

تجزئة السمات الثنائية
---------------------

**تجزئة السمات الثنائية** هي عملية **عتبات الميزات الرقمية للحصول على قيم منطقية**. يمكن أن يكون هذا مفيدًا لمقدرات الاحتمالية التنازلية التي تفترض أن البيانات المدخلة
توزع وفقًا لتوزيع برنولي متعدد المتغيرات
<https://en.wikipedia.org/wiki/Bernoulli_distribution>. على سبيل المثال،
هذه هي الحالة بالنسبة إلى: class: sklearn.neural_network.BernoulliRBM.

ومن الشائع أيضًا في مجتمع معالجة النصوص استخدام قيم السمات الثنائية (ربما لتبسيط الاستدلال الاحتمالي) حتى إذا كانت القيم المحددة (المعروفة باسم تواتر المصطلحات) أو ميزات TF-IDF تؤدي غالبًا بشكل أفضل في الممارسة العملية.

كما هو الحال مع: class: Normalizer، فإن فئة المنفعة
: class: Binarizer يقصد استخدامها في المراحل الأولى من
: class: sklearn.pipeline.Pipeline. لا تفعل طريقة "التناسب" شيئًا حيث تتم معاملة كل عينة بشكل مستقل عن الآخرين::

  >>> X = [[1.، -1.، 2.]،
  ...      [2.، 0.، 0.]،
  ...      [0.، 1.، -1.]]

  >>> المحول الثنائي = preprocessing.Binarizer (). fit (X) # لا يفعل التثبيت شيئًا
  >>> المحول الثنائي
  المحول الثنائي ()

  >>> المحول الثنائي. transform (X)
  array([[1.، 0.، 1.]،
         [1.، 0.، 0.]،
         [0.، 1.، 0.]])

من الممكن ضبط عتبة المحول الثنائي::

  >>> المحول الثنائي = preprocessing.Binarizer (عتبة = 1.1)
  >>> المحول الثنائي. transform (X)
  array([[0.، 0.، 1.]،
         [1.، 0.، 0.]،
         [0.، 0.، 0.]])

كما هو الحال مع فئة: class: Normalizer، توفر وحدة المعالجة ميزة مصاحبة
: func: binarize
يتم استخدامه عندما لا تكون واجهة المحول ضرورية.

لاحظ أن: class: Binarizer يشبه: class: KBinsDiscretizer
عندما "k = 2"، وعندما يكون حافة الحاوية عند القيمة "عتبة".

.. topic :: الإدخال المتناثر

  : func: binarize و: class: Binarizer قبول **كلا من المصفوفات الكثيفة المتشابهة
  والمصفوفات المتناثرة من scipy.sparse كإدخال**.

  بالنسبة للإدخال المتناثر، يتم **تحويل البيانات إلى تمثيل الصفوف المتناثرة المضغوطة**
  (راجع "scipy.sparse.csr_matrix").
  لتجنب عمليات نسخ الذاكرة غير الضرورية، يُنصح باختيار تمثيل CSR
  أعلى النهر.

.. _imputation:

تقدير القيم المفقودة
============================

يتم مناقشة أدوات تقدير القيم المفقودة في: ref: impute.

.. _generating_polynomial_features:

توليد ميزات متعددة الحدود
==============================

غالبًا ما يكون من المفيد إضافة التعقيد إلى نموذج بالنظر إلى الميزات غير الخطية لبيانات الإدخال. نعرض إمكانيتين تعتمدان على متعددات الحدود: الأولى تستخدم متعددات الحدود البحتة، والثانية تستخدم المنحنيات،
أي متعددات الحدود القطعية.

.. _polynomial_features:

ميزات متعددة الحدود
-------------------

تتمثل إحدى الطرق البسيطة والشائعة في استخدام ميزات متعددة الحدود، والتي يمكن أن تحصل على شروط تفاعل وميزات عالية الترتيب. يتم تنفيذه في
: class: PolynomialFeatures::

    >>> import numpy as np
    >>> from sklearn.preprocessing import PolynomialFeatures
    >>> X = np.arange (6). reshape (3، 2)
    >>> X
    array([[0، 1]،
           [2، 3]،
           [4، 5]])
    >>> poly = PolynomialFeatures (2)
    >>> poly.fit_transform (X)
    array([[ 1.، 0.، 1.، 0.، 0.، 1.]،
           [ 1.، 2.، 3.، 4.، 6.، 9.]،
           [ 1.، 4.، 5.، 16.، 20.، 25.]])

تم تحويل ميزات "س" من: math: `(X_1، X_2)` إلى: math: `(1، X_1، X_2، X_1 ^ 2، X_1X_2، X_2 ^ 2)`.

في بعض الحالات، تكون شروط التفاعل بين الميزات مطلوبة فقط، ويمكن الحصول عليها باستخدام الإعداد "interaction_only = True"::

    >>> X = np.arange (9). reshape (3، 3)
    >>> X
    array([[0، 1، 2]،
           [3، 4، 5]،
           [6، 7، 8]])
    >>> poly = PolynomialFeatures (degree = 3، interaction_only = True)
    >>> poly.fit_transform (X)
    array([[ 1.، 0.، 1.، 2.، 0.، 0.، 2.، 0.]،
           [ 1.، 3.، 4.، 5.، 12.، 15.، 20.، 60.]،
           [ 1.، 6.، 7.، 8.، 42.، 48.، 56.، 336.]])

تم تحويل ميزات "س" من: math: `(X_1، X_2، X_3)` إلى: math: `(1، X_1، X_2، X_3، X_1X_2، X_1X_3، X_2X_3، X_1X_2X_3)`.

لاحظ أن ميزات متعددة الحدود تستخدم ضمنيًا في `أساليب النواة
<https://en.wikipedia.org/wiki/Kernel_method>`_ (على سبيل المثال،: class: sklearn.svm.SVC،
: class: sklearn.decomposition.KernelPCA) عند استخدام متعددة الحدود: ref: svm_kernels.

راجع: ref: sphx_glr_auto_examples_linear_model_plot_polynomial_interpolation.py
للتقريب باستخدام ريدج ريجريشن باستخدام ميزات متعددة الحدود التي تم إنشاؤها.

.. _spline_transformer:

محول المنحنى
------------------

طريقة أخرى لإضافة شروط غير خطية بدلاً من متعددات الحدود البحتة للميزات هي
توليد دالات أساس المنحنى لكل ميزة مع
: class: SplineTransformer. المنحنيات هي متعددات حدود قطعية، يتم معلماتها بواسطة
درجة متعددة الحدود الخاصة بها ومواضع العقد. ينفذ: class: SplineTransformer
أساس B-spline، راجع المراجع أدناه.

.. note ::

    يتعامل: class: SplineTransformer مع كل ميزة بشكل منفصل، أي أنه
    لن يعطيك شروط التفاعل.

بعض مزايا المنحنيات على متعددات الحدود هي:

- المنحنيات B مرنة للغاية ومتينة إذا كنت تحتفظ بدرجة منخفضة ثابتة،
  عادة 3، وتكيف عدد العقد بشكل مقتصد. سوف تحتاج متعددات الحدود
  إلى درجة أعلى، مما يؤدي إلى النقطة التالية.
- لا تُظهر المنحنيات B سلوكًا متذبذبًا عند الحدود كما تفعل متعددات الحدود (كلما ارتفعت الدرجة، كلما كان الأمر أسوأ). يُعرف هذا باسم "ظاهرة رونج" <https://en.wikipedia.org/wiki/Runge% 27s_phenomenon>.
- توفر المنحنيات B خيارات جيدة للاستقراء خارج النطاق،
  أي خارج نطاق القيم المناسب. الق نظرة على الخيار
  "الاستقراء".
- تنتج المنحنيات B مصفوفة ميزات ذات بنية محزمة. بالنسبة لميزة واحدة، يحتوي كل صف على "درجة + 1" فقط
  العناصر غير الصفرية، والتي تحدث بشكل متتابع وحتى إيجابية. يؤدي هذا إلى مصفوفة ذات خصائص عددية جيدة،
  على سبيل المثال، عدد شرطي منخفض، على النقيض الشديد من مصفوفة متعددة الحدود، والتي يطلق عليها اسم
  "مصفوفة فانديرموند" <https://en.wikipedia.org/wiki/Vandermonde_matrix>.
  يعد العدد الشرطي المنخفض مهمًا لخوارزميات مستقرة للنماذج الخطية.

توضح مقتطفات التعليمات البرمجية التالية المنحنيات في العمل::

    >>> import numpy as np
    >>> from sklearn.preprocessing import SplineTransformer
    >>> X = np.arange (5). reshape (5، 1)
    >>> X
    array([[0]،
           [1]،
           [2]،
           [3]،
           [4]])
    >>> spline = SplineTransformer (degree = 2، n_knots = 3)
    >>> spline.fit_transform (X)
    array([[0.5، 0.5، 0.، 0.]،
           [0.125، 0.75، 0.125، 0.]،
           [0.، 0.5، 0.5، 0.]،
           [0.، 0.125، 0.75، 0.125]،
           [0.، 0.، 0.5، 0.5]])

نظرًا لفرز "س"، يمكنك بسهولة رؤية المصفوفة المحزمة للإخراج. بالنسبة إلى "درجة = 2"، فإن المصفوفات الثلاثة الوسطى فقط غير صفرية. وكلما ارتفعت الدرجة، زاد تداخل المنحنيات.

من المثير للاهتمام أن: class: SplineTransformer من "درجة = 0" هو نفسه
: class: sklearn.preprocessing.KBinsDiscretizer
مع "encode = 'onehot-dense'" و "n_bins = n_knots - 1" إذا
"العقد = الإستراتيجية".

.. rubric :: أمثلة

* : ref: sphx_glr_auto_examples_linear_model_plot_polynomial_interpolation.py`
* : ref: sphx_glr_auto_examples_applications_plot_cyclical_feature_engineering.py`

.. dropdown :: المراجع

  * Eilers، P.، وMarx، B. (1996). :doi: 'طرق التنعيم المرنة باستخدام B-splines والعقوبات
    <10.1214/ss/1038425655>. Statist. Sci. 11 (1996)، رقم 2، 89-121.

  * Perperoglou، A.، Sauerbrei، W.، Abrahamowicz، M. et al. :doi: 'مراجعة لإجراءات دالة المنحنى في R
    <10.1186/s12874-019-0666-3>.
    BMC Med Res Methodol 19، 46 (2019).


.. _function_transformer:

المحولات المخصصة
في كثير من الأحيان، قد ترغب في تحويل دالة Python موجودة مسبقًا إلى محول للبيانات للمساعدة في تنظيف البيانات أو معالجتها. يمكنك تنفيذ محول من دالة عشوائية باستخدام class: 'FunctionTransformer'. على سبيل المثال، لبناء محول يطبق تحويل اللوغاريتم في خط أنابيب، قم بما يلي::

    >>> import numpy as np
    >>> from sklearn.preprocessing import FunctionTransformer
    >>> transformer = FunctionTransformer(np.log1p, validate=True)
    >>> X = np.array([[0, 1], [2, 3]])
    >>> # بما أن FunctionTransformer لا يفعل أي شيء أثناء التهيئة، يمكننا استدعاء transform مباشرة
    >>> transformer.transform(X)
    array([[0.        , 0.69314718],
           [1.09861229, 1.38629436]])

يمكنك التأكد من أن "func" و "inverse_func" هما العكس لبعضهما البعض من خلال تعيين "check_inverse=True" واستدعاء "fit" قبل "transform". يرجى ملاحظة أنه يتم رفع تحذير ويمكن تحويله إلى خطأ باستخدام "filterwarnings"::

  >>> import warnings
  >>> warnings.filterwarnings("error", message=".*check_inverse*.",
  ...                         category=UserWarning, append=False)

للحصول على مثال كامل للرمز يوضح استخدام "FunctionTransformer" لاستخراج الميزات من بيانات النص، راجع:
ref: 'sphx_glr_auto_examples_compose_plot_column_transformer.py' و
ref: 'sphx_glr_auto_examples_applications_plot_cyclical_feature_engineering.py'.