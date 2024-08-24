تحميل مجموعات بيانات أخرى
مجموعات البيانات النموذجية
---------------------

يحتوي Scikit-learn أيضًا على بعض صور JPEG النموذجية التي نشرها مؤلفوها بموجب ترخيص Creative Commons. يمكن أن تكون هذه الصور مفيدة لاختبار الخوارزميات والخطوط الأنابيب على بيانات ثنائية الأبعاد.

.. autosummary::

   load_sample_images
   load_sample_image

.. image:: ../auto_examples/cluster/images/sphx_glr_plot_color_quantization_001.png
   :target: ../auto_examples/cluster/plot_color_quantization.html
   :scale: 30
   :align: right

.. warning::

   يعتمد الترميز الافتراضي للصور على النوع ``uint8`` لتوفير الذاكرة. غالبًا ما تعمل خوارزميات التعلم الآلي بشكل أفضل إذا تم تحويل الإدخال إلى تمثيل النقطة العائمة أولاً. أيضًا، إذا كنت تخطط لاستخدام ``matplotlib.pyplpt.imshow``، فلا تنس التحويل إلى النطاق 0-1 كما هو موضح في المثال التالي.

أمثلة
~~~~~

* :ref:`sphx_glr_auto_examples_cluster_plot_color_quantization.py`

مجموعات البيانات بتنسيق svmlight / libsvm
------------------------------------

تتضمن Scikit-learn وظائف فائدة لتحميل مجموعات البيانات بتنسيق svmlight / libsvm. في هذا التنسيق، يأخذ كل سطر الشكل ``<label> <feature-id>:<feature-value> <feature-id>:<feature-value> ...``. هذا التنسيق مناسب بشكل خاص لمجموعات البيانات المتناثرة.

في هذه الوحدة، يتم استخدام مصفوفات scipy sparse CSR لـ ``X`` ومصفوفات numpy لـ ``y``.

يمكنك تحميل مجموعة بيانات مثل ما يلي::

  >>> from sklearn.datasets import load_svmlight_file
  >>> X_train, y_train = load_svmlight_file("/path/to/train_dataset.txt")
  ...                                                         # doctest: +SKIP

يمكنك أيضًا تحميل مجموعتين (أو أكثر) من مجموعات البيانات في وقت واحد::

  >>> X_train, y_train, X_test, y_test = load_svmlight_files(
  ...     ("/path/to/train_dataset.txt", "/path/to/test_dataset.txt"))
  ...                                                         # doctest: +SKIP

في هذه الحالة، يضمن أن يكون لـ ``X_train`` و ``X_test`` نفس عدد الميزات. هناك طريقة أخرى لتحقيق نفس النتيجة وهي تثبيت عدد الميزات::

  >>> X_test, y_test = load_svmlight_file(
  ...     "/path/to/test_dataset.txt", n_features=X_train.shape[1])
  ...                                                         # doctest: +SKIP

روابط ذات صلة
~~~~~~~~~~~~

- `مجموعات البيانات العامة بتنسيق svmlight / libsvm`: https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets
- `تنفيذ أسرع متوافق مع واجهة برمجة التطبيقات`: https://github.com/mblondel/svmlight-loader

..
    For doctests:

    >>> import numpy as np
    >>> import os

تحميل مجموعات البيانات من مستودع openml.org
---------------------------------------------------

`openml.org <https://openml.org>`_ هو مستودع عام لبيانات التعلم الآلي والتجارب، يسمح لأي شخص بتحميل مجموعات البيانات المفتوحة.

تتمكن حزمة ``sklearn.datasets`` من تنزيل مجموعات البيانات
من المستودع باستخدام الدالة
:func:`sklearn.datasets.fetch_openml`.

على سبيل المثال، لتنزيل مجموعة بيانات تعبيرات جينية في أدمغة الفئران::

  >>> from sklearn.datasets import fetch_openml
  >>> mice = fetch_openml(name='miceprotein', version=4)

لتحديد مجموعة بيانات بشكل كامل، يلزم توفير اسم وإصدار، على الرغم
من أن الإصدار اختياري، راجع :ref:`openml_versions` أدناه.
تحتوي مجموعة البيانات على ما مجموعه 1080 مثالًا تنتمي إلى 8 فئات مختلفة::

  >>> mice.data.shape
  (1080, 77)
  >>> mice.target.shape
  (1080,)
  >>> np.unique(mice.target)
  array(['c-CS-m', 'c-CS-s', 'c-SC-m', 'c-SC-s', 't-CS-m', 't-CS-s', 't-SC-m', 't-SC-s'], dtype=object)

