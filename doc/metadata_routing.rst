هذا النص هو جزء من توثيق مكتبة "سكيكيت-ليرن" (scikit-learn) في بايثون، ويتم وصف وظيفة توجيه البيانات اعتمادا على البيانات الوصفية.

**توجيه البيانات الوصفية**

بعد تحميل البيانات، قد تحتاج إلى توجيه الملاحظات إلى مجموعات مختلفة بناءً على بعض البيانات الوصفية. على سبيل المثال، قد ترغب في معاملة الملاحظات التي تم جمعها في ظروف مختلفة بشكل مختلف، أو قد يكون لديك بيانات من مصادر متعددة وترغب في معاملتها بشكل منفصل. يوفر scikit-learn طريقة ملائمة للقيام بذلك باستخدام طرق التحويل.

على سبيل المثال، لنفترض أنك تريد تصنيف الصور اعتمادًا على محتواها، ولديك بيانات وصفية لكل صورة تحدد ما إذا كانت الصورة تم التقاطها في الداخل أو في الهواء الطلق. يمكنك توجيه الملاحظات إلى مجموعات منفصلة بناءً على هذه البيانات الوصفية باستخدام طريقة التحويل ```MetadataRouter```.

هنا مثال يوضح كيفية استخدام ```MetadataRouter``` لتوجيه الملاحظات بناءً على بياناتها الوصفية:

```بايثون

من sklearn.compose import MetadataRouter
من sklearn.svm import SVC

# افترض أن X وy هي مصفوفات بياناتك والملاحظات الخاصة بك
# و'metadata' هي مصفوفة أو سلسلة تحتوي على البيانات الوصفية لكل ملاحظة

router = MetadataRouter(metadata='indoor')
مجموعة = router.fit_transform(X, y, metadata=metadata)

# يمكنك الآن الوصول إلى الملاحظات المنفصلة باستخدام مجموعة الدليل
indoor_X, indoor_y = dataset['indoor']

# يمكنك بعد ذلك تدريب نموذج منفصل على كل مجموعة
indoor_model = SVC()
indoor_model.fit(indoor_X, indoor_y)

# يمكنك القيام بعملية مماثلة للملاحظات في الهواء الطلق
outdoor_model = SVC()
outdoor_model.fit(outdoor_X, outdoor_y)
```

في هذا المثال، نقوم بإنشاء ```MetadataRouter``` وتعيين البيانات الوصفية المستهدفة إلى "indoor". ثم نقوم بتمرير مصفوفات بياناتنا والملاحظات والبيانات الوصفية إلى طريقة ```fit_transform```. وسوف تقوم الطريقة بتقسيم البيانات إلى مجموعتين، واحدة للملاحظات التي تحتوي على بيانات وصفية "indoor" والأخرى للملاحظات المتبقية.

يمكنك بعد ذلك الوصول إلى هذه المجموعات المنفصلة باستخدام الدليل ```'indoor'``` على المتغير ```dataset``` الذي تم إرجاعه بواسطة ```fit_transform```. وهذا يسمح لك بتدريب نماذج منفصلة على كل مجموعة من الملاحظات.

تعد ```MetadataRouter``` أداة قوية لتخصيص معالجة البيانات والنمذجة بناءً على البيانات الوصفية. يمكن استخدامه في مجموعة متنوعة من السيناريوهات، مثل تجميع الملاحظات حسب المصدر أو التاريخ أو أي معلومات وصفية أخرى ذات صلة.
API توجيه البيانات الوصفية هو ميزة تجريبية في سكيت-ليرن، ولا يتم تنفيذها بعد لجميع التقديرات. لمزيد من المعلومات، يرجى الرجوع إلى قائمة النماذج المدعومة وغير المدعومة. قد تتغير هذه الميزة دون دورة الإهمال المعتادة. بشكل افتراضي، هذه الميزة غير مفعلة. يمكنك تفعيلها عن طريق ضبط علم "تمكين توجيه البيانات الوصفية" على "صحيح":

