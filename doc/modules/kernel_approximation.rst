تقريب النواة
يحتوي هذا البرنامج الفرعي على دوال تقريبية لتمثيل الخرائط التي تتوافق مع نوى معينة، كما هو مستخدم على سبيل المثال في آلات المتجهات الداعمة (راجع: ref: `svm`).

تقوم دوال الخصائص التالية بتحويلات غير خطية للإدخال، والتي يمكن استخدامها كأساس للتصنيف الخطي أو الخوارزميات الأخرى.

..... currentmodule:: sklearn.linear_model

الميزة النسبية لاستخدام الخرائط الصريحة التقريبية مقارنة بـ "حيلة النواة <https://en.wikipedia.org/wiki/Kernel_trick>`_، والتي تستخدم الخرائط الضمنية للخصائص، هي أن الخرائط الصريحة يمكن أن تكون أكثر ملاءمة للتعلم عبر الإنترنت ويمكن أن تقلل بشكل كبير من تكلفة التعلم مع مجموعات البيانات الكبيرة جدًا.

لا تتوسع SVMs النواة القياسية جيدًا في مجموعات البيانات الكبيرة، ولكن باستخدام خريطة نواة تقريبية، من الممكن استخدام SVMs الخطية الأكثر كفاءة.

وعلى وجه الخصوص، فإن الجمع بين تقريبات خريطة النواة مع: class: `SGDClassifier` يمكن أن يجعل التعلم غير الخطي على مجموعات البيانات الكبيرة ممكنًا.

نظرًا لعدم وجود الكثير من العمل التجريبي الذي يستخدم التضمين التقريبي، فمن المستحسن مقارنة النتائج بطرق النواة الدقيقة عند الإمكان.

..... seealso::

: ref: `polynomial_regression` لتحويل متعدد الحدود الدقيق.

..... currentmodule:: sklearn.kernel_approximation

..... _nystroem_kernel_approx:

طريقة Nystroem لتقريب النواة
----------------------------------------

طريقة Nystroem، كما هو منفذ في: class: `Nystroem` هي طريقة عامة لتقريبات الترتيب المنخفض للنوى. ويحقق ذلك عن طريق أخذ عينات بدون استبدال للصفوف/الأعمدة للبيانات التي يتم تقييم النواة عليها. في حين أن التعقيد الحسابي للأسلوب الدقيق هو: math: `O (n^3 _{\ text {samples}})``، فإن تعقيد التقريب هو: math: `O (n^2 _{\ text {components}} \ cdot n_ {\ text {samples}})``، حيث يمكن تعيين: math: `n_ {\ text {components}} \ ll n_ {\ text {samples}}`` بدون انخفاض كبير في الأداء [WS2001] _.

يمكننا إنشاء التحلل الذاتى لنواة المصفوفة: math: `K``، بناءً على ميزات البيانات، ثم تقسيمها إلى بيانات تم أخذ عينات منها وبيانات غير معاينة.

..... math::

K = U \Lambda U ^ T
= \ begin {bmatrix} U_1 \\ U_2 \ end {bmatrix} \ Lambda \ begin {bmatrix} U_1 \\ U_2 \ end {bmatrix} ^ T
= \ begin {bmatrix} U_1 \ Lambda U_1 ^ T & U_1 \ Lambda U_2 ^ T \\ U_2 \ Lambda U_1 ^ T & U_2 \ Lambda U_2 ^ T \ end {bmatrix}
\ equiv \ begin {bmatrix} K_ {11} & K_ {12} \\ K_ {21} & K_ {22} \ end {bmatrix}

حيث:

* :math: `U` هو متعامد
* :math: `Lambda` هو مصفوفة القطرية للقيم الذاتية
* :math: `U_1` عبارة عن مصفوفة متعامدة للعينات التي تم اختيارها
* :math: `U_2` عبارة عن مصفوفة متعامدة للعينات التي لم يتم اختيارها

نظرًا لأنه يمكن الحصول على: math: `U_1 \ Lambda U_1 ^ T` عن طريق التطبيع المتعامد للمصفوفة: math: `K_ {11}`، ويمكن تقييم: math: `U_2 \ Lambda U_1 ^ T` (وكذلك نقلها)، فإن المصطلح المتبقي الوحيد الذي يجب توضيحه هو: math: `U_2 \ Lambda U_2 ^ T`. للقيام بذلك، يمكننا التعبير عنه من حيث المصفوفات التي تم تقييمها بالفعل:

..... math::

 \ begin {محاذاة} U_2 \ Lambda U_2 ^ T &= left (K_ {21} U_1 \ Lambda ^ {- 1} right) \ Lambda left (K_ {21} U_1 \ Lambda ^ {- 1} right) ^ T
