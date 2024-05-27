"""
This is begining of my learning to build a neural network without a framework.
I'm expecting, it help me understand how work NN under the hood ( perharps, i translated it too literally )
"""

import numpy as np


'''
In this case i can use Logistic Regression to solve classification problem
Logistic regression use SIGMOID function
'''

'''
We'll be create NN which has 4 unit as the features are - sepal lenght,
sepal width, petal width.

Output layer has only one unit since it is the binary classification. 
'''


class my_NN(object):

    def __init__(self):
        self.input = 4
        self.output = 1
        self.hiden_units = 6

        # init matrix of weight
        np.random.seed(1)
        # weight1: input -> hidden layer
        self.w1 = np.random.randn(self.input, self.hiden_units) # 4*6 matrix
        # weight2: hidden layer -> output
        self.w2 = np.random.randn(self.hiden_units, self.output) # 6*1 matrix

    def _sigmoid(self, x):
        return 1/(1+np.exp(-x))

    def _sigmoid_prime(self, x):
        return self._sigmoid(x) * (1 - self._sigmoid(x))

    def _forward_propagation(self, X):
        self.z2 = np.dot(self.w1.T, X.T) # T mean transpose in numpy
        self.a2 = self._sigmoid(self.z2)
        self.z3 = np.dot(self.w2.T, self.a2)
        self.a3 = self._sigmoid(self.z3)
        return self.a3

    def _loss_function(self, predict, y):
        m = y.shape[0]
        logprobs = np.multiply(np.log(predict), y) + np.multiply((1-y), np.log(1-predict))
        loss = -np.sum(logprobs) / m
        return loss

    def _backward_propagation(self, X, y):
        predict = self._forward_propagation(X)
        m = X.shape[0]
        delta3 = predict - y
        dz3 = np.multiply(delta3, self._sigmoid_prime(self.z3))
        self.dw2 = 1/m * np.sum(np.multiply(self.a2, dz3), axis=1).reshape(self.w2.shape)

        delta2 = delta3 * self.w2 * self._sigmoid_prime(self.z2)
        self.dw1 = (1/m)*np.dot(X.T, delta2.T)

    def _update(self, learning_rate=1.2):
        self.w1 = self.w1 - learning_rate*self.dw1
        self.w2 = self.w2 - learning_rate*self.dw2

    def train(self, X, y, iteration=50):
        for i in range(iteration):
            y_hat = self._forward_propagation(X)
            loss = self._loss_function(y_hat, y)
            self._backward_propagation(X, y)
            self._update()
            if i % 10 == 0:
                print(f'Потери: {loss}')

    def predict(self, X):
        y_hat = self._forward_propagation(X)
        y_hat = [1 if i[0] >= 0.5 else 0 for i in y_hat.T]
        return np.array(y_hat)

    def score(self, predict, y):
        count = np.sum(predict == y)
        return count/len(y)*100
