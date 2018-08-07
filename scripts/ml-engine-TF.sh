# from - https://cloud.google.com/ml-engine/docs/tensorflow/getting-started-training-prediction

# The sample builds a wide and deep model for predicting income category based on United States Census 
# Income Dataset. The two income categories (also known as labels) are:
    # >50K—Greater than 50,000 dollars
    # <=50K—Less than or equal to 50,000 dollars
    # Wide and deep models use deep neural nets (DNNs) to learn high level abstractions about complex f
    # features or interactions between such features. These models then combine the outputs from the DNN 
    # with a linear regression performed on simpler features. 
    # This provides a balance between power and speed that is effective on many structured data problems.

# NOTE: can use gcloud shell or local (Mac) w/gcloud sdk
# -----------------------set up-------------------------
# enable Cloud ML and GCE APIs
# create service account (key) for Project Owner
#        -> download the .JSON file
# setup python in a virtualenv
# `gcloud components update`
# install TF and verify 

# download sample data
# wget https://github.com/GoogleCloudPlatform/cloudml-samples/archive/master.zip
# upzip and put data into directories for use by TF
# install requirements.txt

#---------------------run local--------------------------
# training job single mode

# gcloud ml-engine local train \
#     --module-name trainer.task \
#     --package-path trainer/ \
#     --job-dir $MODEL_DIR \
#     -- \
#     --train-files $TRAIN_DATA \
#     --eval-files $EVAL_DATA \
#     --train-steps 1000 \
#     --eval-steps 100

# inspect via TensorBoard
# tensorboard --logdir=$MODEL_DIR --port=8080

# training job distributed mode

# gcloud ml-engine local train \
#     --module-name trainer.task \
#     --package-path trainer/ \
#     --job-dir $MODEL_DIR \
#     --distributed \
#     -- \
#     --train-files $TRAIN_DATA \
#     --eval-files $EVAL_DATA \
#     --train-steps 1000 \
#     --eval-steps 100

#-------------------run GCP--------------------------------
# setup GCS bucket

# train model in single, then distributed mode
# perform hyperparameter tuning
# deploy model
# predict with model

#-------------------clean up--------------------------------
# remove GCP resources, including GCS bucket