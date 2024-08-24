.. _kernel_ridge:

انحدار الركود النووي
===========================

.. currentmodule:: sklearn.kernel_ridge

يُدمج انحدار الركود النووي (KRR) [M2012] _ بين :ref:`ridge_regression`
(المربعات الصغرى الخطية مع الانتظام L2-norm) و "حيلة النواة
<https://en.wikipedia.org/wiki/Kernel_method>`_. وبالتالي، فهو يتعلم وظيفة خطية في الفضاء الذي تحفزه النواة والبيانات. بالنسبة
للنوى غير الخطية، يتوافق هذا مع دالة غير خطية في الفضاء الأصلي.

إن نموذج :class:`KernelRidge` متطابق في الشكل مع انحدار ناقلات الدعم (:class:`~sklearn.svm.SVR`). ومع ذلك، يتم استخدام دالات خسارة مختلفة: يستخدم KRR دالة الخسارة التربيعية في حين يستخدم انحدار ناقلات الدعم :math:`\epsilon`- دالة الخسارة غير الحساسة، وكلاهما مدمج مع الانتظام L2. وعلى عكس :class:`~sklearn.svm.SVR`، يمكن إحكام :class:`KernelRidge` في صورة مغلقة وعادة ما يكون أسرع بالنسبة لمجموعات البيانات متوسطة الحجم. من ناحية أخرى، فإن النموذج المُتعلم غير مُقتصد، وبالتالي فهو أبطأ من :class:`~sklearn.svm.SVR`، الذي يتعلم نموذجًا مقتصدًا لـ :math:`\epsilon > 0`، في وقت التنبؤ.

تقارن الأشكال التالية بين :class:`KernelRidge` و
:class:`~sklearn.svm.SVR` على مجموعة بيانات اصطناعية، تتكون من دالة هدف جيبية وضجيج قوي يُضاف إلى كل نقطة بيانات خامسة.
تم رسم النموذج المُتعلم لكل من :class:`KernelRidge` و :class:`~sklearn.svm.SVR`، حيث تم تحسين كل من التعقيد/الانتظام وعرض نطاق نواة RBF باستخدام البحث الشبكي. الوظائف المُتعلمة متشابهة للغاية؛ ومع ذلك، فإن إحكام :class:`KernelRidge` أسرع حوالي سبع مرات من إحكام :class:`~sklearn.svm.SVR` (كلاهما مع البحث الشبكي). ومع ذلك، فإن التنبؤ بـ 100000 قيمة مستهدفة أسرع ثلاث مرات مع :class:`~sklearn.svm.SVR` لأنه تعلم نموذجًا مقتصدًا باستخدام حوالي 1/3 فقط من نقاط بيانات التدريب البالغ عددها 100 كمتجهات دعم.

.. figure:: ../auto_examples/miscellaneous/images/sphx_glr_plot_kernel_ridge_regression_001.png
   :target: ../auto_examples/miscellaneous/plot_kernel_ridge_regression.html
   :align: center

تقارن الأشكال التالية بين وقت الإحكام والتنبؤ لـ :class:`KernelRidge` و :class:`~sklearn.svm.SVR` لمجموعات تدريب ذات أحجام مختلفة. إن إحكام :class:`KernelRidge` أسرع من
:class:`~sklearn.svm.SVR` لمجموعات التدريب متوسطة الحجم (أقل من 1000
عينة)؛ ومع ذلك، بالنسبة لمجموعات التدريب الأكبر، فإن :class:`~sklearn.svm.SVR` يتوسع بشكل أفضل. فيما يتعلق بوقت التنبؤ، :class:`~sklearn.svm.SVR` أسرع من :class:`KernelRidge` لجميع أحجام مجموعة التدريب بسبب الحل المُقتصد المُتعلم. لاحظ أن درجة الاقتصاص، وبالتالي وقت التنبؤ، تعتمد على معلمي :math:`\epsilon` و :math:`C` من :class:`~sklearn.svm.SVR`؛ :math:`\epsilon = 0` من شأنه أن يتوافق مع نموذج كثيف.

.. figure:: ../auto_examples/miscellaneous/images/sphx_glr_plot_kernel_ridge_regression_002.png
   :target: ../auto_examples/miscellaneous/plot_kernel_ridge_regression.html
   :align: center

.. rubric:: أمثلة

* :ref:`sphx_glr_auto_examples_miscellaneous_plot_kernel_ridge_regression.py`

.. rubric:: المراجع

.. [M2012] "Machine Learning: A Probabilistic Perspective"
   Murphy, K. P. - chapter 14.4.3, pp. 492-493, The MIT Press, 2012