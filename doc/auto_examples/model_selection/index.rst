

.. _sphx_glr_auto_examples_model_selection:

.. _model_selection_examples:

Model Selection
-----------------------

Examples related to the :mod:`sklearn.model_selection` module.



.. raw:: html

    <div class="sphx-glr-thumbnails">

.. thumbnail-parent-div-open

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example balances model complexity and cross-validated score by finding a decent accuracy within 1 standard deviation of the best accuracy score while minimising the number of PCA components [1].">

.. only:: html

  .. image:: /auto_examples/model_selection/images/thumb/sphx_glr_plot_grid_search_refit_callable_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_model_selection_plot_grid_search_refit_callable.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Balance model complexity and cross-validated score</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example demonstrates the class_likelihood_ratios function, which computes the positive and negative likelihood ratios (`LR+`, LR-) to assess the predictive power of a binary classifier. As we will see, these metrics are independent of the proportion between classes in the test set, which makes them very useful when the available data for a study has a different class proportion than the target application.">

.. only:: html

  .. image:: /auto_examples/model_selection/images/thumb/sphx_glr_plot_likelihood_ratios_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_model_selection_plot_likelihood_ratios.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Class Likelihood Ratios to measure classification performance</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Compare randomized search and grid search for optimizing hyperparameters of a linear SVM with SGD training. All parameters that influence the learning are searched simultaneously (except for the number of estimators, which poses a time / quality tradeoff).">

.. only:: html

  .. image:: /auto_examples/model_selection/images/thumb/sphx_glr_plot_randomized_search_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_model_selection_plot_randomized_search.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Comparing randomized search and grid search for hyperparameter estimation</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example compares the parameter search performed by HalvingGridSearchCV and GridSearchCV.">

.. only:: html

  .. image:: /auto_examples/model_selection/images/thumb/sphx_glr_plot_successive_halving_heatmap_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_model_selection_plot_successive_halving_heatmap.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Comparison between grid search and successive halving</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Example of confusion matrix usage to evaluate the quality of the output of a classifier on the iris data set. The diagonal elements represent the number of points for which the predicted label is equal to the true label, while off-diagonal elements are those that are mislabeled by the classifier. The higher the diagonal values of the confusion matrix the better, indicating many correct predictions.">

.. only:: html

  .. image:: /auto_examples/model_selection/images/thumb/sphx_glr_plot_confusion_matrix_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_model_selection_plot_confusion_matrix.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Confusion matrix</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This examples shows how a classifier is optimized by cross-validation, which is done using the GridSearchCV object on a development set that comprises only half of the available labeled data.">

.. only:: html

  .. image:: /auto_examples/model_selection/images/thumb/sphx_glr_plot_grid_search_digits_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_model_selection_plot_grid_search_digits.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Custom refit strategy of a grid search with cross-validation</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Multiple metric parameter search can be done by setting the scoring parameter to a list of metric scorer names or a dict mapping the scorer names to the scorer callables.">

.. only:: html

  .. image:: /auto_examples/model_selection/images/thumb/sphx_glr_plot_multi_metric_evaluation_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_model_selection_plot_multi_metric_evaluation.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Demonstration of multi-metric evaluation on cross_val_score and GridSearchCV</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="In this example, we compare two binary classification multi-threshold metrics: the Receiver Operating Characteristic (ROC) and the Detection Error Tradeoff (DET). For such purpose, we evaluate two different classifiers for the same classification task.">

.. only:: html

  .. image:: /auto_examples/model_selection/images/thumb/sphx_glr_plot_det_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_model_selection_plot_det.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Detection error tradeoff (DET) curve</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example describes the use of the Receiver Operating Characteristic (ROC) metric to evaluate the quality of multiclass classifiers.">

.. only:: html

  .. image:: /auto_examples/model_selection/images/thumb/sphx_glr_plot_roc_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_model_selection_plot_roc.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Multiclass Receiver Operating Characteristic (ROC)</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example compares non-nested and nested cross-validation strategies on a classifier of the iris data set. Nested cross-validation (CV) is often used to train a model in which hyperparameters also need to be optimized. Nested CV estimates the generalization error of the underlying model and its (hyper)parameter search. Choosing the parameters that maximize non-nested CV biases the model to the dataset, yielding an overly-optimistic score.">