يمكنك الحصول على مزيد من المعلومات حول مجموعة البيانات عن طريق النظر في سمات ``DESCR``
و ``details``::

  >>> print(mice.DESCR) # doctest: +SKIP
  **Author**: Clara Higuera, Katheleen J. Gardiner, Krzysztof J. Cios
  **Source**: [UCI](https://archive.ics.uci.edu/ml/datasets/Mice+Protein+Expression) - 2015
  **Please cite**: Higuera C, Gardiner KJ, Cios KJ (2015) Self-Organizing
  Feature Maps Identify Proteins Critical to Learning in a Mouse Model of Down
  Syndrome. PLoS ONE 10(6): e0129126...

  >>> mice.details # doctest: +SKIP
  {'id': '40966', 'name': 'MiceProtein', 'version': '4', 'format': 'ARFF',
  'upload_date': '2017-11-08T16:00:15', 'licence': 'Public',
  'url': 'https://www.openml.org/data/v1/download/17928620/MiceProtein.arff',
  'file_id': '17928620', 'default_target_attribute': 'class',
  'row_id_attribute': 'MouseID',
  'ignore_attribute': ['Genotype', 'Treatment', 'Behavior'],
  'tag': ['OpenML-CC18', 'study_135', 'study_98', 'study_99'],
  'visibility': 'public', 'status': 'active',
  'md5_checksum': '3c479a6885bfa0438971388283a1ce32'}


يحتوي ``DESCR`` على وصف نصي حر للبيانات، بينما يحتوي ``details``
على قاموس من البيانات الوصفية المخزنة بواسطة openml، مثل معرف مجموعة البيانات.
لمزيد من التفاصيل، راجع `وثائق OpenML
<https://docs.openml.org/#data>`_ معرف البيانات الخاص بمجموعة بيانات بروتين الفئران
هو 40966، ويمكنك استخدام هذا (أو الاسم) للحصول على مزيد من المعلومات حول
مجموعة البيانات على موقع openml::

  >>> mice.url
  'https://www.openml.org/d/40966'

يحدد ``data_id`` أيضًا مجموعة بيانات من OpenML بشكل فريد::

  >>> mice = fetch_openml(data_id=40966)
  >>> mice.details # doctest: +SKIP
  {'id': '4550', 'name': 'MiceProtein', 'version': '1', 'format': 'ARFF',
  'creator': ...,
  'upload_date': '2016-02-17T14:32:49', 'licence': 'Public', 'url':
  'https://www.openml.org/data/v1/download/1804243/MiceProtein.ARFF', 'file_id':
  '1804243', 'default_target_attribute': 'class', 'citation': 'Higuera C,
  Gardiner KJ, Cios KJ (2015) Self-Organizing Feature Maps Identify Proteins
  Critical to Learning in a Mouse Model of Down Syndrome. PLoS ONE 10(6):
  e0129126. [Web Link] journal.pone.0129126', 'tag': ['OpenML100', 'study_14',
  'study_34'], 'visibility': 'public', 'status': 'active', 'md5_checksum':
  '3c479a6885bfa0438971388283a1ce32'}

إصدارات مجموعة البيانات
~~~~~~~~~~~~~~~~

يتم تحديد مجموعة البيانات بشكل فريد بواسطة ``data_id``، ولكن ليس بالضرورة بالاسم. يمكن أن توجد عدة "إصدارات" مختلفة لمجموعة بيانات بنفس الاسم والتي قد تحتوي على مجموعات بيانات مختلفة تمامًا.
إذا تم العثور على إصدار معين من مجموعة بيانات بها مشكلات كبيرة، فقد يتم إلغاء تنشيطه. يؤدي استخدام اسم لتحديد مجموعة بيانات إلى الإصدار الأقدم من مجموعة البيانات التي لا تزال نشطة. وهذا يعني أن ``fetch_openml(name="miceprotein")`` يمكن أن ينتج نتائج مختلفة
في أوقات مختلفة إذا أصبحت الإصدارات السابقة غير نشطة.
يمكنك أن ترى أن مجموعة البيانات التي تحتوي على ``data_id`` 40966 التي استخرجناها أعلاه
هي الإصدار الأول من مجموعة بيانات "miceprotein"::

  >>> mice.details['version']  #doctest: +SKIP
  '1'

