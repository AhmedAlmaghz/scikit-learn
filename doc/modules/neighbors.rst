
.. _neighbors:

=================
أقرب الجيران
=================

.. sectionauthor:: Jake Vanderplas <vanderplas@astro.washington.edu>

.. currentmodule:: sklearn.neighbors

يُوفر :mod:`sklearn.neighbors` وظائف لأساليب التعلم غير الخاضعة للإشراف والخاضعة للإشراف القائمة على الجيران. يُعد أقرب الجيران غير الخاضع للإشراف أساسًا للعديد من أساليب التعلم الأخرى، ولا سيما تعلم المشعبات والتجميع الطيفي. يأتي التعلم الخاضع للإشراف القائم على الجيران بنكهتين: `التصنيف`_ للبيانات ذات التسميات المنفصلة، و `الانحدار`_ للبيانات ذات التسميات المستمرة.

المبدأ وراء أساليب أقرب الجيران هو إيجاد عدد مُحدّد مسبقًا من عينات التدريب الأقرب في المسافة إلى النقطة الجديدة، والتنبؤ بالتسمية من هذه العينات. يمكن أن يكون عدد العينات ثابتًا مُحدّدًا من قبل المستخدم (تعلم أقرب k جيران)، أو يختلف بناءً على الكثافة المحلية للنقاط (تعلم الجيران القائم على نصف القطر). يمكن أن تكون المسافة، بشكل عام، أي قياس متري: مسافة إقليدية القياسية هي الخيار الأكثر شيوعًا. تُعرف أساليب التعلم القائمة على الجيران باسم أساليب تعلم الآلة *غير المُعمّمة*، لأنها ببساطة "تتذكر" جميع بيانات التدريب الخاصة بها (ربما يتم تحويلها إلى بنية فهرسة سريعة مثل :ref:`شجرة الكرة <ball_tree>` أو :ref:`شجرة KD <kd_tree>`).

على الرغم من بساطتها، فقد نجح أقرب الجيران في عدد كبير من مشاكل التصنيف والانحدار، بما في ذلك الأرقام المكتوبة بخط اليد ومشاهد صور الأقمار الصناعية. نظرًا لكونها طريقة غير معلمية، فإنها غالبًا ما تنجح في حالات التصنيف حيث يكون حد القرار غير منتظم للغاية.

يمكن للفئات في :mod:`sklearn.neighbors` معالجة مصفوفات NumPy أو مصفوفات `scipy.sparse` كمدخلات. بالنسبة للمصفوفات الكثيفة، يتم دعم عدد كبير من مقاييس المسافة الممكنة. بالنسبة للمصفوفات المتفرقة، يتم دعم مقاييس مينكوفسكي التعسفية للبحث.

هناك العديد من إجراءات التعلم التي تعتمد على أقرب الجيران في جوهرها. أحد الأمثلة هو :ref:`تقدير كثافة النواة <kernel_density>`، الذي تمت مناقشته في قسم :ref:`تقدير الكثافة <density_estimation>`.


.. _unsupervised_neighbors:

أقرب جيران غير خاضع للإشراف
==============================

:class:`NearestNeighbors` تُطبق تعلم أقرب جيران غير خاضع للإشراف. تعمل كواجهة موحدة لثلاث خوارزميات مختلفة لأقرب جيران: :class:`BallTree` و :class:`KDTree` وخوارزمية القوة الغاشمة القائمة على إجراءات في :mod:`sklearn.metrics.pairwise`. يتم التحكم في اختيار خوارزمية بحث الجيران من خلال الكلمة المفتاحية ``'algorithm'``، والتي يجب أن تكون واحدة من ``['auto', 'ball_tree', 'kd_tree', 'brute']``. عندما يتم تمرير القيمة الافتراضية ``'auto'``، تحاول الخوارزمية تحديد أفضل نهج من بيانات التدريب. لمناقشة نقاط القوة والضعف لكل خيار، انظر `خوارزميات أقرب جيران`_.

.. warning::

    فيما يتعلق بخوارزميات أقرب جيران، إذا كان لدى جارين :math:`k+1` و :math:`k` مسافات متطابقة ولكن تسميات مختلفة، فستعتمد النتيجة على ترتيب بيانات التدريب.


إيجاد أقرب جيران
-----------------------------
بالنسبة للمهمة البسيطة المتمثلة في إيجاد أقرب جيران بين مجموعتين من البيانات، يمكن استخدام الخوارزميات غير الخاضعة للإشراف ضمن :mod:`sklearn.neighbors`:


    >>> from sklearn.neighbors import NearestNeighbors
    >>> import numpy as np
    >>> X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    >>> nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(X)
    >>> distances, indices = nbrs.kneighbors(X)
    >>> indices
    array([[0, 1],
           [1, 0],
           [2, 1],
           [3, 4],
           [4, 3],
           [5, 4]]...)
    >>> distances
    array([[0.        , 1.        ],
           [0.        , 1.        ],
           [0.        , 1.41421356],
           [0.        , 1.        ],
           [0.        , 1.        ],
           [0.        , 1.41421356]])


نظرًا لأن مجموعة الاستعلام تتطابق مع مجموعة التدريب، فإن أقرب جار لكل نقطة هو النقطة نفسها، على مسافة صفر.

من الممكن أيضًا إنشاء رسم بياني متفرق بكفاءة يُظهر الاتصالات بين النقاط المجاورة:

    >>> nbrs.kneighbors_graph(X).toarray()
    array([[1., 1., 0., 0., 0., 0.],
           [1., 1., 0., 0., 0., 0.],
           [0., 1., 1., 0., 0., 0.],
           [0., 0., 0., 1., 1., 0.],
           [0., 0., 0., 1., 1., 0.],
           [0., 0., 0., 0., 1., 1.]])


يتم تنظيم مجموعة البيانات بحيث تكون النقاط القريبة من ترتيب الفهرس قريبة في فضاء المعلمات، مما يؤدي إلى مصفوفة شبه قطرية تقريبًا لأقرب K جيران. هذا الرسم البياني المتفرق مفيد في مجموعة متنوعة من الظروف التي تستخدم العلاقات المكانية بين النقاط للتعلم غير الخاضع للإشراف: على وجه الخصوص، انظر :class:`~sklearn.manifold.Isomap` و :class:`~sklearn.manifold.LocallyLinearEmbedding` و :class:`~sklearn.cluster.SpectralClustering`.


