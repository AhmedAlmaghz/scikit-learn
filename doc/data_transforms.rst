.. _data-transforms:

تحويلات مجموعة البيانات
-----------------------

يوفر scikit-learn مكتبة من المحولات التي يمكنها تنظيف (راجع :ref:`preprocessing`) أو تقليل (راجع :ref:`data_reduction`) أو توسيع (راجع :ref:`kernel_approximation`) أو إنشاء (راجع :ref:`feature_extraction`) تمثيلات الخصائص.

مثل التقديرات الأخرى، يتم تمثيل هذه التقديرات بواسطة فئات مع طريقة ``fit``، والتي تتعلم معلمات النموذج (مثل المتوسط والانحراف المعياري للتوحيد) من مجموعة تدريب، وطريقة ``transform`` التي تطبق نموذج التحول هذا على البيانات غير المرئية. قد يكون ``fit_transform`` أكثر ملاءمة وكفاءة لنمذجة البيانات التدريبية وتحويلها في نفس الوقت.

يتم تغطية دمج مثل هذه المحولات، إما بالتوازي أو بالتسلسل، في :ref:`combining_estimators`. يغطي :ref:`metrics` تحويل مساحات الميزة إلى مصفوفات التشابه، في حين أن :ref:`preprocessing_targets` ينظر في تحويلات مساحة الهدف (على سبيل المثال، العلامات الفئوية) للاستخدام في scikit-learn.

.. toctree::
    :maxdepth: 2

    modules/compose
    modules/feature_extraction
    modules/preprocessing
    modules/impute
    modules/unsupervised_reduction
    modules/random_projection
    modules/kernel_approximation
    modules/metrics
    modules/preprocessing_targets