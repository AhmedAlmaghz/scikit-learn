في هذا القسم من دليل المستخدم، نغطي الوظائف المتعلقة بمشاكل التعلم المتعددة، بما في ذلك: multiclass و multilabel و multioutput classification والانحدار.

تنفذ الوحدات النمطية في هذا القسم المصطلح: meta-estimators، والذي يتطلب توفير مُقدِّر أساسي في بنائه. تمدد برامج meta-estimators وظائف المُقدِّر الأساسي لدعم مشاكل التعلم المتعددة، ويتم تحقيق ذلك عن طريق تحويل مشكلة التعلم المتعدد إلى مجموعة من المشكلات البسيطة، ثم تناسب مُقدِّرًا واحدًا لكل مشكلة.

يغطي هذا القسم وحدتين نمطيتين: sklearn.multiclass و sklearn.multioutput. يوضح الرسم البياني أدناه أنواع المشكلات التي تتحمل كل وحدة نمطية مسؤوليتها، والمُقدِّرات meta-estimators المقابلة التي توفرها كل وحدة نمطية.

يوفر الجدول أدناه مرجعًا سريعًا حول الاختلافات بين أنواع المشكلات. يمكن العثور على تفسيرات أكثر تفصيلاً في الأقسام اللاحقة من هذا الدليل.

| | عدد الأهداف | قابلية الهدف | صالح | |
| | --- | --- | --- | --- |
| التصنيف متعدد الفئات | 1 | >2 | 'multiclass' |
| | | | | |
| تصنيف متعدد البطاقات | >1 | 2 (0 أو 1) | 'multilabel-indicator' |
| | | | | |
| تصنيف متعدد الفئات ومتعدد الإخراج | >1 | >2 | 'multiclass-multioutput' |
| | | | | |
| الانحدار متعدد الإخراج | >1 | مستمر | 'continuous-multioutput' |

فيما يلي ملخص لمُقدِّرات scikit-learn التي تدعم التعلم المتعدد المدمج، مجمعة حسب الاستراتيجية. لا تحتاج إلى برامج meta-estimators التي يوفرها هذا القسم إذا كنت تستخدم أحد هذه المُقدِّرات. ومع ذلك، يمكن أن توفر برامج meta-estimators استراتيجيات إضافية تتجاوز المدمج:

- **متعدد الفئات بشكل متأصل:**

  - naive_bayes.BernoulliNB
  - tree.DecisionTreeClassifier
  - tree.ExtraTreeClassifier
  - ensemble.ExtraTreesClassifier
  - naive_bayes.GaussianNB
  - neighbors.KNeighborsClassifier
  - semi_supervised.LabelPropagation
  - semi_supervised.LabelSpreading
  - discriminant_analysis.LinearDiscriminantAnalysis
  - svm.LinearSVC (تعيين multi_class="crammer_singer")
  - linear_model.LogisticRegression (مع معظم المحللين)
  - linear_model.LogisticRegressionCV (مع معظم المحللين)
  - neural_network.MLPClassifier
  - neighbors.NearestCentroid
  - discriminant_analysis.QuadraticDiscriminantAnalysis
  - neighbors.RadiusNeighborsClassifier
  - ensemble.RandomForestClassifier
  - linear_model.RidgeClassifier
  - linear_model.RidgeClassifierCV

- **متعدد الفئات كواحد مقابل واحد:**

  - svm.NuSVC
  - svm.SVC.
  - gaussian_process.GaussianProcessClassifier (تعيين multi_class = "one_vs_one")

- **متعدد الفئات كواحد مقابل الباقي:**

  - ensemble.GradientBoostingClassifier
  - gaussian_process.GaussianProcessClassifier (تعيين multi_class = "one_vs_rest")
  - svm.LinearSVC (تعيين multi_class="ovr")
  - linear_model.LogisticRegression (معظم المحللين)
  - linear_model.LogisticRegressionCV (معظم المحللين)
  - linear_model.SGDClassifier
  - linear_model.Perceptron
  - linear_model.PassiveAggressiveClassifier

