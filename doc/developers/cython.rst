.. _cython:

أفضل الممارسات والتوجيهات والمعرفة في Cython
================================================

توفر هذه الوثيقة نصائح لتطوير تعليمات برمجية بلغة Cython في scikit-learn.

نصائح لتطوير التعليمات البرمجية بلغة Cython في scikit-learn
-----------------------------------------------

نصائح لتسهيل التطوير
^^^^^^^^^^^^^^^^^^^^^^^^

* الوقت الذي تقضيه في قراءة `وثائق Cython <https://cython.readthedocs.io/en/latest/>`_ ليس وقتاً ضائعاً.

* إذا كنت تنوي استخدام OpenMP: على نظام MacOS، لا يوفر توزيع النظام لـ ``clang`` OpenMP.
  يمكنك تثبيت حزمة "المترجمين" المتوفرة في ``conda-forge`` والتي تأتي مع تنفيذ OpenMP.

* قد يساعد تفعيل `التحققات <https://github.com/scikit-learn/scikit-learn/blob/62a017efa047e9581ae7df8bbaa62cf4c0544ee4/sklearn/_build_utils/__init__.py#L68-L87>`_. على سبيل المثال، لتفعيل التحقق من الحدود، استخدم ما يلي:

  .. code-block:: bash

         export SKLEARN_ENABLE_DEBUG_CYTHON_DIRECTIVES=1

* `ابدأ من الصفر في دفتر ملاحظات <https://cython.readthedocs.io/en/latest/src/quickstart/build.html#using-the-jupyter-notebook>`_ لفهم كيفية استخدام Cython والحصول على تعليقات حول عملك بسرعة.
  إذا كنت تخطط لاستخدام OpenMP لتنفيذك في دفتر ملاحظات Jupyter، قم بإضافة حجج مترجم وارتباطات إضافية في التعويذة السحرية لـ Cython.

  .. code-block:: python

         # For GCC and for clang
         %%cython --compile-args=-fopenmp --link-args=-fopenmp
         # For Microsoft's compilers
         %%cython --compile-args=/openmp --link-args=/openmp

* لاستكشاف أخطاء التعليمات البرمجية C وإصلاحها (على سبيل المثال، حدوث خطأ في الإشارة)، استخدم ``gdb`` مع:

  .. code-block:: bash

         gdb --ex r --args python ./entrypoint_to_bug_reproducer.py

* للوصول إلى قيمة معينة في المكان لتصحيح الأخطاء في سياق ``cdef (nogil)``، استخدم:

  .. code-block:: cython

         with gil:
             print(state_to_print)

* لاحظ أن Cython لا يمكنه تحليل السلاسل النصية f مع تعبيرات ``{var=}``، على سبيل المثال:

  .. code-block:: bash

         print(f"{test_val=}")

* يحتوي شيفرة scikit-learn على العديد من تعريفات الأنواع غير الموحدة (المدمجة).
  هناك حاليًا `عمل جارٍ لتبسيط وتوحيد ذلك عبر الشيفرة البرمجية
  <https://github.com/scikit-learn/scikit-learn/issues/25572>`_.
  في الوقت الحالي، تأكد من فهمك للأنواع الملموسة المستخدمة في النهاية.

* قد تجد هذا الاسم المستعار لتجميع ملحقات Cython الفردية مفيدًا:

  .. code-block::

      # قد ترغب في إضافة هذا الاسم المستعار إلى تكوين ملف البرنامج النصي الخاص بك.
      alias cythonX="cython -X language_level=3 -X boundscheck=False -X wraparound=False -X initializedcheck=False -X nonecheck=False -X cdivision=True"

      # هذا يولد `source.c` كما لو كنت قد أعدت تجميع scikit-learn بالكامل.
      cythonX --annotate source.pyx

* يسمح استخدام خيار ``--annotate`` مع هذا العلم بتوليد تقرير HTML لتعليمات الشيفرة.
  يشير هذا التقرير إلى التفاعلات مع مفسر CPython على أساس كل سطر على حدة.
  يجب تجنب التفاعلات مع مفسر CPython قدر الإمكان في الأقسام كثيرة الاستخدام من الخوارزميات.
  لمزيد من المعلومات، يرجى الرجوع إلى `هذا القسم من تعليمي Cython <https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html#primes>`_

  .. code-block::

      # هذا يولد تقرير HTML (`source.html`) لـ `source.c`.
      cythonX --annotate source.pyx

نصائح للأداء
^^^^^^^^^^^^^^^^^^^^

