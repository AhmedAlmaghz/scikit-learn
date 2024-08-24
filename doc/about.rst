حولنا
التاريخ
------

بدأ هذا المشروع في عام 2007 كمشروع صيفي من مشاريع Google Summer of Code بواسطة David Cournapeau. وفي وقت لاحق من ذلك العام، بدأ Matthieu Brucher العمل في هذا المشروع كجزء من أطروحته.

وفي عام 2010، تولى كل من فابيان بيدريجوسا، وجيل فاريوان، وألكسندر جرامفورت، وفينسنت ميشيل من المعهد الوطني الفرنسي للبحث في علوم الكمبيوتر والتحكم (INRIA) قيادة المشروع وأطلقوا الإصدار العام الأول في الأول من فبراير 2010. ومنذ ذلك الحين، ظهرت عدة إصدارات تتبع دورة مدتها حوالي 3 أشهر، وتولت مجتمع دولي مزدهر قيادة التطوير. ونتيجة لذلك، يحتفظ المعهد الوطني الفرنسي للبحث في علوم الكمبيوتر والتحكم (INRIA) بحقوق النشر على العمل الذي قام به الأشخاص الذين كانوا موظفين في المعهد في وقت المساهمة.

الحوكمة
----------

تتم مناقشة عملية صنع القرار وهيكل حوكمة سكيت-ليرن في :ref:`وثيقة الحوكمة <governance>`.

.. يتم وضع مراسي "المؤلف" أدناه لضمان استمرار عمل الروابط التشعبية القديمة (على شكل "about.html#author")

.. _authors:

الأشخاص وراء سكيت-ليرن
------------------------------

سكيت-ليرن هو مشروع مجتمعي، طوره مجموعة كبيرة من الأشخاص من جميع أنحاء العالم. وعلى الرغم من أن هناك عدة فرق، مذكورة أدناه، لديها أدوار مركزية، إلا أنه يمكن العثور على قائمة أكثر اكتمالاً للمساهمين على `جيثب
<https://github.com/scikit-learn/scikit-learn/graphs/contributors>`__.

فريق المديرين
................

الأشخاص التالية أسماؤهم هم حاليًا من المديرين، المسؤولين عن توحيد تطوير سكيت-ليرن وصيانته:

.. include:: maintainers.rst

.. note::

  يرجى عدم إرسال رسائل بريد إلكتروني مباشرة إلى المؤلفين لطلب المساعدة أو الإبلاغ عن المشكلات.
  بدلاً من ذلك، يرجى الاطلاع على `ما هي أفضل طريقة لطرح الأسئلة حول سكيت-ليرن
  <https://scikit-learn.org/stable/faq.html#what-s-the-best-way-to-get-help-on-scikit-learn-usage>`_
  في الأسئلة الشائعة.

.. seealso::

  كيف يمكنك :ref:`المساهمة في المشروع <contributing>`.

فريق التوثيق
..................

يساعد الأشخاص التالية أسماؤهم في توثيق المشروع:

.. include:: documentation_team.rst

فريق تجربة المساهمين
...........................

الأشخاص التالية أسماؤهم هم مساهمون نشطون يساعدون أيضًا في :ref:`فرز المشكلات <bug_triaging>`، وطلبات سحب (PRs)، والصيانة العامة:

.. include:: contributor_experience_team.rst

فريق التواصل
..................

يساعد الأشخاص التالية أسماؤهم في :ref:`التواصل حول سكيت-ليرن
<communication_team>`.

.. include:: communication_team.rst

مطورو النواة المتقاعدون
........................

الأشخاص التالية أسماؤهم كانوا مساهمين نشطين في الماضي، لكنهم لم يعودوا نشطين في المشروع:

.. include:: maintainers_emeritus.rst

فريق التواصل المتقاعد
...........................

كان الأشخاص التالية أسماؤهم نشطين في فريق التواصل في الماضي، لكنهم لم يعودوا يتحملون مسؤوليات التواصل:

.. include:: communication_team_emeritus.rst

فريق تجربة المساهمين المتقاعد
....................................

كان الأشخاص التالية أسماؤهم نشطين في فريق تجربة المساهمين في الماضي:

.. include:: contributor_experience_team_emeritus.rst

.. _citing-scikit-learn:

الاستشهاد بسكيت-ليرن
-------------------