- **دعم التصنيف متعدد البطاقات:**

  - tree.DecisionTreeClassifier
  - tree.ExtraTreeClassifier
  - ensemble.ExtraTreesClassifier
  - neighbors.KNeighborsClassifier
  - neural_network.MLPClassifier
  - neighbors.RadiusNeighborsClassifier
  - ensemble.RandomForestClassifier
  - linear_model.RidgeClassifier
  - linear_model.RidgeClassifierCV

- **دعم التصنيف متعدد الفئات ومتعدد الإخراج:**

  - tree.DecisionTreeClassifier
  - tree.ExtraTreeClassifier
  - ensemble.ExtraTreesClassifier
  - neighbors.KNeighborsClassifier
  - neighbors.RadiusNeighborsClassifier
  - ensemble.RandomForestClassifier

التصنيف متعدد الفئات
تحذير: جميع المصنفات في scikit-learn تقوم بالتصنيف متعدد الفئات بشكل افتراضي. لا تحتاج إلى استخدام نموذج sklearn.multiclass ما لم ترغب في تجربة استراتيجيات متعددة الفئات المختلفة.

التصنيف متعدد الفئات هو مهمة تصنيف تحتوي على أكثر من فئتين. يمكن وضع علامة على كل عينة على أنها تنتمي إلى فئة واحدة فقط.

على سبيل المثال، التصنيف باستخدام الميزات المستخرجة من مجموعة من الصور للفواكه، حيث قد تكون كل صورة إما برتقال أو تفاح أو كمثرى. كل صورة هي عينة واحدة ويتم وضع علامة عليها على أنها واحدة من الفئات الثلاث الممكنة. يفترض التصنيف متعدد الفئات أن كل عينة يتم تعيينها إلى فئة واحدة فقط - على سبيل المثال، لا يمكن أن تكون العينة الواحدة تفاحة وكمثرى في نفس الوقت.

في حين أن جميع مصنفات scikit-learn قادرة على التصنيف متعدد الفئات، فإن المصنفات الفوقية التي يوفرها sklearn.multiclass تسمح بتغيير طريقة تعاملها مع أكثر من فئتين، لأن هذا قد يكون له تأثير على أداء المصنف (من حيث خطأ التعميم أو موارد الكمبيوتر المطلوبة).

تنسيق الهدف
-----

تمثيلات متعددة الفئات الصالحة لـ sklearn.utils.multiclass.type_of_target (y) هي:

- مصفوفة 1D أو متجه عمودي يحتوي على قيم منفصلة أكثر من اثنين. مثال على متجه y لعينات 4:

>>> استيراد نومبي كما np
>>> y = np.array(['apple', 'pear', 'apple', 'orange'])
>>> طباعة (y)
['apple' 'pear' 'apple' 'orange']

- مصفوفة ثنائية كثيفة أو مبعثرة الشكل (n_samples، n_classes) مع عينة واحدة لكل صف، حيث يمثل كل عمود فئة واحدة. مثال على مصفوفة ثنائية كثيفة ومبعثرة y لعينات 4، حيث الأعمدة، بالترتيب، هي التفاح والبرتقال والكمثرى:

>>> استيراد نومبي كما np
>>> من sklearn.preprocessing استيراد LabelBinarizer
>>> y = np.array(['apple', 'pear', 'apple', 'orange'])
>>> y_dense = LabelBinarizer().fit_transform(y)
>>> طباعة (y_dense)
[[1 0 0]
 [0 0 1]
 [1 0 0]
 [0 1 0]]
>>> من scipy استيراد متفرق
>>> y_sparse = sparse.csr_matrix(y_dense)
>>> طباعة (y_sparse)
<Compressed Sparse Row sparse matrix of dtype 'int64'
with 4 stored elements in Compressed Sparse Row format>

