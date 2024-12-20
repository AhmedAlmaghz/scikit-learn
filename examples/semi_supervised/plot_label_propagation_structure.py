"""
==============================================
تعلم انتشار العلامات لهيكل معقد
==============================================

مثال على تعلم انتشار العلامات لهيكل داخلي معقد
لتوضيح "تعلم المنحنى". يجب أن تكون الدائرة الخارجية
مُعَلَّمة باللون "الأحمر" والدائرة الداخلية "باللون الأزرق". لأن كل مجموعة من العلامات
تقع داخل شكلها المميز، يمكننا أن نرى أن العلامات
تنتشر بشكل صحيح حول الدائرة.

"""

# المؤلفون: مطوري سكايلرن
# معرف الترخيص: BSD-3-Clause

# %%
# نقوم بتوليد مجموعة بيانات بدائرتين متحدتي المركز. بالإضافة إلى ذلك، يتم ربط علامة
# بكل عينة من مجموعة البيانات وهي: 0 (تابعة
# للدائرة الخارجية)، 1 (تابعة للدائرة الداخلية)، و -1 (غير معروفة).
# هنا، جميع العلامات ما عدا اثنتين تم وسمها على أنها غير معروفة.

import numpy as np

from sklearn.datasets import make_circles

n_samples = 200
X, y = make_circles(n_samples=n_samples, shuffle=False)
outer, inner = 0, 1
labels = np.full(n_samples, -1.0)
labels[0] = outer
labels[-1] = inner

# %%
# رسم البيانات الخام
import matplotlib.pyplot as plt

plt.figure(figsize=(4, 4))
plt.scatter(
    X[labels == outer, 0],
    X[labels == outer, 1],
    color="navy",
    marker="s",
    lw=0,
    label="outer labeled",
    s=10,
)
plt.scatter(
    X[labels == inner, 0],
    X[labels == inner, 1],
    color="c",
    marker="s",
    lw=0,
    label="inner labeled",
    s=10,
)
plt.scatter(
    X[labels == -1, 0],
    X[labels == -1, 1],
    color="darkorange",
    marker=".",
    label="unlabeled",
)
plt.legend(scatterpoints=1, shadow=False, loc="center")
_ = plt.title("Raw data (2 classes=outer and inner)")

# %%
#
# الهدف من :class:`~sklearn.semi_supervised.LabelSpreading` هو ربط
# علامة بعينة حيث تكون العلامة غير معروفة في البداية.
from sklearn.semi_supervised import LabelSpreading

label_spread = LabelSpreading(kernel="knn", alpha=0.8)
label_spread.fit(X, labels)

# %%
# الآن، يمكننا التحقق من العلامات التي تم ربطها بكل عينة
# عندما كانت العلامة غير معروفة.
output_labels = label_spread.transduction_
output_label_array = np.asarray(output_labels)
outer_numbers = np.where(output_label_array == outer)[0]
inner_numbers = np.where(output_label_array == inner)[0]

plt.figure(figsize=(4, 4))
plt.scatter(
    X[outer_numbers, 0],
    X[outer_numbers, 1],
    color="navy",
    marker="s",
    lw=0,
    s=10,
    label="outer learned",
)
plt.scatter(
    X[inner_numbers, 0],
    X[inner_numbers, 1],
    color="c",
    marker="s",
    lw=0,
    s=10,
    label="inner learned",
)
plt.legend(scatterpoints=1, shadow=False, loc="center")
plt.title("Labels learned with Label Spreading (KNN)")
plt.show()