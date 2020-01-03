# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 10:43:55 2018

@author: Anette Karhu
"""

import tensorflow as tf
import pandas as pd
import numpy as np

#Read data from a file
df = pd.read_csv('train.csv', sep="," , quotechar='"')

npMatrix = np.matrix(df)
x_train = npMatrix[:,0]
y_train = npMatrix[:,1]
# Model parameters
W = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)
# Model input and output
x = tf.placeholder(tf.float32)
linear_model = W*x + b
y = tf.placeholder(tf.float32)
# loss
loss = tf.reduce_sum(tf.square(linear_model - y)) # sum of the squares
# optimizer
optimizer = tf.train.GradientDescentOptimizer(0.0000001)
train = optimizer.minimize(loss)
# training data
#x_train = [1, 2, 3, 4]
#y_train = [0, -1, -2, -3]
# training loop
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init) # reset values to wrong
for i in range(10000):
    sess.run(train, {x: x_train, y: y_train})
# evaluate training accuracy
curr_W, curr_b, curr_loss = sess.run([W, b, loss], {x: x_train, y: y_train})
print("W: %s b: %s loss: %s"%(curr_W, curr_b, curr_loss))
# predict new values
x_predict = [-1, 0, 1, 2]
predicted_values = [(W*x + b).eval(session=sess) for x in x_predict]
print(predicted_values)