للحصول على مزيد من المعلومات حول sklearn.preprocessing.LabelBinarizer، راجع preprocessing_targets.

OneVsRestClassifier
-------------------

تتمثل استراتيجية one-vs-rest، المعروفة أيضًا باسم one-vs-all، في sklearn.multiclass.OneVsRestClassifier. تتكون الاستراتيجية من ملاءمة مصنف واحد لكل فئة. لكل مصنف، يتم ضبط الفئة مقابل جميع الفئات الأخرى. بالإضافة إلى كفاءتها الحسابية (فقط n_classes من المصنفات مطلوبة)، تتمثل إحدى مزايا هذا النهج في إمكانية تفسيره. نظرًا لأن كل فئة ممثلة بمصنف واحد فقط، فمن الممكن اكتساب معرفة حول الفئة عن طريق فحص مصنفها المقابل. هذه هي الاستراتيجية الأكثر استخدامًا بشكل شائع وهي خيار افتراضي عادل.

فيما يلي مثال على التعلم متعدد الفئات باستخدام OvR::

>>> من sklearn استيراد مجموعات البيانات
>>> من sklearn.multiclass استيراد OneVsRestClassifier
>>> من sklearn.svm استيراد LinearSVC
>>> X، y = datasets.load_iris (return_X_y = True)
>>> OneVsRestClassifier (LinearSVC (random_state = 0)). fit (X، y). predict (X)
array ([0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0،
0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0،
0، 0، 0، 0، 1، 1، 1، 1، 1، 1، 1، 1، 1، 1، 1، 1، 1، 1، 1، 1، 1، 1، 1،
1، 2، 1، 1، 1، 1، 1، 1، 1، 1، 1، 1، 1، 1، 2، 2، 1، 1، 1، 1، 1، 1،
1، 1، 1، 1، 1، 1، 1، 1، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2،
2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2])


يدعم sklearn.multiclass.OneVsRestClassifier أيضًا التصنيف متعدد التصنيفات. لاستخدام هذه الميزة، قم بتغذية المصنف بمصفوفة مؤشرات، حيث تشير الخلية [i، j] إلى وجود تسمية j في العينة i.

OneVsOneClassifier
------------------

يقوم sklearn.multiclass.OneVsOneClassifier ببناء مصنف واحد لكل زوج من الفئات. في وقت التنبؤ، يتم اختيار الفئة التي حصلت على أكبر عدد من الأصوات. في حالة التعادل (بين فئتين بعدد متساوٍ من الأصوات)، فإنه يختار الفئة ذات مستوى الثقة الأعلى في التصنيف التراكمي عن طريق جمع مستويات الثقة في التصنيف الثنائي المحسوب بواسطة المصنفات الأساسية.

نظرًا لأنه يتطلب ضبط n_classes * (n_classes - 1) / 2 من المصنفات، فإن هذه الطريقة تكون عادةً أبطأ من one-vs-the-rest، بسبب تعقيدها O (n_classes^2). ومع ذلك، قد تكون هذه الطريقة مفيدة للخوارزميات مثل خوارزميات النواة التي لا تتوسع جيدًا مع n_samples. ويرجع ذلك إلى أن كل مشكلة تعلم فردية لا تنطوي إلا على مجموعة فرعية صغيرة من البيانات، في حين أنه باستخدام one-vs-the-rest، يتم استخدام مجموعة البيانات الكاملة n_classes مرات. دالة القرار هي نتيجة تحويل أحادي الاتجاه للتصنيف أحادي الاتجاه.

فيما يلي مثال على التعلم متعدد الفئات باستخدام OvO::

