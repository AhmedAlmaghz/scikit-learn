يمكنك تثبيت "كوندا" باستخدام Anaconda أو Miniconda installers من الرابط التالي: <https://docs.conda.io/projects/conda/en/latest/user-guide/install/> أو باستخدام miniforge installers من هنا: <https://github.com/conda-forge/miniforge#miniforge> (لا تحتاج أي من هذه الطرق إلى إذن المسؤول). ثم قم بتشغيل ما يلي:

.. prompt:: bash

  conda create -n sklearn-env -c conda-forge scikit-learn
  conda activate sklearn-env

للتأكد من تثبيتك، يمكنك استخدام ما يلي:

.. prompt:: bash

  conda list scikit-learn  # عرض إصدار scikit-learn وموقعه
  conda list               # عرض جميع الحزم المثبتة في البيئة
  python -c "import sklearn; sklearn.show_versions()"