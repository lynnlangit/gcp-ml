# from https://www.tensorflow.org/serving/docker

# 1. get the image
docker pull tensorflow/serving

# 2. get a pre-built model
mkdir -p /tmp/tfserving
cd /tmp/tfserving
git clone --depth=1 https://github.com/tensorflow/serving

# 3. run the container
docker run -p 8501:8501 \
-v /tmp/tfserving/serving/tensorflow_serving/servables/tensorflow/testdata/saved_model_half_plus_three:/models/half_plus_three \
-e MODEL_NAME=half_plus_three -t tensorflow/serving &

# 4. query the model
curl -d '{"instances": [1.0, 2.0, 5.0]}' -X POST http://localhost:8501/v1/models/half_plus_three:predict

# 5. verify the result
{ "predictions": [3.5, 4.0, 5.5] }

#-------------------Alternative Instructions---------------------------
docker pull tensorflow/serving:latest-devel
docker run -it -p 8500:8500 tensorflow/serving:latest-devel

# run this from inside the running container instance
bazel build -c opt //tensorflow_serving/example:mnist_saved_model
# train the mnist model
bazel-bin/tensorflow_serving/example/mnist_saved_model /tmp/mnist_model
# serve the model
tensorflow_model_server --port=8500 --model_name=mnist --model_base_path=/tmp/mnist_model/ &
# build the client
bazel build -c opt //tensorflow_serving/example:mnist_client
# test the client
bazel-bin/tensorflow_serving/example/mnist_client --num_tests=1000 --server=localhost:8500