في الواقع، لدى هذه المجموعة من البيانات إصدار واحد فقط. من ناحية أخرى، تحتوي مجموعة بيانات Iris على إصدارات متعددة::

  >>> iris = fetch_openml(name="iris")
  >>> iris.details['version']  #doctest: +SKIP
  '1'
  >>> iris.details['id']  #doctest: +SKIP
  '61'

  >>> iris_61 = fetch_openml(data_id=61)
  >>> iris_61.details['version']
  '1'
  >>> iris_61.details['id']
  '61'

  >>> iris_969 = fetch_openml(data_id=969)
  >>> iris_969.details['version']
  '3'
  >>> iris_969.details['id']
  '969'

يؤدي تحديد مجموعة البيانات بالاسم "iris" إلى الإصدار الأدنى، الإصدار 1،
مع ``data_id`` 61. لضمان الحصول دائمًا على هذه المجموعة من البيانات بالضبط، من الأكثر أمانًا تحديدها بواسطة معرف مجموعة البيانات ``data_id``. تحتوي المجموعة الأخرى، التي تحتوي على ``data_id`` 969، على الإصدار 3 (أصبح الإصدار 2 غير نشط)، وتحتوي على نسخة مُرقَّمة من البيانات::

  >>> np.unique(iris_969.target)
  array(['N', 'P'], dtype=object)

يمكنك أيضًا تحديد كل من الاسم والإصدار، والذي يحدد أيضًا مجموعة البيانات بشكل فريد::

  >>> iris_version_3 = fetch_openml(name="iris", version=3)
  >>> iris_version_3.details['version']
  '3'
  >>> iris_version_3.details['id']
  '969'


المراجع
~~~~~~~

* :arxiv:`Vanschoren, van Rijn, Bischl and Torgo. "OpenML: networked science in
  machine learning" ACM SIGKDD Explorations Newsletter, 15(2), 49-60, 2014.
  <1407.7722>`

محلل تنسيق ملف ARFF
~~~~~~~~~~~

اعتبارًا من الإصدار 1.2، توفر Scikit-learn وسيطًا جديدًا للكلمة الرئيسية `parser` يوفر عدة خيارات لتحليل ملفات ARFF التي يوفرها OpenML. المحلل القديم (أي `parser="liac-arff"`) يعتمد على مشروع
`LIAC-ARFF <https://github.com/renatopp/liac-arff>`_. ومع ذلك،
فهو بطيء ويستهلك ذاكرة أكثر مما هو مطلوب. المحلل الجديد القائم على pandas
(أي `parser="pandas"`) أسرع وأكثر كفاءة في استخدام الذاكرة.
ومع ذلك، لا يدعم هذا المحلل البيانات المتناثرة.
لذلك، نوصي باستخدام `parser="auto"` والذي سيستخدم أفضل محلل متاح لمجموعة البيانات المطلوبة.

يمكن أن يؤدي استخدام محللي "pandas" و "liac-arff" إلى أنواع بيانات مختلفة في
الإخراج. الاختلافات الملحوظة هي ما يلي:

- يستخدم محلل "liac-arff" دائمًا ترميز الميزات الفئوية ككائنات ``str``. على العكس من ذلك، يستنتج محلل "pandas" النوع أثناء القراءة ويتم تحويل الفئات الرقمية إلى أعداد صحيحة كلما أمكن ذلك.
- يستخدم محلل "liac-arff" float64 لترميز الميزات الرقمية التي تم وضع علامة عليها باسم 'REAL' و 'NUMERICAL' في البيانات الوصفية. يستنتج محلل "pandas" ما إذا كانت هذه الميزات الرقمية تتوافق مع الأعداد الصحيحة ويستخدم نوع بيانات التمديد Integer من pandas.
- على وجه الخصوص، يتم تحميل مجموعات بيانات التصنيف ذات الفئات الصحيحة بشكل نموذجي مثل (0، 1، ...) باستخدام محلل "pandas" بينما سيفرض "liac-arff" استخدام تسميات الفئات المقتبسة مثل "0" و" 1 "وهكذا.
- لن يقوم محلل "pandas" بإزالة علامات الاقتباس الفردية - أي `'` - من أعمدة النص. على سبيل المثال، سيتم الاحتفاظ بسلسلة 'my string' كما هي بينما سيقوم محلل "liac-arff" بإزالة علامات الاقتباس الفردية. بالنسبة للأعمدة الفئوية، يتم إزالة علامات الاقتباس الفردية من القيم.

