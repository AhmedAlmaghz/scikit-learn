مجموعات البيانات التجريبية
=====================

.. currentmodule:: sklearn.datasets

تأتي مكتبة سكايت-ليرن مع بعض مجموعات البيانات القياسية الصغيرة التي لا تتطلب تنزيل أي ملف من أي موقع ويب خارجي.

يمكن تحميلها باستخدام الوظائف التالية:

.. autosummary::

   load_iris
   load_diabetes
   load_digits
   load_linnerud
   load_wine
   load_breast_cancer

هذه المجموعات مفيدة لتوضيح سريع لسلوك الخوارزميات المختلفة المطبقة في سكايت-ليرن. ومع ذلك، فهي غالباً ما تكون صغيرة جداً لتمثيل مهام التعلم الآلي في العالم الحقيقي.

.. include:: ../../sklearn/datasets/descr/iris.rst

.. include:: ../../sklearn/datasets/descr/diabetes.rst

.. include:: ../../sklearn/datasets/descr/digits.rst

.. include:: ../../sklearn/datasets/descr/linnerud.rst

.. include:: ../../sklearn/datasets/descr/wine_data.rst

.. include:: ../../sklearn/datasets/descr/breast_cancer.rst

مجموعة بيانات Iris
------------------------------------

.. سكالبليARN: داتاسايتس: لود_إيريس

تم استخدام مجموعة بيانات Iris على نطاق واسع كمجموعة بيانات اختبار في التعلم الآلي. إنها مجموعة بيانات صغيرة، حيث تحتوي على 150 عينة فقط، موزعة بالتساوي على 3 فئات. هناك 4 ميزات رقمية لكل عينة، تم قياسها من نوع من زهرة Iris. يمكن العثور على مزيد من المعلومات حول مجموعة البيانات على `صفحة ويكيبيديا <https://en.wikipedia.org/wiki/Iris_flower_data_set>`__.

يمكن تحميل مجموعة البيانات باستخدام الدالة التالية:

.. function:: load_iris(return_X_y=False, as_frame=False)

   .. versionadded:: 0.24

   تحميل مجموعة بيانات Iris واسترداد المصفوفات X و y.

   .......

   :param return_X_y: إذا كان True، يعيد المصفوفات X و y، وإلا فإنه يعيد Bunch object. الافتراضي هو False.

   :param as_frame: إذا كان True، يعيد ``DataFrame``\ s، وإلا فإنه يعيد ``ndarray``\ s. الافتراضي هو False.

   :returns: إذا كانت return_X_y == False، فإنها تعيد كائن Bunch مع المفاتيح التالية:

      ``data``
          مصفوفة ميزات الشكل [150، 4].

      ``target``
          مصفوفة الإخراج، الشكل [150].

      ``target_names``
          قائمة بأسماء الفئات.

      ``DESCR``
          وصف سلسلة من مجموعة البيانات.

   إذا كانت return_X_y == True، فإنها تعيد (X، y) بدلاً من ذلك.

   أمثلة
   --------
   >>> from sklearn.datasets import load_iris
   >>> iris = load_iris()
   >>> iris.data.shape
   (150, 4)

مجموعة بيانات Diabetes
------------------------------------

.. سكالبليARN: داتاسايتس: لود_ديابيتيس

هذه مجموعة بيانات لنمذجة مهمة التنبؤ المستمر. الهدف هو التنبؤ بقيم خاصية النتائج المستمرة بدلاً من الفئات المسماة. هذه مجموعة بيانات صغيرة إلى حد ما، حيث تحتوي على 442 عينة فقط، مما يجعلها مناسبة للاستخدام التوضيحي.

يمكن تحميل مجموعة البيانات باستخدام الدالة التالية:

