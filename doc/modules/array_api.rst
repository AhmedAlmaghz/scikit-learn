هذا النص هو جزء من وثائق Scikit-learn، وهو مكتبة للتعلم الآلي في بايثون. يشرح النص دعم Scikit-learn لمواصفات Array API، والتي توفر واجهة برمجة تطبيقات (API) قياسية لمكتبات التعامل مع المصفوفات التي تشبه NumPy.

دعم واجهة برمجة تطبيقات المصفوفة (تجريبي)
===========================================

تحدد مواصفات واجهة برمجة تطبيقات المصفوفة (Array API) واجهة برمجة تطبيقات قياسية لجميع مكتبات التعامل مع المصفوفات التي تشبه NumPy. يتطلب دعم Scikit-learn لبرنامج Array API تثبيت برنامج "array-api-compat".

يمكن تكوين بعض أدوات التقدير في Scikit-learn التي تعتمد بشكل أساسي على NumPy (بدلاً من استخدام Cython) لتنفيذ المنطق الحسابي لأساليبها في التهيئة والتنبؤ والتحويل لقبول أي هياكل بيانات متوافقة مع واجهة برمجة تطبيقات المصفوفة، وإرسال العمليات تلقائيًا إلى مساحة الاسم الأساسية بدلاً من الاعتماد على NumPy.

في هذه المرحلة، يُعتبر هذا الدعم **تجريبيًا** ويجب تمكينه بشكل صريح كما هو موضح أدناه.

ملاحظة:
في الوقت الحالي، من المعروف أن "array-api-strict" و "cupy" و "PyTorch" تعمل مع أدوات التقدير في Scikit-learn.

مثال الاستخدام
===============

فيما يلي مقتطف من التعليمات البرمجية يوضح كيفية استخدام CuPy لتشغيل LinearDiscriminantAnalysis على وحدة معالجة الرسومات (GPU)::

    >>> from sklearn.datasets import make_classification
    >>> from sklearn import config_context
    >>> from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    >>> import cupy

    >>> X_np, y_np = make_classification(random_state=0)
    >>> X_cu = cupy.asarray(X_np)
    >>> y_cu = cupy.asarray(y_np)
    >>> X_cu.device
    <CUDA Device 0>

    >>> with config_context(array_api_dispatch=True):
    ...     lda = LinearDiscriminantAnalysis()
    ...     X_trans = lda.fit_transform(X_cu, y_cu)
    >>> X_trans.device
    <CUDA Device 0>

بعد تدريب النموذج، ستكون السمات المناسبة التي تكون مصفوفات أيضًا من نفس مساحة اسم واجهة برمجة تطبيقات المصفوفة الخاصة ببيانات التدريب. على سبيل المثال، إذا تم استخدام مساحة اسم واجهة برمجة تطبيقات CuPy للتدريب، فستكون السمات المناسبة على وحدة معالجة الرسومات (GPU). نوفر مرفقًا تجريبيًا يسمى "_estimator_with_converted_arrays" يقوم بنقل سمات أداة التقدير من واجهة برمجة تطبيقات المصفوفة إلى مصفوفة ndarray::

    >>> from sklearn.utils._array_api import _estimator_with_converted_arrays
    >>> cupy_to_ndarray = lambda array : array.get()
    >>> lda_np = _estimator_with_converted_arrays(lda, cupy_to_ndarray)
    >>> X_trans = lda_np.transform(X_np)
    >>> type(X_trans)
    <class 'numpy.ndarray'>

دعم PyTorch
------------

يتم دعم PyTorch Tensors من خلال تعيين "array_api_dispatch=True" وإدخال المنسوجات مباشرةً::

    >>> import torch
    >>> X_torch = torch.asarray(X_np, device="cuda", dtype=torch.float32)
    >>> y_torch = torch.asarray(y_np, device="cuda", dtype=torch.float32)

    >>> with config_context(array_api_dispatch=True):
    ...     lda = LinearDiscriminantAnalysis()
    ...     X_trans = lda.fit_transform(X_torch, y_torch)
    >>> type(X_trans)
    <class 'torch.Tensor'>
    >>> X_trans.device.type
    'cuda'

الدعم لمدخلات متوافقة مع واجهة برمجة تطبيقات المصفوفة
=================================================

أدوات التقدير والأدوات الأخرى في Scikit-learn التي تدعم المدخلات المتوافقة مع واجهة برمجة تطبيقات المصفوفة.

أدوات التقدير
----------

- :class:`decomposition.PCA` (مع `svd_solver="full"`، و`svd_solver="randomized"` و`power_iteration_normalizer="QR"`)
- :class:`linear_model.Ridge` (مع `solver="svd"`)
- :class:`discriminant_analysis.LinearDiscriminantAnalysis` (مع `solver="svd"`)
- :class:`preprocessing.KernelCenterer`
- :class:`preprocessing.MaxAbsScaler`
- :class:`preprocessing.MinMaxScaler`
- :class:`preprocessing.Normalizer`

أدوات التقدير الفوقية
---------------

أدوات التقدير الفوقية التي تقبل مدخلات واجهة برمجة تطبيقات المصفوفة بشرط أن تفعل أداة التقدير الأساسية ذلك:

- :class:`model_selection.GridSearchCV`
- :class:`model_selection.RandomizedSearchCV`
- :class:`model_selection.HalvingGridSearchCV`
- :class:`model_selection.HalvingRandomSearchCV`

المقاييس
-------