فئات KDTree و BallTree
---------------------------
بدلاً من ذلك، يمكن للمرء استخدام فئات :class:`KDTree` أو :class:`BallTree` مباشرةً لإيجاد أقرب جيران. هذه هي الوظيفة التي تُغلفها فئة :class:`NearestNeighbors` المستخدمة أعلاه. شجرة الكرة وشجرة KD لهما نفس الواجهة؛ سنعرض هنا مثالاً على استخدام شجرة KD:

    >>> from sklearn.neighbors import KDTree
    >>> import numpy as np
    >>> X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    >>> kdt = KDTree(X, leaf_size=30, metric='euclidean')
    >>> kdt.query(X, k=2, return_distance=False)
    array([[0, 1],
           [1, 0],
           [2, 1],
           [3, 4],
           [4, 3],
           [5, 4]]...)

راجع وثائق فئة :class:`KDTree` و :class:`BallTree` لمزيد من المعلومات حول الخيارات المتاحة لعمليات بحث أقرب جيران، بما في ذلك تحديد استراتيجيات الاستعلام ومقاييس المسافة وما إلى ذلك. للحصول على قائمة بالمقاييس الصالحة، استخدم `KDTree.valid_metrics` و `BallTree.valid_metrics`:


    >>> from sklearn.neighbors import KDTree, BallTree
    >>> KDTree.valid_metrics
    ['euclidean', 'l2', 'minkowski', 'p', 'manhattan', 'cityblock', 'l1', 'chebyshev', 'infinity']
    >>> BallTree.valid_metrics
    ['euclidean', 'l2', 'minkowski', 'p', 'manhattan', 'cityblock', 'l1', 'chebyshev', 'infinity', 'seuclidean', 'mahalanobis', 'hamming', 'canberra', 'braycurtis', 'jaccard', 'dice', 'rogerstanimoto', 'russellrao', 'sokalmichener', 'sokalsneath', 'haversine', 'pyfunc']


.. _classification:

تصنيف أقرب جيران
================================

التصنيف القائم على الجيران هو نوع من *التعلم القائم على المثيل* أو *التعلم غير المُعمّم*: لا يحاول إنشاء نموذج داخلي عام، ولكنه ببساطة يُخزّن مثيلات بيانات التدريب. يتم حساب التصنيف من تصويت أغلبية بسيط لأقرب جيران لكل نقطة: يتم تعيين نقطة الاستعلام فئة البيانات التي لديها أكبر عدد من المُمثلين ضمن أقرب جيران للنقطة.

تُطبق scikit-learn مُصنفين مختلفين لأقرب جيران: تُطبق :class:`KNeighborsClassifier` التعلم القائم على أقرب :math:`k` جيران لكل نقطة استعلام، حيث :math:`k` هي قيمة عدد صحيح يُحددها المستخدم. تُطبق :class:`RadiusNeighborsClassifier` التعلم القائم على عدد الجيران ضمن نصف قطر ثابت :math:`r` لكل نقطة تدريب، حيث :math:`r` هي قيمة فاصلة عائمة يُحددها المستخدم.

تصنيف k-neighbors في :class:`KNeighborsClassifier` هو التقنية الأكثر شيوعًا. الاختيار الأمثل لقيمة :math:`k` يعتمد بشكل كبير على البيانات: بشكل عام، :math:`k` الأكبر يقمع آثار الضوضاء، ولكنه يجعل حدود التصنيف أقل وضوحًا.


في الحالات التي لا يتم فيها أخذ عينات البيانات بشكل منتظم، قد يكون تصنيف الجيران القائم على نصف القطر في :class:`RadiusNeighborsClassifier` خيارًا أفضل. يُحدد المستخدم نصف قطر ثابت :math:`r`، بحيث تستخدم النقاط في الأحياء المتفرقة عددًا أقل من أقرب الجيران للتصنيف. بالنسبة لمساحات المعلمات ذات الأبعاد العالية، تصبح هذه الطريقة أقل فعالية بسبب ما يُسمى "لعنة الأبعاد".

يستخدم تصنيف أقرب الجيران الأساسي أوزانًا موحدة: أي أن القيمة المعينة لنقطة استعلام يتم حسابها من تصويت أغلبية بسيط لأقرب الجيران. في ظل ظروف معينة، من الأفضل ترجيح الجيران بحيث يُساهم الجيران الأقرب بشكل أكبر في الملاءمة. يمكن تحقيق ذلك من خلال الكلمة المفتاحية ``weights``. القيمة الافتراضية، ``weights = 'uniform'``، تُعيّن أوزانًا موحدة لكل جار. ``weights = 'distance'`` تُعيّن أوزانًا تتناسب مع معكوس المسافة من نقطة الاستعلام. بدلاً من ذلك، يمكن توفير دالة مُحدّدة من قبل المستخدم للمسافة لحساب الأوزان.

.. |classification_1| image:: ../auto_examples/neighbors/images/sphx_glr_plot_classification_001.png
   :target: ../auto_examples/neighbors/plot_classification.html
   :scale: 75

.. centered:: |classification_1|


.. rubric:: أمثلة

* :ref:`sphx_glr_auto_examples_neighbors_plot_classification.py`: مثال على التصنيف باستخدام أقرب الجيران.


.. _regression:

انحدار أقرب جيران
============================


يمكن استخدام الانحدار القائم على الجيران في الحالات التي تكون فيها تسميات البيانات متغيرات مستمرة بدلاً من متغيرات منفصلة. يتم حساب التسمية المعينة لنقطة استعلام بناءً على متوسط تسميات أقرب جيرانها.

تُطبق scikit-learn مُنحدِرين مختلفين للجيران: تُطبق :class:`KNeighborsRegressor` التعلم القائم على أقرب :math:`k` جيران لكل نقطة استعلام، حيث :math:`k` هي قيمة عدد صحيح يُحددها المستخدم. تُطبق :class:`RadiusNeighborsRegressor` التعلم القائم على الجيران ضمن نصف قطر ثابت :math:`r` من نقطة الاستعلام، حيث :math:`r` هي قيمة فاصلة عائمة يُحددها المستخدم.

