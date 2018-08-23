"""This module handles training and evaluation of a neural network model.

Invoke the following command to train the model:
python -m trainer --model=cnn --dataset=mnist

You can then monitor the logs on Tensorboard:
tensorboard --logdir=output"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

tf.logging.set_verbosity(tf.logging.INFO)

tf.flags.DEFINE_string("model", "", "Model name.")
tf.flags.DEFINE_string("dataset", "", "Dataset name.")
tf.flags.DEFINE_string("output_dir", "", "Optional output dir.")
tf.flags.DEFINE_string("schedule", "train_and_evaluate", "Schedule.")
tf.flags.DEFINE_string("hparams", "", "Hyper parameters.")
tf.flags.DEFINE_integer("num_epochs", 100000, "Number of training epochs.")
tf.flags.DEFINE_integer("save_summary_steps", 10, "Summary steps.")
tf.flags.DEFINE_integer("save_checkpoints_steps", 10, "Checkpoint steps.")
tf.flags.DEFINE_integer("eval_steps", None, "Number of eval steps.")
tf.flags.DEFINE_integer("eval_frequency", 10, "Eval frequency.")

FLAGS = tf.flags.FLAGS

MODELS = {
    # This is a dictionary of models, the keys are model names, and the values
    # are the module containing get_params, model, and eval_metrics.
    # Example: "cnn": cnn
}

DATASETS = {
    # This is a dictionary of datasets, the keys are dataset names, and the
    # values are the module containing get_params, prepare, read, and parse.
    # Example: "mnist": mnist
}

HPARAMS = {
    "optimizer": "Adam",
    "learning_rate": 0.001,
    "decay_steps": 10000,
    "batch_size": 128
}

def get_params():
    """Aggregates and returns hyper parameters."""
    hparams = HPARAMS
    hparams.update(DATASETS[FLAGS.dataset].get_params())
    hparams.update(MODELS[FLAGS.model].get_params())

    hparams = tf.contrib.training.HParams(**hparams)
    hparams.parse(FLAGS.hparams)

    return hparams

def make_input_fn(mode, params):
    """Returns an input function to read the dataset."""
    def _input_fn():
        dataset = DATASETS[FLAGS.dataset].read(mode)
        if mode == tf.estimator.ModeKeys.TRAIN:
            dataset = dataset.repeat(FLAGS.num_epochs)
            dataset = dataset.shuffle(params.batch_size * 5)
        dataset = dataset.map(
            DATASETS[FLAGS.dataset].parse, num_threads=8)
        dataset = dataset.batch(params.batch_size)
        iterator = dataset.make_one_shot_iterator()
        features, labels = iterator.get_next()
        return features, labels
    return _input_fn

def make_model_fn():
    """Returns a model function."""
    def _model_fn(features, labels, mode, params):
        model_fn = MODELS[FLAGS.model].model
        global_step = tf.train.get_or_create_global_step()
        predictions, loss = model_fn(features, labels, mode, params)

        train_op = None
        if mode == tf.estimator.ModeKeys.TRAIN:
            def _decay(learning_rate, global_step):
                learning_rate = tf.train.exponential_decay(
                    learning_rate, global_step, params.decay_steps, 0.5,
                    staircase=True)
                return learning_rate

            train_op = tf.contrib.layers.optimize_loss(
                loss=loss,
                global_step=global_step,
                learning_rate=params.learning_rate,
                optimizer=params.optimizer,
                learning_rate_decay_fn=_decay)

        return tf.contrib.learn.ModelFnOps(
            mode=mode,
            predictions=predictions,
            loss=loss,
            train_op=train_op)

    return _model_fn

def experiment_fn(run_config, hparams):
    """Constructs an experiment object."""
    estimator = tf.contrib.learn.Estimator(
        model_fn=make_model_fn(), config=run_config, params=hparams)
    return tf.contrib.learn.Experiment(
        estimator=estimator,
        train_input_fn=make_input_fn(tf.estimator.ModeKeys.TRAIN, hparams),
        eval_input_fn=make_input_fn(tf.estimator.ModeKeys.EVAL, hparams),
        eval_metrics=MODELS[FLAGS.model].eval_metrics(hparams),
        eval_steps=FLAGS.eval_steps,
        min_eval_frequency=FLAGS.eval_frequency)

def main(unused_argv):
    """Main entry point."""
    if FLAGS.output_dir:
        model_dir = FLAGS.output_dir
    else:
        model_dir = "output/%s_%s" % (FLAGS.model, FLAGS.dataset)

    DATASETS[FLAGS.dataset].prepare()

    session_config = tf.ConfigProto()
    session_config.allow_soft_placement = True
    session_config.gpu_options.allow_growth = True
    run_config = tf.contrib.learn.RunConfig(
        model_dir=model_dir,
        save_summary_steps=FLAGS.save_summary_steps,
        save_checkpoints_steps=FLAGS.save_checkpoints_steps,
        save_checkpoints_secs=None,
        session_config=session_config)

    tf.contrib.learn.learn_runner.run(
        experiment_fn=experiment_fn,
        run_config=run_config,
        schedule=FLAGS.schedule,
        hparams=get_params())

if __name__ == "__main__":
    tf.app.run()
