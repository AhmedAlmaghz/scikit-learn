.. _random_projection:

==================
الإسقاط العشوائي
==================
.. currentmodule:: sklearn.random_projection

توفر وحدة :mod:`sklearn.random_projection` طريقة بسيطة وفعالة من الناحية الحسابية لخفض الأبعاد البيانات عن طريق التضحية بكمية محكومة من الدقة (كتباين إضافي) مقابل أوقات معالجة أسرع وأحجام نماذج أصغر. تنفذ هذه الوحدة نوعين من المصفوفات العشوائية غير المنظمة:
:ref:`مصفوفة عشوائية غاوسية <gaussian_random_matrix>` و
:ref:`مصفوفة عشوائية مبعثرة <sparse_random_matrix>`.

يتم التحكم في أبعاد وتوزيع مصفوفات الإسقاطات العشوائية للحفاظ على المسافات الزوجية بين أي عينتين من مجموعة البيانات. وبالتالي، فإن الإسقاط العشوائي هو تقنية تقريب مناسبة للأساليب المستندة إلى المسافة.


.. rubric:: المراجع

* سانجوي داسجوبتا. 2000.
  `تجارب مع الإسقاط العشوائي. <https://cseweb.ucsd.edu/~dasgupta/papers/randomf.pdf>`_
  في وقائع المؤتمر السادس عشر حول عدم اليقين في الذكاء الاصطناعي (UAI'00)، كريج بوتيلير ومؤيسيس جولدشميدت (محرران). مورغان كوفمان ناشرون، سان فرانسيسكو، كاليفورنيا، الولايات المتحدة الأمريكية، 143-151.

* إيلا بينجهام وهيكي مانيلا. 2001.
  `الإسقاط العشوائي في خفض الأبعاد: التطبيقات على صورة وبيانات النص. <https://citeseerx.ist.psu.edu/doc_view/pid/aed77346f737b0ed5890b61ad02e5eb4ab2f3dc6>`_
  في وقائع المؤتمر السابع لجمعية آلات الحوسبة ACM SIGKDD حول اكتشاف المعرفة واستخراج البيانات (KDD '01). ACM، نيويورك، NY، الولايات المتحدة الأمريكية،
  245-250.


.. _johnson_lindenstrauss:

مُبرهنَة جونسون-ليندينستراوس
===============================

النتيجة النظرية الرئيسية وراء كفاءة الإسقاط العشوائي هي
`مبرهنة جونسون-ليندينستراوس (اقتباسًا من ويكيبيديا)
<https://en.wikipedia.org/wiki/Johnson%E2%80%93Lindenstrauss_lemma>`_:

  في الرياضيات، مبرهنة جونسون-ليندينستراوس هي نتيجة
  تتعلق بالغرسات ذات التشويه المنخفض لنقاط من الفضاء عالي الأبعاد
  في الفضاء ذي الأبعاد المنخفضة. وتنص المبرهنة على أنه يمكن غرس مجموعة صغيرة
  من النقاط في الفضاء عالي الأبعاد في مساحة ذات أبعاد أقل بكثير
  بطريقة تحافظ تقريبًا على المسافات بين النقاط. ويستخدم الرسم البياني للغرز
  على الأقل ليبشيتز، ويمكن حتى أن يكون إسقاطًا متعامدًا.

معرفة عدد العينات فقط،
:func:`johnson_lindenstrauss_min_dim` تقدر
بحفظ الحد الأدنى من حجم الفضاء الفرعي العشوائي لضمان
تشويه محدود مقدم من الإسقاط العشوائي::

  >>> from sklearn.random_projection import johnson_lindenstrauss_min_dim
  >>> johnson_lindenstrauss_min_dim(n_samples=1e6, eps=0.5)
  663
  >>> johnson_lindenstrauss_min_dim(n_samples=1e6, eps=[0.5, 0.1, 0.01])
  array([    663,   11841, 1112658])
  >>> johnson_lindenstrauss_min_dim(n_samples=[1e4, 1e5, 1e6], eps=0.1)
  array([ 7894,  9868, 11841])

.. figure:: ../auto_examples/miscellaneous/images/sphx_glr_plot_johnson_lindenstrauss_bound_001.png
   :target: ../auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.html
   :scale: 75
   :align: center

.. figure:: ../auto_examples/miscellaneous/images/sphphx_glr_plot_johnson_lindenstrauss_bound_002.png
   :target: ../auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.html
   :scale: 75
   :align: center

.. rubric:: أمثلة

* راجع :ref:`sphx_glr_auto_examples_miscellaneous_plot_johnson_lindenstrauss_bound.py`
  لشرح نظري على مبرهنة جونسون-ليندينستراوس والتحقق التجريبي باستخدام المصفوفات العشوائية المبعثرة.

.. rubric:: المراجع

* سانجوي داسجوبتا وأنوبام جوبتا، 1999.
  `دليل ابتدائي على مبرهنة جونسون-ليندينستراوس.
  <https://citeseerx.ist.psu.edu/doc_view/pid/95cd464d27c25c9c8690b378b894d337cdf021f9>`_

.. _gaussian_random_matrix:

الإسقاط العشوائي الغاوسي
==========================
:class:`GaussianRandomProjection` يقلل من
الأبعاد من خلال إسقاط مساحة الإدخال الأصلية على مصفوفة مُولدة عشوائيًا
حيث يتم سحب المكونات من التوزيع التالي
:math:`N(0, \frac{1}{n_{components}})`.

هنا مقتطف قصير يوضح كيفية استخدام محول الإسقاط العشوائي الغاوسي::

  >>> import numpy as np
  >>> from sklearn import random_projection
  >>> X = np.random.rand(100, 10000)
  >>> transformer = random_projection.GaussianRandomProjection()
  >>> X_new = transformer.fit_transform(X)
  >>> X_new.shape
  (100, 3947)


.. _sparse_random_matrix:

الإسقاط العشوائي المبعثر
========================
:class:`SparseRandomProjection` يقلل من
الأبعاد من خلال إسقاط مساحة الإدخال الأصلية باستخدام مصفوفة عشوائية مبعثرة.

المصفوفات العشوائية المبعثرة هي بديل للمصفوفات العشوائية الغاوسية الكثيفة التي تضمن جودة غمر مماثلة بينما تكون أكثر كفاءة في الذاكرة وتسمح بحساب أسرع للبيانات المُسقطة.

إذا حددنا ``s = 1 / density``، يتم سحب عناصر المصفوفة العشوائية من

.. math::

  \left\{
  \begin{array}{c c l}
  -\sqrt{\frac{s}{n_{\text{components}}}} & & 1 / 2s\\
  0 &\text{with probability}  & 1 - 1 / s \\
  +\sqrt{\frac{s}{n_{\text{components}}}} & & 1 / 2s\\
  \end{array}
  \right.

حيث :math:`n_{\text{components}}` هو حجم الفضاء الفرعي المسقط.
افتراضيًا، يتم تعيين كثافة العناصر غير الصفرية إلى الحد الأدنى من الكثافة كما هو موصى به من قبل بينج لي وآخرون.: :math:`1 / \sqrt{n_{\text{features}}}`.

هنا مقتطف قصير يوضح كيفية استخدام محول الإسقاط العشوائي المبعثر::

  >>> import numpy as np
  >>> from sklearn import random_projection
  >>> X = np.random.rand(100, 10000)
  >>> transformer = random_projection.SparseRandomProjection()
  >>> X_new = transformer.fit_transform(X)
  >>> X_new.shape
  (100, 3947)


.. rubric:: المراجع

* د. أخلوبتاس. 2003.
  `الإسقاطات العشوائية الصديقة لقواعد البيانات: جونسون-ليندينستراوس مع العملات المعدنية الثنائية
  <https://www.sciencedirect.com/science/article/pii/S0022000003000254>`_.
  مجلة علوم الكمبيوتر والنظم 66 (2003) 671-687.

* بينج لي، تريفور جيه. هاستي، وكينيث دبليو. تشرتش. 2006.
  `الإسقاطات العشوائية المبعثرة للغاية. <https://web.stanford.edu/~hastie/Papers/Ping/KDD06_rp.pdf>`_
  في وقائع المؤتمر الدولي الثاني عشر لجمعية آلات الحوسبة ACM SIGKDD حول
  اكتشاف المعرفة واستخراج البيانات (KDD '06). ACM، نيويورك، NY، الولايات المتحدة الأمريكية، 287-296.


.. _random_projection_inverse_transform:

التحويل العكسي
=================
لدى محولات الإسقاط العشوائي معلمة ``compute_inverse_components``، عندما
يتم تعيينها إلى True، بعد إنشاء مصفوفة "components_" العشوائية أثناء التهيئة،
يحسب المحول المقلوب الزائف لهذه المصفوفة ويخزنها كـ
"inverse_components_". تحتوي مصفوفة "inverse_components_" على شكل
:math:`n_{features} \times n_{components}`، وهي دائمًا مصفوفة كثيفة،
بغض النظر عما إذا كانت مصفوفة المكونات مبعثرة أو كثيفة. لذا، اعتمادًا على
عدد الميزات والمكونات، فقد يستخدم الكثير من الذاكرة.

عندما يتم استدعاء طريقة "inverse_transform"، فإنها تحسب حاصل ضرب الإدخال "X"
والمحول الخطي للمكونات العكسية. إذا تم حساب المكونات العكسية أثناء التهيئة،
فسيتم إعادة استخدامها في كل استدعاء لـ "inverse_transform".
وإلا، فسيتم إعادة حسابها في كل مرة، الأمر الذي قد يكون مكلفًا. النتيجة دائمًا
كثيفة، حتى إذا كانت "X" مبعثرة.

هنا مثال صغير على الكود يوضح كيفية استخدام ميزة التحويل العكسي::

  >>> import numpy as np
  >>> from sklearn.random_projection import SparseRandomProjection
  >>> X = np.random.rand(100, 10000)
  >>> transformer = SparseRandomProjection(
  ...   compute_inverse_components=True
  ... )
  ...
  >>> X_new = transformer.fit_transform(X)
  >>> X_new.shape
  (100, 3947)
  >>> X_new_inversed = transformer.inverse_transform(X_new)
  >>> X_new_inversed.shape
  (100, 10000)
  >>> X_new_again = transformer.transform(X_new_inversed)
  >>> np.allclose(X_new, X_new_again)
  True