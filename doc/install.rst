.. _تعليمات-التثبيت:

========================
تثبيت سكايت-ليرن
========================

هناك طرق مختلفة لتثبيت سكايت-ليرن:

* :ref:`تثبيت آخر إصدار رسمي <تثبيت_الإصدار_الرسمي>`. هذه
  أفضل طريقة لمعظم المستخدمين. سيوفر نسخة مستقرة
  وتتوفر حزم مسبقة البناء لمعظم المنصات.

* تثبيت إصدار سكايت-ليرن الذي يوفره
  :ref:`نظام التشغيل أو توزيع بايثون <التثبيت_حسب_التوزيع>`.
  هذه طريقة سريعة لأولئك الذين لديهم أنظمة تشغيل أو توزيعات بايثون
  تقوم بتوزيع سكايت-ليرن.
  قد لا يوفر أحدث إصدار.

* :ref:`بناء الحزمة من المصدر
  <تثبيت_النسخة_الأحدث>`. هذه الطريقة أفضل للمستخدمين الذين يريدون
  أحدث الميزات ولا يخشون تشغيل
  التعليمات البرمجية الجديدة تمامًا. هذا مطلوب أيضًا للمستخدمين الذين يرغبون في المساهمة في
  المشروع.


.. _تثبيت_الإصدار_الرسمي:

تثبيت آخر إصدار
=================

.. raw:: html

  <style>
    /* إظهار التعليق التوضيحي على الشاشات الكبيرة */
    @media screen and (min-width: 960px) {
      .install-instructions .sd-tab-set {
        --tab-caption-width: 20%;
      }

      .install-instructions .sd-tab-set.tabs-os::before {
        content: "نظام التشغيل";
      }

      .install-instructions .sd-tab-set.tabs-package-manager::before {
        content: "مدير الحزم";
      }
    }
  </style>

