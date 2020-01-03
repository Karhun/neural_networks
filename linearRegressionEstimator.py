# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 10:48:55 2018

@author: Anette Karhu
"""
# Linear regression python code tutorial.

import numpy as np
import tensorflow as tf
import pandas as pd

# Train and test data.
df_test = pd.read_csv('test.csv', sep="," , quotechar='"')
df_train = pd.read_csv('train.csv', sep="," , quotechar='"')
#Change the csv file to arrays.
npArray1 = df_test.values
npArray2 = df_train.values

# Model parameters
# Declare list of features. Only one numeric feature.
feature_columns = [tf.feature_column.numeric_column("x", shape=[1])]
estimator = tf.estimator.LinearRegressor(feature_columns=feature_columns)

#Changes the data to one column.
x_train = npArray2[:,0]
y_train = npArray2[:,1]
x_eval = npArray1[:,0]
y_eval = npArray1[:,1]

#x_train = np.array([1., 2., 3., 4.])
#y_train = np.array([0., -1., -2., -3.])
#x_eval = np.array([2., 5., 8., 1.])
#y_eval = np.array([-1.01, -4.1, -7, 0.])
input_fn = tf.estimator.inputs.numpy_input_fn(
    {"x": x_train}, y_train, batch_size=700, num_epochs=None, shuffle=True)
train_input_fn = tf.estimator.inputs.numpy_input_fn(
    {"x": x_train}, y_train, batch_size=700, num_epochs=1000,
    shuffle=False)

eval_input_fn = tf.estimator.inputs.numpy_input_fn(
    {"x": x_eval}, y_eval, batch_size=300, num_epochs=1000,
    shuffle=False)

# 1000 training steps
estimator.train(input_fn=input_fn, steps=1000)

# Evaluate model performance
train_metrics = estimator.evaluate(input_fn=train_input_fn)
eval_metrics = estimator.evaluate(input_fn=eval_input_fn)
print("train metrics: %r"% train_metrics)
print("eval metrics: %r"% eval_metrics)

# Predict values for new inputs.
#new_samples = np.array([-1., 0., 1., 2.])
#predict_input_fn = tf.estimator.inputs.numpy_input_fn(
#{"x": new_samples}, batch_size=4, num_epochs=1,
#shuffle=False)
#predictions = list(estimator.predict(input_fn=predict_input_fn))
#predicted_classes = [p["predictions"][0] for p in predictions]
#print("New Samples, Predictions: {}\n".format(predicted_classes))