\\ كان = K_ {21} U_1 left (\ Lambda ^ {- 1} \ Lambda right) \ Lambda ^ {- 1} U_1 ^ T K_ {21} ^ T
\\ كان = K_ {21} U_1 \ Lambda ^ {- 1} U_1 ^ T K_ {21} ^ T
\\ كان = K_ {21} K_ {11} ^ {- 1} K_ {21} ^ T
\\ كان = left (K_ {21} K_ {11} ^ {- \ frac {1} {2}} right) left (K_ {21} K_ {11} ^ {- \ frac {1} {2}} right) ^ T
. \ end {محاذاة}

أثناء "التناسب"، تقيِّم الفئة: class: `Nystroem` الأساس: math: `U_1`، وتحسب ثابت التطبيع،: math: `K_ {11} ^ {- \ frac {1} {2}}`. لاحقًا، أثناء "التحويل"، يتم تحديد مصفوفة النواة بين الأساس (معطى بواسطة السمة "components_") ونقاط البيانات الجديدة، "X". يتم بعد ذلك ضرب هذه المصفوفة بمصفوفة "normalization_" للحصول على النتيجة النهائية.

بشكل افتراضي، يستخدم: class: `Nystroem` نواة "rbf"، ولكنه يمكن أن يستخدم أي دالة نواة أو مصفوفة نواة محسوبة مسبقًا. يتم إعطاء عدد العينات المستخدمة - وهو أيضًا أبعاد الميزات المحسوبة - بواسطة معلمة "n_components".

..... rubric:: أمثلة

* راجع المثال المعنون
  : ref: `sphx_glr_auto_examples_applications_plot_cyclical_feature_engineering.py`،
  الذي يوضح خط أنابيب التعلم الآلي الفعال الذي يستخدم نواة: class: `Nystroem`.

..... _rbf_kernel_approx:

دالة الأساس الشعاعي
----------------------------

يقوم: class: `RBFSampler` ببناء خريطة تقريبية لدالة الأساس الشعاعي، والمعروفة أيضًا باسم *Random Kitchen Sinks* [RR2007] _. يمكن استخدام هذا التحويل لنمذجة خريطة النواة بشكل صريح، قبل تطبيق خوارزمية خطية، على سبيل المثال SVM الخطي::

>>> من sklearn.kernel_approximation import RBFSampler
>>> من sklearn.linear_model import SGDClassifier
>>> X = [[0،0]، [1،1]، [1،0]، [0،1]]
>>> y = [0،0،1،1]
>>> rbf_feature = RBFSampler (gamma = 1، random_state = 1)
>>> X_features = rbf_feature.fit_transform (X)
>>> clf = SGDClassifier (max_iter = 5)
>>> clf.fit (X_features، y)
SGDClassifier (max_iter = 5)
>>> clf.score (X_features، y)
1.0

يعتمد التحويل على تقريب مونت كارلو لقيم النواة. تقوم دالة "التناسب" بتنفيذ أخذ العينات مونت كارلو، في حين أن طريقة "التحويل" تقوم بتحويل البيانات. نظرًا للعشوائية المتأصلة في العملية، قد تختلف النتائج بين مكالمات مختلفة لدالة "التناسب".

تأخذ دالة "التناسب" حجتين: "n_components"، وهو البعد المستهدف لتحويل الميزة، و"gamma"، وهو معلمة دالة RBF-kernel. ستؤدي قيمة أعلى لـ "n_components" إلى تقريب أفضل للنواة وستنتج نتائج أكثر تشابهًا لتلك التي ينتجها SVM النووي. لاحظ أن "تناسب" دالة الميزة لا يعتمد في الواقع على البيانات المقدمة إلى دالة "التناسب".

يتم استخدام أبعاد البيانات فقط. يمكن العثور على التفاصيل حول الأسلوب في [RR2007] _.

بالنسبة لقيمة معينة من "n_components"، غالبًا ما يكون: class: `RBFSampler` أقل دقة من: class: `Nystroem`. : class: `RBFSampler` أرخص في الحساب، مما يجعل استخدام مساحات الميزات الأكبر أكثر كفاءة.

..... figure:: ../auto_examples/miscellaneous/images/sphx_glr_plot_kernel_approximation_002.png
: target: ../auto_examples/miscellaneous/plot_kernel_approximation.html
: scale: 50٪
: align: center

مقارنة نواة RBF الدقيقة (يسار) بالتقريب (يمين)

..... rubric:: أمثلة

* : ref: `sphx_glr_auto_examples_miscellaneous_plot_kernel_approximation.py`

..... _additive_chi_kernel_approx:

دالة النواة التربيعية الإضافية
---------------------------

دالة النواة التربيعية الإضافية هي نواة على التوزيعات التكرارية، والتي تستخدم غالبًا في رؤية الكمبيوتر.

دالة النواة التربيعية الإضافية المستخدمة هنا هي:

..... math::

