.. _learning_curves:

=====================================================
منحنيات التحقق: رسم الدرجات لتقييم النماذج
=====================================================

.. currentmodule:: sklearn.model_selection

كل خوارزمية تقدير لها مزايا وعيوب. يمكن تحليل خطأ التعميم
من حيث الانحياز والتشتت والضوضاء. **انحياز** خوارزمية التقدير هو متوسط خطأها لمجموعات التدريب المختلفة. يشير **تشتت**
خوارزمية التقدير إلى مدى حساسيتها لمجموعات التدريب المختلفة. الضوضاء هي خاصية البيانات.

في المخطط التالي، نرى دالة :math:`f(x) = \cos (\frac{3}{2} \pi x)`
وبعض العينات المشوشة من تلك الدالة. نستخدم ثلاث خوارزميات تقدير مختلفة
لتناسب الدالة: الانحدار الخطي مع ميزات متعددة الحدود من الدرجة 1،
4 و15. نرى أن أول خوارزمية تقدير لا يمكنها سوى توفير ملاءمة سيئة
للعينات والدالة الحقيقية لأنها بسيطة للغاية (انحياز مرتفع)،
تقريب خوارزمية التقدير الثانية تقريبًا بشكل مثالي وآخر
تقريب خوارزمية التقدير البيانات التدريبية بشكل مثالي ولكنها لا تناسب الدالة الحقيقية
جيدًا، أي أنها حساسة جدًا لبيانات التدريب المتغيرة (تشتت مرتفع).

.. figure:: ../auto_examples/model_selection/images/sphx_glr_plot_underfitting_overfitting_001.png
   :target: ../auto_examples/model_selection/plot_underfitting_overfitting.html
   :align: center
   :scale: 50%

الانحياز والتشتت هما خصائص متأصلة في خوارزميات التقدير وعلينا عادةً اختيار
خوارزميات التعلم وفرط المعلمات بحيث يكون الانحياز والتشتت منخفضين قدر الإمكان (انظر `معضلة الانحياز-التشتت
<https://en.wikipedia.org/wiki/Bias-variance_dilemma>`_). هناك طريقة أخرى لتقليل
تشتت النموذج هي استخدام المزيد من بيانات التدريب. ومع ذلك، يجب عليك فقط
جمع المزيد من بيانات التدريب إذا كانت الدالة الحقيقية معقدة للغاية بحيث لا يمكن
تقريبها بواسطة خوارزمية تقدير ذات تشتت أقل.

في المشكلة الأحادية البعد البسيطة التي رأيناها في المثال، من السهل
أن نرى ما إذا كانت خوارزمية التقدير تعاني من الانحياز أو التشتت. ومع ذلك، في
الأبعاد العالية، يمكن أن تصبح النماذج صعبة للغاية في التصور. لهذا السبب،
من المفيد غالبًا استخدام الأدوات الموضحة أدناه.

.. rubric:: أمثلة

* :ref:`sphx_glr_auto_examples_model_selection_plot_underfitting_overfitting.py`
* :ref:`sphx_glr_auto_examples_model_selection_plot_validation_curve.py`
* :ref:`sphx_glr_auto_examples_model_selection_plot_learning_curve.py`


.. _validation_curve:

منحنى التحقق
================

لتحقق من صحة نموذج، نحتاج إلى دالة تسجيل (راجع :ref:`model_evaluation`)،
على سبيل المثال الدقة للتصنيف. الطريقة الصحيحة لاختيار فرط معلمات متعددة
من خوارزمية التقدير هي بالطبع البحث الشبكي أو طرق مماثلة (راجع :ref:`grid_search`)
التي تحدد فرط المعلمة ذات الدرجة القصوى على مجموعة تحقق واحدة أو أكثر. لاحظ أنه إذا قمنا بتحسين
فرط المعلمات بناءً على درجة التحقق، فإن درجة التحقق متحيزة
وليس تقديرًا جيدًا للتعميم بعد الآن. للحصول على تقدير صحيح للتعميم، يجب علينا حساب الدرجة على مجموعة اختبار أخرى.

ومع ذلك، فمن المفيد أحيانًا رسم تأثير فرط معلمة واحدة على درجة التدريب ودرجة التحقق لمعرفة ما إذا كانت
خوارزمية التقدير مفرطة أو ناقصة التحديد لبعض قيم فرط المعلمات.

يمكن أن تساعد دالة :func:`validation_curve` في هذه الحالة::

  >>> import numpy as np
  >>> from sklearn.model_selection import validation_curve
  >>> from sklearn.datasets import load_iris
  >>> from sklearn.svm import SVC

  >>> np.random.seed(0)
  >>> X, y = load_iris(return_X_y=True)
  >>> indices = np.arange(y.shape[0])
  >>> np.random.shuffle(indices)
  >>> X, y = X[indices], y[indices]

  >>> train_scores, valid_scores = validation_curve(
  ...     SVC(kernel="linear"), X, y, param_name="C", param_range=np.logspace(-7, 3, 3),
  ... )
  >>> train_scores
  array([[0.90..., 0.94..., 0.91..., 0.89..., 0.92...],
         [0.9... , 0.92..., 0.93..., 0.92..., 0.93...],
         [0.97..., 1...   , 0.98..., 0.97..., 0.99...]])
  >>> valid_scores
  array([[0.9..., 0.9... , 0.9... , 0.96..., 0.9... ],
         [0.9..., 0.83..., 0.96..., 0.96..., 0.93...],
         [1.... , 0.93..., 1....  , 1....  , 0.9... ]])

