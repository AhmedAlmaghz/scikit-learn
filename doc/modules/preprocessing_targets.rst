.. currentmodule:: sklearn.preprocessing

.. _preprocessing_targets:

==========================================
تحويل هدف التنبؤ (``y``)
==========================================

هذه هي المحولات التي لا يقصد استخدامها على الميزات، ولكن فقط على أهداف التعلم الخاضع للإشراف. راجع أيضًا :ref:`transformed_target_regressor` إذا كنت تريد تحويل هدف التنبؤ للتعلم، ولكن تقييم النموذج في المجال الأصلي (غير المحول).

تثبيت التسمية
==================

LabelBinarizer
--------------

:class:`LabelBinarizer` هي فئة مساعدة لإنشاء مصفوفة مؤشرات التسمية من قائمة تسميات متعددة الفئات::

    >>> from sklearn import preprocessing
    >>> lb = preprocessing.LabelBinarizer()
    >>> lb.fit([1, 2, 6, 4, 2])
    LabelBinarizer()
    >>> lb.classes_
    array([1, 2, 4, 6])
    >>> lb.transform([1, 6])
    array([[1, 0, 0, 0],
           [0, 0, 0, 1]])

يمكن أن يمكّن استخدام هذا التنسيق التصنيف متعدد الفئات في المقدرات التي تدعم تنسيق مصفوفة مؤشر التسمية.

.. warning::

    لا يلزم استخدام LabelBinarizer إذا كنت تستخدم مقدرًا يدعم بالفعل بيانات متعددة الفئات.

للحصول على مزيد من المعلومات حول التصنيف متعدد الفئات، راجع :ref:`multiclass_classification`.

MultiLabelBinarizer
-------------------

في التعلم متعدد التصنيفات، يتم التعبير عن المجموعة المشتركة من مهام التصنيف الثنائية باستخدام مصفوفة مؤشرات التصنيف الثنائية: كل عينة عبارة عن صف واحد من مصفوفة ثنائية الأبعاد ذات شكل (n_samples، n_classes) مع قيم ثنائية حيث الرقم 1، أي العناصر غير الصفرية، يقابل مجموعة التصنيفات لتلك العينة. تمثل مصفوفة مثل ``np.array([[1, 0, 0], [0, 1, 1], [0, 0, 0]])`` التصنيف 0 في العينة الأولى، والتصنيفين 1 و2 في العينة الثانية، ولا توجد تصنيفات في العينة الثالثة.

قد يكون إنتاج بيانات متعددة التصنيفات على شكل قائمة مجموعات من التصنيفات أكثر بديهية. يمكن استخدام محول :class:`MultiLabelBinarizer <sklearn.preprocessing.MultiLabelBinarizer>` لتحويل البيانات بين مجموعة من مجموعات التصنيفات وتنسيق المؤشرات::

    >>> from sklearn.preprocessing import MultiLabelBinarizer
    >>> y = [[2, 3, 4], [2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2]]
    >>> MultiLabelBinarizer().fit_transform(y)
    array([[0, 0, 1, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 1, 0, 1, 0],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 0, 0]])

للحصول على مزيد من المعلومات حول التصنيف متعدد التصنيفات، راجع :ref:`multilabel_classification`.

الترميز التصنيفي
==============

:class:`LabelEncoder` هي فئة مساعدة لتطبيع التسميات بحيث تحتوي فقط على قيم بين 0 وn_classes-1. قد يكون هذا مفيدًا في بعض الأحيان لكتابة روتينات Cython الفعالة. يمكن استخدام :class:`LabelEncoder` كما يلي::

    >>> from sklearn import preprocessing
    >>> le = preprocessing.LabelEncoder()
    >>> le.fit([1, 2, 2, 6])
    LabelEncoder()
    >>> le.classes_
    array([1, 2, 6])
    >>> le.transform([1, 1, 2, 6])
    array([0, 0, 1, 2])
    >>> le.inverse_transform([0, 0, 1, 2])
    array([1, 1, 2, 6])

يمكن استخدامه أيضًا لتحويل التسميات غير الرقمية (طالما أنها قابلة للتجزئة وقابلة للمقارنة) إلى تسميات رقمية::

    >>> le = preprocessing.LabelEncoder()
    >>> le.fit(["paris", "paris", "tokyo", "amsterdam"])
    LabelEncoder()
    >>> list(le.classes_)
    ['amsterdam', 'paris', 'tokyo']
    >>> le.transform(["tokyo", "tokyo", "paris"])
    array([2, 2, 1])
    >>> list(le.inverse_transform([2, 2, 1]))
    ['tokyo', 'tokyo', 'paris']