.. div:: install-instructions

  .. tab-set::
    :class: tabs-os

    .. tab-item:: ويندوز
      :class-label: tab-4

      .. tab-set::
        :class: tabs-package-manager

        .. tab-item:: باي باي
          :class-label: tab-6
          :sync: package-manager-pip

          قم بتثبيت إصدار 64 بت من بايثون 3، على سبيل المثال من
          `الموقع الرسمي <https://www.python.org/downloads/windows/>`__.

          الآن قم بإنشاء `بيئة افتراضية (venv)
          <https://docs.python.org/3/tutorial/venv.html>`_ وثبت سكايت-ليرن.
          لاحظ أن البيئة الافتراضية اختيارية ولكن يوصى بها بشدة،
          لتجنب أي تعارضات محتملة مع الحزم الأخرى.

          .. prompt:: powershell

            python -m venv sklearn-env
            sklearn-env\Scripts\activate  # التنشيط
            pip install -U scikit-learn

          للتحقق من تثبيتك، يمكنك استخدام ما يلي:

          .. prompt:: powershell

            python -m pip show scikit-learn  # إظهار إصدار وتموقع سكايت-ليرن
            python -m pip freeze             # إظهار جميع الحزم المثبتة في البيئة
            python -c "import sklearn; sklearn.show_versions()"

        .. tab-item:: كوندا
          :class-label: tab-6
          :sync: package-manager-conda

          .. include:: ./install_instructions_conda.rst

    .. tab-item:: ماك أو إس
      :class-label: tab-4

      .. tab-set::
        :class: tabs-package-manager

        .. tab-item:: باي باي
          :class-label: tab-6
          :sync: package-manager-pip

          قم بتثبيت بايثون 3 باستخدام `هومبريو <https://brew.sh/>`_ (`brew install python`)
          أو عن طريق تثبيت الحزمة يدويًا من `الموقع الرسمي
          <https://www.python.org/downloads/macos/>`__.

          الآن قم بإنشاء `بيئة افتراضية (venv)
          <https://docs.python.org/3/tutorial/venv.html>`_ وثبت سكايت-ليرن.
          لاحظ أن البيئة الافتراضية اختيارية ولكن يوصى بها بشدة،
          لتجنب أي تعارضات محتملة مع الحزم الأخرى.

          .. prompt:: bash

            python -m venv sklearn-env
            source sklearn-env/bin/activate  # التنشيط
            pip install -U scikit-learn

          للتحقق من تثبيتك، يمكنك استخدام ما يلي:

          .. prompt:: bash

            python -m pip show scikit-learn  # إظهار إصدار وتموقع سكايت-ليرن
            python -m pip freeze             # إظهار جميع الحزم المثبتة في البيئة
            python -c "import sklearn; sklearn.show_versions()"

        .. tab-item:: كوندا
          :class-label: tab-6
          :sync: package-manager-conda

          .. include:: ./install_instructions_conda.rst

    .. tab-item:: لينكس
      :class-label: tab-4

      .. tab-set::
        :class: tabs-package-manager

        .. tab-item:: باي باي
          :class-label: tab-6
          :sync: package-manager-pip

          عادة ما يكون بايثون 3 مثبتًا بشكل افتراضي على معظم توزيعات لينكس. للتحقق مما إذا كان
          مثبتًا، جرب ما يلي:

          .. prompt:: bash

            python3 --version
            pip3 --version

          إذا لم يكن لديك بايثون 3 مثبتًا، يرجى تثبيت `python3` و
          `python3-pip` من مدير حزم توزيعك.

          الآن قم بإنشاء `بيئة افتراضية (venv)
          <https://docs.python.org/3/tutorial/venv.html>`_ وثبت سكايت-ليرن.
          لاحظ أن البيئة الافتراضية اختيارية ولكن يوصى بها بشدة،
          لتجنب أي تعارضات محتملة مع الحزم الأخرى.

          .. prompt:: bash

            python3 -m venv sklearn-env
            source sklearn-env/bin/activate  # التنشيط
            pip3 install -U scikit-learn

          للتحقق من تثبيتك، يمكنك استخدام ما يلي:

          .. prompt:: bash

            python3 -m pip show scikit-learn  # إظهار إصدار وتموقع سكايت-ليرن
            python3 -m pip freeze             # إظهار جميع الحزم المثبتة في البيئة
            python3 -c "import sklearn; sklearn.show_versions()"

        .. tab-item:: كوندا
          :class-label: tab-6
          :sync: package-manager-conda

          .. include:: ./install_instructions_conda.rst


يُمكِّن استخدام بيئة معزولة مثل باي باي فينف أو كوندا من
تثبيت إصدار محدد من سكايت-ليرن باستخدام باي باي أو كوندا واعتماداته
بمعزل عن أي حزم بايثون مثبتة مسبقًا. خاصة في لينكس، لا يُنصح بتثبيت حزم باي باي
بجانب الحزم التي يديرها مدير حزم التوزيع (أبت، دنياف، باكمان...).

لاحظ أنه يجب عليك دائمًا تذكر تنشيط بيئة اختيارك
قبل تشغيل أي أمر بايثون في كل مرة تبدأ فيها جلسة طرفية جديدة.

إذا لم تقم بتثبيت نومبي أو سايباي بعد، فيمكنك أيضًا تثبيتهما باستخدام
كوندا أو باي باي. عند استخدام باي باي، يرجى التأكد من استخدام *عجلات ثنائية*،
وألا يتم إعادة تجميع نومبي وسايباي من المصدر، والذي يمكن أن يحدث عند استخدام
تكوينات معينة من نظام التشغيل والأجهزة (مثل لينكس على
راسبيري باي).

تتطلب قدرات سكايت-ليرن للرسم البياني (أي الدالات التي تبدأ بـ `plot_ `
والفئات التي تنتهي بـ `Display`) ماتبلوتليب. تتطلب الأمثلة
ماتبلوتليب ويتطلب بعض الأمثلة سكايت-إيماج أو بانداس أو سيبورن. يتم سرد الحد الأدنى
من إصدارات اعتمادات سكايت-ليرن أدناه جنبًا إلى جنب مع الغرض منها.

.. include:: min_dependency_table.rst