يستخدم انحدار أقرب الجيران الأساسي أوزانًا موحدة: أي أن كل نقطة في الحي المحلي تُساهم بشكل منتظم في تصنيف نقطة الاستعلام. في ظل ظروف معينة، يمكن أن يكون من المفيد ترجيح النقاط بحيث تُساهم النقاط القريبة بشكل أكبر في الانحدار من النقاط البعيدة. يمكن تحقيق ذلك من خلال الكلمة المفتاحية ``weights``. القيمة الافتراضية، ``weights = 'uniform'``، تُعيّن أوزانًا متساوية لجميع النقاط. ``weights = 'distance'`` تُعيّن أوزانًا تتناسب مع معكوس المسافة من نقطة الاستعلام. بدلاً من ذلك، يمكن توفير دالة مُحدّدة من قبل المستخدم للمسافة، والتي سيتم استخدامها لحساب الأوزان.

.. figure:: ../auto_examples/neighbors/images/sphx_glr_plot_regression_001.png
   :target: ../auto_examples/neighbors/plot_regression.html
   :align: center
   :scale: 75

يتم توضيح استخدام أقرب جيران متعدد المخرجات للانحدار في :ref:`sphx_glr_auto_examples_miscellaneous_plot_multioutput_face_completion.py`. في هذا المثال، المدخلات X هي وحدات بكسل النصف العلوي من الوجوه والمخرجات Y هي وحدات بكسل النصف السفلي من تلك الوجوه.

.. figure:: ../auto_examples/miscellaneous/images/sphx_glr_plot_multioutput_face_completion_001.png
   :target: ../auto_examples/miscellaneous/plot_multioutput_face_completion.html
   :scale: 75
   :align: center

.. rubric:: أمثلة

* :ref:`sphx_glr_auto_examples_neighbors_plot_regression.py`: مثال على الانحدار باستخدام أقرب الجيران.

* :ref:`sphx_glr_auto_examples_miscellaneous_plot_multioutput_face_completion.py`: مثال على الانحدار متعدد المخرجات باستخدام أقرب الجيران.

خوارزميات أقرب جيران
===========================

.. _brute_force:

القوة الغاشمة
-----------

الحساب السريع لأقرب الجيران هو مجال بحث نشط في تعلم الآلة. يتضمن تطبيق بحث الجيران الأكثر سذاجة حساب القوة الغاشمة للمسافات بين جميع أزواج النقاط في مجموعة البيانات: بالنسبة لـ :math:`N` عينات في :math:`D` أبعاد، يتدرج هذا النهج كـ :math:`O[D N^2]`. يمكن أن تكون عمليات بحث الجيران بالقوة الغاشمة الفعالة تنافسية للغاية لعينات البيانات الصغيرة. ومع ذلك، مع نمو عدد العينات :math:`N`، سرعان ما يُصبح نهج القوة الغاشمة غير مُجدٍ. في الفئات ضمن :mod:`sklearn.neighbors`، يتم تحديد عمليات بحث الجيران بالقوة الغاشمة باستخدام الكلمة المفتاحية ``algorithm = 'brute'``، ويتم حسابها باستخدام الإجراءات المتاحة في :mod:`sklearn.metrics.pairwise`.


.. _kd_tree:

شجرة K-D
--------


لمعالجة أوجه القصور الحسابية لنهج القوة الغاشمة، تم اختراع مجموعة متنوعة من هياكل البيانات القائمة على الأشجار. بشكل عام، تحاول هذه الهياكل تقليل العدد المطلوب من حسابات المسافة عن طريق ترميز معلومات المسافة الإجمالية للعينة بكفاءة. الفكرة الأساسية هي أنه إذا كانت النقطة :math:`A` بعيدة جدًا عن النقطة :math:`B`،  والنقطة :math:`B` قريبة جدًا من النقطة :math:`C`، فإننا نعلم أن النقطتين :math:`A` و :math:`C` بعيدتان جدًا، *دون الحاجة إلى حساب المسافة بينهما بشكل صريح*. بهذه الطريقة، يمكن تقليل التكلفة الحسابية لبحث أقرب جيران إلى :math:`O[D N \log(N)]` أو أفضل. هذا تحسن كبير مقارنة بالقوة الغاشمة لـ :math:`N` كبيرة.

كان النهج المُبكّر للاستفادة من هذه المعلومات الإجمالية هو بنية بيانات *شجرة KD* (اختصار لـ *شجرة K الأبعاد*)، التي تُعمّم *أشجار Quad* ثنائية الأبعاد و *أشجار Oct* ثلاثية الأبعاد إلى عدد تعسفي من الأبعاد. شجرة KD هي بنية شجرة ثنائية تُقسّم مساحة المعلمات بشكل مُتكرّر على طول محاور البيانات، وتُقسّمها إلى مناطق متداخلة متعامدة يتم فيها حفظ نقاط البيانات. إنشاء شجرة KD سريع جدًا: نظرًا لأنه يتم إجراء التقسيم على طول محاور البيانات فقط، فلا حاجة لحساب أي مسافات :math:`D` الأبعاد. بمجرد الإنشاء، يمكن تحديد أقرب جار لنقطة استعلام باستخدام :math:`O[\log(N)]` حسابات مسافة فقط. على الرغم من أن نهج شجرة KD سريع جدًا لعمليات بحث الجيران ذات الأبعاد المنخفضة (:math:`D < 20`)، إلا أنه يُصبح غير فعال مع نمو :math:`D` بشكل كبير جدًا: هذا أحد مظاهر ما يُسمى "لعنة الأبعاد". في scikit-learn، يتم تحديد عمليات بحث الجيران لشجرة KD باستخدام الكلمة المفتاحية ``algorithm = 'kd_tree'``، ويتم حسابها باستخدام الفئة :class:`KDTree`.

.. dropdown:: المراجع

  * `"Multidimensional binary search trees used for associative searching"
    <https://dl.acm.org/citation.cfm?doid=361002.361007>`_,
    Bentley, J.L., Communications of the ACM (1975)


.. _ball_tree:

شجرة الكرة
---------

لمعالجة أوجه القصور في أشجار KD في الأبعاد الأعلى، تم تطوير بنية بيانات *شجرة الكرة*. حيث تُقسّم أشجار KD البيانات على طول المحاور الديكارتية، تُقسّم أشجار الكرة البيانات في سلسلة من التداخلات الفائقة. هذا يجعل إنشاء الشجرة أكثر تكلفة من شجرة KD، ولكنه يؤدي إلى بنية بيانات يمكن أن تكون فعالة جدًا على البيانات عالية التنظيم، حتى في الأبعاد العالية جدًا.

