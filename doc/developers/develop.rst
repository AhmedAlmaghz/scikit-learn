تطوير مُقدّرات scikit-learn
==================================

سواء كنت تقترح مُقدّرًا لإدراجه في scikit-learn، أو تطور حزمة منفصلة متوافقة مع scikit-learn، أو تنفذ مكونات مخصصة لمشاريعك الخاصة، يشرح هذا الفصل كيفية تطوير كائنات تتفاعل بأمان مع أنابيب scikit-learn وأدوات اختيار النماذج.

.. currentmodule:: sklearn

.. _api_overview:

واجهات برمجة تطبيقات كائنات scikit-learn
============================

للحصول على واجهة برمجة تطبيقات موحدة، نحاول أن يكون لدينا واجهة برمجة تطبيقات أساسية مشتركة لجميع الكائنات. بالإضافة إلى ذلك، لتجنب انتشار كود الإطار، نحاول تبني اتفاقيات بسيطة والحد من عدد الطرق التي يجب أن ينفذها الكائن إلى الحد الأدنى.

توصف عناصر واجهة برمجة تطبيقات scikit-learn بشكل أكثر تحديدًا في: ref:`glossary`.

كائنات مختلفة
-----------------

الكائنات الرئيسية في scikit-learn هي (يمكن لفئة واحدة تنفيذ واجهات متعددة):

:Estimator:

    الكائن الأساسي، ينفذ طريقة "fit" لتعلم البيانات، إما::

      estimator = estimator.fit(data, targets)

    أو::

      estimator = estimator.fit(data)

:Predictor:

    للتعلم الخاضع للإشراف، أو بعض المشكلات غير الخاضعة للإشراف، ينفذ::

      prediction = predictor.predict(data)

    عادة ما توفر خوارزميات التصنيف أيضًا طريقة لقياس مدى التأكد من التنبؤ، إما باستخدام "decision_function" أو "predict_proba"::

      probability = predictor.predict_proba(data)

:Transformer:

    لتعديل البيانات بطريقة خاضعة للإشراف أو غير خاضعة للإشراف (على سبيل المثال، عن طريق إضافة أعمدة أو تغييرها أو إزالتها، ولكن ليس عن طريق إضافة صفوف أو إزالتها). ينفذ::

      new_data = transformer.transform(data)

    عندما يمكن تنفيذ التجهيز والتحويل معًا بكفاءة أكبر من تنفيذهما بشكل منفصل، ينفذ::

      new_data = transformer.fit_transform(data)

:Model:

    نموذج يمكنه إعطاء مقياس "goodness of fit" أو احتمال حدوث بيانات غير مرئية، ينفذ (الأعلى أفضل)::

      score = model.score(data)

المُقدّرات
----------

لدى واجهة برمجة التطبيقات كائن واحد سائد: المُقدّر. المُقدّر هو كائن يتناسب مع نموذج بناءً على بعض بيانات التدريب وقادر على استنتاج بعض الخصائص على بيانات جديدة. يمكن أن يكون، على سبيل المثال، مصنفًا أو مُرجعًا. تنفذ جميع المُقدّرات طريقة "fit"::

    estimator.fit(X, y)

لدى جميع المُقدّرات المدمجة أيضًا طريقة "set_params"، والتي تقوم بتعيين معلمات مستقلة عن البيانات (باستبدال قيم المعلمات السابقة التي تم تمريرها إلى "__init__").

يجب أن ترث جميع المُقدّرات في شيفرة scikit-learn الأساسية من "sklearn.base.BaseEstimator".

التهيئة
^^^^^^^^^^^^^

يتعلق هذا الأمر بإنشاء كائن. قد تقبل طريقة "__init__" الخاصة بالكائن ثوابت كوسيطات تحدد سلوك المُقدّر (مثل ثابت "C" في SVMs). ومع ذلك، يجب ألا يأخذ بيانات التدريب الفعلية كوسيط، حيث يتم ترك ذلك لطريقة "fit"::

    clf2 = SVC(C=2.3)
    clf3 = SVC([[1, 2], [2, 3]], [-1, 1]) # خطأ!

يجب أن تكون جميع الوسيطات التي تقبلها "__init__" وسيطات كلمات رئيسية بقيم افتراضية. وبعبارة أخرى، يجب أن يكون المستخدم قادرًا على إنشاء مثيل من المُقدّر دون تمرير أي وسيطات إليه. يجب أن تتوافق الوسيطات جميعها مع معلمات تصف النموذج أو مشكلة التحسين التي يحاول المُقدّر حلها. يتم تذكر هذه الوسيطات الأولية (أو المعلمات) دائمًا بواسطة المُقدّر.

لاحظ أيضًا أنه لا يجب توثيقها في قسم "Attributes"، ولكن بدلاً من ذلك في قسم "Parameters" لهذا المُقدّر.

بالإضافة إلى ذلك، يجب أن **يتوافق كل وسيط كلمة رئيسية تقبله** "__init__" **مع خاصية على المثيل**. يعتمد scikit-learn على هذا للعثور على الخصائص ذات الصلة لتعيينها على مُقدّر عند إجراء اختيار النموذج.

لتلخيص، يجب أن تبدو "__init__" كالتالي::

    def __init__(self, param1=1, param2=2):
        self.param1 = param1
        self.param2 = param2

لا يجب أن يكون هناك أي منطق، حتى التحقق من صحة الإدخال، ويجب عدم تغيير المعلمات. يجب وضع المنطق المقابل حيث يتم استخدام المعلمات، عادة في "fit".

ما يلي خطأ::

    def __init__(self, param1=1, param2=2, param3=3):
        # خطأ: لا يجب تعديل المعلمات
        if param1 > 1:
            param2 += 1
        self.param1 = param1
        # خطأ: يجب أن يكون للخصائص الخاصة بالكائن نفس اسم
        # الوسيط في الباني
        self.param3 = param2

والسبب في تأجيل التحقق من الصحة هو أنه يجب إجراء نفس التحقق من الصحة في "set_params"، والذي يتم استخدامه في خوارزميات مثل "GridSearchCV".

