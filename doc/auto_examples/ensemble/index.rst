

.. _sphx_glr_auto_examples_ensemble:

.. _ensemble_examples:

Ensemble methods
----------------

Examples concerning the :mod:`sklearn.ensemble` module.



.. raw:: html

    <div class="sphx-glr-thumbnails">

.. thumbnail-parent-div-open

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="In this example, we will compare the training times and prediction performances of HistGradientBoostingRegressor with different encoding strategies for categorical features. In particular, we will evaluate:">

.. only:: html

  .. image:: /auto_examples/ensemble/images/thumb/sphx_glr_plot_gradient_boosting_categorical_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_ensemble_plot_gradient_boosting_categorical.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Categorical Feature Support in Gradient Boosting</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Stacking refers to a method to blend estimators. In this strategy, some estimators are individually fitted on some training data while a final estimator is trained using the stacked predictions of these base estimators.">

.. only:: html

  .. image:: /auto_examples/ensemble/images/thumb/sphx_glr_plot_stack_predictors_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_ensemble_plot_stack_predictors.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Combine predictors using stacking</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="In this example we compare the performance of Random Forest (RF) and Histogram Gradient Boosting (HGBT) models in terms of score and computation time for a regression dataset, though all the concepts here presented apply to classification as well.">

.. only:: html

  .. image:: /auto_examples/ensemble/images/thumb/sphx_glr_plot_forest_hist_grad_boosting_comparison_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_ensemble_plot_forest_hist_grad_boosting_comparison.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Comparing Random Forests and Histogram Gradient Boosting models</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="An example to compare multi-output regression with random forest and the multiclass meta-estimator.">

.. only:: html

  .. image:: /auto_examples/ensemble/images/thumb/sphx_glr_plot_random_forest_regression_multioutput_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_ensemble_plot_random_forest_regression_multioutput.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Comparing random forests and the multi-output meta estimator</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="A decision tree is boosted using the AdaBoost.R2 [1]_ algorithm on a 1D sinusoidal dataset with a small amount of Gaussian noise. 299 boosts (300 decision trees) is compared with a single decision tree regressor. As the number of boosts is increased the regressor can fit more detail.">

.. only:: html

  .. image:: /auto_examples/ensemble/images/thumb/sphx_glr_plot_adaboost_regression_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_ensemble_plot_adaboost_regression.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Decision Tree Regression with AdaBoost</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Gradient Boosting is an ensemble technique that combines multiple weak learners, typically decision trees, to create a robust and powerful predictive model. It does so in an iterative fashion, where each new stage (tree) corrects the errors of the previous ones.">

.. only:: html

  .. image:: /auto_examples/ensemble/images/thumb/sphx_glr_plot_gradient_boosting_early_stopping_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_ensemble_plot_gradient_boosting_early_stopping.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Early stopping in Gradient Boosting</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example shows the use of a forest of trees to evaluate the importance of features on an artificial classification task. The blue bars are the feature importances of the forest, along with their inter-trees variability represented by the error bars.">

.. only:: html

  .. image:: /auto_examples/ensemble/images/thumb/sphx_glr_plot_forest_importances_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_ensemble_plot_forest_importances.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Feature importances with a forest of trees</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Transform your features into a higher dimensional, sparse space. Then train a linear model on these features.">

.. only:: html

  .. image:: /auto_examples/ensemble/images/thumb/sphx_glr_plot_feature_transformation_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_ensemble_plot_feature_transformation.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Feature transformations with ensembles of trees</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="histogram_based_gradient_boosting (HGBT) models may be one of the most useful supervised learning models in scikit-learn. They are based on a modern gradient boosting implementation comparable to LightGBM and XGBoost. As such, HGBT models are more feature rich than and often outperform alternative models like random forests, especially when the number of samples is larger than some ten thousands (see sphx_glr_auto_examples_ensemble_plot_forest_hist_grad_boosting_comparison.py).">

.. only:: html

  .. image:: /auto_examples/ensemble/images/thumb/sphx_glr_plot_hgbt_regression_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_ensemble_plot_hgbt_regression.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Features in Histogram Gradient Boosting Trees</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Gradient Boosting Out-of-Bag estimates">