تقوم شجرة الكرة بتقسيم البيانات بشكل مُتكرّر إلى عقد مُحدّدة بواسطة مركز :math:`C` ونصف قطر :math:`r`، بحيث تقع كل نقطة في العقدة داخل الكرة الفائقة المُحدّدة بواسطة :math:`r` و :math:`C`. يتم تقليل عدد النقاط المُرشّحة لبحث الجيران من خلال استخدام *متباينة المثلث*:


.. math::   |x+y| \leq |x| + |y|


مع هذا الإعداد، يكون حساب مسافة واحدة بين نقطة اختبار والمركز كافيًا لتحديد الحد الأدنى والأعلى للمسافة إلى جميع النقاط داخل العقدة. نظرًا للهندسة الكروية لعقد شجرة الكرة، يمكنها أن تتفوق على *شجرة KD* في الأبعاد العالية، على الرغم من أن الأداء الفعلي يعتمد بشكل كبير على بنية بيانات التدريب. في scikit-learn، يتم تحديد عمليات بحث الجيران القائمة على شجرة الكرة باستخدام الكلمة المفتاحية ``algorithm = 'ball_tree'``، ويتم حسابها باستخدام الفئة :class:`BallTree`. بدلاً من ذلك، يمكن للمستخدم العمل مع فئة :class:`BallTree` مباشرةً.


.. dropdown:: المراجع

  * `"Five Balltree Construction Algorithms"
    <https://citeseerx.ist.psu.edu/doc_view/pid/17ac002939f8e950ffb32ec4dc8e86bdd8cb5ff1>`_,
    Omohundro, S.M., International Computer Science Institute
    Technical Report (1989)



.. dropdown:: اختيار خوارزمية أقرب جيران

  الخوارزمية المثلى لمجموعة بيانات مُعطاة هي اختيار مُعقّد، وتعتمد على عدد من العوامل:

  * عدد العينات :math:`N` (أي ``n_samples``) والأبعاد :math:`D` (أي ``n_features``).

    * ينمو وقت استعلام *القوة الغاشمة* كـ :math:`O[D N]`
    * ينمو وقت استعلام *شجرة الكرة* كـ :math:`O[D \log(N)]` تقريبًا
    * يتغير وقت استعلام *شجرة KD* مع :math:`D` بطريقة يصعب تحديدها بدقة. بالنسبة لـ :math:`D` الصغيرة (أقل من 20 أو نحو ذلك)، فإن التكلفة هي تقريبًا :math:`O[D\log(N)]`، ويمكن أن يكون استعلام شجرة KD فعالاً للغاية. بالنسبة لـ :math:`D` الأكبر، تزداد التكلفة إلى ما يقرب من :math:`O[DN]`، ويمكن أن تؤدي النفقات العامة بسبب بنية الشجرة إلى استعلامات أبطأ من القوة الغاشمة.

    بالنسبة لمجموعات البيانات الصغيرة (:math:`N` أقل من 30 أو نحو ذلك)، فإن :math:`\log(N)` تُقارن بـ :math:`N`، ويمكن أن تكون خوارزميات القوة الغاشمة أكثر كفاءة من النهج القائم على الشجرة. يعالج كل من :class:`KDTree` و :class:`BallTree` هذا من خلال توفير معلمة *حجم الورقة*: يتحكم هذا في عدد العينات التي يتحول عندها الاستعلام إلى القوة الغاشمة. يسمح هذا لكلا الخوارزميتين بالاقتراب من كفاءة حساب القوة الغاشمة لـ :math:`N` الصغيرة.


  * بنية البيانات: *الأبعاد الجوهرية* للبيانات و/أو *التفرق* للبيانات. تشير الأبعاد الجوهرية إلى بُعد :math:`d \le D` لمشعب تقع عليه البيانات، والذي يمكن تضمينه خطيًا أو غير خطيًا في فضاء المعلمات. يشير التفرق إلى الدرجة التي تملأ بها البيانات فضاء المعلمات (يجب تمييز هذا عن المفهوم كما هو مستخدم في المصفوفات "المتفرقة". قد لا تحتوي مصفوفة البيانات على إدخالات صفرية، ولكن لا يزال من الممكن أن يكون *البنية* "متفرقة" بهذا المعنى).

    * وقت استعلام *القوة الغاشمة* لا يتغير حسب بنية البيانات.

    * يمكن أن تتأثر أوقات استعلام *شجرة الكرة* و *شجرة KD* بشكل كبير ببنية البيانات. بشكل عام، تؤدي البيانات الأكثر تفرقًا ذات أبعاد جوهرية أصغر إلى أوقات استعلام أسرع. نظرًا لأن التمثيل الداخلي لشجرة KD مُحاذي لمحاور المعلمات، فلن يُظهر بشكل عام تحسنًا كبيرًا مثل شجرة الكرة للبيانات المُنظّمة بشكل تعسفي.

    تميل مجموعات البيانات المستخدمة في تعلم الآلة إلى أن تكون مُنظّمة للغاية، وهي مُناسبة جدًا للاستعلامات القائمة على الأشجار.

  * عدد الجيران :math:`k` المطلوب لنقطة استعلام.

    * وقت استعلام *القوة الغاشمة* لا يتأثر إلى حد كبير بقيمة :math:`k`
    * سيُصبح وقت استعلام *شجرة الكرة* و *شجرة KD* أبطأ مع زيادة :math:`k`. هذا يرجع إلى تأثيرين: أولاً، يؤدي :math:`k` الأكبر إلى ضرورة البحث في جزء أكبر من مساحة المعلمات. ثانيًا، يتطلب استخدام :math:`k > 1` تنظيم قائمة انتظار داخلية للنتائج أثناء اجتياز الشجرة.

    مع كبر :math:`k` مقارنة بـ :math:`N`، يتم تقليل القدرة على تقليم الفروع في استعلام قائم على الشجرة. في هذه الحالة، يمكن أن تكون استعلامات القوة الغاشمة أكثر كفاءة.


  * عدد نقاط الاستعلام. يتطلب كل من شجرة الكرة وشجرة KD مرحلة إنشاء. تُصبح تكلفة هذا الإنشاء ضئيلة عند استهلاكها على العديد من الاستعلامات. ومع ذلك، إذا تم تنفيذ عدد قليل فقط من الاستعلامات، فقد يُشكّل الإنشاء جزءًا كبيرًا من التكلفة الإجمالية. إذا كانت هناك حاجة إلى عدد قليل جدًا من نقاط الاستعلام، فإن القوة الغاشمة أفضل من الطريقة القائمة على الشجرة.

  يُحدد ``algorithm = 'auto'`` حاليًا ``'brute'`` إذا تم التحقق من أي من الشروط التالية:


  * بيانات الإدخال متفرقة

  * ``metric = 'precomputed'``
  * :math:`D > 15`
  * :math:`k >= N/2`
  * ``effective_metric_`` ليس في قائمة ``VALID_METRICS`` إما لـ ``'kd_tree'`` أو ``'ball_tree'``

  وإلا، فإنه يختار أولاً من ``'kd_tree'`` و ``'ball_tree'`` التي تحتوي على ``effective_metric_`` في قائمة ``VALID_METRICS``. تعتمد هذه الاستدلالية على الافتراضات التالية:


  * عدد نقاط الاستعلام على الأقل بنفس ترتيب عدد نقاط التدريب

  * ``leaf_size`` قريب من قيمته الافتراضية ``30``

  * عندما :math:`D > 15`، تكون الأبعاد الجوهرية للبيانات عالية جدًا بشكل عام بالنسبة للطرق القائمة على الشجرة.


