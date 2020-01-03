from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

#import os
#from six.moves.urllib.request import urlopen

import numpy as np
import tensorflow as tf
import pandas as pd

# Data sets, Titanic data.
df = pd.read_csv('test2.csv', sep="," , quotechar='"')
test_set = df.values

df2 = pd.read_csv('train2.csv', sep="," , quotechar='"')
training_set = df2.values

# Specify that all features have real-value data
feature_columns = [tf.feature_column.numeric_column("x", shape=[12])]

# Build 3 layer DNN with 10, 20, 10 units respectively.
classifier = tf.estimator.DNNClassifier(feature_columns=feature_columns,
                                          hidden_units=[10, 20, 10],
                                          n_classes=2,
                                          model_dir="/tmp/test_model")
# Define the training inputs
train_input_fn = tf.estimator.inputs.numpy_input_fn(
      x={"x": np.array(training_set.data)},
      y=np.array(training_set),
      num_epochs=None,
      shuffle=True)

# Train model.
classifier.train(input_fn=train_input_fn, steps=2000)

# Define the test inputs
test_input_fn = tf.estimator.inputs.numpy_input_fn(
      x={"x": np.array(test_set.data)},
      y=np.array(test_set),
      num_epochs=1,
      shuffle=False)

# Evaluate accuracy.
accuracy_score = classifier.evaluate(input_fn=test_input_fn)["accuracy"]

print("\nTest Accuracy: {0:f}\n".format(accuracy_score))