.. only:: html

  .. image:: /auto_examples/ensemble/images/thumb/sphx_glr_plot_gradient_boosting_oob_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_ensemble_plot_gradient_boosting_oob.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Gradient Boosting Out-of-Bag estimates</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example demonstrates Gradient Boosting to produce a predictive model from an ensemble of weak predictive models. Gradient boosting can be used for regression and classification problems. Here, we will train a model to tackle a diabetes regression task. We will obtain the results from GradientBoostingRegressor with least squares loss and 500 regression trees of depth 4.">

.. only:: html

  .. image:: /auto_examples/ensemble/images/thumb/sphx_glr_plot_gradient_boosting_regression_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_ensemble_plot_gradient_boosting_regression.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Gradient Boosting regression</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Illustration of the effect of different regularization strategies for Gradient Boosting. The example is taken from Hastie et al 2009 [1]_.">

.. only:: html

  .. image:: /auto_examples/ensemble/images/thumb/sphx_glr_plot_gradient_boosting_regularization_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_ensemble_plot_gradient_boosting_regularization.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Gradient Boosting regularization</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="RandomTreesEmbedding provides a way to map data to a very high-dimensional, sparse representation, which might be beneficial for classification. The mapping is completely unsupervised and very efficient.">

.. only:: html

  .. image:: /auto_examples/ensemble/images/thumb/sphx_glr_plot_random_forest_embedding_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_ensemble_plot_random_forest_embedding.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Hashing feature transformation using Totally Random Trees</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="An example using IsolationForest for anomaly detection.">

.. only:: html

  .. image:: /auto_examples/ensemble/images/thumb/sphx_glr_plot_isolation_forest_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_ensemble_plot_isolation_forest.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">IsolationForest example</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example illustrates the effect of monotonic constraints on a gradient boosting estimator.">

.. only:: html

  .. image:: /auto_examples/ensemble/images/thumb/sphx_glr_plot_monotonic_constraints_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_ensemble_plot_monotonic_constraints.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Monotonic Constraints</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example shows how boosting can improve the prediction accuracy on a multi-label classification problem. It reproduces a similar experiment as depicted by Figure 1 in Zhu et al [1]_.">

.. only:: html

  .. image:: /auto_examples/ensemble/images/thumb/sphx_glr_plot_adaboost_multiclass_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_ensemble_plot_adaboost_multiclass.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Multi-class AdaBoosted Decision Trees</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="The RandomForestClassifier is trained using bootstrap aggregation, where each new tree is fit from a bootstrap sample of the training observations z_i = (x_i, y_i). The out-of-bag (OOB) error is the average error for each z_i calculated using predictions from the trees that do not contain z_i in their respective bootstrap sample. This allows the RandomForestClassifier to be fit and validated whilst being trained [1]_.">

.. only:: html

  .. image:: /auto_examples/ensemble/images/thumb/sphx_glr_plot_ensemble_oob_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_ensemble_plot_ensemble_oob.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">OOB Errors for Random Forests</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example shows the use of a forest of trees to evaluate the impurity based importance of the pixels in an image classification task on the faces dataset. The hotter the pixel, the more important it is.">

.. only:: html

  .. image:: /auto_examples/ensemble/images/thumb/sphx_glr_plot_forest_importances_faces_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_ensemble_plot_forest_importances_faces.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Pixel importances with a parallel forest of trees</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Plot the class probabilities of the first sample in a toy dataset predicted by three different classifiers and averaged by the VotingClassifier.">

.. only:: html

  .. image:: /auto_examples/ensemble/images/thumb/sphx_glr_plot_voting_probas_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_ensemble_plot_voting_probas.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Plot class probabilities calculated by the VotingClassifier</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="A voting regressor is an ensemble meta-estimator that fits several base regressors, each on the whole dataset. Then it averages the individual predictions to form a final prediction. We will use three different regressors to predict the data: GradientBoostingRegressor, RandomForestRegressor, and LinearRegression). Then the above 3 regressors will be used for the VotingRegressor.">