.. dropdown:: تأثير ``leaf_size``

  كما هو مذكور أعلاه، بالنسبة لأحجام العينات الصغيرة، يمكن أن يكون بحث القوة الغاشمة أكثر كفاءة من الاستعلام القائم على الشجرة. يتم حساب هذه الحقيقة في شجرة الكرة وشجرة KD عن طريق التبديل داخليًا إلى عمليات بحث القوة الغاشمة داخل عقد الأوراق. يمكن تحديد مستوى هذا المفتاح باستخدام المعلمة ``leaf_size``. خيار المعلمة هذا له تأثيرات كثيرة:


  **وقت الإنشاء**
    يؤدي ``leaf_size`` الأكبر إلى وقت إنشاء شجرة أسرع، لأنه يلزم إنشاء عدد أقل من العقد


  **وقت الاستعلام**
    يمكن أن يؤدي كل من ``leaf_size`` الكبير أو الصغير إلى تكلفة استعلام غير مثالية. بالنسبة لـ ``leaf_size`` التي تقترب من 1، يمكن أن تؤدي النفقات العامة المُتعلقة باجتياز العقد إلى إبطاء أوقات الاستعلام بشكل كبير. بالنسبة لـ ``leaf_size`` التي تقترب من حجم مجموعة التدريب، تُصبح الاستعلامات أساسًا قوة غاشمة. حل وسط جيد بينهما هو ``leaf_size = 30``، القيمة الافتراضية للمعلمة.


  **الذاكرة**
    مع زيادة ``leaf_size``، تقل الذاكرة المطلوبة لتخزين بنية الشجرة. هذا مهم بشكل خاص في حالة شجرة الكرة، التي تُخزّن مركزًا :math:`D` الأبعاد لكل عقدة. مساحة التخزين المطلوبة لـ :class:`BallTree` هي تقريبًا ``1 / leaf_size`` ضعف حجم مجموعة التدريب.

  لا تتم الإشارة إلى ``leaf_size`` لاستعلامات القوة الغاشمة.


.. dropdown:: المقاييس الصالحة لخوارزميات أقرب جيران

  للحصول على قائمة بالمقاييس المتاحة، انظر وثائق فئة :class:`~sklearn.metrics.DistanceMetric` والمقاييس المدرجة في `sklearn.metrics.pairwise.PAIRWISE_DISTANCE_FUNCTIONS`. لاحظ أن المقياس "cosine" يستخدم :func:`~sklearn.metrics.pairwise.cosine_distances`.

  يمكن الحصول على قائمة بالمقاييس الصالحة لأي من الخوارزميات المذكورة أعلاه باستخدام سمة ``valid_metric``. على سبيل المثال، يمكن إنشاء مقاييس صالحة لـ ``KDTree`` عن طريق:

      >>> from sklearn.neighbors import KDTree
      >>> print(sorted(KDTree.valid_metrics))
      ['chebyshev', 'cityblock', 'euclidean', 'infinity', 'l1', 'l2', 'manhattan', 'minkowski', 'p']


.. _nearest_centroid_classifier:

مُصنف أقرب مركز
===========================

المُصنف :class:`NearestCentroid` هو خوارزمية بسيطة تُمثل كل فئة بواسطة مركز أعضائها. في الواقع، هذا يجعلها مشابهة لمرحلة تحديث التسميات لخوارزمية :class:`~sklearn.cluster.KMeans`. كما أنه لا يحتوي على معلمات للاختيار، مما يجعله مُصنفًا أساسيًا جيدًا. ومع ذلك، فإنه يُعاني من الفئات غير المحدبة، وكذلك عندما يكون للفئات تباينات مختلفة اختلافًا جذريًا، حيث يُفترض أن يكون التباين متساويًا في جميع الأبعاد. انظر التحليل التمييزي الخطي (:class:`~sklearn.discriminant_analysis.LinearDiscriminantAnalysis`) والتحليل التمييزي التربيعي (:class:`~sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis`) للحصول على طرق أكثر تعقيدًا لا تفترض هذا الافتراض. استخدام :class:`NearestCentroid` الافتراضي بسيط:

    >>> from sklearn.neighbors import NearestCentroid
    >>> import numpy as np
    >>> X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    >>> y = np.array([1, 1, 1, 2, 2, 2])
    >>> clf = NearestCentroid()
    >>> clf.fit(X, y)
    NearestCentroid()
    >>> print(clf.predict([[-0.8, -1]]))
    [1]


أقرب مركز مُنكمش
-------------------------

يحتوي المُصنف :class:`NearestCentroid` على معلمة ``shrink_threshold``، التي تُطبق مُصنف أقرب مركز مُنكمش. في الواقع، يتم قسمة قيمة كل ميزة لكل مركز على تباين تلك الميزة داخل الفئة. ثم يتم تقليل قيم الميزات بمقدار ``shrink_threshold``. والأهم من ذلك، إذا تجاوزت قيمة ميزة معينة الصفر، فسيتم تعيينها على صفر. في الواقع، هذا يُزيل الميزة من التأثير على التصنيف. هذا مفيد، على سبيل المثال، لإزالة الميزات المزعجة.