k (x، y) = \ sum_i \ frac {2x_iy_i} {x_i + y_i}

هذا لا يتوافق بالضبط مع: func: `sklearn.metrics.pairwise.additive_chi2_kernel`. يفضل مؤلفو [VZ2010] _ الإصدار أعلاه لأنه إيجابي محدد دائمًا.

نظرًا لأن النواة مضافة، فمن الممكن معاملة جميع المكونات: math: `x_i` بشكل منفصل للتضمين. وهذا يجعل من الممكن أخذ عينات من تحويل فورييه في فترات منتظمة، بدلاً من التقريب باستخدام أخذ العينات مونت كارلو.

تنفذ الفئة: class: `AdditiveChi2Sampler` أخذ العينات المحددة المكونة من المكونات. يتم أخذ عينات من كل مكون: math: `n` مرة، مما يؤدي إلى: math: `2n + 1` أبعاد لكل بعد إدخال (ينتج الضرب في اثنين عن الجزء الحقيقي والتخيلي لتحويل فورييه).

في الأدبيات، يتم عادةً اختيار: math: `n` لتكون 1 أو 2، مما يحول مجموعة البيانات إلى حجم "n_samples * 5 * n_features" (في حالة: math: `n = 2`).

يمكن دمج خريطة الميزة التقريبية التي يوفرها: class: `AdditiveChi2Sampler` مع خريطة الميزة التقريبية التي يوفرها: class: `RBFSampler` لإنتاج خريطة ميزة تقريبية لدالة النواة التربيعية الأسية.

راجع [VZ2010] _ للتفاصيل و [VVZ2010] _ للجمع مع: class: `RBFSampler`.

..... _skewed_chi_kernel_approx:

دالة النواة التربيعية المنحرفة
-------------------------

دالة النواة التربيعية المنحرفة هي:

..... math::

k (x، y) = \ prod_i \ frac {2 \ sqrt {x_i + c} \ sqrt {y_i + c}} {x_i + y_i + 2c}


لديك خصائص مشابهة لدالة النواة التربيعية الأسية المستخدمة غالبًا في رؤية الكمبيوتر، ولكنها تسمح بتقريب مونت كارلو البسيط لخريطة الميزة.

يتم استخدام: class: `SkewedChi2Sampler` بنفس طريقة الاستخدام الموضحة أعلاه لـ: class: `RBFSampler`. الفرق الوحيد هو في المعلمة الحرة، والتي يطلق عليها: math: `c`.

للاطلاع على الدافع وراء هذا التحويل والتفاصيل الرياضية، راجع [LS2010] _.

..... _polynomial_kernel_approx:

تقريب دالة النواة متعددة الحدود عبر رسم تخطيطي للمخطط
-------------------------------------------------

دالة النواة متعددة الحدود: ref: `polynomial_kernel` هي نوع شائع من دالة النواة معطاة بواسطة:

..... math::

k (x، y) = (\ gamma x ^ top y +c_0) ^ d

حيث:

* ``x``، ``y`` هما متجهات الإدخال
* ``d`` هو درجة النواة

بديهياً، تتكون مساحة الميزة لدالة النواة متعددة الحدود من الدرجة `d`

من جميع المنتجات المحتملة من الدرجة `d` بين ميزات الإدخال، مما يمكّن

خوارزميات التعلم التي تستخدم هذه النواة من مراعاة التفاعلات بين الميزات.

تعد طريقة TensorSketch [PP2013] _، كما هو منفذ في: class: `PolynomialCountSketch`، طريقة قابلة للتطوير ومستقلة عن بيانات الإدخال لتقريب دالة النواة متعددة الحدود.

يستند إلى مفهوم Count sketch [WIKICS] _ [CCF2002] _، وهي تقنية لخفض الأبعاد تشبه تجزئة الميزات، والتي تستخدم بدلاً من ذلك عدة دوال تجزئة مستقلة. يحصل TensorSketch على رسم تخطيطي للعدد من حاصل الضرب الخارجي لمتجهين (أو متجه مع نفسه)، والذي يمكن استخدامه كتقريب لمساحة ميزة دالة النواة متعددة الحدود. على وجه الخصوص، بدلاً من حساب الضرب الخارجي بشكل صريح، يحسب TensorSketch رسم تخطيطي للعدد من المتجهات ثم يستخدم الضرب متعدد الحدود عبر التحويل المتقطع السريع لحساب رسم تخطيطي للعدد من حاصل الضرب الخارجي.

لحسن الحظ، تتكون مرحلة التدريب لـ TensorSketch ببساطة من تهيئة بعض المتغيرات العشوائية. وبالتالي فهو مستقل عن بيانات الإدخال، أي أنه يعتمد فقط على عدد ميزات الإدخال، وليس على قيم البيانات.

