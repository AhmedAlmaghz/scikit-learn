"""
================================================
تقدير كثافة النواة لتوزيع الأنواع
================================================
هذا يوضح مثالًا على استعلام يعتمد على الجيران (على وجه التحديد تقدير كثافة النواة) على بيانات جغرافية مكانية، باستخدام شجرة الكرة المبنية على مقياس مسافة هافرساين - أي المسافات عبر النقاط في خطوط العرض/الطول.
توفر مجموعة البيانات من قبل فيليبس وآخرون. (2006).
إذا كان متاحًا، يستخدم المثال
`basemap <https://matplotlib.org/basemap/>`_
لرسم خطوط السواحل والحدود الوطنية لأمريكا الجنوبية.

هذا المثال لا يؤدي أي تعلم على البيانات (انظر
:ref:`sphx_glr_auto_examples_applications_plot_species_distribution_modeling.py` لمثال
على التصنيف القائم على السمات في مجموعة البيانات هذه). إنه يُظهر ببساطة تقدير كثافة النواة لنقاط البيانات الملاحظة في الإحداثيات الجغرافية المكانية.

الأنواعان هما:

- `"Bradypus variegatus"
  <https://www.iucnredlist.org/species/3038/47437046>`_ ،
  الكسلان البني الحنجرة.

- `"Microryzomys minutus"
  <http://www.iucnredlist.org/details/13408/0>`_ ،
  المعروف أيضًا باسم فأر الأرز الصغير الغابات، وهو قارض يعيش في بيرو
  كولومبيا، الإكوادور، بيرو، وفنزويلا.

المراجع
----------

- `"نمذجة الحد الأقصى من الإنتروبيا لتوزيعات الأنواع الجغرافية"
  <http://rob.schapire.net/papers/ecolmod.pdf>`_
  س. ج. فيليبس، ر. ب. أندرسون، ر. إي. شابير - النمذجة الإيكولوجية،
  190:231-259، 2006.
"""  # noqa: E501

# المؤلفون: مطوري سكايلرن
# معرف SPDX-License: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import fetch_species_distributions
from sklearn.neighbors import KernelDensity

# إذا كان basemap متاحًا، فسنستخدمه.
# وإلا، سنقوم بالارتجال لاحقًا...
try:
    from mpl_toolkits.basemap import Basemap

    basemap = True
except:
    basemap = False


def construct_grids(batch):
    """بناء شبكة الخريطة من كائن الدفعة

    المعلمات
    ----------
    الدفعة : كائن الدفعة
        الكائن الذي تم إرجاعه بواسطة :func:`fetch_species_distributions`

    الإرجاع
    -------
    (xgrid, ygrid) : صفائف 1-D
        الشبكة المقابلة للقيم في batch.coverages
    """
    # إحداثيات x,y لخلايا الزاوية
    xmin = batch.x_left_lower_corner + batch.grid_size
    xmax = xmin + (batch.Nx * batch.grid_size)
    ymin = batch.y_left_lower_corner + batch.grid_size
    ymax = ymin + (batch.Ny * batch.grid_size)

    # إحداثيات x لخلايا الشبكة
    xgrid = np.arange(xmin, xmax, batch.grid_size)
    # إحداثيات y لخلايا الشبكة
    ygrid = np.arange(ymin, ymax, batch.grid_size)

    return (xgrid, ygrid)


# الحصول على مصفوفات/صفائف معرفات الأنواع والمواقع
data = fetch_species_distributions()
species_names = ["Bradypus Variegatus", "Microryzomys Minutus"]

Xtrain = np.vstack([data["train"]["dd lat"], data["train"]["dd long"]]).T
ytrain = np.array(
    [d.decode("ascii").startswith("micro") for d in data["train"]["species"]],
    dtype="int",
)
Xtrain *= np.pi / 180.0  # تحويل lat/long إلى راديان

# إعداد شبكة البيانات لرسم المخطط
xgrid, ygrid = construct_grids(data)
X, Y = np.meshgrid(xgrid[::5], ygrid[::5][::-1])
land_reference = data.coverages[6][::5, ::5]
land_mask = (land_reference > -9999).ravel()

xy = np.vstack([Y.ravel(), X.ravel()]).T
xy = xy[land_mask]
xy *= np.pi / 180.0

# رسم خريطة لأمريكا الجنوبية مع توزيعات كل نوع
الشكل = plt.figure()
الشكل.subplots_adjust(left=0.05, right=0.95, wspace=0.05)

for i in range(2):
    plt.subplot(1, 2, i + 1)

    # إنشاء تقدير كثافة النواة للتوزيع
    print(" - حساب KDE في الإحداثيات الكروية")
    kde = KernelDensity(
        bandwidth=0.04, metric="haversine", kernel="gaussian", algorithm="ball_tree"
    )
    kde.fit(Xtrain[ytrain == i])

    # تقييم فقط على الأرض: -9999 يشير إلى المحيط
    Z = np.full(land_mask.shape[0], -9999, dtype="int")
    Z[land_mask] = np.exp(kde.score_samples(xy))
    Z = Z.reshape(X.shape)

    # رسم المخططات الكنتورية للكثافة
    levels = np.linspace(0, Z.max(), 25)
    plt.contourf(X, Y, Z, levels=levels, cmap=plt.cm.Reds)

    if basemap:
        print(" - رسم خطوط السواحل باستخدام basemap")
        m = Basemap(
            projection="cyl",
            llcrnrlat=Y.min(),
            urcrnrlat=Y.max(),
            llcrnrlon=X.min(),
            urcrnrlon=X.max(),
            resolution="c",
        )
        m.drawcoastlines()
        m.drawcountries()
    else:
        print(" - رسم خطوط السواحل من التغطية")
        plt.contour(
            X, Y, land_reference, levels=[-9998], colors="k", linestyles="solid"
        )
        plt.xticks([])
        plt.yticks([])

    plt.title(species_names[i])

plt.show()