.. only:: html

  .. image:: /auto_examples/model_selection/images/thumb/sphx_glr_plot_nested_cross_validation_iris_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_model_selection_plot_nested_cross_validation_iris.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Nested versus non-nested cross-validation</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example shows how to use cross_val_predict together with PredictionErrorDisplay to visualize prediction errors.">

.. only:: html

  .. image:: /auto_examples/model_selection/images/thumb/sphx_glr_plot_cv_predict_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_model_selection_plot_cv_predict.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Plotting Cross-Validated Predictions</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="In this example, we show how to use the class LearningCurveDisplay to easily plot learning curves. In addition, we give an interpretation to the learning curves obtained for a naive Bayes and SVM classifiers.">

.. only:: html

  .. image:: /auto_examples/model_selection/images/thumb/sphx_glr_plot_learning_curve_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_model_selection_plot_learning_curve.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Plotting Learning Curves and Checking Models' Scalability</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="In this plot you can see the training scores and validation scores of an SVM for different values of the kernel parameter gamma. For very low values of gamma, you can see that both the training score and the validation score are low. This is called underfitting. Medium values of gamma will result in high values for both scores, i.e. the classifier is performing fairly well. If gamma is too high, the classifier will overfit, which means that the training score is good but the validation score is poor.">

.. only:: html

  .. image:: /auto_examples/model_selection/images/thumb/sphx_glr_plot_validation_curve_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_model_selection_plot_validation_curve.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Plotting Validation Curves</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Once a binary classifier is trained, the predict method outputs class label predictions corresponding to a thresholding of either the decision_function or the predict_proba output. The default threshold is defined as a posterior probability estimate of 0.5 or a decision score of 0.0. However, this default strategy may not be optimal for the task at hand.">

.. only:: html

  .. image:: /auto_examples/model_selection/images/thumb/sphx_glr_plot_tuned_decision_threshold_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_model_selection_plot_tuned_decision_threshold.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Post-hoc tuning the cut-off point of decision function</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Once a classifier is trained, the output of the predict method outputs class label predictions corresponding to a thresholding of either the decision_function or the predict_proba output. For a binary classifier, the default threshold is defined as a posterior probability estimate of 0.5 or a decision score of 0.0.">

.. only:: html

  .. image:: /auto_examples/model_selection/images/thumb/sphx_glr_plot_cost_sensitive_learning_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_model_selection_plot_cost_sensitive_learning.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Post-tuning the decision threshold for cost-sensitive learning</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Example of Precision-Recall metric to evaluate classifier output quality.">

.. only:: html

  .. image:: /auto_examples/model_selection/images/thumb/sphx_glr_plot_precision_recall_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_model_selection_plot_precision_recall.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Precision-Recall</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example presents how to estimate and visualize the variance of the Receiver Operating Characteristic (ROC) metric using cross-validation.">

.. only:: html

  .. image:: /auto_examples/model_selection/images/thumb/sphx_glr_plot_roc_crossval_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_model_selection_plot_roc_crossval.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Receiver Operating Characteristic (ROC) with cross validation</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="The dataset used in this example is 20newsgroups_dataset which will be automatically downloaded, cached and reused for the document classification example.">

.. only:: html

  .. image:: /auto_examples/model_selection/images/thumb/sphx_glr_plot_grid_search_text_feature_extraction_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_model_selection_plot_grid_search_text_feature_extraction.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Sample pipeline for text feature extraction and evaluation</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example illustrates how to statistically compare the performance of models trained and evaluated using GridSearchCV.">

.. only:: html

  .. image:: /auto_examples/model_selection/images/thumb/sphx_glr_plot_grid_search_stats_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_model_selection_plot_grid_search_stats.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Statistical comparison of models using grid search</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example illustrates how a successive halving search (~sklearn.model_selection.HalvingGridSearchCV and HalvingRandomSearchCV) iteratively chooses the best parameter combination out of multiple candidates.">