.. only:: html

  .. image:: /auto_examples/ensemble/images/thumb/sphx_glr_plot_voting_regressor_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_ensemble_plot_voting_regressor.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Plot individual and voting regression predictions</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Plot the decision boundaries of a VotingClassifier for two features of the Iris dataset.">

.. only:: html

  .. image:: /auto_examples/ensemble/images/thumb/sphx_glr_plot_voting_decision_regions_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_ensemble_plot_voting_decision_regions.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Plot the decision boundaries of a VotingClassifier</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Plot the decision surfaces of forests of randomized trees trained on pairs of features of the iris dataset.">

.. only:: html

  .. image:: /auto_examples/ensemble/images/thumb/sphx_glr_plot_forest_iris_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_ensemble_plot_forest_iris.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Plot the decision surfaces of ensembles of trees on the iris dataset</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example shows how quantile regression can be used to create prediction intervals. See sphx_glr_auto_examples_ensemble_plot_hgbt_regression.py for an example showcasing some other features of HistGradientBoostingRegressor.">

.. only:: html

  .. image:: /auto_examples/ensemble/images/thumb/sphx_glr_plot_gradient_boosting_quantile_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_ensemble_plot_gradient_boosting_quantile.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Prediction Intervals for Gradient Boosting Regression</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example illustrates and compares the bias-variance decomposition of the expected mean squared error of a single estimator against a bagging ensemble.">

.. only:: html

  .. image:: /auto_examples/ensemble/images/thumb/sphx_glr_plot_bias_variance_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_ensemble_plot_bias_variance.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Single estimator versus bagging: bias-variance decomposition</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example fits an AdaBoosted decision stump on a non-linearly separable classification dataset composed of two &quot;Gaussian quantiles&quot; clusters (see sklearn.datasets.make_gaussian_quantiles) and plots the decision boundary and decision scores. The distributions of decision scores are shown separately for samples of class A and B. The predicted class label for each sample is determined by the sign of the decision score. Samples with decision scores greater than zero are classified as B, and are otherwise classified as A. The magnitude of a decision score determines the degree of likeness with the predicted class label. Additionally, a new dataset could be constructed containing a desired purity of class B, for example, by only selecting samples with a decision score above some value.">

.. only:: html

  .. image:: /auto_examples/ensemble/images/thumb/sphx_glr_plot_adaboost_twoclass_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_ensemble_plot_adaboost_twoclass.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Two-class AdaBoost</div>
    </div>


.. thumbnail-parent-div-close

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/ensemble/plot_gradient_boosting_categorical
   /auto_examples/ensemble/plot_stack_predictors
   /auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison
   /auto_examples/ensemble/plot_random_forest_regression_multioutput
   /auto_examples/ensemble/plot_adaboost_regression
   /auto_examples/ensemble/plot_gradient_boosting_early_stopping
   /auto_examples/ensemble/plot_forest_importances
   /auto_examples/ensemble/plot_feature_transformation
   /auto_examples/ensemble/plot_hgbt_regression
   /auto_examples/ensemble/plot_gradient_boosting_oob
   /auto_examples/ensemble/plot_gradient_boosting_regression
   /auto_examples/ensemble/plot_gradient_boosting_regularization
   /auto_examples/ensemble/plot_random_forest_embedding
   /auto_examples/ensemble/plot_isolation_forest
   /auto_examples/ensemble/plot_monotonic_constraints
   /auto_examples/ensemble/plot_adaboost_multiclass
   /auto_examples/ensemble/plot_ensemble_oob
   /auto_examples/ensemble/plot_forest_importances_faces
   /auto_examples/ensemble/plot_voting_probas
   /auto_examples/ensemble/plot_voting_regressor
   /auto_examples/ensemble/plot_voting_decision_regions
   /auto_examples/ensemble/plot_forest_iris
   /auto_examples/ensemble/plot_gradient_boosting_quantile
   /auto_examples/ensemble/plot_bias_variance
   /auto_examples/ensemble/plot_adaboost_twoclass