```بيثون
>>> استيراد سكيتليرن
>>> سكيتليرن.set_config(enable_metadata_routing=True)
```

لاحظ أن الطرق والمتطلبات المقدمة في هذه الوثيقة ذات صلة فقط إذا كنت ترغب في تمرير البيانات الوصفية (على سبيل المثال، "sample_weight") إلى طريقة. إذا كنت تمرر فقط "X" و "y" ولا توجد معلمات/بيانات وصفية أخرى إلى طرق مثل "fit" أو "transform"، فلست بحاجة إلى ضبط أي شيء.

يُظهر هذا الدليل كيف يمكن توجيه البيانات الوصفية ونقلها بين الكائنات في سكيت-ليرن. إذا كنت تقوم بتطوير تقدير متوافق مع سكيت-ليرن أو ميتا-تقدير، فيمكنك مراجعة دليل المطورين ذي الصلة الخاص بنا.

البيانات الوصفية هي بيانات يأخذها التقدير أو المسجل أو أداة تقسيم CV في الاعتبار إذا قام المستخدم بتمريرها صراحةً كمعلمة. على سبيل المثال، تقبل "KMeans" "sample_weight" في طريقة "fit()" الخاصة بها وتأخذها في الاعتبار عند حساب النوى المركزية الخاصة بها. يتم استهلاك "classes" بواسطة بعض المصنفات ويتم استخدام "groups" في بعض أدوات التقسيم، ولكن يمكن اعتبار أي بيانات يتم تمريرها إلى طرق كائن ما بخلاف "X" و "y" كبيانات وصفية. قبل إصدار سكيت-ليرن 1.3، لم يكن هناك API واحد لتمرير البيانات الوصفية مثل تلك إذا تم استخدام هذه الكائنات بالاقتران مع كائنات أخرى، على سبيل المثال، مسجل يقبل "sample_weight" داخل "GridSearchCV".

مع API توجيه البيانات الوصفية، يمكننا نقل البيانات الوصفية إلى التقديرات والمسجلات وأدوات تقسيم CV باستخدام الميتا-تقديرات (مثل "Pipeline" أو "GridSearchCV") أو الوظائف مثل "cross_validate" التي تقوم بتوجيه البيانات إلى كائنات أخرى. من أجل تمرير البيانات الوصفية إلى طريقة مثل "fit" أو "score"، يجب على الكائن الذي يستهلك البيانات الوصفية *طلبها*. يتم ذلك عبر طرق "set_method_request()"، حيث يتم استبدال "{method}" باسم الطريقة التي تطلب البيانات الوصفية. على سبيل المثال، تستخدم التقديرات التي تستخدم البيانات الوصفية في طريقة "fit()" الخاصة بها "set_fit_request()"، ويستخدم المسجلات "set_score_request()". تسمح لنا هذه الطرق بتحديد البيانات الوصفية التي سيتم طلبها، على سبيل المثال "set_fit_request(sample_weight=True)".

بالنسبة إلى أدوات التقسيم المجمعة مثل "GroupKFold"، يتم طلب معلمة "groups" بشكل افتراضي. يتم توضيح ذلك بشكل أفضل من خلال الأمثلة التالية.

أمثلة الاستخدام
***************

نقدم هنا بعض الأمثلة لإظهار بعض حالات الاستخدام الشائعة. هدفنا هو تمرير "sample_weight" و "groups" من خلال "cross_validate"، والتي تقوم بتوجيه البيانات الوصفية إلى "LogisticRegressionCV" وإلى مسجل مخصص مصنوع باستخدام "make_scorer"، وكلاهما *يمكن* استخدام البيانات الوصفية في طرقهما. في هذه الأمثلة، نريد تعيين ما إذا كنا سنستخدم البيانات الوصفية داخل المستهلكين المختلفين بشكل فردي.

