.. _cross_decomposition:

===================
التحليل التفكيكي المتقاطع
===================

.. currentmodule:: sklearn.cross_decomposition

يحتوي نموذج التحليل التفكيكي المتقاطع على خوارزميات إشرافية لخفض الأبعاد والتنبؤ، والتي تنتمي إلى عائلة "المربعات الصغرى الجزئية".

.. figure:: ../auto_examples/cross_decomposition/images/sphx_glr_plot_compare_cross_decomposition_001.png
   :target: ../auto_examples/cross_decomposition/plot_compare_cross_decomposition.html
   :scale: 75%
   :align: center

تجد خوارزميات التحليل التفكيكي المتقاطع العلاقات الأساسية بين مصفوفتين (X و Y). وهي عبارة عن نهج متغيرات خفية لنمذجة هياكل الارتباط في هذين الفراغين. ستحاول هذه الخوارزميات إيجاد الاتجاه متعدد الأبعاد في فراغ X الذي يفسر اتجاه التباين متعدد الأبعاد الأقصى في فراغ Y. وبعبارة أخرى، يقوم نموذج PLS بمشروع كل من X و Y إلى فراغ فرعي أقل أبعادًا بحيث يكون الارتباط بين X المحوّل وY المحوّل هو الأقصى.

ويُشبه نموذج PLS "انحدار المكون الرئيسي" (PCR)، حيث يتم أولاً تحويل العينات إلى فراغ فرعي أقل أبعادًا، ويتم التنبؤ بالأهداف y باستخدام X المحوّل. إحدى المشكلات مع PCR هي أن تقليل الأبعاد غير مُشرف، وقد يفقد بعض المتغيرات المهمة: سيحتفظ PCR بالميزات ذات التباين الأكبر، ولكن من الممكن أن تكون الميزات ذات التباينات الصغيرة ذات صلة بالتنبؤ بالهدف. وبطريقة ما، يسمح PLS بنفس نوع تقليل الأبعاد، ولكن عن طريق أخذ الأهداف y في الاعتبار. ويتم توضيح هذه الحقيقة في المثال التالي:
* :ref:`sphx_glr_auto_examples_cross_decomposition_plot_pcr_vs_pls.py`.

وباستثناء CCA، فإن خوارزميات PLS مناسبة بشكل خاص عندما تحتوي مصفوفة المتنبئات على عدد أكبر من المتغيرات من الملاحظات، وعندما يكون هناك ارتباط متعدد بين الميزات. وعلى النقيض من ذلك، فإن الانحدار الخطي القياسي سيفشل في هذه الحالات ما لم يتم تنظيمه.

تشمل الفئات المُدرجة في هذا النموذج PLSRegression وPLSCanonical وCCA وPLSSVD

PLSCanonical
------------

نصف هنا الخوارزمية المستخدمة في: class: PLSCanonical. تستخدم الخوارزميات الأخرى المتغيرات من هذه الخوارزمية، ويتم تفصيلها أدناه.
نوصي القسم [1]_ لمزيد من التفاصيل والمقارنات بين هذه الخوارزميات. في [1]_، يتوافق: class: PLSCanonical مع "PLSW2A".

بالنسبة لمصفوفتين ممركزتين: math: `X \ in \ mathbb {R} ^ {n \ times d}` و math: `Y \ in \ mathbb {R} ^ {n \ times t}`، وعدد من المكونات: math: `K`، فإن: class: PLSCanonical تعمل كما يلي:

اضبط: math: `X_1` إلى: math: `X` و: math: `Y_1` إلى: math: `Y`. بعد ذلك، لكل: math: `k \ in [1، K]`:

- أ) احسب: math: `u_k \ in \ mathbb {R} ^ d` و: math: `v_k \ in \ mathbb {R} ^ t`، المتجهات اليسرى واليمنى الأولى للمصفوفة المتقاطعة للتباين المشترك: math: `C = X_k ^ T Y_k`.
  تسمى: math: `u_k` و: math: `v_k` بـ "الأوزان".
  بحكم التعريف، يتم اختيار: math: `u_k` و: math: `v_k`
  بحيث تُضاعف الارتباط بين: math: `X_k` المحوّل والهدف المحوّل، أي: math: `\ text {Cov} (X_k u_k، Y_k v_k)`.