إذا كنت تستخدم سكيت-ليرن في منشور علمي، فإننا نقدر الاستشهاد بالورقة التالية:

`سكيت-ليرن: التعلم الآلي في بايثون
<https://jmlr.csail.mit.edu/papers/v12/pedregosa11a.html>`_، بيدريجوسا
*وآخرون*، JMLR 12، الصفحات 2825-2830، 2011.

إدخال Bibtex::

  @article{scikit-learn,
    title={Scikit-learn: Machine Learning in {P}ython},
    author={Pedregosa, F. and Varoquaux, G. and Gramfort, A. and Michel, V.
            and Thirion, B. and Grisel, O. and Blondel, M. and Prettenhofer, P.
            and Weiss, R. and Dubourg, V. and Vanderplas, J. and Passos, A. and
            Cournapeau, D. and Brucher, M. and Perrot, M. and Duchesnay, E.},
    journal={Journal of Machine Learning Research},
    volume={12},
    pages={2825--2830},
    year={2011}
  }

إذا كنت ترغب في الاستشهاد بسكيت-ليرن بسبب واجهة برمجة التطبيقات (API) أو التصميم الخاص بها، فقد ترغب أيضًا في مراعاة الورقة التالية:

:arxiv:`تصميم واجهة برمجة التطبيقات لبرامج التعلم الآلي: التجارب من مشروع سكيت-ليرن
<1309.0238>`، بويتينك *وآخرون*، 2013.