>>> من sklearn استيراد مجموعات البيانات
>>> من sklearn.multiclass استيراد OneVsOneClassifier
>>> من sklearn.svm استيراد LinearSVC
>>> X، y = datasets.load_iris (return_X_y = True)
>>> OneVsOneClassifier (LinearSVC (random_state = 0)). fit (X، y). predict (X)
array ([0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0،
0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0،
0، 0، 0، 0، 1، 1، 1، 1، 1، 1، 1، 1، 1، 1، 1، 1، 1، 1، 1، 1، 1، 1، 1،
1، 2، 1، 2، 1، 1، 1، 1، 1، 1، 1، 1، 1، 1، 2، 1، 1، 1، 1، 1، 1، 1،
1، 1، 1، 1، 1، 1، 1، 1، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2،
2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2])

المراجع
------

- "النمط والتعرف الآلي والتعلم الآلي. سبرينغر"، كريستوفر م. بيشوب، الصفحة 183، (الطبعة الأولى)

OutputCodeClassifier
--------------------

تختلف استراتيجيات Output-Correcting Output Code اختلافًا كبيرًا عن one-vs-the-rest وone-vs-one. في هذه الاستراتيجيات، يتم تمثيل كل فئة في مساحة أوروبية، حيث يمكن أن يكون كل بُعد إما 0 أو 1. وبعبارة أخرى، يتم تمثيل كل فئة بواسطة رمز ثنائي (مصفوفة من 0 و1). تسمى المصفوفة التي تحتفظ بموقع/رمز كل فئة باسم كتاب الرموز. حجم الرمز هو أبعادية المساحة المذكورة. بديهيا، يجب تمثيل كل فئة برمز فريد قدر الإمكان، وينبغي تصميم كتاب رموز جيد لتحسين دقة التصنيف. في هذا التنفيذ، نستخدم ببساطة كتاب رموز تم إنشاؤه بشكل عشوائي كما هو موضح في [3]_ على الرغم من أنه قد يتم إضافة طرق أكثر تعقيدًا في المستقبل.

في وقت الضبط، يتم ضبط مصنف ثنائي واحد لكل بت في كتاب الرموز. في وقت التنبؤ، يتم استخدام المصنفات لمشروع النقاط الجديدة في مساحة الفئة ويتم اختيار الفئة الأقرب إلى النقاط.

في sklearn.multiclass.OutputCodeClassifier، يسمح سمة code_size للمستخدم بالتحكم في عدد المصنفات التي سيتم استخدامها. إنها نسبة مئوية من العدد الإجمالي للفئات.

سيؤدي الرقم الذي يتراوح بين 0 و1 إلى تقليل عدد المصنفات المطلوبة مقارنةً بـ one-vs-the-rest. من الناحية النظرية، فإن "log2 (n_classes) / n_classes" كافٍ لتمثيل كل فئة بشكل لا لبس فيه. ومع ذلك، في الممارسة العملية، قد لا يؤدي ذلك إلى دقة جيدة نظرًا لأن "log2 (n_classes)" أصغر بكثير من "n_classes".

سيؤدي الرقم الذي يزيد عن 1 إلى زيادة عدد المصنفات المطلوبة مقارنةً بـ one-vs-the-rest. في هذه الحالة، سيقوم بعض المصنفين من الناحية النظرية بتصحيح أخطاء المصنفين الآخرين، ومن هنا جاء اسم "تصحيح الخطأ". ومع ذلك، في الممارسة العملية، قد لا يحدث ذلك حيث من المحتمل أن تكون أخطاء المصنف مرتبطة. تعمل رموز الإخراج التصحيحية على تصحيح الأخطاء بشكل مشابه لتصنيف Bagging.

فيما يلي مثال على التعلم متعدد الفئات باستخدام رموز الإخراج::

>>> من sklearn استيراد مجموعات البيانات
>>> من sklearn.multiclass استيراد OutputCodeClassifier
>>> من sklearn.svm استيراد LinearSVC
>>> X، y = datasets.load_iris (return_X_y = True)
>>> clf = OutputCodeClassifier (LinearSVC (random_state = 0)، code_size = 2، random_state = 0)
>>> clf.fit (X، y). predict (X)
array ([0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0،
0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0، 0،
0، 0، 0، 0، 1، 1، 1، 1، 1، 1، 2، 1، 1، 1، 1، 1، 1، 1، 1، 1، 2، 1، 1،
1، 2، 1، 1، 1، 1، 1، 1، 2، 1، 1، 1، 1، 1، 2، 2، 2، 1، 1، 1، 1، 1، 1،
1، 1، 1، 1، 1، 1، 1، 1، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2،
2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2، 2])

