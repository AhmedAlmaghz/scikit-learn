بدء الاستخدام
================

الغرض من هذا الدليل هو توضيح بعض الميزات الرئيسية التي يوفرها ``scikit-learn``. يفترض وجود معرفة أساسية جدًا بممارسات التعلم الآلي (مثل تكييف النموذج، والتنبؤ، والتحقق من الصلاحية المتقاطعة، وما إلى ذلك). يرجى الرجوع إلى تعليمات التثبيت الخاصة بنا <installation-instructions> لتثبيت ``scikit-learn``.

``Scikit-learn`` هي مكتبة تعلم آلي مفتوحة المصدر تدعم التعلم المُراقَب وغير المُراقَب. كما يوفر أدوات مختلفة لضبط النماذج، ومعالجة البيانات مسبقًا، واختيار النماذج، وتقييم النماذج، والعديد من المرافق الأخرى.

الضبط والتنبؤ: أساسيات المُقدِّر
----------------------------------------

يوفر ``Scikit-learn`` عشرات خوارزميات ونماذج التعلم الآلي المدمجة، والتي يُطلق عليها اسم :term: `المُقدِّرات`. يمكن ضبط كل مُقدِّر على بعض البيانات باستخدام طريقة :term: `الضبط` الخاصة به.

فيما يلي مثال بسيط نقوم فيه بضبط :class: `RandomForestClassifier` على بعض البيانات الأساسية جدًا::

  >>> from sklearn.ensemble import RandomForestClassifier
  >>> clf = RandomForestClassifier(random_state=0)
  >>> X = [[ 1,  2,  3],  # 2 samples, 3 features
  ...      [11, 12, 13]]
  >>> y = [0, 1]  # classes of each sample
  >>> clf.fit(X, y)
  RandomForestClassifier(random_state=0)

تقبل طريقة :term: `الضبط` عمومًا مدخلين:

- مصفوفة العينات (أو مصفوفة التصميم) :term: `X`. حجم ``X`` هو عادة ``(n_samples، n_features)``، مما يعني أن العينات مُمَثَلة كصفوف والميزات مُمَثَلة كأعمدة.
- قيم الهدف :term: `y` التي هي أعداد حقيقية لمهام الانحدار، أو أعداد صحيحة للتصنيف (أو أي مجموعة منفصلة أخرى من القيم). بالنسبة لمهام التعلم غير المُراقَب، لا يلزم تحديد ``y``. عادةً ما يكون ``y`` مصفوفة أحادية البعد حيث يتوافق الإدخال ``i`` مع هدف العينة ``i`` (الصف) من ``X``.

يُتوقع أن يكون كل من ``X`` و ``y`` مصفوفتين Numpy أو أنواع بيانات مماثلة :term: `array-like`، على الرغم من أن بعض المُقدِّرات تعمل بتنسيقات أخرى مثل المصفوفات المُنَضَّدة.

بمجرد ضبط المُقدِّر، يمكن استخدامه للتنبؤ بقيم الهدف لبيانات جديدة. لا تحتاج إلى إعادة تدريب المُقدِّر::

  >>> clf.predict(X)  # predict classes of the training data
  array([0, 1])
  >>> clf.predict([[4, 5, 6], [14, 15, 16]])  # predict classes of new data
  array([0, 1])

يمكنك التحقق من :ref: `ml_map` لمعرفة كيفية اختيار النموذج المناسب لحالتك الاستخدام.

المحوِّلات والمعالجات المُسبَقة
-------------------------------

غالبًا ما تتكون تدفقات عمل التعلم الآلي من أجزاء مختلفة. يتكون الأنبوب النموذجي من خطوة معالجة مُسبَقة تقوم بتحويل البيانات أو استكمالها، ومُتنبئ نهائي يتنبأ بقيم الهدف.

في ``scikit-learn``، تتبع المعالجات المُسبَقة والمحوِّلات نفس واجهة برمجة التطبيقات مثل كائنات المُقدِّر (في الواقع، جميعها ترث من فئة ``BaseEstimator`` نفسها). لا تحتوي كائنات المحوِّل على طريقة :term: `predict` ولكن بدلاً من ذلك تحتوي على طريقة :term: `transform` التي تُخرج مصفوفة عينات مُحوَّلة حديثًا ``X``::

  >>> from sklearn.preprocessing import StandardScaler
  >>> X = [[0, 15],
  ...      [1, -10]]
  >>> # scale data according to computed scaling values
  >>> StandardScaler().fit(X).transform(X)
  array([[-1.,  1.],
         [ 1., -1.]])