تتطلب الأمثلة في هذا القسم الواردات والبيانات التالية::

>>> استيراد نومبي كما np
>>> من sklearn.metrics استيراد make_scorer، accuracy_score
>>> من sklearn.linear_model استيراد LogisticRegressionCV، LogisticRegression
>>> من sklearn.model_selection استيراد cross_validate، GridSearchCV، GroupKFold
>>> من sklearn.feature_selection استيراد SelectKBest
>>> من sklearn.pipeline استيراد make_pipeline
>>> n_samples، n_features = 100، 4
>>> rng = np.random.RandomState(42)
>>> X = rng.rand(n_samples، n_features)
>>> y = rng.randint(0، 2، size=n_samples)
>>> my_groups = rng.randint(0، 10، size=n_samples)
>>> my_weights = rng.rand(n_samples)
>>> my_other_weights = rng.rand(n_samples)

التسجيل والتناسب المرجح
----------------------------

تطلب أداة التقسيم المستخدمة داخليًا في "LogisticRegressionCV"، "GroupKFold"، معلمة "groups" بشكل افتراضي. ومع ذلك، نحتاج إلى طلب "sample_weight" لها وللمسجل المخصص لدينا عن طريق تحديد "sample_weight=True" في طريقة "set_fit_request()" الخاصة بـ "LogisticRegressionCV" وفي طريقة "set_score_request()" الخاصة بـ "make_scorer". يعرف كلا المستهلكين كيفية استخدام "sample_weight" في طرقهما "fit()" أو "score()". بعد ذلك، يمكننا تمرير البيانات الوصفية في "cross_validate" والتي ستقوم بتوجيهها إلى أي مستهلكين نشطين::