المراجع
------

- "حل مشكلات التعلم متعدد الفئات عبر رموز الإخراج التصحيحية"، Dietterich T.، Bakiri G.، Journal of Artificial Intelligence Research 2، 1995.

- "طريقة الترميز التصحيحي ورسومات PICTs"، James G.، Hastie T.، Journal of Computational and Graphical statistics 7، 1998.

- "عناصر التعلم الإحصائي"، Hastie T.، Tibshirani R.، Friedman J.، الصفحة 606 (الطبعة الثانية)، 2008.

التصنيف متعدد التصنيفات
**التصنيف متعدد التصنيفات** (المتعلق ارتباطًا وثيقًا بـ **التصنيف متعدد المخرجات**) هي مهمة تصنيف يتم فيها وضع علامة على كل عينة باستخدام "m" تسميات من "n_classes" من الفئات المحتملة، حيث يمكن أن تكون "m" من 0 إلى "n_classes" بما في ذلك. يمكن اعتبار هذا كتوقع خصائص العينة التي ليست حصرية متبادلة. رسميًا، يتم تعيين إخراج ثنائي لكل فئة، لكل عينة. يتم الإشارة إلى الفئات الإيجابية بـ 1 والفئات السلبية بـ 0 أو -1. وبالتالي، يمكن مقارنته بتشغيل "n_classes" من مهام التصنيف الثنائية، على سبيل المثال مع: class: ~ sklearn.multioutput.MultiOutputClassifier. تعامل هذه الطريقة كل تسمية بشكل مستقل في حين أن مصنفات التصنيفات المتعددة *قد* تعامل الفئات المتعددة في وقت واحد، مع مراعاة السلوك المترابط بينها.

على سبيل المثال، التنبؤ بالموضوعات ذات الصلة بوثيقة نصية أو فيديو. قد تكون الوثيقة أو الفيديو حول أحد "الدين" أو "السياسة" أو "المالية" أو "التعليم"، أو العديد من فئات الموضوعات أو جميع فئات الموضوعات.

تنسيق الهدف
-------------

تمثيل صالح لـ: مصطلح: multilabel `y` هو مصفوفة ثنائية كثيفة أو مبعثرة الشكل: term: `(n_samples، n_classes)`. يمثل كل عمود فئة. تشير "1" في كل صف إلى الفئات الإيجابية التي تم وضع علامة على العينة بها. مثال على مصفوفة كثيفة "y" لثلاث عينات:

  >>> y = np.array ([[1،0،0،1]، [0،0،1،1]، [0،0،0،0]])
  >>> print (ي)
  [[1 0 0 1]
   [0 0 1 1]
   [0 0 0 0]]

يمكن أيضًا إنشاء مصفوفات ثنائية كثيفة باستخدام: class: ~ sklearn.preprocessing.MultiLabelBinarizer. لمزيد من المعلومات، راجع: ref: preprocessing_targets.

مثال على نفس "y" في شكل مصفوفة مبعثرة:

  >>> y_sparse = sparse.csr_matrix (y)
  >>> print (y_sparse)
  <مصفوفة مبعثرة صف مضغوط من النوع 'int64'
    مع 4 عناصر مخزنة وشكل (3، 4)>
    Coords	القيم
    (0، 0)	1
    (0، 3)	1
    (1، 2)	1
    (1، 3)	1

.. _multioutputclassfier:

MultiOutputClassifier
---------------------

