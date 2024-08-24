.. _visualizations:

===============
التمثيل المرئي
===============

يحدد Scikit-learn واجهة برمجة تطبيقات (API) بسيطة لإنشاء التمثيلات المرئية لتعلم الآلة. الميزة الرئيسية لواجهة برمجة التطبيقات هذه هي السماح بالضبط المرئي والرسوم البيانية السريعة دون إعادة الحساب. نوفر فئات "العرض" التي تعرض طريقتين لإنشاء الرسوم البيانية: "from_estimator" و "from_predictions". ستأخذ طريقة "from_estimator" مصنفًا ملائمًا وبعض البيانات ("X" و "y") وتنشئ كائن "عرض". في بعض الأحيان، قد نرغب في حساب التوقعات مرة واحدة فقط، وفي هذه الحالة يجب استخدام "from_predictions" بدلاً من ذلك. في المثال التالي، نقوم برسم منحنى ROC لآلة ناقلات الدعم الملائمة:

.. plot::
   :context: close-figs
   :align: center

    from sklearn.model_selection import train_test_split
    from sklearn.svm import SVC
    from sklearn.metrics import RocCurveDisplay
    from sklearn.datasets import load_wine

    X, y = load_wine(return_X_y=True)
    y = y == 2  # جعل البيانات ثنائية التصنيف
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    svc = SVC(random_state=42)
    svc.fit(X_train, y_train)

    svc_disp = RocCurveDisplay.from_estimator(svc, X_test, y_test)

يسمح كائن "svc_disp" الذي تم إرجاعه لنا بمواصلة استخدام منحنى ROC المحسوب بالفعل لآلة ناقلات الدعم في الرسوم البيانية المستقبلية. في هذه الحالة، "svc_disp" هو :class:`~sklearn.metrics.RocCurveDisplay` الذي يخزن القيم المحسوبة كسمات تسمى "roc_auc" و "fpr" و "tpr". لاحظ أنه كان بإمكاننا الحصول على التوقعات من آلة ناقلات الدعم ثم استخدام "from_predictions" بدلاً من "from_estimator". بعد ذلك، نقوم بتدريب مصنف غابة عشوائي ونرسم مرة أخرى منحنى ROC المحسوب مسبقًا باستخدام طريقة "plot" لكائن "العرض".

.. plot::
   :context: close-figs
   :align: center

    import matplotlib.pyplot as plt
    from sklearn.ensemble import RandomForestClassifier

    rfc = RandomForestClassifier(n_estimators=10, random_state=42)
    rfc.fit(X_train, y_train)

    ax = plt.gca()
    rfc_disp = RocCurveDisplay.from_estimator(rfc, X_test, y_test, ax=ax, alpha=0.8)
    svc_disp.plot(ax=ax, alpha=0.8)

لاحظ أننا نمرر "alpha=0.8" إلى دالات الرسم لتعديل قيم ألفا للمنحنيات.

.. rubric:: أمثلة

* :ref:`sphx_glr_auto_examples_miscellaneous_plot_roc_curve_visualization_api.py`
* :ref:`sphx_glr_auto_examples_miscellaneous_plot_partial_dependence_visualization_api.py`
* :ref:`sphx_glr_auto_examples_miscellaneous_plot_display_object_visualization.py`
* :ref:`sphx_glr_auto_examples_calibration_plot_compare_calibration.py`

أدوات الرسوم البيانية المتاحة
============================

كائنات العرض
---------------

.. currentmodule:: sklearn

.. autosummary::

   calibration.CalibrationDisplay
   inspection.PartialDependenceDisplay
   inspection.DecisionBoundaryDisplay
   metrics.ConfusionMatrixDisplay
   metrics.DetCurveDisplay
   metrics.PrecisionRecallDisplay
   metrics.PredictionErrorDisplay
   metrics.RocCurveDisplay
   model_selection.LearningCurveDisplay
   model_selection.ValidationCurveDisplay

آمل أن تكون هذه الترجمة مفيدة! إذا كانت هناك أي مصطلحات محددة في النص الأصلي تفضل أن تظل باللغة الإنجليزية، فيرجى إبلاغي بذلك، وسأحرص على تضمينها في الترجمة.