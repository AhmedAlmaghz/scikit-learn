هذا الفصل يشرح بعض التقنيات غير المُشرف عليها لتخفيض الأبعاد. إذا كان عدد الخصائص (الميزات) لديك كبيرًا، فقد يكون من المفيد تقليله باستخدام خطوة غير مُشرف عليها قبل الخطوات المُشرف عليها. العديد من طرق التعلم غير المُشرف عليها :ref:`unsupervised-learning` تنفذ طريقة "التحويل" :code:`transform` التي يمكن استخدامها لتخفيض الأبعاد. نناقش أدناه مثالين محددين لهذا النمط المستخدم على نطاق واسع.

**التنفيذ التتابعي**:
يمكن تنفيذ تقليل البيانات غير المُشرف عليه والمُقدر المُشرف عليه على التوالي في خطوة واحدة. راجع :ref:`pipeline`.

PCA: التحليل التكويني الرئيسي
-----------------------------

تبحث :class:`decomposition.PCA` عن مجموعة من الميزات التي تلتقط جيدًا تباين الميزات الأصلية. راجع :ref:`decompositions`.

**أمثلة**:
* :ref:`sphx_glr_auto_examples_applications_plot_face_recognition.py`

الإسقاطات العشوائية
---------------------

يوفر الوحدة النمطية :mod:`~sklearn.random_projection` عدة أدوات لتخفيض البيانات من خلال الإسقاطات العشوائية. راجع قسم الوثائق ذي الصلة: :ref:`random_projection`.

**أمثلة**:
* :ref:`sphx_glr_auto_examples_miscellaneous_plot_johnson_lindenstrauss_bound.py`

تجمع الميزات
----------------

يطبق :class:`cluster.FeatureAgglomeration` التجميع الهرمي لجمع الميزات التي تتصرف بشكل مشابه.

**أمثلة**:
* :ref:`sphx_glr_auto_examples_cluster_plot_feature_agglomeration_vs_univariate_selection.py`
* :ref:`sphx_glr_auto_examples_cluster_plot_digits_agglomeration.py`

**مقياس الميزة**:

لاحظ أنه إذا كانت الميزات ذات مقاييس أو خصائص إحصائية مختلفة جدًا، فقد لا يتمكن :class:`cluster.FeatureAgglomeration` من التقاط الروابط بين الميزات ذات الصلة. قد يكون استخدام :class:`preprocessing.StandardScaler` مفيدًا في هذه الحالات.