.. warning::

    كان سكايت-ليرن 0.20 هو الإصدار الأخير الذي يدعم بايثون 2.7 و 3.4.
    دعم سكايت-ليرن 0.21 بايثون 3.5-3.7.
    دعم سكايت-ليرن 0.22 بايثون 3.5-3.8.
    تطلب سكايت-ليرن 0.23-0.24 بايثون 3.6 أو أحدث.
    دعم سكايت-ليرن 1.0 بايثون 3.7-3.10.
    تدعم سكايت-ليرن 1.1 و 1.2 و 1.3 بايثون 3.8-3.12
    يتطلب سكايت-ليرن 1.4 بايثون 3.9 أو أحدث.

.. _التثبيت_حسب_التوزيع:

توزيعات الطرف الثالث من سكايت-ليرن
=================================

توفر بعض توزيعات الطرف الثالث إصدارات من
سكايت-ليرن مدمجة مع أنظمة إدارة الحزم الخاصة بها.

يمكن أن يجعل هذا التثبيت والترقية أسهل بكثير للمستخدمين نظرًا لأن
التكامل يشمل القدرة على تثبيت
الاعتمادات تلقائيًا (نومبي، سايباي) التي يحتاجها سكايت-ليرن.

فيما يلي قائمة غير مكتملة بأنظمة التشغيل وتوزيعات بايثون
التي توفر إصداراتها الخاصة من سكايت-ليرن.

ألباين لينكس
------------

تتوفر حزمة ألباين لينكس من خلال `المستودعات الرسمية
<https://pkgs.alpinelinux.org/packages?name=py3-scikit-learn>`__ باسم
``py3-scikit-learn`` لبايثون.
يمكن تثبيته عن طريق كتابة الأمر التالي:

.. prompt:: bash

  sudo apk add py3-scikit-learn


أرتش لينكس
----------

تتوفر حزمة أرتش لينكس من خلال `المستودعات الرسمية
<https://www.archlinux.org/packages/?q=scikit-learn>`_ باسم
``python-scikit-learn`` لبايثون.
يمكن تثبيته عن طريق كتابة الأمر التالي:

.. prompt:: bash

  sudo pacman -S python-scikit-learn


دبيان/أوبونتو
-------------

تم تقسيم حزمة دبيان/أوبونتو إلى ثلاث حزم مختلفة تسمى
``python3-sklearn`` (وحدات بايثون)، ``python3-sklearn-lib`` (التطبيقات
والروابط منخفضة المستوى)، ``python3-sklearn-doc`` (الوثائق).
لاحظ أن سكايت-ليرن يتطلب بايثون 3، وبالتالي الحاجة إلى استخدام أسماء الحزم
ذات البادئة `python3-`.
يمكن تثبيت الحزم باستخدام ``apt-get``:

.. prompt:: bash

  sudo apt-get install python3-sklearn python3-sklearn-lib python3-sklearn-doc


فيدورا
------

تسمى حزمة فيدورا ``python3-scikit-learn`` للإصدار 3 من بايثون،
وهو الإصدار الوحيد المتاح في فيدورا.
يمكن تثبيته باستخدام ``dnf``:

.. prompt:: bash

  sudo dnf install python3-scikit-learn


نت بي إس دي
------

سكايت-ليرن متاح عبر `pkgsrc-wip <http://pkgsrc-wip.sourceforge.net/>`_:
https://pkgsrc.se/math/py-scikit-learn


ماك بورتس لنظام ماك أو إس إكس
--------------------

تسمى حزمة ماك بورتس ``py<XY>-scikits-learn``،
حيث ``XY`` تشير إلى إصدار بايثون.
يمكن تثبيته عن طريق كتابة الأمر التالي:

.. prompt:: bash

  sudo port install py39-scikit-learn


أناكوندا وإينثوت دبلويمنت ماناجر لجميع المنصات المدعومة
---------------------------------------------------------------------