يمكن إضافة دعم التصنيف متعدد التصنيفات إلى أي مصنف باستخدام: class: ~ sklearn.multioutput.MultiOutputClassifier. تتكون هذه الاستراتيجية من ملاءمة مصنف واحد لكل هدف. يسمح هذا بالتصنيفات متعددة المتغيرات المستهدفة. الغرض من هذه الفئة هو توسيع المقدرين
لتكون قادرة على تقدير سلسلة من وظائف الهدف (f1، f2، f3 ...، fn)
التي يتم تدريبها على مصفوفة X متغير تنبؤ واحد للتنبؤ بسلسلة
من الاستجابات (y1، y2، y3 ...، yn).

يمكنك العثور على مثال للاستخدام
: class: ~ sklearn.multioutput.MultiOutputClassifier
كجزء من القسم: ref: multiclass_multioutput_classification
نظرًا لأنه تعميم لتصنيف التصنيفات المتعددة على
مخرجات متعددة الفئات بدلاً من المخرجات الثنائية.

.. _classifierchain:

ClassifierChain
---------------

سلاسل المصنفات (راجع: class: ~ sklearn.multioutput.ClassifierChain) هي طريقة
لدمج عدد من المصنفات الثنائية في نموذج تصنيف واحد متعدد التسميات
قادر على استغلال الارتباطات بين الأهداف.

بالنسبة لمشكلة التصنيف متعدد التصنيفات ذات الفئات N، يتم تعيين N من المصنفات الثنائية
رقم صحيح بين 0 و N-1. تحدد هذه الأعداد الصحيحة ترتيب النماذج في السلسلة. ثم يتم ضبط كل مصنف على بيانات التدريب المتاحة بالإضافة إلى التسميات الصحيحة للفئات التي تم تعيين نماذجها لرقم أقل.

عند التنبؤ، لن تكون التسميات الصحيحة متاحة. بدلاً من ذلك، يتم تمرير تنبؤات كل نموذج إلى النماذج اللاحقة في
السلسلة لاستخدامها كميزات.

من الواضح أن ترتيب السلسلة مهم. لا يحتوي النموذج الأول في السلسلة على أي معلومات حول التسميات الأخرى في حين أن النموذج الأخير في السلسلة لديه ميزات تشير إلى وجود جميع التسميات الأخرى. بشكل عام
لا يعرف المرء الترتيب الأمثل للنماذج في السلسلة، لذلك عادة ما يتم ضبط العديد من السلاسل ذات الترتيب العشوائي ويتم حساب متوسط تنبؤاتها معًا.

.. rubric:: المراجع

* جيسي ريد، بيرنهارد بفارينجر، جيف هولمز، إيب فرانك،
  "سلاسل المصنفات للتصنيف متعدد التصنيفات"، 2009.

.. _multiclass_multioutput_classification:

تصنيف متعدد الفئات متعدد المخرجات
=====================================

**تصنيف متعدد الفئات متعدد المخرجات**
(المعروف أيضًا باسم **تصنيف المهام المتعددة**) هي
مهمة تصنيف يتم فيها وضع علامة على كل عينة بمجموعة من الخصائص **غير الثنائية**. كل من عدد الخصائص
عدد الفئات
لكل خاصية أكبر من 2. وبالتالي، فإن المقدر الفردي
يتعامل مع العديد من مهام التصنيف المشتركة. هذا هو تعميم ل
مهمة التصنيف متعددة *التسميات*، والتي تنظر فقط في السمات الثنائية، وكذلك تعميم
مهمة التصنيف متعددة *الفئات*، حيث يتم النظر في خاصية واحدة فقط.

على سبيل المثال، تصنيف خصائص "نوع الفاكهة" و "اللون"
لمجموعة من الصور الفاكهة. تحتوي الخاصية "نوع الفاكهة" على الفئات المحتملة: "تفاحة" و "كمثرى" و "برتقال". تحتوي الخاصية "اللون" على الفئات المحتملة: "أخضر" و "أحمر" و "أصفر" و "برتقالي". كل عينة هي
صورة فاكهة، يتم إخراج تسمية لكل من الخصائص وكل تسمية
هي واحدة من الفئات المحتملة للخاصية المقابلة.