.. only:: html

  .. image:: /auto_examples/model_selection/images/thumb/sphx_glr_plot_successive_halving_iterations_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_model_selection_plot_successive_halving_iterations.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Successive Halving Iterations</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example demonstrates the use of permutation_test_score to evaluate the significance of a cross-validated score using permutations.">

.. only:: html

  .. image:: /auto_examples/model_selection/images/thumb/sphx_glr_plot_permutation_tests_for_classification_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_model_selection_plot_permutation_tests_for_classification.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Test with permutations the significance of a classification score</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Illustration of how the performance of an estimator on unseen data (test data) is not the same as the performance on training data. As the regularization increases the performance on train decreases while the performance on test is optimal within a range of values of the regularization parameter. The example with an Elastic-Net regression model and the performance is measured using the explained variance a.k.a. R^2.">

.. only:: html

  .. image:: /auto_examples/model_selection/images/thumb/sphx_glr_plot_train_error_vs_test_error_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_model_selection_plot_train_error_vs_test_error.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Train error vs Test error</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example demonstrates the problems of underfitting and overfitting and how we can use linear regression with polynomial features to approximate nonlinear functions. The plot shows the function that we want to approximate, which is a part of the cosine function. In addition, the samples from the real function and the approximations of different models are displayed. The models have polynomial features of different degrees. We can see that a linear function (polynomial with degree 1) is not sufficient to fit the training samples. This is called underfitting. A polynomial of degree 4 approximates the true function almost perfectly. However, for higher degrees the model will overfit the training data, i.e. it learns the noise of the training data. We evaluate quantitatively overfitting / underfitting by using cross-validation. We calculate the mean squared error (MSE) on the validation set, the higher, the less likely the model generalizes correctly from the training data.">

.. only:: html

  .. image:: /auto_examples/model_selection/images/thumb/sphx_glr_plot_underfitting_overfitting_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_model_selection_plot_underfitting_overfitting.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Underfitting vs. Overfitting</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Choosing the right cross-validation object is a crucial part of fitting a model properly. There are many ways to split data into training and test sets in order to avoid model overfitting, to standardize the number of groups in test sets, etc.">

.. only:: html

  .. image:: /auto_examples/model_selection/images/thumb/sphx_glr_plot_cv_indices_thumb.png
    :alt:

  :ref:`sphx_glr_auto_examples_model_selection_plot_cv_indices.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Visualizing cross-validation behavior in scikit-learn</div>
    </div>


.. thumbnail-parent-div-close

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /auto_examples/model_selection/plot_grid_search_refit_callable
   /auto_examples/model_selection/plot_likelihood_ratios
   /auto_examples/model_selection/plot_randomized_search
   /auto_examples/model_selection/plot_successive_halving_heatmap
   /auto_examples/model_selection/plot_confusion_matrix
   /auto_examples/model_selection/plot_grid_search_digits
   /auto_examples/model_selection/plot_multi_metric_evaluation
   /auto_examples/model_selection/plot_det
   /auto_examples/model_selection/plot_roc
   /auto_examples/model_selection/plot_nested_cross_validation_iris
   /auto_examples/model_selection/plot_cv_predict
   /auto_examples/model_selection/plot_learning_curve
   /auto_examples/model_selection/plot_validation_curve
   /auto_examples/model_selection/plot_tuned_decision_threshold
   /auto_examples/model_selection/plot_cost_sensitive_learning
   /auto_examples/model_selection/plot_precision_recall
   /auto_examples/model_selection/plot_roc_crossval
   /auto_examples/model_selection/plot_grid_search_text_feature_extraction
   /auto_examples/model_selection/plot_grid_search_stats
   /auto_examples/model_selection/plot_successive_halving_iterations
   /auto_examples/model_selection/plot_permutation_tests_for_classification
   /auto_examples/model_selection/plot_train_error_vs_test_error
   /auto_examples/model_selection/plot_underfitting_overfitting
   /auto_examples/model_selection/plot_cv_indices