يأتي كل من `أناكوندا <https://www.anaconda.com/download>`_ و
`إينثوت دبلويمنت ماناجر <https://assets.enthought.com/downloads/>`_
مع سكايت-ليرن بالإضافة إلى مجموعة كبيرة من مكتبات بايثون العلمية لنظام
ويندوز وماك أو إس إكس ولينكس.

تقدم أناكوندا سكايت-ليرن كجزء من توزيعها المجاني.


إنتل إكستينشن لسكايت-ليرن
--------------------------------

تحافظ إنتل على حزمة x86_64 المحسنة، المتاحة في باي باي آي (عبر `باي باي`)،
وفي قنوات `main` و`conda-forge` و`intel` كوندا:

.. prompt:: bash

  conda install scikit-learn-intelex

تحتوي هذه الحزمة على إصدار محسن من إنتل للعديد من الخوارزميات. عندما
لا يوجد تنفيذ بديل، يتم استخدام تنفيذ سكايت-ليرن كخيار ثانوي. تأتي هذه الخوارزميات المحسنة
من مكتبة سي++ ون ديل وهي محسنة لهندسة x86_64، ومحسنة لمعالجات إنتل متعددة النواة.

لاحظ أن هذه الخوارزميات غير مفعلة افتراضيًا، يرجى الرجوع إلى
وثائق `scikit-learn-intelex <https://intel.github.io/scikit-learn-intelex/latest/what-is-patching.html>`_
لمزيد من التفاصيل حول سيناريوهات الاستخدام. مثال على الاستخدام المباشر:

.. prompt:: python >>>

  from sklearnex.neighbors import NearestNeighbors

يتم التحقق من التوافق مع خوارزميات سكايت-ليرن القياسية عن طريق تشغيل
جناح اختبار سكايت-ليرن الكامل عبر تكامل مستمر تلقائي كما هو مبلغ عنه
على https://github.com/intel/scikit-learn-intelex. إذا لاحظت أي مشكلة
مع `scikit-learn-intelex`، يرجى الإبلاغ عن المشكلة على
`مسجل المشكلات <https://github.com/intel/scikit-learn-intelex/issues>`__ الخاص بهم.


وينبايثون لنظام ويندوز
---------------------

يقوم مشروع `وينبايثون <https://winpython.github.io/>`_ بتوزيع
سكايت-ليرن كإضافة إضافية.


استكشاف الأخطاء وإصلاحها
إذا واجهتك أخطاء غير متوقعة أثناء تثبيت سكيت-ليرن، يمكنك تقديم مشكلة إلى "تتبع المشكلات <https://github.com/scikit-learn/scikit-learn/issues>". قبل ذلك، يرجى التأكد أيضًا من التحقق من مشكلات عامة التالية.

.. _windows_longpath:

خطأ بسبب حد طول مسار الملف في نظام التشغيل Windows
-------------------------------------------------

قد يحدث أن يفشل باي باي في تثبيت الحزم عند الوصول إلى حد حجم المسار الافتراضي في نظام التشغيل Windows إذا تم تثبيت بايثون في موقع متداخل مثل هيكل مجلد "AppData" ضمن دليل المنزل للمستخدم، على سبيل المثال::

    C:\Users\username>C:\Users\username\AppData\Local\Microsoft\WindowsApps\python.exe -m pip install scikit-learn
    Collecting scikit-learn
    ...
    Installing collected packages: scikit-learn
    ERROR: Failed to build sklearn C:\Users\username\AppData\Local\Temp\pip-install-q29_u2a2\scikit-learn\
    ...
    ERROR: Could not build wheels for sklearn which use PEP 517 and cannot be installed directly

في هذه الحالة، يمكن رفع هذا الحد في سجل Windows باستخدام أداة "regedit":

#. اكتب "regedit" في قائمة ابدأ في Windows لتشغيل "regedit".

#. انتقل إلى
   ``Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem``
   المفتاح.

#. قم بتحرير قيمة خاصية "LongPathsEnabled" لهذا المفتاح وضبطها على 1.

#. أعد تثبيت سكيت-ليرن (مع تجاهل التثبيت السابق المعطوب):

   .. prompt:: powershell

      pip install --exists-action=i scikit-learn