التجهيز
^^^^^^^

الشيء التالي الذي قد ترغب في فعله هو تقدير بعض المعلمات في النموذج. يتم تنفيذ ذلك في طريقة "fit".

تأخذ طريقة "fit" بيانات التدريب كوسيطات، والتي يمكن أن تكون مصفوفة واحدة في حالة التعلم غير الخاضع للإشراف، أو مصفوفتين في حالة التعلم الخاضع للإشراف.

لاحظ أنه يتم تجهيز النموذج باستخدام "X" و "y"، ولكن الكائن لا يحتوي على مرجع إلى "X" و "y". ومع ذلك، هناك بعض الاستثناءات لهذا، كما هو الحال في حالة النواة المحسوبة مسبقًا حيث يجب تخزين هذه البيانات لاستخدامها بواسطة طريقة "predict".

============= ======================================================
المعلمات
============= ======================================================
X             مصفوفة الشكل (n_samples، n_features)

y             مصفوفة الشكل (n_samples،)

kwargs        وسيطات اختيارية تعتمد على البيانات
============= ======================================================

يجب أن يكون "X.shape[0]" هو نفسه "y.shape[0]". إذا لم يتم استيفاء هذا الشرط، فيجب إثارة استثناء من النوع "ValueError".

قد يتم تجاهل "y" في حالة التعلم غير الخاضع للإشراف. ومع ذلك، لجعل من الممكن استخدام المُقدّر كجزء من خط أنابيب يمكنه مزج المحولات الخاضعة للإشراف وغير الخاضعة للإشراف، حتى المُقدّرات غير الخاضعة للإشراف تحتاج إلى قبول وسيط "y=None" في
المركز الثاني الذي يتم تجاهله ببساطة بواسطة المُقدّر. لنفس السبب، تحتاج طرق "fit_predict" و "fit_transform" و "score" و "partial_fit" إلى قبول وسيط "y" في
المركز الثاني إذا تم تنفيذها.

يجب أن تعيد الطريقة الكائن ( "self"). هذا النمط مفيد ليكون من الممكن تنفيذ عبارات سريعة في جلسة IPython مثل::

  y_predicted = SVC(C=100).fit(X_train, y_train).predict(X_test)

اعتمادًا على طبيعة الخوارزمية، يمكن أن تقبل "fit" أيضًا وسيطات كلمات رئيسية إضافية. ومع ذلك، يجب أن تكون أي معلمة يمكن تعيين قيمة لها قبل الوصول إلى البيانات وسيطة "__init__" كلمة رئيسية. يجب تقييد **معلمات التجهيز** لتكون متغيرات تعتمد بشكل مباشر على البيانات. على سبيل المثال، مصفوفة غرام أو مصفوفة تشابه محسوبة مسبقًا من مصفوفة البيانات "X" تعتمد على البيانات. معيار التوقف "tol" ليس مباشرًا
يعتمد على البيانات (على الرغم من أن القيمة المثالية وفقًا لبعض دالة التقييم ربما تكون كذلك).

عندما يتم استدعاء "fit"، يجب تجاهل أي استدعاء سابق لـ "fit". بشكل عام، يجب أن يكون استدعاء "estimator.fit(X1)" ثم "estimator.fit(X2)" هو نفسه مثل استدعاء "estimator.fit(X2)" فقط. ومع ذلك، قد لا يكون هذا صحيحًا في الممارسة عندما تعتمد "fit" على بعض العمليات العشوائية، راجع: term:`random_state`. استثناء آخر لهذه القاعدة هو عندما يتم تعيين المعلمة الفائقة "warm_start" إلى "True" للمُقدّرات التي تدعمها. "warm_start=True" يعني أنه يتم إعادة استخدام حالة المعلمات القابلة للتدريب السابقة للمُقدّر بدلاً من استخدام استراتيجية التهيئة الافتراضية.

الخصائص المقدرة
^^^^^^^^^^^^^^^^^^^^

يجب أن يكون للخصائص المقدرة من البيانات دائمًا اسم ينتهي بشرطة سفلية، على سبيل المثال، سيتم تخزين معاملات بعض مُقدّر الانحدار في خاصية "coef_" بعد استدعاء "fit".

من المتوقع أن يتم تجاوز الخصائص المقدرة عند استدعاء "fit" للمرة الثانية.

وسيطات اختيارية
^^^^^^^^^^^^^^^^^^

في الخوارزميات التكرارية، يجب تحديد عدد التكرارات بواسطة عدد صحيح يسمى "n_iter".

الخصائص العالمية
^^^^^^^^^^^^^^^^^^^^

يجب على المُقدّرات التي تتوقع إدخال جدول بيانات تعيين خاصية "n_features_in_" في وقت "fit" للإشارة إلى عدد الميزات التي يتوقعها المُقدّر للمكالمات اللاحقة إلى "predict" أو "transform".
راجع
`SLEP010
<https://scikit-learn-enhancement-proposals.readthedocs.io/en/latest/slep010/proposal.html>`_
للحصول على التفاصيل.

.. _rolling_your_own_estimator:

إنشاء مُقدّرك الخاص
بالتأكيد! فيما يلي ترجمة لنص ReStructuredText إلى اللغة العربية:

==========================
إذا كنت ترغب في تنفيذ مصدر تقدير متوافق مع scikit-learn، سواء كان ذلك للاستخدام الشخصي أو للمساهمة في scikit-learn، فهناك العديد من التفاصيل الداخلية لـ scikit-learn التي يجب أن تكون على دراية بها بالإضافة إلى واجهة برمجة التطبيقات scikit-learn الموضحة أعلاه. يمكنك التحقق مما إذا كان مصدر التقدير الخاص بك يلتزم بواجهة برمجة التطبيقات والمعايير الخاصة بـ scikit-learn عن طريق تشغيل :func: ~ sklearn.utils.estimator_checks.check_estimator على مثيل. يمكن أيضًا استخدام زخرفة pytest :func: ~ sklearn.utils.estimator_checks.parametrize_with_checks (راجع docstring للتفاصيل والتفاعلات المحتملة مع pytest)::

  >>> من sklearn.utils.estimator_checks استيراد check_estimator
  >>> من sklearn.svm استيراد LinearSVC
  >>> check_estimator (LinearSVC ()) # يمر