إدخال Bibtex::

  @inproceedings{sklearn_api,
    author    = {Lars Buitinck and Gilles Louppe and Mathieu Blondel and
                  Fabian Pedregosa and Andreas Mueller and Olivier Grisel and
                  Vlad Niculae and Peter Prettenhofer and Alexandre Gramfort
                  and Jaques Grobler and Robert Layton and Jake VanderPlas and
                  Arnaud Joly and Brian Holt and Ga{\"{e}}l Varoquaux},
    title     = {{API} design for machine learning software: experiences from the scikit-learn
                  project},
    booktitle = {ECML PKDD Workshop: Languages for Data Mining and Machine Learning},
    year      = {2013},
    pages = {108--122},
  }

الرسومات
-------

شعارات عالية الجودة بتنسيق PNG وSVG متوفرة في دليل مصدر `doc/logos/
<https://github.com/scikit-learn/scikit-learn/tree/main/doc/logos>`_.

.. image:: images/scikit-learn-logo-notext.png
  :align: center

التمويل
سكيت-ليرن هو مشروع مدفوع من قبل المجتمع، ولكن المنح المؤسسية والخاصة تساعد في ضمان استدامته.

ويود المشروع أن يشكر الجهات المانحة التالية.

...................................

.. div:: sk-text-image-grid-small

  .. div:: text-box

    `:probabl. <https://probabl.ai>`_ توظف أدرين جالالي، وأرتورو أمور،
    فرانسوا جوبيل، جيلوم ليماتر، جيريمي دو بوا بيرانجر، لوايك ستيف،
    أوليفييه جريسيل، وستيفاني سينجر.

  .. div:: image-box

    .. image:: images/probabl.png
      :target: https://probabl.ai

..........

.. |chanel| image:: images/chanel.png
  :target: https://www.chanel.com

.. |axa| image:: images/axa.png
  :target: https://www.axa.fr/

.. |bnp| image:: images/bnp.png
  :target: https://www.bnpparibascardif.com/

.. |dataiku| image:: images/dataiku.png
  :target: https://www.dataiku.com/

.. |nvidia| image:: images/nvidia.png
  :target: https://www.nvidia.com

.. |inria| image:: images/inria-logo.jpg
  :target: https://www.inria.fr

.. raw:: html

  <style>
    table.image-subtable tr {
      border-color: transparent;
    }

    table.image-subtable td {
      width: 50%;
      vertical-align: middle;
      text-align: center;
    }

    table.image-subtable td img {
      max-height: 40px !important;
      max-width: 90% !important;
    }
  </style>

.. div:: sk-text-image-grid-small

  .. div:: text-box

    يساعد أعضاء `أعضاء <https://scikit-learn.fondation-inria.fr/en/home/#sponsors>`_
    من اتحاد سكيت-ليرن في `مؤسسة إنريا <https://scikit-learn.fondation-inria.fr/en/home/>`_
    في صيانة وتحسين المشروع من خلال دعمهم المالي.

  .. div:: image-box

    .. table::
      :class: image-subtable

      +----------+-----------+
      |       |chanel|       |
      +----------+-----------+
      |  |axa|   |    |bnp|  |
      +----------+-----------+
      |       |nvidia|       |
      +----------+-----------+
      |       |dataiku|      |
      +----------+-----------+
      |        |inria|       |
      +----------+-----------+

..........

.. div:: sk-text-image-grid-small

  .. div:: text-box

    `إنفيديا <https://nvidia.com>`_ تمول تيم هيد منذ عام 2022
    وهي جزء من اتحاد سكيت-ليرن في إنريا.

  .. div:: image-box

    .. image:: images/nvidia.png
      :target: https://nvidia.com

..........

.. div:: sk-text-image-grid-small

  .. div:: text-box

    `مايكروسوفت <https://microsoft.com/>`_ تمول أندرياس مولر منذ عام 2020.

  .. div:: image-box

    .. image:: images/microsoft.png
      :target: https://microsoft.com

...........

.. div:: sk-text-image-grid-small

  .. div:: text-box

    `مختبرات كوانسيت <https://labs.quansight.org>`_ تمول لوسي ليو منذ عام 2022.

  .. div:: image-box

    .. image:: images/quansight-labs.png
      :target: https://labs.quansight.org

...........

.. |czi| image:: images/czi.png
  :target: https://chanzuckerberg.com

.. |wellcome| image:: images/wellcome-trust.png
  :target: https://wellcome.org/

.. div:: sk-text-image-grid-small

  .. div:: text-box

    `مبادرة تشان زوكربيرج <https://chanzuckerberg.com/>`_ و
    `مؤسسة ويلكم <https://wellcome.org/>`_ تمول سكيت-ليرن من خلال
    `البرمجيات مفتوحة المصدر الأساسية للعلوم (EOSS) <https://chanzuckerberg.com/eoss/>`_
    الدورة 6.

    تدعم لوسي ليو ومبادرات التنوع والشمول التي سيتم الإعلان عنها في المستقبل.

  .. div:: image-box

    .. table::
      :class: image-subtable

      +----------+----------------+
      |  |czi|   |    |wellcome|  |
      +----------+----------------+

...........

.. div:: sk-text-image-grid-small

  .. div:: text-box

    `تايدليفت <https://tidelift.com/>`_ تدعم المشروع من خلال اتفاقية خدمتهم.

  .. div:: image-box

    .. image:: images/Tidelift-logo-on-light.svg
      :target: https://tidelift.com/

...........


الجهات الراعية السابقة
.............

.. div:: sk-text-image-grid-small

  .. div:: text-box

    `مختبرات كوانسيت <https://labs.quansight.org>`_ مولت ميكائيل زين في عامي 2022 و2023،
    ومولت توماس جي. فان من عام 2021 إلى عام 2023.

  .. div:: image-box

    .. image:: images/quansight-labs.png
      :target: https://labs.quansight.org

...........

.. div:: sk-text-image-grid-small

  .. div:: text-box

    `جامعة كولومبيا <https://columbia.edu/>`_ مولت أندرياس مولر
    (2016-2020).

  .. div:: image-box

    .. image:: images/columbia.png
      :target: https://columbia.edu

........

.. div:: sk-text-image-grid-small

  .. div:: text-box

    `جامعة سيدني <https://sydney.edu.au/>`_ مولت جويل نوثمان
    (2017-2021).

  .. div:: image-box

    .. image:: images/sydney-primary.jpeg
      :target: https://sydney.edu.au/

...........

.. div:: sk-text-image-grid-small

  .. div:: text-box

    حصل أندرياس مولر على منحة لتحسين سكيت-ليرن من
    `مؤسسة ألفريد بي سلون <https://sloan.org>`_ .
    دعم هذا المنحة منصب نيكولاس هوج وتوماس جي. فان.

  .. div:: image-box

    .. image:: images/sloan_banner.png
      :target: https://sloan.org/

.............

.. div:: sk-text-image-grid-small

  .. div:: text-box

    `إنريا <https://www.inria.fr>`_ تدعم هذا المشروع بنشاط. وقد وفرت التمويل لفابيان بيدريجوسا (2010-2012)،
    جاك جروبلر (2012-2013) وأوليفييه جريسيل (2013-2017) للعمل على هذا المشروع
    بدوام كامل. كما تستضيف إنريا فعاليات سبرينت الترميز وغيرها من الفعاليات.

  .. div:: image-box

    .. image:: images/inria-logo.jpg
      :target: https://www.inria.fr

.....................

.. div:: sk-text-image-grid-small

  .. div:: text-box

    `مركز باريس-ساكلي لعلوم البيانات <http://www.datascience-paris-saclay.fr/>`_
    مولت مطورًا للعمل على المشروع بدوام كامل لمدة عام واحد (2014-2015)، 50%
    من وقت جيلوم ليماتر (2016-2017) و50% من وقت جوريس فان دين
    بوسشي (2017-2018).

  .. div:: image-box

    .. image:: images/cds-logo.png
      :target: http://www.datascience-paris-saclay.fr/

..........................

.. div:: sk-text-image-grid-small

  .. div:: text-box

    `بيئة بيانات مور-سلوان في جامعة نيويورك <https://cds.nyu.edu/mooresloan/>`_
    مولت أندرياس مولر (2014-2016) للعمل على هذا المشروع. كما تمول بيئة بيانات مور-سلوان
    العديد من الطلاب للعمل على المشروع بدوام جزئي.

  .. div:: image-box

    .. image:: images/nyu_short_color.png
      :target: https://cds.nyu.edu/mooresloan/

........................

.. div:: sk-text-image-grid-small

  .. div:: text-box

    `تيليكوم باريس تك <https://www.telecom-paristech.fr/>`_ مولت مانوج كومار
    (2014)، وتوم دوبري لا تور (2015)، وراغاف آر في (2015-2017)، وتييري جويوموت
    (2016-2017) وألبرت توماس (2017) للعمل على سكيت-ليرن.

  .. div:: image-box

    .. image:: images/telecom.png
      :target: https://www.telecom-paristech.fr/

.....................

.. div:: sk-text-image-grid-small

  .. div:: text-box

    `مختبر إكس ديجيكوسم <https://digicosme.lri.fr>`_ مول نيكولاس جويكس
    (2015-2016)، وتوم دوبري لا تور (2015-2016 و2017-2018)، وماثورين ماسياس
    (2018-2019) للعمل بدوام جزئي على سكيت-ليرن خلال دراسات الدكتوراه الخاصة بهم. كما
    مولت المختبرات سبرينت ترميز سكيت-ليرن في عام 2015.

  .. div:: image-box

    .. image:: images/digicosme.png
      :target: https://digicosme.lri.fr

.....................

.. div:: sk-text-image-grid-small

  .. div:: text-box

    `مبادرة تشان زوكربيرج <https://chanzuckerberg.com/>`_ مولت نيكولاس
    هوج للعمل بدوام كامل على سكيت-ليرن في عام 2020.

  .. div:: image-box

    .. image:: images/czi.png
      :target: https://chanzuckerberg.com

......................

تم رعاية الطلاب التالية أسماؤهم من قبل `جوجل
<https://opensource.google/>`_ للعمل على سكيت-ليرن من خلال
برنامج `جوجل صيف الشفرة <https://en.wikipedia.org/wiki/Google_Summer_of_Code>`_
.

- 2007 - ديفيد كورناpeau
- 2011 - `فلاد نيكولاي`_
- 2012 - `فلاد نيكولاي`_، إيمانويل باير
- 2013 - كمال إرين، نيكولاس تريسيجني
- 2014 - حمزة الصالحي، عصام لارادجي، ماهيشاكيا ويجيواردينا، مانوج كومار
- 2015 - `راغاف آر في <https://github.com/raghavrv>`_، ويي شيوي
- 2016 - `نيلسون ليو <http://nelsonliu.me>`_، `يين تشين لين <https://yenchenlin.me/>`_

.. _فلاد نيكولاي: https://vene.ro/

...................

يدعم مشروع `نورو دبيان <http://neuro.debian.net>`_ الذي يوفر `دبيان
<https://www.debian.org/>`_ التعبئة والمساهمات من قبل
`الدكتور جيمس في. هاكسبي <http://haxbylab.dartmouth.edu/>`_ (`كلية دارتموث
<https://pbs.dartmouth.edu/>`_).

...................

قامت المنظمات التالية بتمويل اتحاد سكيت-ليرن في إنريا في
الماضي:

.. |msn| image:: images/microsoft.png
  :target: https://www.microsoft.com/

.. |bcg| image:: images/bcg.png
  :target: https://www.bcg.com/beyond-consulting/bcg-gamma/default.aspx

.. |fujitsu| image:: images/fujitsu.png
  :target: https://www.fujitsu.com/global/

.. |aphp| image:: images/logo_APHP_text.png
  :target: https://aphp.fr/

.. |hf| image:: images/huggingface_logo-noborder.png
  :target: https://huggingface.co

.. raw:: html

  <style>
    div.image-subgrid img {
      max-height: 50px;
      max-width: 90%;
    }
  </style>

.. grid:: 2 2 4 4
  :class-row: image-subgrid
  :gutter: 1

  .. grid-item::
    :class: sd-text-center
    :child-align: center

    |msn|

  .. grid-item::
    :class: sd-text-center
    :child-align: center

    |bcg|

  .. grid-item::
    :class: sd-text-center
    :child-align: center

    |fujitsu|

  .. grid-item::
    :class: sd-text-center
    :child-align: center

    |aphp|

  .. grid-item::
    :class: sd-text-center
    :child-align: center

    |hf|

سبرينت الترميز
--------------

للمشروع سكيت-ليرن تاريخ طويل من `سبرينت الترميز مفتوحة المصدر
<https://blog.scikit-learn.org/events/sprints-value/>`_ مع أكثر من 50 حدث سبرينت
من عام 2010 إلى يومنا هذا. هناك العديد من الجهات الراعية التي ساهمت
في التكاليف التي تشمل مكان الإقامة، والطعام، والسفر، ووقت المطور والمزيد. راجع
`سبرينت سكيت-ليرن <https://blog.scikit-learn.org/sprints/>`_ للحصول على قائمة
كاملة بالأحداث.

التبرع للمشروع
-----------------------

إذا كنت مهتمًا بالتبرع للمشروع أو لأحد سبرينت الترميز الخاصة بنا،
يرجى التبرع عبر `صفحة التبرعات لنمفوكاس
<https://numfocus.org/donate-to-scikit-learn>`_.

.. raw:: html

  <p class="text-center">
    <a class="btn sk-btn-orange mb-1" href="https://numfocus.org/donate-to-scikit-learn">
      ساعدنا، <strong>تبرع!</strong>
    </a>
  </p>

ستذهب جميع التبرعات إلى `نمفوكاس <https://numfocus.org/>`_، وهي منظمة غير ربحية
يديرها مجلس إدارة من `أعضاء مجتمع سايبي <https://numfocus.org/board.html>`_. تتمثل
مهمة نمفوكاس في تعزيز برمجيات الحوسبة العلمية، خاصة في بايثون. وكمسكن ضريبي
لمشروع سكيت-ليرن، فإنها تضمن توفر الأموال عند الحاجة لإبقاء المشروع ممولًا ومتاحًا
مع الامتثال للوائح الضريبية.

وستذهب التبرعات التي تم تلقيها لمشروع سكيت-ليرن في الغالب إلى تغطية نفقات السفر
لسبرينت الترميز، وكذلك إلى ميزانية تنظيم المشروع [#f1]_.

.. rubric:: ملاحظات

.. [#f1] فيما يتعلق بميزانية التنظيم، على وجه الخصوص، قد نستخدم بعض الأموال المتبرع بها
    لدفع نفقات المشروع الأخرى مثل نظام أسماء النطاقات،
    أو الاستضافة أو خدمات التكامل المستمر.


دعم البنية التحتية
----------------------

نود أيضًا أن نشكر `مايكروسوفت أزور <https://azure.microsoft.com/en-us/>`_،
`سيررس سي إل <https://cirrus-ci.org>`_، `سيركل سي إل <https://circleci.com/>`_ على وقت وحدة المعالجة المركزية
المجاني على خوادم التكامل المستمر الخاصة بهم، و`أناكوندا إنك. <https://www.anaconda.com>`_
على التخزين الذي توفره لبنائنا المرحلي والليلي.