إذا كنت تنوي رسم منحنيات التحقق فقط، فإن الفئة
:class:`~sklearn.model_selection.ValidationCurveDisplay` أكثر مباشرة من
استخدام matplotlib يدويًا على نتائج مكالمة إلى :func:`validation_curve`.
يمكنك استخدام الأسلوب
:meth:`~sklearn.model_selection.ValidationCurveDisplay.from_estimator` بشكل مشابه
إلى :func:`validation_curve` لتوليد ورسم منحنى التحقق:

.. plot::
   :context: close-figs
   :align: center

      from sklearn.datasets import load_iris
      from sklearn.model_selection import ValidationCurveDisplay
      from sklearn.svm import SVC
      from sklearn.utils import shuffle
      X, y = load_iris(return_X_y=True)
      X, y = shuffle(X, y, random_state=0)
      ValidationCurveDisplay.from_estimator(
         SVC(kernel="linear"), X, y, param_name="C", param_range=np.logspace(-7, 3, 10)
      )

إذا كانت درجة التدريب ودرجة التحقق منخفضة، فستكون خوارزمية التقدير ناقصة التحديد. إذا كانت درجة التدريب مرتفعة ودرجة التحقق منخفضة،
فإن خوارزمية التقدير مفرطة في التحديد وإلا فهي تعمل بشكل جيد جدًا. من غير الممكن عادةً الحصول على درجة تدريب منخفضة ودرجة تحقق عالية. نقص التحديد،
فرط التحديد، ونموذج العمل موضح في المخطط أدناه حيث نغير
معلمة `gamma` لخوارزمية SVM ذات نواة RBF على مجموعة بيانات الأرقام.

.. figure:: ../auto_examples/model_selection/images/sphx_glr_plot_validation_curve_001.png
   :target: ../auto_examples/model_selection/plot_validation_curve.html
   :align: center
   :scale: 50%

.. _learning_curve:

منحنى التعلم
==============

يظهر منحنى التعلم درجات التحقق والتدريب لخوارزمية تقدير
لأعداد متنوعة من عينات التدريب. إنها أداة لمعرفة مدى استفادتنا من إضافة المزيد من بيانات التدريب وما إذا كانت خوارزمية التقدير تعاني
من خطأ التباين أو خطأ الانحياز. ضع في اعتبارك المثال التالي حيث نرسم منحنى التعلم لخوارزمية بايز البسيط وخوارزمية SVM.

بالنسبة لخوارزمية بايز البسيطة، تتقارب كل من درجة التحقق ودرجة التدريب
إلى قيمة منخفضة جدًا مع زيادة حجم مجموعة التدريب. وبالتالي، فمن المحتمل ألا نستفيد كثيرًا من المزيد من بيانات التدريب.

على النقيض من ذلك، بالنسبة لكميات صغيرة من البيانات، تكون درجة التدريب لخوارزمية SVM
أكبر بكثير من درجة التحقق. من المحتمل أن يؤدي إضافة المزيد من عينات التدريب إلى زيادة التعميم.

.. figure:: ../auto_examples/model_selection/images/sphx_glr_plot_learning_curve_001.png
   :target: ../auto_examples/model_selection/plot_learning_curve.html
   :align: center
   :scale: 50%

يمكننا استخدام دالة :func:`learning_curve` لتوليد القيم
اللازمة لرسم مثل هذا المنحنى التعليمي (عدد العينات
التي تم استخدامها، متوسط الدرجات على مجموعات التدريب و
متوسط الدرجات على مجموعات التحقق)::

  >>> from sklearn.model_selection import learning_curve
  >>> from sklearn.svm import SVC

  >>> train_sizes, train_scores, valid_scores = learning_curve(
  ...     SVC(kernel='linear'), X, y, train_sizes=[50, 80, 110], cv=5)
  >>> train_sizes
  array([ 50, 80, 110])
  >>> train_scores
  array([[0.98..., 0.98 , 0.98..., 0.98..., 0.98...],
         [0.98..., 1.   , 0.98..., 0.98..., 0.98...],
         [0.98..., 1.   , 0.98..., 0.98..., 0.99...]])
  >>> valid_scores
  array([[1. ,  0.93...,  1. ,  1. ,  0.96...],
         [1. ,  0.96...,  1. ,  1. ,  0.96...],
         [1. ,  0.96...,  1. ,  1. ,  0.96...]])

إذا كنت تنوي رسم منحنيات التعلم فقط، فإن الفئة
:class:`~sklearn.model_selection.LearningCurveDisplay` ستكون أسهل في الاستخدام.
يمكنك استخدام الأسلوب
:meth:`~sklearn.model_selection.LearningCurveDisplay.from_estimator` بشكل مشابه
إلى :func:`learning_curve` لتوليد ورسم منحنى التعلم:

.. plot::
   :context: close-figs
   :align: center

      from sklearn.datasets import load_iris
      from sklearn.model_selection import LearningCurveDisplay
      from sklearn.svm import SVC
      from sklearn.utils import shuffle
      X, y = load_iris(return_X_y=True)
      X, y = shuffle(X, y, random_state=0)
      LearningCurveDisplay.from_estimator(
         SVC(kernel="linear"), X, y, train_sizes=[50, 80, 110], cv=5)