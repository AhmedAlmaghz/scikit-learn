"""
# تحليل المكونات الأساسية التزايدي

يستخدم تحليل المكونات الأساسية التزايدي (IPCA) عادة كبديل لتحليل المكونات الأساسية (PCA) عندما تكون مجموعة البيانات المراد تحليلها كبيرة جدًا بحيث لا يمكن تحميلها في الذاكرة. يقوم IPCA ببناء تقريب منخفض الرتبة لبيانات الإدخال باستخدام كمية من الذاكرة لا تعتمد على عدد عينات بيانات الإدخال. لا يزال يعتمد على ميزات بيانات الإدخال، ولكن تغيير حجم الدفعة يسمح بالتحكم في استخدام الذاكرة.

يعمل هذا المثال كفحص مرئي للتأكد من أن IPCA قادر على إيجاد إسقاط مشابه للبيانات مثل PCA (إلى انقلاب الإشارة)، بينما يقوم بمعالجة بضع عينات فقط في كل مرة. يمكن اعتبار هذا المثال "مثالًا توضيحيًا"، حيث أن IPCA مخصص لمجموعات البيانات الكبيرة التي لا يمكن تحميلها في الذاكرة الرئيسية، مما يتطلب نهجًا تزايديًا.
"""
# المؤلفون: مطوري scikit-learn
# معرف الترخيص: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA, IncrementalPCA

iris = load_iris()
X = iris.data
y = iris.target

n_components = 2
ipca = IncrementalPCA(n_components=n_components, batch_size=10)
X_ipca = ipca.fit_transform(X)

pca = PCA(n_components=n_components)
X_pca = pca.fit_transform(X)

colors = ["navy", "turquoise", "darkorange"]

for X_transformed, title in [(X_ipca, "Incremental PCA"), (X_pca, "PCA")]:
    plt.figure(figsize=(8, 8))
    for color, i, target_name in zip(colors, [0, 1, 2], iris.target_names):
        plt.scatter(
            X_transformed[y == i, 0],
            X_transformed[y == i, 1],
            color=color,
            lw=2,
            label=target_name,
        )

    if "Incremental" in title:
        err = np.abs(np.abs(X_pca) - np.abs(X_ipca)).mean()
        plt.title(
            title + " of iris dataset\nMean absolute unsigned error %.6f" % err)
    else:
        plt.title(title + " of iris dataset")
    plt.legend(loc="best", shadow=False, scatterpoints=1)
    plt.axis([-4, 4, -1.5, 1.5])

plt.show()