بالإضافة إلى ذلك، يمكن لهذه الطريقة تحويل العينات في: math: `O (n_ {\ text {samples}} (n_ {\ text {features}} + n_ {\ text {components}} \ log (n_ {\ text {components}})))`

الوقت، حيث: math: `n_ {\ text {components}}` هو البعد المطلوب،

يتم تحديده بواسطة "n_components".

..... rubric:: أمثلة

* : ref: `sphx_glr_auto_examples_kernel_approximation_plot_scalable_poly_kernels.py`

..... _tensor_sketch_kernel_approx:

التفاصيل الرياضية
تعتمد طرق النواة مثل آلات المتجهات الداعمة أو التحليل الرئيسي المُحسّن باستخدام النواة على خاصية فضاءات هيلبرت ذات النواة القابلة للتكرار. بالنسبة لأي دالة نواة محددة إيجابية :math:`k` (ما يسمى نواة ميرسر)، من المضمون وجود تطبيق :math:`\phi` إلى فضاء هيلبرت :math:`\mathcal{H}`، بحيث

.. math::

        k(x,y) = \langle \phi(x), \phi(y) \rangle

حيث :math:`\langle \cdot, \cdot \rangle` يرمز إلى المنتج الداخلي في
فضاء هيلبرت.

إذا كانت خوارزمية، مثل آلة المتجهات الداعمة الخطية أو التحليل الرئيسي،
تعتمد فقط على المنتج القياسي لنقاط البيانات :math:`x_i`، فيمكن استخدام
قيمة :math:`k(x_i, x_j)`، والتي تتوافق مع تطبيق الخوارزمية
على نقاط البيانات المُمَثَلة :math:`\phi(x_i)`.
تكمن ميزة استخدام :math:`k` في أنه لا يلزم أبدًا حساب التطبيق :math:`\phi` بشكل صريح، مما يسمح بميزات كبيرة جدًا
(حتى اللانهاية).

أحد عيوب طرق النواة هو أنه قد يكون من الضروري
تخزين العديد من قيم النواة :math:`k(x_i, x_j)` أثناء التحسين.
إذا تم تطبيق مُصنِّف مُحسَّن باستخدام النواة على بيانات جديدة :math:`y_j`،
فيجب حساب :math:`k(x_i, y_j)` للتنبؤ،
وربما بالنسبة للعديد من :math:`x_i` المختلفة في مجموعة التدريب.

تسمح الفئات في هذا الوحدة الفرعية بحساب التضمين التقريبي
:math:`\phi`، وبالتالي العمل بشكل صريح مع التمثيلات
:math:`\phi(x_i)`، مما يلغي الحاجة إلى تطبيق النواة
أو تخزين أمثلة التدريب.


.. rubric:: المراجع

.. [WS2001] `"Using the Nyström method to speed up kernel machines"
  <https://papers.nips.cc/paper_files/paper/2000/hash/19de10adbaa1b2ee13f77f679fa1483a-Abstract.html>`_
  Williams, C.K.I.; Seeger, M. - 2001.
.. [RR2007] `"Random features for large-scale kernel machines"
  <https://papers.nips.cc/paper/2007/hash/013a006f03dbc5392effeb8f18fda755-Abstract.html>`_
  Rahimi, A. and Recht, B. - Advances in neural information processing 2007,
.. [LS2010] `"Random Fourier approximations for skewed multiplicative histogram kernels"
  <https://www.researchgate.net/publication/221114584_Random_Fourier_Approximations_for_Skewed_Multiplicative_Histogram_Kernels>`_
  Li, F., Ionescu, C., and Sminchisescu, C.
  - Pattern Recognition,  DAGM 2010, Lecture Notes in Computer Science.
.. [VZ2010] `"Efficient additive kernels via explicit feature maps"
  <https://www.robots.ox.ac.uk/~vgg/publications/2011/Vedaldi11/vedaldi11.pdf>`_
  Vedaldi, A. and Zisserman, A. - Computer Vision and Pattern Recognition 2010
.. [VVZ2010] `"Generalized RBF feature maps for Efficient Detection"
  <https://www.robots.ox.ac.uk/~vgg/publications/2010/Sreekanth10/sreekanth10.pdf>`_
  Vempati, S. and Vedaldi, A. and Zisserman, A. and Jawahar, CV - 2010
.. [PP2013] :doi:`"Fast and scalable polynomial kernels via explicit feature maps"
  <10.1145/2487575.2487591>`
  Pham, N., & Pagh, R. - 2013
.. [CCF2002] `"Finding frequent items in data streams"
  <https://www.cs.princeton.edu/courses/archive/spring04/cos598B/bib/CharikarCF.pdf>`_
  Charikar, M., Chen, K., & Farach-Colton - 2002
.. [WIKICS] `"Wikipedia: Count sketch"
  <https://en.wikipedia.org/wiki/Count_sketch>`_