>>> weighted_acc = make_scorer(accuracy_score).set_score_request(sample_weight=True)
>>> lr = LogisticRegressionCV(
... cv=GroupKFold()،
... scoring=weighted_acc
...).set_fit_request(sample_weight=True)
>>> cv_results = cross_validate(
... lr،
... X،
... y،
... params={"sample_weight": my_weights، "groups": my_groups"}،
... cv=GroupKFold()،
... scoring=weighted_acc،
...)

لاحظ أنه في هذا المثال، يقوم "cross_validate" بتوجيه "my_weights" إلى كل من المسجل و"LogisticRegressionCV".

إذا قمنا بتمرير "sample_weight" في معلمات "cross_validate"، ولكن لم نقم بتعيين أي كائن لطلبها، فسيتم إثارة خطأ "UnsetMetadataPassedError"، مما يشير إلى أننا بحاجة إلى تعيين مكان توجيهها بشكل صريح. ينطبق الشيء نفسه إذا تم تمرير "params={"sample_weights": my_weights، ...}" (لاحظ الخطأ الإملائي، أي "weights" بدلاً من "weight")، نظرًا لأن "sample_weights" لم يتم طلبها بواسطة أي من كائناتها الأساسية.

التسجيل المرجح والتناسب غير المرجح
---------------------------------------

عند تمرير البيانات الوصفية مثل "sample_weight" إلى جهاز توجيه (ميتا-تقديرات أو وظيفة توجيه)، يجب على جميع مستهلكي "sample_weight" طلب الأوزان بشكل صريح أو عدم طلبها بشكل صريح (أي "True" أو "False"). لذلك، لأداء تناسب غير مرجح، نحتاج إلى تكوين "LogisticRegressionCV" لعدم طلب أوزان العينة، بحيث لا يقوم "cross_validate" بتمرير الأوزان::

>>> weighted_acc = make_scorer(accuracy_score).set_score_request(sample_weight=True)
>>> lr = LogisticRegressionCV(
... cv=GroupKFold()، scoring=weighted_acc،
...).set_fit_request(sample_weight=False)
>>> cv_results = cross_validate(
... lr،
... X،
... y،
... cv=GroupKFold()،
... params={"sample_weight": my_weights، "groups": my_groups"}،
... scoring=weighted_acc،
...)

إذا لم يتم استدعاء "LogisticRegressionCV.set_fit_request"، فسيؤدي "cross_validate" إلى حدوث خطأ لأن "sample_weight" يتم تمريره ولكن "LogisticRegressionCV" لن يتم تكوينه بشكل صريح للتعرف على الأوزان.

اختيار الميزة غير المرجحة
----------------------------

توجيه البيانات الوصفية ممكن فقط إذا كانت طريقة الكائن تعرف كيفية استخدام البيانات الوصفية، والتي في معظم الحالات تعني أنها تحتوي على معلمة صريحة لها. فقط عندئذٍ يمكننا تعيين قيم الطلب للبيانات الوصفية باستخدام "set_fit_request(sample_weight=True)"، على سبيل المثال. يجعل هذا الكائن مستهلكًا.

على عكس "LogisticRegressionCV"، لا يمكن لـ "SelectKBest" استهلاك الأوزان، لذلك لا يتم تعيين أي قيمة طلب لـ "sample_weight" على مثيله ولا يتم توجيه "sample_weight" إليه::

>>> weighted_acc = make_scorer(accuracy_score).set_score_request(sample_weight=True)
>>> lr = LogisticRegressionCV(
... cv=GroupKFold()، scoring=weighted_acc،
...).set_fit_request(sample_weight=True)
>>> sel = SelectKBest(k=2)
>>> pipe = make_pipeline(sel، lr)
>>> cv_results = cross_validate(
... pipe،
... X،
... y،
... cv=GroupKFold()،
... params={"sample_weight": my_weights، "groups": my_groups"}،
... scoring=weighted_acc،
...)

أوزان تسجيل وتناسب مختلفة
على الرغم من أن كلاً من :func:`~metrics.make_scorer` و :class:`~linear_model.LogisticRegressionCV` يتوقعان المفتاح "sample_weight"، إلا أنه يمكننا استخدام الأسماء المستعارة لتمرير أوزان مختلفة إلى مستهلكين مختلفين. في هذا المثال، نمرر "scoring_weight" إلى المقيّم، و "fitting_weight" إلى :class:`~linear_model.LogisticRegressionCV":

  >>> weighted_acc = make_scorer(accuracy_score).set_score_request(
  ...    sample_weight="scoring_weight"
  ... )
  >>> lr = LogisticRegressionCV(
  ...     cv=GroupKFold(), scoring=weighted_acc,
  ... ).set_fit_request(sample_weight="fitting_weight")
  >>> cv_results = cross_validate(
  ...     lr,
  ...     X,
  ...     y,
  ...     cv=GroupKFold(),
  ...     params={
  ...         "scoring_weight": my_weights,
  ...         "fitting_weight": my_other_weights,
  ...         "groups": my_groups,
  ...     },
  ...     scoring=weighted_acc,
  ... )

واجهة برمجة التطبيقات API Interface
*********************************

مصطلح "consumer" هو كائن (مُقدِّر، أو ميتا-مُقدِّر، أو مُقيِّم، أو مُقسِّم) يقبل ويستخدم بعض البيانات الوصفية :term:`metadata` في واحدة على الأقل من طرقه (على سبيل المثال، "fit"، "predict"، "inverse_transform"، "transform"، "score"، "split"). الميتا-مُقدِّرات التي تقوم فقط بتمرير البيانات الوصفية إلى كائنات أخرى (المُقدِّرات أو المُقيِّمين أو المُقسِّمين التابعين) ولا تستخدم البيانات الوصفية بأنفسهم ليست مستهلكين. المُقدِّرات (الميتا) التي تقوم بتوجيه البيانات الوصفية إلى كائنات أخرى هي :term:`routers <router>`. يمكن أن يكون المُقدِّر (الميتا) مُستهلكًا و :term:`router` في نفس الوقت. تعرض المُقدِّرات (الميتا) والمُقسِّمات طريقة `set_{method}_request` لكل طريقة تقبل على الأقل بيانات وصفية واحدة. على سبيل المثال، إذا كان المُقدِّر يدعم "sample_weight" في "fit" و "score"، فإنه يعرض "estimator.set_fit_request(sample_weight=value)" و "estimator.set_score_request(sample_weight=value)". يمكن أن يكون "value" ما يلي:

- ``True``: تشير الطريقة إلى طلب "sample_weight". وهذا يعني أنه إذا تم توفير البيانات الوصفية، فسيتم استخدامها، وإلا فلن يتم رفع أي خطأ.
- ``False``: الطريقة لا تطلب "sample_weight".
- ``None``: سيرفع الراوتر خطأً إذا تم تمرير "sample_weight". هذه هي القيمة الافتراضية في جميع الحالات تقريبًا عند إنشاء كائن، ويضمن أن المستخدم يحدد طلبات البيانات الوصفية بشكل صريح عندما يتم تمرير البيانات الوصفية. والاستثناء الوحيد هو مُقسِّمات "Group*Fold".
- ``"param_name"``: اسم مستعار لـ "sample_weight" إذا كنا نريد تمرير أوزان مختلفة إلى مستهلكين مختلفين. إذا تم استخدام الأسماء المستعارة، فيجب ألا يقوم الميتا-مُقدِّر بتمرير "param_name" إلى المُستهلك، ولكن "sample_weight" بدلاً من ذلك، لأن المُستهلك سيتوقع معلمة تسمى "sample_weight". وهذا يعني أن الخريطة بين البيانات الوصفية المطلوبة بواسطة الكائن، على سبيل المثال "sample_weight" واسم المتغير المقدم من قبل المستخدم، على سبيل المثال "my_weights"، تتم على مستوى الراوتر، وليس بواسطة الكائن المستهلك نفسه.

يتم طلب البيانات الوصفية بنفس الطريقة للمُقيِّمين باستخدام "set_score_request".

إذا قام المستخدم بتمرير بيانات وصفية، على سبيل المثال "sample_weight"، فيجب على المستخدم تعيين طلب البيانات الوصفية لجميع الكائنات التي يمكنها استهلاك "sample_weight"، وإلا سيرفع كائن الراوتر خطأً. على سبيل المثال، يرفع الكود التالي خطأً، لأنه لم يتم تحديد ما إذا كان يجب تمرير "sample_weight" إلى مُقيِّم المُقدِّر بشكل صريح أم لا::

    >>> param_grid = {"C": [0.1, 1]}
    >>> lr = LogisticRegression().set_fit_request(sample_weight=True)
    >>> try:
    ...     GridSearchCV(
    ...         estimator=lr, param_grid=param_grid
    ...     ).fit(X, y, sample_weight=my_weights)
    ... except ValueError as e:
    ...     print(e)
    [sample_weight] يتم تمريرها ولكن لم يتم تحديدها بشكل صريح على أنها مطلوبة أو غير مطلوبة لـ LogisticRegression.score، والتي يتم استخدامها داخل GridSearchCV.fit.
    استدعاء `LogisticRegression.set_score_request({metadata}=True/False)` لكل البيانات الوصفية التي تريد طلبها/تجاهلها.

يمكن إصلاح المشكلة عن طريق تعيين قيمة الطلب بشكل صريح::

    >>> lr = LogisticRegression().set_fit_request(
    ...     sample_weight=True
    ... ).set_score_request(sample_weight=False)

في نهاية قسم **أمثلة الاستخدام**، نقوم بتعطيل علم التهيئة لتوجيه البيانات الوصفية::

    >>> sklearn.set_config(enable_metadata_routing=False)

.. _metadata_routing_models:

حالة دعم توجيه البيانات الوصفية
*******************************
يدعم جميع المستهلكين (أي المُقدِّرات البسيطة التي تستهلك البيانات الوصفية فقط ولا تقوم بتوجيهها) توجيه البيانات الوصفية، مما يعني أنه يمكن استخدامها داخل الميتا-مُقدِّرات التي تدعم توجيه البيانات الوصفية. ومع ذلك، فإن تطوير دعم توجيه البيانات الوصفية للميتا-مُقدِّرات قيد التقدم، وفيما يلي قائمة بالميتا-مُقدِّرات والأدوات التي تدعم توجيه البيانات الوصفية ولا تدعمها بعد.

الميتا-مُقدِّرات والوظائف التي تدعم توجيه البيانات الوصفية:

- :class:`sklearn.calibration.CalibratedClassifierCV`
- :class:`sklearn.compose.ColumnTransformer`
- :class:`sklearn.compose.TransformedTargetRegressor`
- :class:`sklearn.covariance.GraphicalLassoCV`
- :class:`sklearn.ensemble.StackingClassifier`
- :class:`sklearn.ensemble.StackingRegressor`
- :class:`sklearn.ensemble.VotingClassifier`
- :class:`sklearn.ensemble.VotingRegressor`
- :class:`sklearn.ensemble.BaggingClassifier`
- :class:`sklearn.ensemble.BaggingRegressor`
- :class:`sklearn.feature_selection.RFE`
- :class:`sklearn.feature_selection.RFECV`
- :class:`sklearn.feature_selection.SelectFromModel`
- :class:`sklearn.feature_selection.SequentialFeatureSelector`
- :class:`sklearn.impute.IterativeImputer`
- :class:`sklearn.linear_model.ElasticNetCV`
- :class:`sklearn.linear_model.LarsCV`
- :class:`sklearn.linear_model.LassoCV`
- :class:`sklearn.linear_model.LassoLarsCV`
- :class:`sklearn.linear_model.LogisticRegressionCV`
- :class:`sklearn.linear_model.MultiTaskElasticNetCV`
- :class:`sklearn.linear_model.MultiTaskLassoCV`
- :class:`sklearn.linear_model.OrthogonalMatchingPursuitCV`
- :class:`sklearn.linear_model.RANSACRegressor`
- :class:`sklearn.linear_model.RidgeClassifierCV`
- :class:`sklearn.linear_model.RidgeCV`
- :class:`sklearn.model_selection.GridSearchCV`
- :class:`sklearn.model_selection.HalvingGridSearchCV`
- :class:`sklearn.model_selection.HalvingRandomSearchCV`
- :class:`sklearn.model_selection.RandomizedSearchCV`
- :class:`sklearn.model_selection.permutation_test_score`
- :func:`sklearn.model_selection.cross_validate`
- :func:`sklearn.model_selection.cross_val_score`
- :func:`sklearn.model_selection.cross_val_predict`
- :class:`sklearn.model_selection.learning_curve`
- :class:`sklearn.model_selection.validation_curve`
- :class:`sklearn.multiclass.OneVsOneClassifier`
- :class:`sklearn.multiclass.OneVsRestClassifier`
- :class:`sklearn.multiclass.OutputCodeClassifier`
- :class:`sklearn.multioutput.ClassifierChain`
- :class:`sklearn.multioutput.MultiOutputClassifier`
- :class:`sklearn.multioutput.MultiOutputRegressor`
- :class:`sklearn.multioutput.RegressorChain`
- :class:`sklearn.pipeline.FeatureUnion`
- :class:`sklearn.pipeline.Pipeline`
- :class:`sklearn.semi_supervised.SelfTrainingClassifier`

الميتا-مُقدِّرات والأدوات التي لا تدعم توجيه البيانات الوصفية بعد:

- :class:`sklearn.ensemble.AdaBoostClassifier`
- :class:`sklearn.ensemble.AdaBoostRegressor`