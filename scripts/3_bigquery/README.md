# BigQuery Machine Learning

Code samples BigQuery Machine Learning.  BQ ML currently supports the following types of models:  

 - **Linear regression** — use to predict a numerical value  

 - **Binary logistic regression** — use to predict whether an input is a member of a class or not  

 - **Multiclass logistic regression for classification** — use to predict whether an input is a member of 2+ classes 
        such as whether an input is "low-value", "medium-value", or "high-value"

 ## Samples

  - [BQ ML for Analysts](FROM 'https://cloud.google.com/bigquery/docs/bigqueryml-analyst-start') code walkthrough
  - [CREATE MODEL](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create#models_in_bqml_name') syntax

  ## About EVALUATE

    - ML.EVALUATE()
    - ML.ROC_CURVE()
    - ML.CONFUSION_MATRIX()

  ## About PREDICT

   - For logistic regression models: 
        - The predicted_<label_column_name>_probs output column is an array of STRUCTs of type [<label, prob>] that contains the predicted probability of each label.
        - The predicted_<label_column_name> output column is one of the two input labels, depending on which label has the higher predicted probability.  

    - For multiclass logistic regression models:
        - The predicted_<label_column_name>_probs output column is the probability for each class label calculated using a softmax function.
        - The predicted_<label_column_name> output column is the label with the highest predicted probability score.  

    - For linear regression models:
        - The predicted_<label_column_name> output column is the predicted value of the label.

    - [More info](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-predict) about PREDICT