قد يكون الدافع الرئيسي لجعل فئة متوافقة مع واجهة مصدر تقدير scikit-learn هو أنك تريد استخدامها مع أدوات تقييم النموذج واختياره مثل :class: model_selection.GridSearchCV و :class: pipeline.Pipeline.

قبل تفصيل الواجهة المطلوبة أدناه، سنصف طريقتين لتحقيق الواجهة الصحيحة بسهولة أكبر.

.. موضوع:: قالب المشروع:

    نقدم `قالب المشروع <https://github.com/scikit-learn-contrib/project-template/>`_
    الذي يساعد في إنشاء حزم Python التي تحتوي على مصادر تقدير متوافقة مع scikit-learn.
    يوفر ما يلي:

    * مستودع git الأولي به هيكل دليل حزمة Python
    * قالب مصدر تقدير scikit-learn
    * جناح اختبار أولي بما في ذلك استخدام "check_estimator"
    * هياكل الدلائل والنصوص لتجميع الوثائق وصالات العرض التوضيحية
    * النصوص لإدارة التكامل المستمر (الاختبار على Linux و Windows)
    * تعليمات من البداية إلى النشر على `PyPi <https://pypi.org/>`_

.. موضوع:: "BaseEstimator" والمزيج:

    نميل إلى استخدام "duck typing"، لذا فإن بناء مصدر تقدير يتبع
    تكفي واجهة برمجة التطبيقات للتوافق، دون الحاجة إلى الميراث من أو
    حتى استيراد أي فئات scikit-learn.

    ومع ذلك، إذا كان الاعتماد على scikit-learn مقبولًا في كودك،
    يمكنك منع الكثير من كود التمهيد
    عن طريق اشتقاق فئة من "BaseEstimator"
    وفئات المزج الاختيارية في "sklearn.base".
    على سبيل المثال، فيما يلي مصنف مخصص، مع تضمين المزيد من الأمثلة
    في قالب المساهمة scikit-learn
    `قالب المشروع <https://github.com/scikit-learn-contrib/project-template/blob/master/skltemplate/_template.py>`__.

    من المهم بشكل خاص ملاحظة أن المزيج يجب أن يكون "على اليسار" في حين
    يجب أن يكون "BaseEstimator" "على اليمين" في قائمة الوراثة لـ MRO الصحيح.

      >>> استيراد numpy كالن
      >>> من sklearn.base استيراد BaseEstimator، ClassifierMixin
      >>> من sklearn.utils.validation استيراد check_X_y، check_array، check_is_fitted
      >>> من sklearn.utils.multiclass استيراد unique_labels
      >>> من sklearn.metrics استيراد euclidean_distances
      >>> class TemplateClassifier (ClassifierMixin، BaseEstimator):
      ...
      ... def __init__ (self، demo_param = 'demo'):
      ... self.demo_param = demo_param
      ...
      ... def fit (self، X، y):
      ...
      ... # تحقق مما إذا كان X و y لهما الشكل الصحيح
      ... X، y = check_X_y (X، y)
      ... # تخزين الفئات التي شوهدت أثناء التثبيت
      ... self.classes_ = unique_labels (y)
      ...
      ... self.X_ = X
      ... self.y_ = y
      ... # إعادة المصنف
      ... return self
      ...
      ... def predict (self، X):
      ...
      ... # تحقق مما إذا كان fit قد تم استدعاؤه
      ... check_is_fitted (self)
      ...
      ... # التحقق من صحة الإدخال
      ... X = check_array (X)
      ...
      ... الأقرب = np.argmin (euclidean_distances (X، self.X_), axis = 1)
      ... return self.y_ [الأقرب]


احصل على معلمات وحدد معلمات
-------------------------
تحتوي جميع مصادر scikit-learn على وظائف "get_params" و "set_params".
لا تأخذ وظيفة "get_params" أي وسيطات وتعيد قاموسًا لمعلمات "init" الخاصة بالمصدر، إلى جانب قيمها.

يجب أن يأخذ وسيطًا واحدًا، "deep"، والذي يتلقى قيمة منطقية
تحديد ما إذا كان يجب على الطريقة إعادة معلمات
المقدرات الفرعية (بالنسبة لمعظم المقدرات، يمكن تجاهل هذا). يجب أن تكون القيمة الافتراضية
من أجل "عميق" `صحيح`. على سبيل المثال بالنظر إلى المقدر التالي::

    >>> من sklearn.base استيراد BaseEstimator
    >>> من sklearn.linear_model استيراد LogisticRegression
    >>> class MyEstimator (BaseEstimator):
    ... def __init__ (self، subestimator = None، my_extra_param = "random"):
    ... self.subestimator = subestimator
    ... self.my_extra_param = my_extra_param

سيتحكم المعلمة `deep` فيما إذا كان يجب الإبلاغ عن معلمات
`subestimator`. وبالتالي عندما `deep = True`، فإن الإخراج سيكون::

    >>> my_estimator = MyEstimator (subestimator = LogisticRegression ())
    >>> لكل معلمة، قيمة في my_estimator.get_params (deep = True).items ():
    ... طباعة (f "{param} -> {value}")
    my_extra_param -> random
    subestimator__C -> 1.0
    subestimator__class_weight -> لا شيء
    subestimator__dual -> false
    subestimator__fit_intercept -> true
    subestimator__intercept_scaling -> 1
    subestimator__l1_ratio -> لا شيء
    subestimator__max_iter -> 100
    subestimator__multi_class -> غير مستخدم
    subestimator__n_jobs -> لا شيء
    subestimator__penalty -> l2
    subestimator__random_state -> لا شيء
    subestimator__solver -> lbfgs
    subestimator__tol -> 0.0001
    subestimator__verbose -> 0
    subestimator__warm_start -> false
    subestimator -> LogisticRegression ()