في المثال أدناه، يؤدي استخدام عتبة انكماش صغيرة إلى زيادة دقة النموذج من 0.81 إلى 0.82.


.. |nearest_centroid_1| image:: ../auto_examples/neighbors/images/sphx_glr_plot_nearest_centroid_001.png
   :target: ../auto_examples/neighbors/plot_nearest_centroid.html
   :scale: 50

.. |nearest_centroid_2| image:: ../auto_examples/neighbors/images/sphx_glr_plot_nearest_centroid_002.png
   :target: ../auto_examples/neighbors/plot_nearest_centroid.html
   :scale: 50

.. centered:: |nearest_centroid_1| |nearest_centroid_2|



.. rubric:: أمثلة

* :ref:`sphx_glr_auto_examples_neighbors_plot_nearest_centroid.py`: مثال على التصنيف باستخدام أقرب مركز مع عتبات انكماش مختلفة.



.. _neighbors_transformer:

محول أقرب جيران
=============================


يعتمد العديد من مقدرات scikit-learn على أقرب جيران: العديد من المُصنفات والمنحدرات مثل :class:`KNeighborsClassifier` و :class:`KNeighborsRegressor`، ولكن أيضًا بعض أساليب التجميع مثل :class:`~sklearn.cluster.DBSCAN` و :class:`~sklearn.cluster.SpectralClustering`، وبعض تضمينات المشعبات مثل :class:`~sklearn.manifold.TSNE` و :class:`~sklearn.manifold.Isomap`.


يمكن لجميع هذه المقدرات حساب أقرب جيران داخليًا، ولكن معظمها يقبل أيضًا :term:`رسم بياني متفرق` لأقرب جيران محسوب مسبقًا، كما هو مُعطى بواسطة :func:`~sklearn.neighbors.kneighbors_graph` و :func:`~sklearn.neighbors.radius_neighbors_graph`. مع الوضع `mode='connectivity'`، تُعيد هذه الدوال رسمًا بيانيًا متفرقًا ثنائيًا متجاورًا كما هو مطلوب، على سبيل المثال، في :class:`~sklearn.cluster.SpectralClustering`. بينما مع `mode='distance'`، تُعيد رسمًا بيانيًا متفرقًا للمسافة كما هو مطلوب، على سبيل المثال، في :class:`~sklearn.cluster.DBSCAN`. لتضمين هذه الدوال في خط أنابيب scikit-learn، يمكن للمرء أيضًا استخدام الفئات المقابلة :class:`KNeighborsTransformer` و :class:`RadiusNeighborsTransformer`. فوائد واجهة برمجة التطبيقات هذه للرسم البياني المتفرق متعددة.

أولاً، يمكن إعادة استخدام الرسم البياني المحسوب مسبقًا عدة مرات، على سبيل المثال أثناء تغيير معلمة المقدّر. يمكن القيام بذلك يدويًا بواسطة المستخدم، أو باستخدام خصائص التخزين المؤقت لخط أنابيب scikit-learn:


    >>> import tempfile
    >>> from sklearn.manifold import Isomap
    >>> from sklearn.neighbors import KNeighborsTransformer
    >>> from sklearn.pipeline import make_pipeline
    >>> from sklearn.datasets import make_regression
    >>> cache_path = tempfile.gettempdir()  # نستخدم مجلدًا مؤقتًا هنا
    >>> X, _ = make_regression(n_samples=50, n_features=25, random_state=0)
    >>> estimator = make_pipeline(
    ...     KNeighborsTransformer(mode='distance'),
    ...     Isomap(n_components=3, metric='precomputed'),
    ...     memory=cache_path)
    >>> X_embedded = estimator.fit_transform(X)
    >>> X_embedded.shape
    (50, 3)



ثانيًا، يمكن أن يُعطي حساب الرسم البياني مسبقًا تحكمًا أدق في تقدير أقرب جيران، على سبيل المثال تمكين المعالجة المتعددة من خلال المعلمة `n_jobs`، والتي قد لا تكون متاحة في جميع المقدرات.

أخيرًا، يمكن إجراء الحساب المسبق بواسطة مقدرات مخصصة لاستخدام تطبيقات مختلفة، مثل أساليب أقرب جيران التقريبية، أو التنفيذ مع أنواع بيانات خاصة. يجب تنسيق :term:`الرسم البياني المتفرق` للجيران المحسوب مسبقًا كما في إخراج :func:`~sklearn.neighbors.radius_neighbors_graph`:

* مصفوفة CSR (على الرغم من قبول COO أو CSC أو LIL).
*  تخزين أقرب جيران لكل عينة بشكل صريح فيما يتعلق ببيانات التدريب فقط. يجب أن يشمل ذلك تلك التي على مسافة 0 من نقطة استعلام، بما في ذلك قطري المصفوفة عند حساب أقرب جيران بين بيانات التدريب ونفسها.