بالإضافة إلى ذلك، عند استخدام `as_frame=False`، يعيد محلل "liac-arff" بيانات مشفرة ترتيبياً حيث يتم توفير الفئات في السمة
`categories` من مثيل `Bunch`. من ناحية أخرى، يعيد "pandas" مصفوفة NumPy حيث الفئات. ثم يتولى المستخدم تصميم خط أنابيب هندسة الميزات باستخدام مثيل من  `OneHotEncoder` أو
`OrdinalEncoder` ملفوف عادةً في `ColumnTransformer` لمعالجة الأعمدة الفئوية بشكل صريح. راجع على سبيل المثال: :ref:`sphx_glr_auto_examples_compose_plot_column_transformer_mixed_types.py`.

تحميل من مجموعات البيانات الخارجية
يعمل scikit-learn على أي بيانات رقمية مخزنة على شكل مصفوفات نومبي أو مصفوفات متفرقة من سايسبي. كما يتم قبول الأنواع الأخرى القابلة للتحويل إلى مصفوفات رقمية مثل بانداس داتا فريم.

فيما يلي بعض الطرق الموصى بها لتحميل البيانات العمودية القياسية إلى تنسيق يمكن لـ scikit-learn استخدامه:

* يوفر "بانداس.آي.أو <https://pandas.pydata.org/pandas-docs/stable/io.html>`_" أدوات لقراءة البيانات من التنسيقات الشائعة بما في ذلك CSV و Excel و JSON و SQL. يمكن أيضًا بناء أطر البيانات من قوائم tupples أو القواميس. تتعامل Pandas بسلاسة مع البيانات غير المتجانسة وتوفر أدوات للمناورة والتحويل إلى مصفوفة رقمية مناسبة لـ scikit-learn.

* "سايسبي.آي.أو <https://docs.scipy.org/doc/scipy/reference/io.html>`_" متخصص في التنسيقات الثنائية المستخدمة غالبًا في سياق الحوسبة العلمية مثل .mat و .arff

* "نومبي/روتينز.آي.أو <https://docs.scipy.org/doc/numpy/reference/routines.io.html>`_" لتحميل البيانات العمودية القياسية إلى مصفوفات نومبي

* "سكيت-ليرن لود_سفلمايت_فايل" scikit-learn's :func:`load_svmlight_file` لتنسيق svmlight أو libSVM المتناثر

* "سكيت-ليرن لود_فايلز" scikit-learn's :func:`load_files` لدلائل ملفات النص حيث يكون اسم كل دليل هو اسم كل فئة وكل ملف داخل كل دليل يقابل عينة من تلك الفئة

بالنسبة لبعض البيانات المتنوعة مثل الصور ومقاطع الفيديو والصوت، قد ترغب في الرجوع إلى ما يلي:

* "سكيماج.آي.أو <https://scikit-image.org/docs/dev/api/skimage.io.html>`_" أو "إيماجيو <https://imageio.readthedocs.io/en/stable/reference/core_v3.html>`_" لتحميل الصور ومقاطع الفيديو إلى مصفوفات نومبي

* "سايس.آي.أو.واففيل.ريد <https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.read.html>`_" لقراءة ملفات WAV في مصفوفة نومبي

ستحتاج الميزات الفئوية (أو الاسمية) المخزنة على شكل سلاسل (شائعة في أطر بيانات بانداس) إلى التحويل إلى ميزات رقمية باستخدام "سكيليرن.بريبيروسيسينغ.وانهوتينكودر" :class:`~sklearn.preprocessing.OneHotEncoder` أو "سكيليرن.بريبيروسيسينغ.أوردينالينكودر" :class:`~sklearn.preprocessing.OrdinalEncoder` أو ما شابه. راجع :ref:`preprocessing`.

ملاحظة: إذا كنت تدير بياناتك الرقمية الخاصة، فمن المستحسن استخدام تنسيق ملف محسن مثل HDF5 لتقليل أوقات تحميل البيانات. توفر مكتبات مختلفة مثل H5Py و PyTables و pandas واجهة برمجة تطبيقات Python لقراءة البيانات وكتابتها بهذا التنسيق.