في بعض الأحيان، تريد تطبيق تحويلات مختلفة على ميزات مختلفة: تم تصميم :ref: `ColumnTransformer` لهذه الحالات الاستخدام.

الأنابيب: ربط المعالجات المُسبَقة والمُقدِّرات
--------------------------------------------------

يمكن دمج المحوِّلات والمُقدِّرات (المُتنبئين) معًا في كائن موحد: :class: `Pipeline`. يوفر الأنبوب نفس واجهة برمجة التطبيقات مثل المُقدِّر العادي: يمكن ضبطه واستخدامه للتنبؤ باستخدام ``fit`` و ``predict``. كما سنرى لاحقًا، فإن استخدام الأنبوب سيحميك أيضًا من تسرب البيانات، أي الكشف عن بعض بيانات الاختبار في بيانات التدريب الخاصة بك.

في المثال التالي، نقوم بتحميل مجموعة بيانات Iris :ref: `datasets`، وتقسيمها إلى مجموعات تدريب واختبار، وحساب درجة الدقة لأنبوب على بيانات الاختبار::

  >>> from sklearn.preprocessing import StandardScaler
  >>> from sklearn.linear_model import LogisticRegression
  >>> from sklearn.pipeline import make_pipeline
  >>> from sklearn.datasets import load_iris
  >>> from sklearn.model_selection import train_test_split
  >>> from sklearn.metrics import accuracy_score
  ...
  >>> # create a pipeline object
  >>> pipe = make_pipeline(
  ...     StandardScaler(),
  ...     LogisticRegression()
  ... )
  ...
  >>> # load the iris dataset and split it into train and test sets
  >>> X, y = load_iris(return_X_y=True)
  >>> X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
  ...
  >>> # ضبط الأنبوب بالكامل
  >>> pipe.fit(X_train, y_train)
  Pipeline(steps=[('standardscaler', StandardScaler()),
                  ('logisticregression', LogisticRegression())])
  >>> # يمكننا الآن استخدامه مثل أي مُقدِّر آخر
  >>> accuracy_score(pipe.predict(X_test), y_test)
  0.97...

تقييم النموذج
----------------

لا يعني ضبط نموذج على بعض البيانات أنه سيتنبأ جيدًا بالبيانات غير المرئية. يجب تقييم ذلك مباشرةً. لقد رأينا للتو المساعد :func: `train_test_split` الذي يقسم مجموعة بيانات إلى مجموعات تدريب واختبار، ولكن يوفر ``scikit-learn`` العديد من الأدوات الأخرى لتقييم النماذج، خاصةً للتحقق من الصلاحية المتقاطعة :ref: `cross_validation`.

نُظهِر هنا بإيجاز كيفية إجراء عملية تحقق من الصلاحية متقاطعة بخمسة أضعاف، باستخدام المساعد :func: `cross_validate`. لاحظ أنه من الممكن أيضًا التكرار يدويًا عبر الطيات، واستخدام استراتيجيات تقسيم البيانات المختلفة، واستخدام دالات التسجيل المخصصة. يرجى الرجوع إلى دليل المستخدم الخاص بنا :ref: `cross_validation` لمزيد من التفاصيل::

  >>> from sklearn.datasets import make_regression
  >>> from sklearn.linear_model import LinearRegression
  >>> from sklearn.model_selection import cross_validate
  ...
  >>> X, y = make_regression(n_samples=1000, random_state=0)
  >>> lr = LinearRegression()
  ...
  >>> result = cross_validate(lr, X, y)  # defaults to 5-fold CV
  >>> result['test_score']  # r_squared score is high because dataset is easy
  array([1., 1., 1., 1., 1.])

عمليات البحث التلقائي عن المعلمات
----------------------------

لجميع المُقدِّرات معلمات (تُسمى غالبًا معلمات فائقة في الأدبيات) يمكن ضبطها. غالبًا ما تعتمد قوة تعميم المُقدِّر بشكل حاسم على بعض المعلمات. على سبيل المثال، لدى :class: `RandomForestRegressor` معلمة ``n_estimators`` تحدد عدد الأشجار في الغابة، ومعلمة ``max_depth`` تحدد العمق الأقصى لكل شجرة. غالبًا ما يكون من غير الواضح ما هي القيم الدقيقة لهذه المعلمات لأنها تعتمد على البيانات المتاحة.

