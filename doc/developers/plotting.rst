يُعرِّف سكايت-ليرن واجهة برمجة تطبيقات (API) بسيطة لإنشاء الرسوم البيانية لتعلم الآلة. وتتمثل الميزات الرئيسية لهذه الواجهة في إجراء الحسابات مرة واحدة والمرونة في تعديل الرسوم البيانية بعد ذلك. هذا القسم مخصص للمطورين الذين يرغبون في تطوير أو صيانة أدوات إنشاء الرسوم البيانية. وللاستخدام، يجب أن يرجع المستخدمون إلى دليل المستخدم.

نظرة عامة على واجهة برمجة التطبيقات للرسم البياني
-------------------------------------------------

يتم تضمين هذا المنطق في كائن عرض حيث يتم تخزين البيانات المحسوبة ويتم إجراء الرسم البياني في طريقة "رسم". تحتوي طريقة "__init__" الخاصة بكائن العرض فقط على البيانات اللازمة لإنشاء الرسم البياني. وتأخذ طريقة "رسم" كمعلمات تلك التي لها علاقة فقط بالرسم البياني، مثل محاور matplotlib. ستقوم طريقة "رسم" بتخزين كائنات matplotlib الفنية كسمات، مما يسمح بتعديلات الأسلوب من خلال كائن العرض. يجب أن تحدد فئة "العرض" طريقة أو كلا الطريقتين: "من_المُقدِّر" و "من_التنبؤات". تسمح هذه الطرق بإنشاء كائن "العرض" من المُقدِّر وبعض البيانات أو من القيم الحقيقية والمتنبأ بها. بعد أن تقوم هذه الطرق بإنشاء كائن العرض بالقيم المحسوبة، يتم استدعاء طريقة عرض "رسم". لاحظ أن طريقة "رسم" تحدد سمات تتعلق بـ matplotlib، مثل كائن الخط. يسمح هذا بالتخصيصات بعد استدعاء طريقة "رسم".

على سبيل المثال، يحدد "RocCurveDisplay" الطرق والسمات التالية::

   class RocCurveDisplay:
       def __init__(self, fpr, tpr, roc_auc, estimator_name):
           ...
           self.fpr = fpr
           self.tpr = tpr
           self.roc_auc = roc_auc
           self.estimator_name = estimator_name

       @classmethod
       def from_estimator(cls, estimator, X, y):
           # الحصول على التنبؤات
           y_pred = estimator.predict_proba(X)[:, 1]
           return cls.from_predictions(y, y_pred, estimator.__class__.__name__)

       @classmethod
       def from_predictions(cls, y, y_pred, estimator_name):
           # إجراء حساب ROC من y و y_pred
           fpr, tpr, roc_auc = ...
           viz = RocCurveDisplay(fpr, tpr, roc_auc, estimator_name)
           return viz.plot()

       def plot(self, ax=None, name=None, **kwargs):
           ...
           self.line_ = ...
           self.ax_ = ax
           self.figure_ = ax.figure_

اقرأ المزيد في :ref:sphx_glr_auto_examples_miscellaneous_plot_roc_curve_visualization_api.py` ودليل المستخدم <visualizations>.

الرسم البياني باستخدام محاور متعددة
----------------------------------

تدعم بعض أدوات إنشاء الرسوم البيانية، مثل :func:`~sklearn.inspection.PartialDependenceDisplay.from_estimator` و :class:`~sklearn.inspection.PartialDependenceDisplay`، الرسم البياني على محاور متعددة. يتم دعم سيناريوهين مختلفين:

1. إذا تم تمرير قائمة من المحاور، فسيتحقق "رسم" مما إذا كان عدد المحاور متوافقًا مع عدد المحاور التي يتوقعها، ثم يقوم بالرسم على تلك المحاور.
2. إذا تم تمرير محور واحد، فإن هذا المحور يحدد مساحة لمحاور متعددة ليتم وضعها. في هذه الحالة، نقترح استخدام matplotlib's'~matplotlib.gridspec.GridSpecFromSubplotSpec` لتقسيم المساحة::

   import matplotlib.pyplot as plt
   from matplotlib.gridspec import GridSpecFromSubplotSpec

   fig, ax = plt.subplots()
   gs = GridSpecFromSubplotSpec(2, 2, subplot_spec=ax.get_subplotspec())

   ax_top_left = fig.add_subplot(gs[0, 0])
   ax_top_right = fig.add_subplot(gs[0, 1])
   ax_bottom = fig.add_subplot(gs[1, :])

بشكل افتراضي، تكون كلمة "ax" الأساسية في طريقة "رسم" هي "لا شيء". في هذه الحالة، يتم إنشاء محور واحد ويتم استخدام واجهة برمجة تطبيقات "gridspec" لإنشاء مناطق للرسم فيها.

على سبيل المثال، قم بزيارة :meth:`~sklearn.inspection.PartialDependenceDisplay.from_estimator` الذي يقوم برسم خطوط وخطوط محيط متعددة باستخدام واجهة برمجة التطبيقات هذه. يتم حفظ المحور الذي يحدد حدود الصندوق في سمة "bounding_ax_". يتم تخزين المحاور الفردية التي تم إنشاؤها في مصفوفة "axes_"، والتي تتوافق مع موضع المحور على الشبكة. يتم تعيين المواضع التي لا يتم استخدامها إلى "لا شيء". علاوة على ذلك، يتم تخزين كائنات matplotlib الفنية في "lines_" و "contours_" حيث يكون المفتاح هو الموضع على الشبكة. عندما يتم تمرير قائمة من المحاور، تكون "axes_" و "lines_" و "contours_" عبارة عن مصفوفة أحادية الأبعاد تتوافق مع قائمة المحاور التي تم تمريرها.