- ب) قم بتحويل: math: `X_k` و: math: `Y_k` على المتجهات الفردية للحصول على
  "النتائج": math: `\ xi_k = X_k u_k` و: math: `\ omega_k = Y_k v_k`
- ج) قم بالانحدار: math: `X_k` على: math: `\ xi_k`، أي ابحث عن متجه: math: `\ gamma_k
  \ in \ mathbb {R} ^ d` بحيث تكون المصفوفة ذات الرتبة 1: math: `\ xi_k \ gamma_k ^ T`
  قريبة قدر الإمكان من: math: `X_k`. قم بالشيء نفسه في: math: `Y_k` مع
  : math: `\ omega_k` للحصول على: math: `\ delta_k`. تسمى المتجهات
  : math: `\ gamma_k` و: math: `\ delta_k` بـ "التحميلات".
- د) "إزالة تضخيم": math: `X_k` و: math: `Y_k`، أي اطرح التقريبات ذات الرتبة 1: math: `X_ {k + 1} = X_k - \ xi_k \ gamma_k ^ T`، و
  : math: `Y_ {k + 1} = Y_k - \ omega_k \ delta_k ^ T`.

في النهاية، نقوم بتقريب: math: `X` كمبلغ من المصفوفات ذات الرتبة 1:
: math: `X = \ Xi \ Gamma ^ T` حيث: math: `\ Xi \ in \ mathbb {R} ^ {n \ times K}`
يحتوي على النتائج في أعمدته، و: math: `\ Gamma ^ T \ in \ mathbb {R} ^ {K
\ times d}` يحتوي على التحميلات في صفوفه. وبالمثل لـ: math: `Y`، لدينا: math: `Y = \ Omega \ Delta ^ T`.

لاحظ أن مصفوفات النتائج: math: `\ Xi` و: math: `\ Omega` تتوافق مع
مشاريع بيانات التدريب: math: `X` و: math: `Y`، على التوالي.

يمكن تنفيذ الخطوة أ) بطريقتين: إما عن طريق حساب SVD الكامل للمصفوفة: math: `C` والاحتفاظ فقط بالمتجهات الفردية ذات أكبر القيم الفردية، أو عن طريق حساب المتجهات الفردية مباشرةً باستخدام طريقة القوة (راجع القسم 11.3 في [1]_)،
والذي يتوافق مع خيار "nipals" لخوارزمية المعلمة.

.. dropdown:: تحويل البيانات

  لتحويل: math: `X` إلى: math: `\ bar {X}`، نحتاج إلى إيجاد مصفوفة تحويل: math: `P` بحيث: math: `\ bar {X} = XP`. نحن نعلم أنه بالنسبة لبيانات التدريب،: math: `\ Xi = XP`، و: math: `X = \ Xi \ Gamma ^ T`. عن طريق الضبط
  : math: `P = U (\ Gamma ^ T U) ^ {- 1}` حيث: math: `U` هي المصفوفة مع
  : math: `u_k` في الأعمدة، لدينا: math: `XP = X U (\ Gamma ^ T U) ^ {- 1} = \ Xi
  (\ Gamma ^ T U) (\ Gamma ^ T U) ^ {- 1} = \ Xi` كما هو مطلوب. يمكن الوصول إلى مصفوفة الدوران
  : math: `P` من السمة x_rotations_.

  وبالمثل، يمكن تحويل: math: `Y` باستخدام مصفوفة الدوران
  : math: `V (\ Delta ^ T V) ^ {- 1}`، والتي يمكن الوصول إليها عبر السمة y_rotations_.

.. dropdown:: التنبؤ بالأهداف `Y`

  للتنبؤ بالأهداف لبعض البيانات: math: `X`، نبحث عن مصفوفة معاملات: math: `\ beta \ in R ^ {d \ times t}` بحيث: math: `Y =
  X \ beta`.

  الفكرة هي محاولة التنبؤ بالأهداف المحوّلة: math: `\ Omega` كدالة للعينات المحوّلة: math: `\ Xi`، عن طريق حساب: math: `\ alpha
  \ in \ mathbb {R}` بحيث: math: `\ Omega = \ alpha \ Xi`.

  بعد ذلك، لدينا: math: `Y = \ Omega \ Delta ^ T = \ alpha \ Xi \ Delta ^ T`، ولأن
  : math: `\ Xi` هي بيانات التدريب المحولة، لدينا: math: `Y = X \ alpha
  P \ Delta ^ T`، ونتيجة لذلك، تكون مصفوفة المعاملات: math: `\ beta = \ alpha P
  \ Delta ^ T`.

  يمكن الوصول إلى: math: `\ beta` من خلال السمة coef_.