- :func:`sklearn.metrics.cluster.entropy`
- :func:`sklearn.metrics.accuracy_score`
- :func:`sklearn.metrics.d2_tweedie_score`
- :func:`sklearn.metrics.max_error`
- :func:`sklearn.metrics.mean_absolute_error`
- :func:`sklearn.metrics.mean_absolute_percentage_error`
- :func:`sklearn.metrics.mean_gamma_deviance`
- :func:`sklearn.metrics.mean_poisson_deviance` (يتطلب تمكين دعم واجهة برمجة تطبيقات المصفوفة لـ SciPy)
- :func:`sklearn.metrics.mean_squared_error`
- :func:`sklearn.metrics.mean_tweedie_deviance`
- :func:`sklearn.metrics.pairwise.additive_chi2_kernel`
- :func:`sklearn.metrics.pairwise.chi2_kernel`
- :func:`sklearn.metrics.pairwise.cosine_similarity`
- :func:`sklearn.metrics.pairwise.cosine_distances`
- :func:`sklearn.metrics.pairwise.euclidean_distances` (راجع قسم "device_support_for_float64")
- :func:`sklearn.metrics.pairwise.paired_cosine_distances`
- :func:`sklearn.metrics.pairwise.paired_euclidean_distances`
- :func:`sklearn.metrics.pairwise.rbf_kernel` (راجع قسم "device_support_for_float64")
- :func:`sklearn.metrics.r2_score`
- :func:`sklearn.metrics.zero_one_loss`

الأدوات
-----

- :func:`model_selection.train_test_split`

من المتوقع أن تزداد التغطية بمرور الوقت. يرجى متابعة المشكلة المخصصة على GitHub لتتبع التقدم.

نوع قيم الإرجاع والسمات المناسبة
-------------------------------------------

عند استدعاء الدوال أو الأساليب مع مدخلات متوافقة مع واجهة برمجة تطبيقات المصفوفة، تكون الاتفاقية هي إرجاع قيم المصفوفة من نفس نوع حاوية المصفوفة والجهاز مثل بيانات الإدخال.

بالمثل، عندما يتم تكييف أداة التقدير مع مدخلات متوافقة مع واجهة برمجة تطبيقات المصفوفة، ستكون السمات المناسبة مصفوفات من نفس المكتبة مثل الإدخال ويتم تخزينها على نفس الجهاز. تتوقع أساليب "التنبؤ" و"التحويل" بعد ذلك إدخالات من نفس مكتبة المصفوفات والجهاز مثل البيانات التي تم تمريرها إلى طريقة "التهيئة".

لاحظ، مع ذلك، أن دالات التسجيل التي تعيد قيمًا قياسية تعيد قيمًا قياسية من Python (عادةً مثيل "float") بدلاً من قيمة قياسية للمصفوفة.

فحوصات أداة التقدير الشائعة
=======================

أضف علامة "array_api_support" إلى مجموعة العلامات الخاصة بأداة التقدير للإشارة إلى أنها تدعم واجهة برمجة تطبيقات المصفوفة. سيمكن ذلك الفحوصات المخصصة كجزء من الاختبارات الشائعة للتحقق من أن نتائج أداة التقدير متطابقة عند استخدام مدخلات NumPy العادية ومدخلات واجهة برمجة تطبيقات المصفوفة.

لتشغيل هذه الفحوصات، تحتاج إلى تثبيت "array_api_compat" في بيئة الاختبار الخاصة بك. لتشغيل المجموعة الكاملة من الفحوصات، تحتاج إلى تثبيت كل من "PyTorch" و"CuPy" وامتلاك وحدة معالجة الرسومات (GPU). سيتم تخطي الفحوصات التي لا يمكن تنفيذها أو التي بها تبعيات مفقودة تلقائيًا. لذلك من المهم تشغيل الاختبارات باستخدام علم "-v" لمعرفة الفحوصات التي يتم تخطيها:

.. prompt:: bash $

    pip install array-api-compat  # والمكتبات الأخرى حسب الحاجة
    pytest -k "array_api" -v

ملاحظة حول دعم جهاز MPS
--------------------------

في macOS، يمكن لـ PyTorch استخدام Metal Performance Shaders (MPS) للوصول إلى المعجلات (مثل مكون وحدة معالجة الرسومات (GPU) الداخلي لشريحة M1 أو M2). ومع ذلك، فإن دعم جهاز MPS لـ PyTorch غير مكتمل في وقت الكتابة. راجع مشكلة GitHub التالية للحصول على مزيد من التفاصيل:

- https://github.com/pytorch/pytorch/issues/77764

لتمكين دعم MPS في PyTorch، قم بتعيين متغير البيئة "PYTORCH_ENABLE_MPS_FALLBACK=1" قبل تشغيل الاختبارات:

.. prompt:: bash $

    PYTORCH_ENABLE_MPS_FALLBACK=1 pytest -k "array_api" -v

في وقت الكتابة، يجب أن تنجح جميع اختبارات Scikit-learn، ومع ذلك، فإن السرعة الحسابية ليست بالضرورة أفضل من جهاز CPU.

ملاحظة حول دعم الجهاز لـ "float64"
--------------------------------------

ستقوم بعض العمليات داخل Scikit-learn تلقائيًا بتنفيذ العمليات على القيم ذات الدقة العائمة "float64" لمنع حدوث فيضانات وضمان الدقة (على سبيل المثال، :func:`metrics.pairwise.euclidean_distances`). ومع ذلك، فإن بعض مجموعات مساحات أسماء المصفوفات والأجهزة، مثل "PyTorch on MPS" (راجع قسم "mps_support")، لا تدعم نوع البيانات "float64". في هذه الحالات، سيتم الرجوع إلى استخدام نوع البيانات "float32" بدلاً من ذلك. قد يؤدي ذلك إلى حدوث سلوك مختلف (عادةً ما تكون النتائج غير مستقرة عدديًا) مقارنة بعدم استخدام إرسال واجهة برمجة تطبيقات المصفوفة أو استخدام جهاز يدعم "float64".