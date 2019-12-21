# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 22:38:11 2019

@author: Anette

neural network tutorial trial
"""
import numpy as np

# Activation function
def sigmoid(x):
    return 1.0/(1+ np.exp(-x))

def sigmoid_derivative(x):
    return x * (1.0 - x)

class NeuralNetwork:
    """
    Simple neural network trial
    x = input layer
    y= output layer
    """
    def __init__(self,x,y):
        self.input = x
        self.weights1 = np.random.rand(self.input.shape[1],4)
        self.weights2 = np.random.rand(4,1)
        self.y = y
        self.output = np.zeros(self.y.shape)
        

    def feedforward(self):
        """
        calculates the predicted output y
        y = sig(w2*sig(w1*x+b1)+b2)
        """
        self.layer1 = sigmoid(np.dot(self.input,self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))
        
    def backprop(self):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2
        
if __name__ == "__main__":
    """
    Apply the NN, given x and y
    """
    X = np.array([[0,0,1],
          [0,1,1],
          [1,0,1],
          [1,1,1]])
    y = np.array([[0],[0],[1],[1]])
    nn = NeuralNetwork(X,y)
    
    #Train network for 1500 iterations
    for i in range(20000):
        nn.feedforward()
        nn.backprop()
    #output of the NN and wanted values    
    print(nn.output, y)