غالبًا ما يكون لـ `subestimator` اسم (كما هو الحال على سبيل المثال الخطوات المسماة في
:class: ~ sklearn.pipeline.Pipeline` كائن)، في هذه الحالة يجب أن تكون المفتاح
تصبح `<name> __C`، `<name> __class_weight`، إلخ.

بينما عندما `deep = False`، فإن الإخراج سيكون::

    >>> لكل معلمة، قيمة في my_estimator.get_params (deep = False).items ():
    ... طباعة (f "{param} -> {value}")
    my_extra_param -> random
    subestimator -> LogisticRegression ()

من ناحية أخرى، يأخذ "set_params" معلمات "init"
كوسيطات الكلمات الرئيسية، وفكها في قاموس من النموذج
`` 'parameter': value`` ويحدد معلمات المصدر باستخدام هذا القاموس.
يجب أن تكون قيمة الإرجاع هي المصدر نفسه.

بينما لا تكون آلية "get_params" ضرورية (راجع: ref: cloning أدناه)،
تعد وظيفة "set_params" ضرورية حيث يتم استخدامها لتعيين المعلمات أثناء
عمليات البحث الشبكي.

أسهل طريقة لتنفيذ هذه الوظائف، والحصول على طريقة معقولة
`` __repr__`` الطريقة، هي الميراث من `` sklearn.base.BaseEstimator``. إذا كنت
لا تريد جعل الكود الخاص بك يعتمد على scikit-learn، فإن أسهل طريقة لتنفيذ الواجهة هي::

    def get_params (self، deep = True):
        # افترض أن هذا المصدر له معلمات "alpha" و "recursive"
        return {"alpha": self.alpha، "recursive": self.recursive}

    def set_params (self، ** parameters):
        لكل معلمة، قيمة في المعلمات.العناصر ():
            setattr (self، parameter، value)
        return self


المعلمات و init
-------------------
نظرًا لأن :class: model_selection.GridSearchCV يستخدم "set_params"
لتطبيق إعداد المعلمات على المقدرات،
فمن الضروري أن يكون لاستدعاء "set_params" نفس التأثير
كما هو الحال عند إعداد المعلمات باستخدام طريقة "init".
أسهل طريقة وأكثرها موثوقية لتحقيق ذلك هي
**لا تفعل أي تحقق من صحة المعلمة في** `` __init__``.
كل المنطق وراء معلمات المصدر،
مثل ترجمة وسيطات السلسلة إلى وظائف، يجب أن يتم في "fit".

من المتوقع أيضًا أن المعلمات التي تحتوي على علامة سفلية متبوعة بـ `` _`` **لا يتم تعيينها
داخل طريقة** `` __init__``. جميع المعلمات العامة الوحيدة التي تم تعيينها بواسطة
تناسب لها علامة سفلية. ونتيجة لذلك، يتم استخدام وجود معلمات مع
علامة سفلية للتحقق مما إذا كان المصدر قد تم تثبيته.

.. _cloning:

الاستنساخ
-------
لاستخدامها مع :mod: ~ sklearn.model_selection module،
يجب أن يدعم المصدر وظيفة "base.clone" لاستنساخ مصدر تقدير.
يمكن القيام بذلك عن طريق توفير طريقة "get_params".
إذا كان "get_params" موجودًا، فسيتم "clone (estimator)" مثيلًا لـ
`` type (estimator)`` على الذي تم استدعاء "set_params" باستخدام استنساخات
نتيجة "estimator.get_params ()".

سيتم نسخ الكائنات التي لا توفر هذه الطريقة بعمق
(باستخدام وظيفة Python القياسية "copy.deepcopy")
إذا تم تمرير "safe=False" إلى "clone".

يمكن لمصادر التقدير تخصيص سلوك :func: base.clone عن طريق تعريف
`__sklearn_clone__` طريقة. يجب أن تعيد طريقة `__sklearn_clone__` مثيلًا من المصدر. `__sklearn_clone__` مفيد عندما يحتاج مصدر تقدير إلى الاحتفاظ ببعض الحالات عند استدعاء :func: base.clone على المصدر. على سبيل المثال، يمكن تعريف محول مجمد على النحو التالي::

    class FrozenTransformer (BaseEstimator):
        def __init__ (self، fitted_transformer):
            self.fitted_transformer = fitted_transformer

        def __getattr__ (self، name):
            # أصبحت سمات 'fitted_transformer' الآن قابلة للوصول
            return getattr (self.fitted_transformer، name)

        def __sklearn_clone__ (self):
            return self

        def fit (self، X، y = None):
            # لا يغير التثبيت حالة المصدر
            return self

        def fit_transform (self، X، y = None):
            # fit_transform يحول البيانات فقط
            return self.fitted_transformer.transform (X، y)

توافق الأنابيب
----------------------
لكي يكون مصدر التقدير قابلًا للاستخدام مع "pipeline.Pipeline" في أي شيء بخلاف
الخطوة الأخيرة، يجب أن توفر وظيفة "fit" أو "fit_transform".
ليكون قادرًا على تقييم الأنبوب على أي بيانات ولكن مجموعة التدريب،
يجب أن يوفر أيضًا وظيفة "transform".
لا توجد متطلبات خاصة للخطوة الأخيرة في الأنبوب، باستثناء أن
لديها وظيفة "fit". يجب أن تأخذ جميع وظائف "fit" و "fit_transform"
وسائط "X، y"، حتى إذا لم يتم استخدام y. وبالمثل، لكي يكون "score" قابلًا للاستخدام،
يجب أن تكون الخطوة الأخيرة في الأنبوب بها وظيفة "score" تقبل "y" اختيارية.

أنواع المقدرات
---------------
تعتمد بعض الوظائف الشائعة على نوع مصدر التقدير الذي تم تمريره.
على سبيل المثال، يكون التثليث الافتراضي في :class: model_selection.GridSearchCV و
:func: model_selection.cross_val_score استراتيجيًا عند استخدامه
على مصنف، ولكن ليس بخلاف ذلك. وبالمثل، تحتاج درجات الدقة المتوسطة التي تأخذ تنبؤًا مستمرًا إلى استدعاء "decision_function" للمصنفات،
ولكن "predict" للمرجعين. يتم تنفيذ هذا التمييز بين المصنفات والمراجع
باستخدام سمة "estimator_type"، والتي تأخذ قيمة سلسلة.
يجب أن يكون "المصنف" للمصنفات و"regressor" للمراجع و"clusterer" لطرق التجميع، للعمل كما هو متوقع.
سيؤدي الميراث من "ClassifierMixin" أو "RegressorMixin" أو "ClusterMixin"
إلى تعيين السمة تلقائيًا. عندما يحتاج مصدر تقدير ميتا إلى التمييز
بين أنواع مصادر التقدير، بدلاً من التحقق من "estimator_type" مباشرةً، يجب استخدام المساعدين
مثل :func: base.is_classifier.

نماذج محددة
بالتأكيد! فيما يلي ترجمة للنص المحدد بتنسيق ReStructuredText إلى اللغة العربية:

يجب أن تقبل المصنفات حجة "y" (الهدف) إلى "fit" التي تكون تسلسلات (قوائم، مصفوفات) من السلاسل النصية أو الأعداد الصحيحة. يجب ألا تفترض أن تسميات الفئات هي نطاق متصل من الأعداد الصحيحة؛ بدلاً من ذلك، يجب أن تخزن قائمة من الفئات في سمة أو خاصية "classes_". يجب أن يتطابق ترتيب تسميات الفئات في هذه السمة مع الترتيب الذي تعيد به الدوال "predict_proba" و"predict_log_proba" و"decision_function" قيمها. وأسهل طريقة لتحقيق ذلك هي وضع ما يلي في "fit":

.. code:: python

   self.classes_, y = np.unique(y, return_inverse=True)

هذا يعيد "y" جديدة تحتوي على فهارس الفئات، بدلاً من التسميات، في النطاق [0، "n_classes").

يجب أن تعيد طريقة "predict" في المصنف مصفوفات تحتوي على تسميات الفئات من "classes_". في مصنف ينفذ "decision_function"، يمكن تحقيق ذلك بما يلي:

.. code:: python

   def predict(self, X):
       D = self.decision_function(X)
       return self.classes_[np.argmax(D, axis=1)]

في النماذج الخطية، يتم تخزين المعاملات في مصفوفة تسمى "coef_"، ويتم تخزين المصطلح المستقل في "intercept_". يحتوي "sklearn.linear_model._base" على بعض الفئات الأساسية وmixins التي تنفذ أنماط النماذج الخطية الشائعة.

يحتوي نموذج "sklearn.utils.multiclass" على وظائف مفيدة للعمل مع مشكلات التصنيف المتعدد والمتعدد التصنيفات.

.. _estimator_tags:

علامات المقدر
--------------
.. warning::

   علامات المقدر تجريبية وواجهة برمجة التطبيقات الخاصة بها عرضة للتغيير.

قدمت Scikit-learn علامات المقدر في الإصدار 0.21. هذه هي علامات المقدرين التي تسمح بالتفتيش البرمجي لقدراتهم، مثل دعم مصفوفة متفرقة، وأنواع الإخراج المدعومة، والطرق المدعومة. علامات المقدر هي قاموس يعيده الأسلوب "_get_tags()". تُستخدم هذه العلامات في الفحوصات الشائعة التي تقوم بها وظيفة "sklearn.utils.estimator_checks.check_estimator" والزخرفة "sklearn.utils.estimator_checks.parametrize_with_checks". تحدد العلامات الفحوصات التي سيتم تشغيلها ومدخلات البيانات المناسبة. يمكن أن تعتمد العلامات على معلمات المقدر أو حتى على بنية النظام ويمكن تحديدها بشكل عام في وقت التشغيل فقط.

المجموعة الحالية من علامات المقدر هي:

allow_nan (default=False)
   ما إذا كان المقدر يدعم البيانات التي تحتوي على قيم مفقودة مشفرة كـ np.nan

array_api_support (default=False)
   ما إذا كان المقدر يدعم المدخلات المتوافقة مع واجهة برمجة تطبيقات المصفوفة.

binary_only (default=False)
   ما إذا كان المقدر يدعم التصنيف الثنائي ولكنه يفتقر إلى دعم التصنيف متعدد الفئات.

multilabel (default=False)
   ما إذا كان المقدر يدعم الإخراج متعدد التصنيفات.

multioutput (default=False)
   ما إذا كان المقدر يدعم الإخراج متعدد الأهداف.

multioutput_only (default=False)
   ما إذا كان المقدر يدعم فقط التصنيف أو الانحدار متعدد الإخراج.

no_validation (default=False)
   ما إذا كان المقدر يتخطى التحقق من صحة الإدخال. هذا مخصص فقط للمحولات عديمة الحالة والاحتياطية!

non_deterministic (default=False)
   ما إذا كان المقدر غير محدد نظرًا لقيمة "random_state" ثابتة

pairwise (default=False)
   يشير هذا السمة المنطقي إلى ما إذا كانت البيانات ("X") :term: تتكون من مقاييس زوجية عبر العينات بدلاً من تمثيل الميزة لكل عينة. عادة ما يكون "صحيح" حيث يكون للمقدر معلمة "metric" أو "affinity" أو "kernel" بقيمة "precomputed". الغرض الأساسي منها هو دعم :term: 'meta-estimator' أو إجراء التحقق من صحة متقاطع يستخرج عينة فرعية من البيانات المقصود بها مقدر زوجي، حيث تحتاج البيانات إلى الفهرسة على كلا المحورين. يتم استخدام هذه العلامة على وجه التحديد بواسطة "sklearn.utils.metaestimators._safe_split" لتقطيع الصفوف والأعمدة.

preserves_dtype (default=["np.float64"])
   ينطبق فقط على المحولات. فهو يقابل أنواع البيانات التي سيتم الحفاظ عليها بحيث تكون "X_trans.dtype" هي نفسها مثل "X.dtype" بعد استدعاء "transformer.transform(X)". إذا كانت هذه القائمة فارغة، فمن المتوقع ألا يحافظ المحول على نوع البيانات. تعتبر القيمة الأولى في القائمة نوع البيانات الافتراضي، والذي يقابل نوع بيانات الإخراج عندما لا يتم الاحتفاظ بنوع بيانات الإدخال.

poor_score (default=False)
   ما إذا كان المقدر يفشل في توفير نتيجة "معقولة" لمجموعة الاختبار، والتي حاليًا بالنسبة للانحدار هي R2 من 0.5 على "make_regression(n_samples=200, n_features=10, n_informative=1, bias=5.0, noise=20, random_state=42)"، وبالنسبة للتصنيف دقة 0.83 على "make_blobs(n_samples=300, random_state=0)". تستند هذه المجموعات والقيم إلى المقدرين الحاليين في sklearn وقد يتم استبدالها بشيء أكثر منهجية.

requires_fit (default=True)
   ما إذا كان المقدر يتطلب التجهيز قبل استدعاء أحد الأساليب "transform" أو "predict" أو "predict_proba" أو "decision_function".

requires_positive_X (default=False)
   ما إذا كان المقدر يتطلب قيمة إيجابية لـ "X".

requires_y (default=False)
   ما إذا كان المقدر يتطلب تمرير "y" إلى أساليب "fit" أو "fit_predict" أو "fit_transform". تكون العلامة "صحيح" للمقدرين الذين يرثون من "~sklearn.base.RegressorMixin" و "~sklearn.base.ClassifierMixin".

requires_positive_y (default=False)
   ما إذا كان المقدر يتطلب "y" إيجابية (ينطبق فقط على الانحدار).

_skip_test (default=False)
   ما إذا كان سيتم تخطي الاختبارات الشائعة تمامًا. لا تستخدم هذا إلا إذا كان لديك سبب *جيد جدًا*.

_xfail_checks (default=False)
   قاموس "{check_name: reason}" من الفحوصات الشائعة التي سيتم وضع علامة عليها كـ "XFAIL" لـ pytest، عند استخدام "sklearn.utils.estimator_checks.parametrize_with_checks". سيتم ببساطة تجاهل هذه الفحوصات ولن يتم تشغيلها بواسطة "sklearn.utils.estimator_checks.check_estimator"، ولكن سيتم رفع تحذير "SkipTestWarning". لا تستخدم هذا إلا إذا كان هناك سبب *جيد جدًا* لعدم مرور المقدر الخاص بك في الفحص. لاحظ أيضًا أن استخدام هذه العلامة عرضة للتغيير حيث نحاول جعلها أكثر مرونة: كن مستعدًا للتغييرات التي قد تحدث في المستقبل.

stateless (default=False)
   ما إذا كان المقدر يحتاج إلى الوصول إلى البيانات للتجهيز. حتى إذا كان المقدر عديم الحالة، فقد يحتاج إلى استدعاء "fit" للتهيئة.

X_types (default=['2darray'])
   أنواع الإدخال المدعومة لـ "X" كقائمة من السلاسل النصية. يتم تشغيل الاختبارات حاليًا فقط إذا كان "2darray" موجودًا في القائمة، مما يشير إلى أن المقدر يأخذ مصفوفات Numpy ثنائية الأبعاد مستمرة كإدخال. القيمة الافتراضية هي ["2darray"]. الأنواع المحتملة الأخرى هي "string" و"sparse" و"categorical" و"dict" و"1dlabels" و"2dlabels". الهدف هو أن نوع الإدخال المدعوم سيحدد البيانات المستخدمة أثناء الاختبار، خاصة بالنسبة لبيانات "string" و"sparse" و"categorical". بالنسبة الآن، لا تستفيد اختبارات البيانات النادرة من علامة "sparse".

من غير المحتمل أن تناسب القيم الافتراضية لكل علامة احتياجات المقدر المحدد. يمكن إنشاء علامات إضافية أو يمكن تجاوز العلامات الافتراضية عن طريق تعريف طريقة "_more_tags()" والتي تعيد قاموسًا بالعلامات التي تم تجاوزها أو العلامات الجديدة المرغوبة. على سبيل المثال::

   class MyMultiOutputEstimator(BaseEstimator):

       def _more_tags(self):
           return {'multioutput_only': True,
                   'non_deterministic': True}

ستعود أي علامة غير موجودة في "_more_tags()" ببساطة إلى القيم الافتراضية الموثقة أعلاه.

على الرغم من أنه غير موصى به، فمن الممكن تجاوز طريقة "_get_tags()". لاحظ مع ذلك أن **يجب أن تكون جميع العلامات موجودة في القاموس**. إذا كان أي من المفاتيح الموثقة أعلاه غير موجود في إخراج "_get_tags()"، فسيحدث خطأ.

بالإضافة إلى العلامات، يجب على المقدرين أيضًا الإعلان عن أي معلمات غير اختيارية إلى "__init__" في سمة الفئة "required_parameters"، والتي هي قائمة أو مجموعة. إذا كانت "required_parameters" هي فقط "["estimator"]" أو "["base_estimator"]"، فسيتم إنشاء المقدر في الاختبارات باستخدام مثيل من "LogisticRegression" (أو "RidgeRegression" إذا كان المقدر هو نموذج تنظيمي). اختيار هذه النماذج غريب إلى حد ما ولكن يجب أن توفر حلولًا قوية مغلقة الشكل.

.. _developer_api_set_output:

واجهة برمجة تطبيقات المطور لـ "set_output"
بالتزامن مع "SLEP018"، يقدم سكيت-ليرن واجهة برمجة التطبيقات (API) "set_output" لتهيئة المحولات لإخراج أطر بيانات بانداس. يتم تعريف واجهة برمجة التطبيقات "set_output" تلقائيًا إذا حدد المحول "get_feature_names_out" و"subclasses" لـ "base.TransformerMixin". ويُستخدم "get_feature_names_out" للحصول على أسماء أعمدة إخراج بانداس.

"base.OneToOneFeatureMixin" و"base.ClassNamePrefixFeaturesOutMixin" هما مزيجان مفيدان لتحديد "get_feature_names_out". "base.OneToOneFeatureMixin" مفيد عندما يكون هناك تطابق واحد لواحد بين ميزات الإدخال والمخرجات في المحول، مثل "preprocessing.StandardScaler". "base.ClassNamePrefixFeaturesOutMixin" مفيد عندما يحتاج المحول إلى إنشاء أسماء ميزاته الخاصة، مثل "decomposition.PCA".

يمكنك إلغاء الاشتراك في واجهة برمجة التطبيقات "set_output" عن طريق تعيين "auto_wrap_output_keys=None" عند تحديد فئة فرعية مخصصة::

    class MyTransformer(TransformerMixin, BaseEstimator, auto_wrap_output_keys=None):

        def fit(self, X, y=None):
            return self
        def transform(self, X, y=None):
            return X
        def get_feature_names_out(self, input_features=None):
            ...

القيمة الافتراضية لـ "auto_wrap_output_keys" هي "("transform"،)"، والتي تقوم تلقائيًا بتغليف "fit_transform" و"transform". يستخدم "TransformerMixin" آلية "__init_subclass__" لاستهلاك "auto_wrap_output_keys" وتمرير جميع الحجج الكلمة الأخرى إلى فئة المستوى الأعلى الخاصة بها. يجب **عدم** اعتماد "auto_wrap_output_keys" في فئة المستوى الأعلى "__init_subclass__".

بالنسبة للمحولات التي تعيد مصفوفات متعددة في "transform"، سيقوم التغليف التلقائي بتغليف المصفوفة الأولى فقط ولن يغير المصفوفات الأخرى.

راجع: ref:`sphx_glr_auto_examples_miscellaneous_plot_set_output.py<sphx_glr_auto_examples_miscellaneous_plot_set_output.py>` للحصول على مثال حول كيفية استخدام واجهة برمجة التطبيقات.

.. _developer_api_check_is_fitted:

واجهة برمجة التطبيقات للمطورين لـ "check_is_fitted"
===================================

بشكل افتراضي، يتحقق "sklearn.utils.validation.check_is_fitted" مما إذا كان هناك أي سمات في المثيل مع شرطة سفلية ختامية، على سبيل المثال "coef_". يمكن لمقدّر تغيير السلوك عن طريق تنفيذ طريقة "__sklearn_is_fitted__" لا تأخذ أي إدخال وتعيد قيمة منطقية. إذا وجدت هذه الطريقة، فإن "sklearn.utils.validation.check_is_fitted" ببساطة تعيد إخراجها.

راجع: ref:`sphx_glr_auto_examples_developing_estimators_sklearn_is_fitted.py<sphx_glr_auto_examples_developing_estimators_sklearn_is_fitted.py>` للحصول على مثال حول كيفية استخدام واجهة برمجة التطبيقات.

واجهة برمجة التطبيقات للمطورين للتمثيل HTML
=====================================

.. warning::

    واجهة برمجة التطبيقات لتمثيل HTML تجريبية وقد تخضع للتغيير.

تعرض المقدرات التي ترث من "sklearn.base.BaseEstimator" تمثيل HTML لنفسها في بيئات البرمجة التفاعلية مثل دفاتر Jupyter. على سبيل المثال، يمكننا عرض مخطط HTML هذا::

    from sklearn.base import BaseEstimator

    BaseEstimator()

يتم الحصول على تمثيل HTML الخام عن طريق استدعاء الدالة "sklearn.utils.estimator_html_repr" على مثيل المقدر.

لتخصيص عنوان URL الذي يرتبط بوثائق المقدر (أي عند النقر فوق أيقونة "؟")، قم بإلغاء تحديد سمات "_doc_link_module" و"_doc_link_template". بالإضافة إلى ذلك، يمكنك توفير طريقة "_doc_link_url_param_generator". قم بتعيين "_doc_link_module" إلى اسم الوحدة النمطية (من المستوى الأعلى) التي تحتوي على المقدر الخاص بك. إذا لم تتطابق القيمة مع اسم الوحدة النمطية من المستوى الأعلى، فلن يحتوي تمثيل HTML على رابط إلى الوثائق. يتم تعيينه على "scikit-learn" لمقدرات scikit-learn.

يتم استخدام "_doc_link_template" لبناء عنوان URL النهائي. بشكل افتراضي، يمكن أن يحتوي على متغيرين: "estimator_module" (الاسم الكامل للوحدة النمطية التي تحتوي على المقدر) و"estimator_name" (اسم فئة المقدر). إذا كنت بحاجة إلى مزيد من المتغيرات، فيجب عليك تنفيذ طريقة "_doc_link_url_param_generator" التي يجب أن تعيد قاموسًا للمتغيرات وقيمها. سيتم استخدام هذا القاموس لعرض "_doc_link_template".

.. _coding-guidelines:

المبادئ التوجيهية للترميز
=================

فيما يلي بعض الإرشادات حول كيفية كتابة التعليمات البرمجية الجديدة لإدراجها في سكيت-ليرن، والتي قد يكون من المناسب اعتمادها في المشاريع الخارجية. بالطبع، هناك حالات خاصة وسيتم استثناءات لهذه القواعد. ومع ذلك، فإن اتباع هذه القواعد عند تقديم تعليمات برمجية جديدة يجعل المراجعة أسهل، لذا يمكن دمج التعليمات البرمجية الجديدة في وقت أقل.

يجعل تنسيق التعليمات البرمجية الموحد من السهل مشاركة ملكية التعليمات البرمجية. تحاول سكيت-ليرن المشروع اتباع المبادئ التوجيهية الرسمية لـ Python الموضحة بالتفصيل في "PEP8" والتي توضح كيفية تنسيق التعليمات البرمجية وإدراجها. يرجى قراءتها واتباعها.

بالإضافة إلى ذلك، نضيف المبادئ التوجيهية التالية:

* استخدم شرطات سفلية للفصل بين الكلمات في أسماء غير الفئات: "n_samples" بدلاً من "nsamples".

* تجنب عدة عبارات في سطر واحد. يفضل العودة إلى سطر بعد عبارة تحكم (إذا/لـ).

* استخدم الواردات النسبية للمراجع داخل سكيت-ليرن.

* تعد اختبارات الوحدة استثناءً لهذه القاعدة؛ يجب أن تستخدم الواردات المطلقة، تمامًا كما يفعل كود العميل. وبالتالي، إذا تم تصدير فئة أو دالة من "sklearn.foo" يتم تنفيذها في "sklearn.foo.bar.baz"، فيجب أن تستور الاختبار منها "sklearn.foo".

* **يرجى عدم استخدام** "import *" **في أي حال**. يعتبر ضارًا من قبل "التوصيات الرسمية لـ Python <https://docs.python.org/3.1/howto/doanddont.html#at-module-level>`_". يجعل الكود أكثر صعوبة في القراءة حيث لم يعد يتم الإشارة إلى أصل الرموز بشكل صريح، ولكن الأهم من ذلك، أنه يمنع استخدام أداة تحليل ثابتة مثل "pyflakes <https://divmod.readthedocs.io/en/latest/products/pyflakes.html>`_" للعثور تلقائيًا على الأخطاء في سكيت-ليرن.

* استخدم "معيار سلسلة وثائق نومبي <https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard>`_" في جميع سلاسل الوثائق الخاصة بك.

يمكن العثور على مثال جيد للكود الذي نفضله هنا `هنا <https://gist.github.com/nateGeorge/5455d2c57fb33c1ae04706f2dc4fee01>`_.

التحقق من صحة الإدخال
----------------

.. currentmodule:: sklearn.utils

تحتوي الوحدة النمطية "sklearn.utils" على وظائف مختلفة للتحقق من صحة الإدخال والتحويل. في بعض الأحيان، تكون "np.asarray" كافية للتحقق من الصحة؛ لا تستخدم "np.asanyarray" أو "np.atleast_2d"، لأنها تسمح لـ "np.matrix" من نومبي، والتي لها واجهة برمجة تطبيقات مختلفة (على سبيل المثال، "*" تعني المنتج النقطي على "np.matrix"، ولكن المنتج هادامارد على "np.ndarray").

في حالات أخرى، تأكد من استدعاء "check_array" على أي وسيط يشبه المصفوفة التي يتم تمريرها إلى دالة واجهة برمجة تطبيقات سكيت-ليرن. تعتمد المعلمات الدقيقة المستخدمة بشكل أساسي على ما إذا كان يجب قبول مصفوفات "scipy.sparse" وأي منها.

لمزيد من المعلومات، راجع صفحة: ref:`developers-utils` .

الأرقام العشوائية
--------------

إذا كانت التعليمات البرمجية الخاصة بك تعتمد على مولد الأرقام العشوائية، فلا تستخدم "numpy.random.random()" أو الروتينات المماثلة. لضمان إمكانية إعادة الإنتاج في التحقق من الأخطاء، يجب أن تقبل الروتين كلمة أساسية "random_state" واستخدامها لإنشاء كائن "numpy.random.RandomState". راجع: func:`sklearn.utils.check_random_state` في: ref:`developers-utils`.

فيما يلي مثال بسيط للكود الذي يستخدم بعض الإرشادات الموضحة أعلاه::

    from sklearn.utils import check_array, check_random_state

    def choose_random_sample(X, random_state=0):
        """Choose a random point from X.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            An array representing the data.
        random_state : int or RandomState instance, default=0
            The seed of the pseudo random number generator that selects a
            random sample. Pass an int for reproducible output across multiple
            function calls.
            See :term:`Glossary <random_state>`.

        Returns
        -------
        x : ndarray of shape (n_features,)
            A random point selected from X.
        """
        X = check_array(X)
        random_state = check_random_state(random_state)
        i = random_state.randint(X.shape[0])
        return X[i]

إذا كنت تستخدم العشوائية في مقدر بدلاً من دالة مستقلة، فتنطبق بعض الإرشادات الإضافية.

أولاً، يجب أن يأخذ المقدر وسيط "random_state" في "__init__" مع قيمة افتراضية "None". يجب أن يقوم بتخزين قيمة وسيطه، **بدون تعديل**، في سمة "random_state". يمكن أن يستدعي "fit" "check_random_state" على هذه السمة للحصول على مولد أرقام عشوائية حقيقي. إذا كانت هناك حاجة إلى العشوائية بعد "fit"، فيجب تخزين مولد الأرقام العشوائية في سمة "random_state_". يجب أن يوضح المثال التالي هذا::

    class GaussianNoise(BaseEstimator, TransformerMixin):
        """This estimator ignores its input and returns random Gaussian noise.

        It also does not adhere to all scikit-learn conventions,
        but showcases how to handle randomness.
        """

        def __init__(self, n_components=100, random_state=None):
            self.random_state = random_state
            self.n_components = n_components

        # the arguments are ignored anyway, so we make them optional
        def fit(self, X=None, y=None):
            self.random_state_ = check_random_state(self.random_state)

        def transform(self, X):
            n_samples = X.shape[0]
            return self.random_state_.randn(n_samples, self.n_components)

والسبب في هذا الإعداد هو إمكانية إعادة الإنتاج: عندما يتم "تناسب" المقدر مرتين مع نفس البيانات، يجب أن ينتج نموذجًا متطابقًا في كلتا الحالتين، وبالتالي يتم التحقق من الصحة في "fit"، وليس "__init__".

التأكيدات العددية في الاختبارات
-----------------------------

عند التأكيد على تكافؤ المصفوفات تقريبًا، استخدم "sklearn.utils._testing.assert_allclose".

يتم استنتاج التسامح النسبي تلقائيًا من مصفوفات dtypes المقدمة (بالنسبة إلى أنواع float32 وfloat64 على وجه الخصوص) ولكن يمكنك تجاوزها عبر "rtol".

عند مقارنة المصفوفات ذات العناصر الصفرية، يرجى توفير قيمة غير صفرية للتسامح المطلق عبر "atol".

لمزيد من المعلومات، يرجى الرجوع إلى سلسلة وثائق "sklearn.utils._testing.assert_allclose".