يوفر ``Scikit-learn`` أدوات للعثور تلقائيًا على أفضل مجموعات المعلمات (عبر التحقق من الصلاحية المتقاطعة). في المثال التالي، نقوم بالبحث عشوائيًا في مساحة المعلمات لنموذج غابة عشوائي باستخدام كائن :class: `RandomizedSearchCV`. عندما ينتهي البحث، يتصرف :class: `RandomizedSearchCV` مثل :class: `RandomForestRegressor` الذي تم ضبطه بأفضل مجموعة من المعلمات. اقرأ المزيد في دليل المستخدم :ref: `grid_search`::

  >>> from sklearn.datasets import fetch_california_housing
  >>> from sklearn.ensemble import RandomForestRegressor
  >>> from sklearn.model_selection import RandomizedSearchCV
  >>> from sklearn.model_selection import train_test_split
  >>> from scipy.stats import randint
  ...
  >>> X, y = fetch_california_housing(return_X_y=True)
  >>> X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
  ...
  >>> # define the parameter space that will be searched over
  >>> param_distributions = {'n_estimators': randint(1, 5),
  ...                        'max_depth': randint(5, 10)}
  ...
  >>> # now create a searchCV object and fit it to the data
  >>> search = RandomizedSearchCV(estimator=RandomForestRegressor(random_state=0),
  ...                             n_iter=5,
  ...                             param_distributions=param_distributions,
  ...                             random_state=0)
  >>> search.fit(X_train, y_train)
  RandomizedSearchCV(estimator=RandomForestRegressor(random_state=0), n_iter=5,
                     param_distributions={'max_depth': ...,
                                          'n_estimators': ...},
                     random_state=0)
  >>> search.best_params_
  {'max_depth': 9, 'n_estimators': 4}

  >>> # the search object now acts like a normal random forest estimator
  >>> # with max_depth=9 and n_estimators=4
  >>> search.score(X_test, y_test)
  0.73...

.. note::

    في الممارسة العملية، تريد دائمًا :ref: `البحث في الأنبوب
    <composite_grid_search>`، بدلاً من مُقدِّر واحد. أحد الأسباب الرئيسية هو أنه إذا قمت بتطبيق خطوة معالجة مُسبَقة على مجموعة البيانات بأكملها دون استخدام الأنبوب، ثم قمت بأي نوع من التحقق من الصلاحية المتقاطعة، فستكون قد كسرت الافتراض الأساسي لاستقلال البيانات التدريبية وبيانات الاختبار. في الواقع، نظرًا لأنك عالجت البيانات مُسبَقًا باستخدام مجموعة البيانات بأكملها، فإن بعض المعلومات حول مجموعات الاختبار متاحة لمجموعات التدريب. سيؤدي هذا إلى المبالغة في تقدير قوة تعميم المُقدِّر (يمكنك قراءة المزيد في هذا المنشور على Kaggle <https://www.kaggle.com/alexisbcook/data-leakage>`_).

    سيحميك استخدام الأنبوب للتحقق من الصلاحية المتقاطعة والبحث إلى حد كبير من هذا الفخ الشائع.


الخطوات التالية
----------

لقد غطينا بإيجاز ضبط المُقدِّر والتنبؤ، وخطوات المعالجة المُسبَقة، والأنابيب، وأدوات التحقق من الصلاحية المتقاطعة، وعمليات البحث التلقائي عن المعلمات الفائقة. يجب أن يمنحك هذا الدليل نظرة عامة على بعض الميزات الرئيسية للمكتبة، ولكن هناك الكثير في ``scikit-learn``!

يرجى الرجوع إلى دليل المستخدم الخاص بنا :ref: `user_guide` للحصول على تفاصيل حول جميع الأدوات التي نوفرها. يمكنك أيضًا العثور على قائمة شاملة بواجهة برمجة التطبيقات العامة في :ref: `api_ref`.

يمكنك أيضًا الاطلاع على العديد من الأمثلة لدينا :ref: `general_examples` التي توضح استخدام ``scikit-learn`` في العديد من السياقات المختلفة.