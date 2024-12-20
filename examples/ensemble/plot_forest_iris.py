"""
====================================================================
رسم أسطح القرار لمجموعات الأشجار على مجموعة بيانات إيريس
====================================================================

ارسم أسطح القرار لغابات الأشجار العشوائية المدربة على أزواج
من سمات مجموعة بيانات إيريس.

يقارن هذا الرسم بين أسطح القرار التي تعلمها مصنف شجرة القرار
(العمود الأول)، ومصنف غابة عشوائية (العمود الثاني)، ومصنف الأشجار الإضافية
(العمود الثالث) ومصنف AdaBoost (العمود الرابع).

في الصف الأول، يتم بناء المصنفات باستخدام ميزات عرض الكأس
وميزات طول الكأس فقط، وفي الصف الثاني باستخدام طول الكأس فقط
وعرض الكأس، وفي الصف الثالث باستخدام طول الكأس وعرض الكأس فقط.

بترتيب تنازلي للجودة، عند التدريب (خارج هذا المثال) على جميع
4 ميزات باستخدام 30 مقدرًا وتسجيل النقاط باستخدام 10 طية للتحقق المتقاطع،
نحن نرى::

    ExtraTreesClassifier()  # 0.95 score
    RandomForestClassifier()  # 0.94 score
    AdaBoost(DecisionTree(max_depth=3))  # 0.94 score
    DecisionTree(max_depth=None)  # 0.94 score

زيادة `max_depth` ل AdaBoost يقلل الانحراف المعياري
من الدرجات (لكن متوسط الدرجات لا يتحسن).

راجع إخراج وحدة التحكم للحصول على مزيد من التفاصيل حول كل نموذج.

في هذا المثال، قد ترغب في:

1) تغيير "max_depth" لـ "DecisionTreeClassifier" و
   "AdaBoostClassifier"، ربما جرب "max_depth=3" لـ "DecisionTreeClassifier" أو
   "max_depth=None" لـ "AdaBoostClassifier"
2) تغيير "n_estimators"

من الجدير بالذكر أن RandomForests وExtraTrees يمكن أن تتلاءم بالتوازي
على العديد من النوى حيث يتم بناء كل شجرة بشكل مستقل عن الآخرين.
تُبنى عينات AdaBoost بشكل متسلسل ولا تستخدم نوى متعددة.
"""
# المؤلفون: مطوري scikit-learn
# معرف SPDX-License: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

from sklearn.datasets import load_iris
from sklearn.ensemble import (
    AdaBoostClassifier,
    ExtraTreesClassifier,
    RandomForestClassifier,
)
from sklearn.tree import DecisionTreeClassifier

# المعلمات
n_classes = 3
n_estimators = 30
cmap = plt.cm.RdYlBu
plot_step = 0.02  # عرض خطوة دقيقة لحواف أسطح القرار
plot_step_coarser = 0.5  # عرض الخطوات للتخمينات المصنفة الخشنة
RANDOM_SEED = 13  # إصلاح البذرة على كل تكرار

# تحميل البيانات
iris = load_iris()

plot_idx = 1

models = [
    DecisionTreeClassifier(max_depth=None),
    RandomForestClassifier(n_estimators=n_estimators),
    ExtraTreesClassifier(n_estimators=n_estimators),
    AdaBoostClassifier(DecisionTreeClassifier(
        max_depth=3), n_estimators=n_estimators),
]

for pair in ([0, 1], [0, 2], [2, 3]):
    for model in models:
        # نأخذ فقط الميزتين المقابلتين
        X = iris.data[:, pair]
        y = iris.target

        # خلط
        idx = np.arange(X.shape[0])
        np.random.seed(RANDOM_SEED)
        np.random.shuffle(idx)
        X = X[idx]
        y = y[idx]

        # توحيد
mean = X.mean(axis=0)
std = X.std(axis=0)
X = (X - mean) / std

# تدريب
model.fit(X, y)

scores = model.score(X, y)
# إنشاء عنوان لكل عمود والوحدة الطرفية باستخدام str() و
# تقطيع الأجزاء عديمة الفائدة من السلسلة
model_title = str(type(model)).split(".")[-1][:-2][: -len("Classifier")]

model_details = model_title
if hasattr(model, "estimators_"):
    model_details += " with {} estimators".format(len(model.estimators_))
print(model_details + " with features", pair, "has a score of", scores)

plt.subplot(3, 4, plot_idx)
if plot_idx <= len(models):
    # إضافة عنوان في أعلى كل عمود
    plt.title(model_title, fontsize=9)
plt.subplot(3, 4, plot_idx)
if plot_idx <= len(models):
    # إضافة عنوان في أعلى كل عمود
    plt.title(model_title, fontsize=9)

# الآن ارسم حدود القرار باستخدام شبكة دقيقة كإدخال ل
# رسم تخطيطي مملوء بالملامح
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(
    np.arange(x_min, x_max, plot_step), np.arange(y_min, y_max, plot_step)
)

# ارسم إما شجرة قرار واحدة أو مزج ألفا لأسطح القرار
# لمجموعة المصنفات
if isinstance(model, DecisionTreeClassifier):
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    cs = plt.contourf(xx, yy, Z, cmap=cmap)
else:
    # اختر مستوى مزج ألفا فيما يتعلق بعدد
    # من المقدرين
    # التي تستخدم (مع ملاحظة أن AdaBoost يمكن أن يستخدم عددًا أقل من المقدرين
    # من الحد الأقصى إذا حقق ملاءمة جيدة بما فيه الكفاية في وقت مبكر)
    estimator_alpha = 1.0 / len(model.estimators_)
    for tree in model.estimators_:
        Z = tree.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        cs = plt.contourf(xx, yy, Z, alpha=estimator_alpha, cmap=cmap)

# بناء شبكة أكثر خشونة لرسم مجموعة من التصنيفات
# لإظهار كيف أنها مختلفة عما نراه في أسطح القرار.
# هذه النقاط متباعدة بانتظام ولا تحتوي على
# حدود سوداء
xx_coarser, yy_coarser = np.meshgrid(
    np.arange(x_min, x_max, plot_step_coarser),
    np.arange(y_min, y_max, plot_step_coarser),
)
Z_points_coarser = model.predict(
    np.c_[xx_coarser.ravel(), yy_coarser.ravel()]
).reshape(xx_coarser.shape)
cs_points = plt.scatter(
    xx_coarser,
    yy_coarser,
    s=15,
    c=Z_points_coarser,
    cmap=cmap,
    edgecolors="none",
)

# ارسم نقاط التدريب، هذه متجمعة معًا ولها
# حدود سوداء
plt.scatter(
    X[:, 0],
    X[:, 1],
    c=y,
    cmap=ListedColormap(["r", "y", "b"]),
    edgecolor="k",
    s=20,
)
plot_idx += 1  # الانتقال إلى الرسم البياني التالي في التسلسل

plt.suptitle("Classifiers on feature subsets of the Iris dataset", fontsize=12)
plt.axis("tight")
plt.tight_layout(h_pad=0.2, w_pad=0.2, pad=2.5)
plt.show()