لاحظ أن جميع المصنفات التي تتعامل مع التصنيف متعدد الفئات متعدد المخرجات (المعروف أيضًا باسم
تصنيف المهام المتعددة) المهام، تدعم مهمة التصنيف متعدد التصنيفات كحالة خاصة. يشبه تصنيف المهام المتعددة مهمة التصنيف متعددة المخرجات مع صيغ نماذج مختلفة. لمزيد من المعلومات،
راجع وثائق المقدر ذات الصلة.

فيما يلي مثال على التصنيف متعدد الفئات متعدد المخرجات:

    >>> من sklearn.datasets import make_classification
    >>> من sklearn.multioutput import MultiOutputClassifier
    >>> من sklearn.ensemble import RandomForestClassifier
    >>> من sklearn.utils import shuffle
    >>> استيراد numpy as np
    >>> X، y1 = make_classification (n_samples = 10، n_features = 100،
    ...                             n_informative = 30، n_classes = 3،
    ...                             random_state = 1)
    >>> y2 = shuffle (y1، random_state = 1)
    >>> y3 = shuffle (y1، random_state = 2)
    >>> Y = np.vstack ((y1، y2، y3)). T
    >>> n_samples، n_features = X.shape # 10،100
    >>> n_outputs = Y.shape [1] # 3
    >>> n_classes = 3
    >>> forest = RandomForestClassifier (random_state = 1)
    >>> multi_target_forest = MultiOutputClassifier (forest، n_jobs = 2)
    >>> multi_target_forest.fit (X، Y). predict (X)
    array ([[2، 2، 0]
           [1، 2، 1]
           [2، 1، 0]
           [0، 0، 2]
           [0، 2، 1]
           [0، 0، 2]
           [1، 1، 0]
           [1، 1، 1]
           [0، 0، 2]
           [2، 0، 0]])

.. warning::
    في الوقت الحالي، لا توجد مقاييس في: mod: sklearn.metrics
    يدعم مهمة التصنيف متعدد الفئات متعدد المخرجات.

تنسيق الهدف
-------------

تمثيل صالح لـ: مصطلح: multioutput `y` هو مصفوفة كثيفة الشكل
`` (n_samples، n_classes) '' من تسميات الفئات. دمج عامودي لـ 1d
: مصطلح: متغيرات متعددة الفئات. مثال على "y" لثلاث عينات:

  >>> y = np.array ([['apple'، 'green']، ['orange'، 'orange']، ['pear'، 'green']])
  >>> print (y)
  [['apple' 'green']
   ['orange' 'orange']
   ['pear' 'green']]

.. _multioutput_regression:

الانحدار متعدد المخرجات
======================

**الانحدار متعدد المخرجات** يتنبأ بعدة خصائص رقمية لكل
عينة. كل خاصية هي متغير رقمي وعدد الخصائص
يتم التنبؤ بها لكل عينة أكبر من أو يساوي 2. بعض المقدرات التي تدعم الانحدار متعدد المخرجات أسرع من مجرد تشغيل "n_output"
المقدرات.

على سبيل المثال، التنبؤ بكل من سرعة الرياح واتجاه الرياح، بالدرجات،
باستخدام البيانات التي تم الحصول عليها من موقع معين. ستكون كل عينة بيانات
تم الحصول عليها من موقع واحد وسيتم إخراج كل من سرعة الرياح واتجاهها
بالنسبة لكل عينة.