* يجب أن تُخزّن `data` لكل صف المسافة بترتيب تصاعدي (اختياري. سيتم فرز البيانات غير المُرتبة بشكل ثابت، مما يُضيف نفقات عامة حسابية).
* يجب أن تكون جميع القيم في البيانات غير سالبة.
* يجب ألا يكون هناك `indices` مُكرّرة في أي صف (انظر https://github.com/scipy/scipy/issues/5807).
* إذا كانت الخوارزمية التي تم تمرير المصفوفة المحسوبة مسبقًا إليها تستخدم أقرب k جيران (على عكس جيرة نصف القطر)، فيجب تخزين k جيران على الأقل في كل صف (أو k+1، كما هو موضح في الملاحظة التالية).


.. note::
  عند الاستعلام عن عدد مُحدّد من الجيران (باستخدام :class:`KNeighborsTransformer`)، يكون تعريف `n_neighbors` غامضًا لأنه يمكن إما تضمين كل نقطة تدريب كجار لها، أو استبعادها. لا يوجد خيار مثالي، لأن تضمينها يؤدي إلى عدد مختلف من الجيران غير الذاتيين أثناء التدريب والاختبار، بينما يؤدي استبعادها إلى اختلاف بين `fit(X).transform(X)` و `fit_transform(X)`، وهو ما يتعارض مع واجهة برمجة تطبيقات scikit-learn. في :class:`KNeighborsTransformer`، نستخدم التعريف الذي يتضمن كل نقطة تدريب كجار لها في عدد `n_neighbors`. ومع ذلك، لأسباب تتعلق بالتوافق مع المقدرات الأخرى التي تستخدم التعريف الآخر، سيتم حساب جار إضافي واحد عندما `mode == 'distance'`. لزيادة التوافق مع جميع المقدرات، فإن الخيار الآمن هو دائمًا تضمين جار إضافي واحد في مقدر أقرب جيران مخصص، حيث سيتم تصفية الجيران غير الضروريين بواسطة المقدرات التالية.


.. rubric:: أمثلة

* :ref:`sphx_glr_auto_examples_neighbors_approximate_nearest_neighbors.py`: مثال على توصيل :class:`KNeighborsTransformer` و :class:`~sklearn.manifold.TSNE`. يقترح أيضًا مُقدّرين مخصصين لأقرب جيران بناءً على حزم خارجية.

* :ref:`sphx_glr_auto_examples_neighbors_plot_caching_nearest_neighbors.py`: مثال على توصيل :class:`KNeighborsTransformer` و :class:`KNeighborsClassifier` لتمكين التخزين المؤقت للرسم البياني للجيران أثناء بحث شبكي للمعلمات الفائقة.


.. _nca:

تحليل مكونات الجوار
================================

.. sectionauthor:: William de Vazelhes <william.de-vazelhes@inria.fr>

تحليل مكونات الجوار (NCA، :class:`NeighborhoodComponentsAnalysis`) هو خوارزمية لتعلم مقياس المسافة تهدف إلى تحسين دقة تصنيف أقرب جيران مقارنة بمسافة إقليدية القياسية. تُعظّم الخوارزمية بشكل مباشر متغيرًا عشوائيًا من درجة أقرب k جيران (KNN) اترك واحدًا في مجموعة التدريب. يمكنها أيضًا تعلم إسقاط خطي منخفض الأبعاد للبيانات يمكن استخدامه لتصور البيانات والتصنيف السريع.

.. |nca_illustration_1| image:: ../auto_examples/neighbors/images/sphx_glr_plot_nca_illustration_001.png
   :target: ../auto_examples/neighbors/plot_nca_illustration.html
   :scale: 50

.. |nca_illustration_2| image:: ../auto_examples/neighbors/images/sphx_glr_plot_nca_illustration_002.png
   :target: ../auto_examples/neighbors/plot_nca_illustration.html
   :scale: 50


.. centered:: |nca_illustration_1| |nca_illustration_2|

في الشكل التوضيحي أعلاه، نعتبر بعض النقاط من مجموعة بيانات تم إنشاؤها عشوائيًا. نُركز على تصنيف KNN العشوائي للنقطة رقم 3. سمك الرابط بين العينة 3 ونقطة أخرى يتناسب مع المسافة بينهما، ويمكن اعتباره الوزن النسبي (أو الاحتمال) الذي تُعيّنه قاعدة تنبؤ الجيران العشوائية الأقرب لهذه النقطة. في المساحة الأصلية، تحتوي العينة 3 على العديد من الجيران العشوائيين من فئات مُختلفة، لذا فإن الفئة الصحيحة ليست مُحتملة للغاية. ومع ذلك، في المساحة المُسقطة التي تعلمتها NCA، فإن الجيران العشوائيين الوحيدين ذوي الوزن غير المهمل هم من نفس فئة العينة 3، مما يضمن أن الأخيرة سيتم تصنيفها جيدًا. انظر :ref:`الصيغة الرياضية <nca_mathematical_formulation>` لمزيد من التفاصيل.


التصنيف
--------------

بالاقتران مع مُصنف أقرب جيران (:class:`KNeighborsClassifier`)، فإن NCA جذابة للتصنيف لأنه يمكنها معالجة مشاكل متعددة الفئات بشكل طبيعي دون أي زيادة في حجم النموذج، ولا تُقدّم معلمات إضافية تتطلب ضبطًا دقيقًا من قبل المستخدم.


لقد ثبت أن تصنيف NCA يعمل بشكل جيد في الممارسة العملية لمجموعات البيانات ذات الأحجام والصعوبات المُتفاوتة. على عكس الطرق ذات الصلة مثل التحليل التمييزي الخطي، لا تُجري NCA أي افتراضات حول توزيعات الفئات. يمكن لتصنيف أقرب جيران أن يُنتج بشكل طبيعي حدود قرار غير منتظمة للغاية.

لاستخدام هذا النموذج للتصنيف، يحتاج المرء إلى دمج مثيل :class:`NeighborhoodComponentsAnalysis` الذي يتعلم التحويل الأمثل مع مثيل :class:`KNeighborsClassifier` الذي يُجري التصنيف في المساحة المُسقطة. فيما يلي مثال باستخدام الفئتين:


    >>> from sklearn.neighbors import (NeighborhoodComponentsAnalysis,
    ... KNeighborsClassifier)
    >>> from sklearn.datasets import load_iris
    >>> from sklearn.model_selection import train_test_split
    >>> from sklearn.pipeline import Pipeline
    >>> X, y = load_iris(return_X_y=True)
    >>> X_train, X_test, y_train, y_test = train_test_split(X, y,
    ... stratify=y, test_size=0.7, random_state=42)
    >>> nca = NeighborhoodComponentsAnalysis(random_state=42)
    >>> knn = KNeighborsClassifier(n_neighbors=3)
    >>> nca_pipe = Pipeline([('nca', nca), ('knn', knn)])
    >>> nca_pipe.fit(X_train, y_train)
    Pipeline(...)
    >>> print(nca_pipe.score(X_test, y_test))
    0.96190476...


.. |nca_classification_1| image:: ../auto_examples/neighbors/images/sphx_glr_plot_nca_classification_001.png
   :target: ../auto_examples/neighbors/plot_nca_classification.html
   :scale: 50

.. |nca_classification_2| image:: ../auto_examples/neighbors/images/sphx_glr_plot_nca_classification_002.png
   :target: ../auto_examples/neighbors/plot_nca_classification.html
   :scale: 50


.. centered:: |nca_classification_1| |nca_classification_2|

يُظهر الرسم التخطيطي حدود القرار لتصنيف أقرب جيران وتصنيف تحليل مكونات الجوار على مجموعة بيانات زهرة القزحية، عند التدريب والتهديف على ميزتين فقط، لأغراض التصور.



.. _nca_dim_reduction:

تخفيض الأبعاد
------------------------

يمكن استخدام NCA لإجراء تخفيض الأبعاد الخاضع للإشراف. يتم إسقاط بيانات الإدخال على فضاء جزئي خطي يتكون من الاتجاهات التي تُقلل هدف NCA. يمكن تعيين الأبعاد المطلوبة باستخدام المعلمة ``n_components``. على سبيل المثال، يُظهر الشكل التالي مقارنة لتخفيض الأبعاد باستخدام تحليل المكونات الرئيسية (:class:`~sklearn.decomposition.PCA`)، والتحليل التمييزي الخطي (:class:`~sklearn.discriminant_analysis.LinearDiscriminantAnalysis`)، وتحليل مكونات الجوار (:class:`NeighborhoodComponentsAnalysis`) على مجموعة بيانات Digits، وهي مجموعة بيانات بحجم :math:`n_{samples} = 1797` و :math:`n_{features} = 64`. يتم تقسيم مجموعة البيانات إلى مجموعة تدريب ومجموعة اختبار متساويتين في الحجم، ثم يتم توحيدها. من أجل التقييم، يتم حساب دقة تصنيف أقرب 3 جيران على النقاط المُسقطة ثنائية الأبعاد التي تم إيجادها بواسطة كل طريقة. تنتمي كل عينة بيانات إلى واحدة من 10 فئات.


.. |nca_dim_reduction_1| image:: ../auto_examples/neighbors/images/sphx_glr_plot_nca_dim_reduction_001.png
   :target: ../auto_examples/neighbors/plot_nca_dim_reduction.html
   :width: 32%

.. |nca_dim_reduction_2| image:: ../auto_examples/neighbors/images/sphx_glr_plot_nca_dim_reduction_002.png
   :target: ../auto_examples/neighbors/plot_nca_dim_reduction.html
   :width: 32%


.. |nca_dim_reduction_3| image:: ../auto_examples/neighbors/images/sphx_glr_plot_nca_dim_reduction_003.png
   :target: ../auto_examples/neighbors/plot_nca_dim_reduction.html
   :width: 32%


.. centered:: |nca_dim_reduction_1| |nca_dim_reduction_2| |nca_dim_reduction_3|




.. rubric:: أمثلة

* :ref:`sphx_glr_auto_examples_neighbors_plot_nca_classification.py`
* :ref:`sphx_glr_auto_examples_neighbors_plot_nca_dim_reduction.py`
* :ref:`sphx_glr_auto_examples_manifold_plot_lle_digits.py`



.. _nca_mathematical_formulation:


الصيغة الرياضية
------------------------

هدف NCA هو تعلم مصفوفة تحويل خطي مثالية بحجم ``(n_components, n_features)``، والتي تُعظّم المجموع على جميع العينات :math:`i` من الاحتمال :math:`p_i` بأن :math:`i` مُصنّف بشكل صحيح، أي:

.. math::

  \underset{L}{\arg\max} \sum\limits_{i=0}^{N - 1} p_{i}

مع :math:`N` = ``n_samples`` و :math:`p_i` احتمال تصنيف العينة :math:`i` بشكل صحيح وفقًا لقاعدة الجيران العشوائية الأقرب في المساحة المُضمنة المُتعلّمة:


.. math::

  p_{i}=\sum\limits_{j \in C_i}{p_{i j}}

حيث :math:`C_i` هي مجموعة النقاط في نفس فئة العينة :math:`i`، و :math:`p_{i j}` هي دالة softmax على مسافات إقليدية في المساحة المُضمنة:

.. math::

  p_{i j} = \frac{\exp(-||L x_i - L x_j||^2)}{\sum\limits_{k \ne
            i} {\exp{-(||L x_i - L x_k||^2)}}} , \quad p_{i i} = 0


.. dropdown:: مسافة ماهالانوبيس

  يمكن اعتبار NCA على أنها تعلم مقياس مسافة ماهالانوبيس (تربيعي):

  .. math::

      || L(x_i - x_j)||^2 = (x_i - x_j)^TM(x_i - x_j),


  حيث :math:`M = L^T L` هي مصفوفة شبه موجبة متماثلة بحجم ``(n_features, n_features)``.


التنفيذ
--------------

يتبع هذا التنفيذ ما هو موضح في الورقة الأصلية [1]_. بالنسبة لطريقة التحسين، فإنها تستخدم حاليًا L-BFGS-B من scipy مع حساب تدرج كامل في كل تكرار، لتجنب ضبط معدل التعلم وتوفير تعلم مستقر.

انظر الأمثلة أدناه وسلسلة docstring لـ :meth:`NeighborhoodComponentsAnalysis.fit` لمزيد من المعلومات.


التعقيد
----------


التدريب
^^^^^^^^
تُخزّن NCA مصفوفة من المسافات الزوجية، تأخذ ``n_samples ** 2`` ذاكرة. يعتمد التعقيد الزمني على عدد التكرارات التي تُجريها خوارزمية التحسين. ومع ذلك، يمكن للمرء تعيين الحد الأقصى لعدد التكرارات باستخدام الوسيطة ``max_iter``. لكل تكرار، التعقيد الزمني هو ``O(n_components x n_samples x min(n_samples, n_features))``.



التحويل
^^^^^^^^^
هنا تُعيد عملية ``transform`` :math:`LX^T`، وبالتالي فإن تعقيدها الزمني يساوي ``n_components * n_features * n_samples_test``. لا يوجد تعقيد مساحة مُضافة في العملية.


.. rubric:: المراجع

.. [1] `"Neighbourhood Components Analysis"
  <http://www.cs.nyu.edu/~roweis/papers/ncanips.pdf>`_,
  J. Goldberger, S. Roweis, G. Hinton, R. Salakhutdinov, Advances in
  Neural Information Processing Systems, Vol. 17, May 2005, pp. 513-520.


* `إدخال ويكيبيديا على تحليل مكونات الجوار <https://en.wikipedia.org/wiki/Neighbourhood_components_analysis>`_