* افهم GIL في سياق CPython (ما هي المشكلات التي يحلها، وما هي قيودها)
  واحصل على فهم جيد للوقت الذي سيتم فيه رسم خريطة Cython إلى شيفرة C خالية من التفاعلات مع
  CPython، وعندما لا يحدث ذلك، وعندما لا يمكن ذلك (على سبيل المثال، وجود تفاعلات مع كائنات Python، والتي تشمل الدوال). وفي هذا الصدد، `PEP073 <https://peps.python.org/pep-0703/>`_
  يوفر نظرة عامة جيدة وسياقًا ومسارات للإزالة.

* تأكد من تعطيل `التحققات <https://github.com/scikit-learn/scikit-learn/blob/62a017efa047e9581ae7df8bbaa62cf4c0544ee4/sklearn/_build_utils/__init__.py#L68-L87>`_.

* يفضل دائمًا استخدام memoryviews بدلاً من ``cnp.ndarray`` عند الإمكان: memoryviews خفيفة الوزن.

* تجنب تقطيع memoryview: قد يكون تقطيع memoryview مكلفًا أو مضللًا في بعض الحالات
  ومن الأفضل عدم استخدامه، حتى إذا كان التعامل مع أبعاد أقل في بعض السياقات مفضلًا.

* قم بتزيين الفصول أو الطرق النهائية باستخدام ``@final`` (يسمح هذا بإزالة الجداول الافتراضية عند الحاجة)

* قم بتضمين الطرق والدوال عندما يكون ذلك منطقيًا

* عند الشك، اقرأ الشيفرة C أو C++ المولدة إذا استطعت: "كلما قل عدد تعليمات C والإشارات
  لخط من شيفرة Cython، كان ذلك أفضل" هي قاعدة جيدة للإبهام.

* تعتبر إعلانات ``nogil`` مجرد تلميحات: عند إعلان دالة ``cdef``
  على أنها nogil، يعني ذلك أنه يمكن استدعاؤها دون الاحتفاظ بـ GIL، ولكنها لا تطلق
  GIL عند الدخول إليها. يجب عليك القيام بذلك بنفسك إما عن طريق تمرير ``nogil=True`` إلى
  ``cython.parallel.prange`` بشكل صريح، أو باستخدام مدير سياق صريح:

  .. code-block:: cython

      cdef inline void my_func(self) nogil:

          # بعض المنطق الذي يتفاعل مع CPython، على سبيل المثال، تخصيص المصفوفات عبر NumPy.

          with nogil:
              # يتم تشغيل الشيفرة هنا كما لو كانت مكتوبة في C.

          return 0

  يعتمد هذا البند على `هذا التعليق من Stéfan's Benhel <https://github.com/cython/cython/issues/2798#issuecomment-459971828>`_

* من الممكن إجراء مكالمات مباشرة إلى روتينات BLAS عبر الواجهات المحددة في ``sklearn.utils._cython_blas``.

استخدام OpenMP
^^^^^^^^^^^^

نظرًا لأنه يمكن بناء scikit-learn بدون OpenMP، فمن الضروري حماية كل
مكالمة مباشرة إلى OpenMP.

تقدم وحدة نمطية `_openmp_helpers`، المتوفرة في
`sklearn/utils/_openmp_helpers.pyx <https://github.com/scikit-learn/scikit-learn/blob/main/sklearn/utils/_openmp_helpers.pyx>`_
إصدارات محمية من روتينات OpenMP. لاستخدام روتينات OpenMP، يجب
استيرادها من هذه الوحدة النمطية وليس من مكتبة OpenMP مباشرة:

.. code-block:: cython

   from sklearn.utils._openmp_helpers cimport omp_get_max_threads
   max_threads = omp_get_max_threads()


تم بالفعل حماية حلقة التكرار المتوازية، `prange`، بواسطة cython ويمكن استخدامها مباشرة
من `cython.parallel`.

الأنواع
~~~~~

يتطلب شيفرة Cython استخدام أنواع صريحة. هذا هو أحد الأسباب التي تحصل عليها
تعزيز الأداء. لتجنب ازدواجية الشيفرة، لدينا مكان مركزي
لأنواع الأكثر استخدامًا في
`sklearn/utils/_typedefs.pyd <https://github.com/scikit-learn/scikit-learn/blob/main/sklearn/utils/_typedefs.pyd>`_.
من الناحية المثالية، تبدأ بالنظر هناك و ``cimport`` الأنواع التي تحتاجها، على سبيل المثال

.. code-block:: cython

    from sklear.utils._typedefs cimport float32, float64