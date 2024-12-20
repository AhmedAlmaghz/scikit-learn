"""
هذا مثال يوضح إعادة بناء صورة من مجموعة من الإسقاطات المتوازية، والتي تم الحصول عليها على طول زوايا مختلفة. يتم الحصول على مثل هذه البيانات في **التصوير المقطعي المحوسب** (CT).

بدون أي معلومات مسبقة عن العينة، فإن عدد الإسقاطات المطلوبة لإعادة بناء الصورة هو من نفس ترتيب الحجم الخطي ``l`` للصورة (بالبكسل). من أجل البساطة، نحن نعتبر هنا صورة نادرة، حيث تحتوي البكسلات على حدود الأجسام فقط على قيمة غير صفرية. يمكن أن تتوافق مثل هذه البيانات، على سبيل المثال، مع مادة خلوية.

ومع ذلك، تجدر الإشارة إلى أن معظم الصور نادرة في أساس مختلف، مثل موجات هارا. يتم الحصول على ``l/7`` إسقاطات فقط، لذلك من الضروري استخدام المعلومات المسبقة المتاحة عن العينة (نُدرتها): هذا مثال على **الاستشعار الضاغط**.

عملية إسقاط التصوير المقطعي هي تحويل خطي. بالإضافة إلى مصطلح مطابقة البيانات المقابل للانحدار الخطي، فإننا نعاقب معيار L1 للصورة لمراعاة ندرتها. تسمى مشكلة التحسين الناتجة بـ :ref:`lasso`. نستخدم الفئة :class:`~sklearn.linear_model.Lasso`، التي تستخدم خوارزمية النزول المنسق. من المهم أن نلاحظ أن هذا التنفيذ أكثر كفاءة من الناحية الحسابية على مصفوفة نادرة، من مشغل الإسقاط المستخدم هنا.

تعطي إعادة البناء مع عقوبة L1 نتيجة بدون خطأ (تمت تسمية جميع البكسلات بنجاح بـ 0 أو 1)، حتى إذا تمت إضافة ضوضاء إلى الإسقاطات. على سبيل المقارنة، تنتج عقوبة L2 (:class:`~sklearn.linear_model.Ridge`) عددًا كبيرًا من أخطاء التسمية للبكسلات. يتم ملاحظة الآثار المهمة على الصورة المعاد بناؤها، على عكس عقوبة L1. لاحظ بشكل خاص الأثر الدائري الذي يفصل البكسلات في الزوايا، والتي ساهمت في عدد أقل من الإسقاطات من القرص المركزي.
"""
# المؤلفون: مطوري سكايلرين
# معرف SPDX-License: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage, sparse

from sklearn.linear_model import Lasso, Ridge

def _weights(x, dx=1, orig=0):
    x = np.ravel(x)
    floor_x = np.floor((x - orig) / dx).astype(np.int64)
    alpha = (x - orig - floor_x * dx) / dx
    return np.hstack((floor_x, floor_x + 1)), np.hstack((1 - alpha, alpha))

def _generate_center_coordinates(l_x):
    X, Y = np.mgrid[:l_x, :l_x].astype(np.float64)
    center = l_x / 2.0
    X += 0.5 - center
    Y += 0.5 - center
    return X, Y

def build_projection_operator(l_x, n_dir):
    """حساب مصفوفة تصميم التصوير المقطعي.

    المعلمات
    ----------

    l_x : int
        الحجم الخطي لمصفوفة الصورة

    n_dir : int
        عدد الزوايا التي يتم عندها الحصول على الإسقاطات.

    العوائد
    -------
    p : مصفوفة نادرة الشكل (n_dir l_x, l_x**2)
    """
    X, Y = _generate_center_coordinates(l_x)
    angles = np.linspace(0, np.pi, n_dir, endpoint=False)
    data_inds, weights, camera_inds = [], [], []
    data_unravel_indices = np.arange(l_x**2)
    data_unravel_indices = np.hstack((data_unravel_indices, data_unravel_indices))
    for i, angle in enumerate(angles):
        Xrot = np.cos(angle) * X - np.sin(angle) * Y
        inds, w = _weights(Xrot, dx=1, orig=X.min())
        mask = np.logical_and(inds >= 0, inds < l_x)
        weights += list(w[mask])
        camera_inds += list(inds[mask] + i * l_x)
        data_inds += list(data_unravel_indices[mask])
    proj_operator = sparse.coo_matrix((weights, (camera_inds, data_inds)))
    return proj_operator
def generate_synthetic_data():
    """البيانات الثنائية الاصطناعية"""
    rs = np.random.RandomState(0)
    n_pts = 36
    x, y = np.ogrid[0:l, 0:l]
    mask_outer = (x - l / 2.0) ** 2 + (y - l / 2.0) ** 2 < (l / 2.0) ** 2
    mask = np.zeros((l, l))
    points = l * rs.rand(2, n_pts)
    mask[(points[0]).astype(int), (points[1]).astype(int)] = 1
    mask = ndimage.gaussian_filter(mask, sigma=l / n_pts)
    res = np.logical_and(mask > mask.mean(), mask_outer)
    return np.logical_xor(res, ndimage.binary_erosion(res))

# توليد صور اصطناعية وإسقاطات
l = 128
proj_operator = build_projection_operator(l, l // 7)
data = generate_synthetic_data()
proj = proj_operator @ data.ravel()[:, np.newaxis]
proj += 0.15 * np.random.randn(*proj.shape)

# إعادة البناء مع عقوبة L2 (Ridge)
rgr_ridge = Ridge(alpha=0.2)
rgr_ridge.fit(proj_operator, proj.ravel())
rec_l2 = rgr_ridge.coef_.reshape(l, l)

# إعادة البناء مع عقوبة L1 (Lasso)
# تم تحديد أفضل قيمة لـ alpha باستخدام التحقق المتقاطع
# مع LassoCV
rgr_lasso = Lasso(alpha=0.001)
rgr_lasso.fit(proj_operator, proj.ravel())
rec_l1 = rgr_lasso.coef_.reshape(l, l)

plt.figure(figsize=(8, 3.3))
plt.subplot(131)
plt.imshow(data, cmap=plt.cm.gray, interpolation="nearest")
plt.axis("off")
plt.title("الصورة الأصلية")
plt.subplot(132)
plt.imshow(rec_l2, cmap=plt.cm.gray, interpolation="nearest")
plt.title("عقوبة L2")
plt.axis("off")
plt.subplot(133)
plt.imshow(rec_l1, cmap=plt.cm.gray, interpolation="nearest")
plt.title("عقوبة L1")
plt.axis("off")

plt.subplots_adjust(hspace=0.01, wspace=0.01, top=1, bottom=0, left=0, right=1)

plt.show()