PLSSVD
------

: class: PLSSVD هو إصدار مبسط من: class: PLSCanonical
تم وصفه سابقًا: بدلاً من إزالة تضخيم المصفوفات بشكل تكراري: math: `X_k`
و: math: `Y_k`، يحسب: class: PLSSVD SVD للمصفوفة: math: `C = X ^ TY`
*مرة واحدة*، ويخزن المتجهات الفردية: math: `n_components` المقابلة لأكبر القيم الفردية في المصفوفات: math: `U` و: math: `V`، والتي تتوافق مع
المعلمات: math: `x_weights_` و: math: `y_weights_`. هنا، تكون البيانات المحولة ببساطة: math: `transformed (X) = XU` و: math: `transformed (Y) = YV`.

إذا كان: math: `n_components == 1`، فإن: class: PLSSVD و: class: PLSCanonical متكافئان تمامًا.

PLSRegression
-------------

خوارزمية التنبؤ: class: PLSRegression مماثلة لـ
: class: PLSCanonical مع `algorithm='nipals'`، مع اختلافين مهمين:

- في الخطوة أ) في طريقة القوة لحساب: math: `u_k` و: math: `v_k`،
  : math: `v_k` غير معياري أبدًا.
- في الخطوة ج)، يتم تقريب الأهداف: math: `Y_k` باستخدام تحويل
  : math: `X_k` (أي: math: `\ xi_k`) بدلاً من تحويل
  : math :`Y_k` (أي: math: `\ omega_k`). وبعبارة أخرى، تختلف عملية حساب التحميلات. ونتيجة لذلك، ستتأثر عملية إزالة التضخيم في الخطوة د) أيضًا.

يؤثر هذان التعديلان على إخراج الدالتين predict وtransform،
والتي ليست هي نفسها كما في: class: PLSCanonical. أيضًا، في حين أن عدد المكونات محدود بـ: math: `min (n_samples، n_features، n_targets)` في
: class: PLSCanonical، فإن الحد هنا هو رتبة: math: `X ^ TX`، أي
: math: `min (n_samples، n_features)`.

يُعرف: class: PLSRegression أيضًا باسم PLS1 (أهداف فردية) وPLS2
(أهداف متعددة). تمامًا مثل: class: sklearn.linear_model.Lasso،
: class: PLSRegression هو شكل من أشكال الانحدار الخطي المنتظم حيث يتحكم عدد المكونات في قوة الانتظام.

تحليل الارتباط الكنسي
------------------------------

تم تطوير تحليل الارتباط الكنسي قبل PLS وبشكل مستقل عنه.
ولكن اتضح أن: class: CCA هي حالة خاصة من PLS، وتتوافق مع PLS في "الوضع B" في الأدبيات.

يختلف: class: CCA عن: class: PLSCanonical في طريقة حساب الأوزان
: math: `u_k` و: math: `v_k` في طريقة القوة للخطوة أ).
يمكن العثور على التفاصيل في القسم 10 من [1]_.

نظرًا لأن: class: CCA ينطوي على عكس: math: `X_k ^ TX_k` و
: math: `Y_k ^ TY_k`، فقد يكون هذا الخوارزم غير مستقر إذا كان عدد الميزات أو الأهداف أكبر من عدد العينات.

.. rubric:: المراجع

.. [1] `استطلاع لأساليب المربعات الصغرى الجزئية (PLS)، مع التركيز على حالة الكتلتين <https://stat.uw.edu/sites/default/files/files/reports/2000/tr371.pdf>`_،
  JA Wegelin

.. rubric:: أمثلة

* : ref: `sphx_glr_auto_examples_cross_decomposition_plot_compare_cross_decomposition.py`
* : ref: `sphx_glr_auto_examples_cross_decomposition_plot_pcr_vs_pls.py`