تعتبر أدوات الانحدار التالية أصلية تدعم الانحدار متعدد المخرجات:

  - : class: `cross_decomposition.CCA`
  - : class: `tree.DecisionTreeRegressor`
  - : class: `dummy.DummyRegressor`
  - : class: `linear_model.ElasticNet`
  - : class: `tree.ExtraTreeRegressor`
  - : class: `ensemble.ExtraTreesRegressor`
  - : class: `gaussian_process.GaussianProcessRegressor`
  - : class: `neighbors.KNeighborsRegressor`
  - : class: `kernel_ridge.KernelRidge`
  - : class: `linear_model.Lars`
  - : class: `linear_model.Lasso`
  - : class: `linear_model.LassoLars`
  - : class: `linear_model.LinearRegression`
  - : class: `multioutput.MultiOutputRegressor`
  - : class: `linear_model.MultiTaskElasticNet`
  - : class: `linear_model.MultiTaskElasticNetCV`
  - : class: `linear_model.MultiTaskLasso`
  - : class: `linear_model.MultiTaskLassoCV`
  - : class: `linear_model.OrthogonalMatchingPursuit`
  - : class: `cross_decomposition.PLSCanonical`
  - : class: `cross_decomposition.PLSRegression`
  - : class: `linear_model.RANSACRegressor`
  - : class: `neighbors.RadiusNeighborsRegressor`
  - : class: `ensemble.RandomForestRegressor`
  - : class: `multioutput.RegressorChain`
  - : class: `linear_model.Ridge`
  - : class: `linear_model.RidgeCV`
  - : class: `compose.TransformedTargetRegressor`

تنسيق الهدف
-------------

تمثيل صالح لـ: مصطلح: multioutput `y` هو مصفوفة كثيفة الشكل
`` (n_samples، n_output) '' من النقاط العائمة. دمج عامودي من
: مصطلح: متغيرات مستمرة. مثال على "y" لثلاث عينات:

  >>> y = np.array ([[31.4، 94]، [40.5، 109]، [25.0، 30]])
  >>> print (y)
  [[31.4 94.]
   [40.5 109.]
   [25. 30.]]

.. _multioutputregressor:

MultiOutputRegressor
--------------------

يمكن إضافة دعم الانحدار متعدد المخرجات إلى أي أداة انحدار باستخدام: class: ~ sklearn.multioutput.MultiOutputRegressor. تتكون هذه الاستراتيجية من
ضبط أداة انحدار واحدة لكل هدف. نظرًا لأن كل هدف يمثله بالضبط
يمكن لأداة انحدار واحدة اكتساب المعرفة حول الهدف عن طريق
فحص المقدر المقابل لها. بما أن: class: ~ sklearn.multioutput.MultiOutputRegressor يتناسب مع أداة انحدار واحدة لكل
الهدف لا يمكنه الاستفادة من الارتباطات بين الأهداف.

فيما يلي مثال على الانحدار متعدد المخرجات:

  >>> من sklearn.datasets import make_regression
  >>> من sklearn.multioutput import MultiOutputRegressor
  >>> من sklearn.ensemble import GradientBoostingRegressor
  >>> X، y = make_regression (n_samples = 10، n_targets = 3، random_state = 1)
  >>> MultiOutputRegressor (GradientBoostingRegressor (random_state = 0)). fit (X، y). predict (X)
  array ([[-154.75474165، -147.03498585، -50.03812219]
         [7.12165031، 5.12914884، -81.46081961]
         [-187.8948621، -100.44373091، 13.88978285]
         [-141.62745778، 95.02891072، -191.48204257]
         [97.03260883، 165.34867495، 139.52003279]
         [123.92529176، 21.25719016، -7.84253]
         [-122.25193977، -85.16443186، -107.12274212]
         [-30.170388، -94.80956739، 12.16979946]
         [140.72667194، 176.50941682، -17.50447799]
         [149.37967282، -81.15699552، -5.72850319]])

.. _regressorchain:

RegressorChain
--------------

سلاسل أدوات الانحدار (راجع: class: ~ sklearn.multioutput.RegressorChain) مماثلة لـ: class: ~ sklearn.multioutput.ClassifierChain كطريقة
لدمج عدد من الانحدارات في نموذج واحد متعدد الأهداف قادر على
استغلال الارتباطات بين الأهداف.