.. function:: load_diabetes(return_X_y=False, as_frame=False)

   .. versionadded:: 0.24

   تحميل مجموعة بيانات مرض السكري واسترداد المصفوفات X و y.

   .......

   :param return_X_y: إذا كان True، يعيد المصفوفات X و y، وإلا فإنه يعيد Bunch object. الافتراضي هو False.

   :param as_frame: إذا كان True، يعيد ``DataFrame``\ s، وإلا فإنه يعيد ``ndarray``\ s. الافتراضي هو False.

   :returns: إذا كانت return_X_y == False، فإنها تعيد كائن Bunch مع المفاتيح التالية:

      ``data``
          مصفوفة ميزات الشكل [442، 10].

      ``target``
          مصفوفة الإخراج، الشكل [442].

      ``DESCR``
          وصف سلسلة من مجموعة البيانات.

   إذا كانت return_X_y == True، فإنها تعيد (X، y) بدلاً من ذلك.

   أمثلة
   --------
   >>> from sklearn.datasets import load_diabetes
   >>> diabetes = load_diabetes()
   >>> diabetes.data.shape
   (442, 10)

مجموعة بيانات Digits
------------------------------------

.. سكالبليARN: داتاسايتس: لود_ديجيتس

هذه مجموعة بيانات لنمذجة مهمة التصنيف. تم أخذ الصور من مجموعة بيانات NIST، وتمت إزالة الصور التي يصعب قراءتها حتى يظل الإنسان على يقين من التسميات.

يمكن تحميل مجموعة البيانات باستخدام الدالة التالية:

.. function:: load_digits(n_class=10, test_size=None, random_state=None, return_X_y=False,
                       as_frame=False)

   .. versionadded:: 0.24

   تحميل مجموعة بيانات الرقم واسترداد المصفوفات X و y.

   .......

   :param n_class: عدد الفئات التي يجب استخدامها. إذا تم تعيينه على 10، فسيتم استخدام جميع الفئات. إذا تم تعيينه على 2، فسيتم استخدام الفئات {1, 2} فقط. الافتراضي هو 10.

   :param test_size: إذا لم يكن None، يتم تقسيم البيانات إلى مجموعات تدريب واختبار عشوائية. إذا كان float، يجب أن يكون بين 0.0 و 1.0 ويمثل النسبة المئوية للعينات في مجموعة الاختبار. إذا كان int، فسيتم تقسيم هذا العدد من العينات إلى مجموعة الاختبار من مجموعة البيانات. إذا كان None، فلا يتم تقسيم البيانات. الافتراضي هو None.

   :param random_state: تحديد العشوائية العشوائية للتقسيم. يستخدم عند test_size محدد. قد يكون البذور، عشوائية، أو None. الافتراضي هو None.

   :param return_X_y: إذا كان True، يعيد المصفوفات X و y، وإلا فإنه يعيد Bunch object. الافتراضي هو False.

   :param as_frame: إذا كان True، يعيد ``DataFrame``\ s، وإلا فإنه يعيد ``ndarray``\ s. الافتراضي هو False.

   :returns: إذا كانت return_X_y == False، فإنها تعيد كائن Bunch مع المفاتيح التالية:

      ``data``
          مصفوفة ميزات الشكل [1797، 64].

      ``target``
          مصفوفة الإخراج، الشكل [1797].

      ``images``
          مصفوفة من الصور 8x8، الشكل [1797، 8، 8].

      ``target_names``
          قائمة بأسماء الفئات.

      ``DESCR``
          وصف سلسلة من مجموعة البيانات.

   إذا كانت return_X_y == True، فإنها تعيد (X، y) بدلاً من ذلك.

   أمثلة
   --------
   >>> from sklearn.datasets import load_digits
   >>> digits = load_digits()
   >>> digits.data.shape
   (1797, 64)

مجموعة بيانات Linnerud
------------------------------------

.. سكالبليARN: داتاسايتس: لود_لينييرود

هذه مجموعة بيانات لنمذجة مهمة الانحدار. يتم استخدامه كمثال على الانحدار متعدد المتغيرات، حيث يتم التنبؤ بقيم الخصائص المتعددة في نفس الوقت.

يمكن تحميل مجموعة البيانات باستخدام الدالة التالية:

.. function:: load_linnerud(return_X_y=False, as_frame=False)

   .. versionadded:: 0.24

   تحمMultiplier Multiplire مجموعة بيانات Linnerud واسترداد المصفوفات X و y.

   .......

   :param return_X_y: إذا كان True، يعيد المصفوفات X و y، وإلا فإنه يعيد Bunch object. الافتراضي هو False.

   :param as_frame: إذا كان True، يعيد ``DataFrame``\ s، وإلا فإنه يعيد ``ndarray``\ s. الافتراضي هو False.

   :returns: إذا كانت return_X_y == False، فإنها تعيد كائن Bunch مع المفاتيح التالية:

      ``data``
          مصفوفة ميزات الشكل [20، 3].

      ``target``
          مصفوفة الإخراج، الشكل [20، 3].

      ``target_names``
          قائمة بأسماء الفئات.

      ``DESCR``
          وصف سلسلة من مجموعة البيانات.

   إذا كانت return_X_y == True، فإنها تعيد (X، y) بدلاً من ذلك.

   أمثلة
   --------
   >>> from sklearn.datasets import load_linnerud
   >>> linnerud = load_linnerud()
   >>> linnerud.data.shape
   (20, 3)

مجموعة بيانات Wine
------------------------------------

.. سكالبليARN: داتاسايتس: لود_واين_داتا

هذه مجموعة بيانات لنمذجة مهمة التصنيف. يتم استخدامه كمثال على التصنيف متعدد الفئات، حيث هناك أكثر من فئتين.

يمكن تحميل مجموعة البيانات باستخدام الدالة التالية:

.. function:: load_wine(return_X_y=False, as_frame=False)

   .. versionadded:: 0.24

   تحميل مجموعة بيانات النبيذ واسترداد المصفوفات X و y.

   .......

   :param return_X_y: إذا كان True، يعيد المصفوفات X و y، وإلا فإنه يعيد Bunch object. الافتراضي هو False.

   :param as_frame: إذا كان True، يعيد ``DataFrame``\ s، وإلا فإنه يعيد ``ndarray``\ s. الافتراضي هو False.

   :returns: إذا كانت return_X_y == False، فإنها تعيد كائن Bunch مع المفاتيح التالية:

      ``data``
          مصفوفة ميزات الشكل [178، 13].

      ``target``
          مصفوفة الإخراج، الشكل [178].

      ``target_names``
          قائمة بأسماء الفئات.

      ``DESCR``
          وصف سلسلة من مجموعة البيانات.

   إذا كانت return_X_y == True، فإنها تعيد (X، y) بدلاً من ذلك.

   أمثلة
   --------
   >>> from sklearn.datasets import load_wine
   >>> wine = load_wine()
   >>> wine.target_names
   array(['class_0', 'class_1', 'class_2'], dtype='<U7')

مجموعة بيانات Breast Cancer
------------------------------------

.. سكالبليARN: داتاسايتس: لود_بريست_كانسير

هذه مجموعة بيانات لنمذجة مهمة التصنيف. يتم استخدامه كمثال على التصنيف ثنائي الفئة.

يمكن تحميل مجموعة البيانات باستخدام الدالة التالية:

.. function:: load_breast_cancer(return_X_y=False, as_frame=False)

   .. versionadded:: 0.24

   تحميل مجموعة بيانات سرطان الثدي واسترداد المصفوفات X و y.

   .......

   :param return_X_y: إذا كان True، يعيد المصفوفات X و y، وإلا فإنه يعيد Bunch object. الافتراضي هو False.

   :param as_frame: إذا كان True، يعيد ``DataFrame``\ s، وإلا فإنه يعيد ``ndarray``\ s. الافتراضي هو False.

   :returns: إذا كانت return_X_y == False، فإنها تعيد كائن Bunch مع المفاتيح التالية:

      ``data``
          مصفوفة ميزات الشكل [569، 30].

      ``target``
          مصفوفة الإخراج، الشكل [569].

      ``target_names``
          قائمة بأسماء الفئات.

      ``DESCR``
          وصف سلسلة من مجموعة البيانات.

   إذا كانت return_X_y == True، فإنها تعيد (X، y) بدلاً من ذلك.

   أمثلة
   --------
   >>> from sklearn.datasets import load_breast_cancer
   >>> cancer = load_breast_cancer()
   >>> cancer.target_names
   array(['malignant', 'benign'], dtype='<U9')