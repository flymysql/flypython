import sys, os
import numpy as np
from functions import *
from gradient_descent import num_gradient

class TwolayerNet:
    def __init__(self, in_size, hide_size, out_size):
        self.par = {}
        self.par['w1'] = np.random.randn(in_size, hide_size)
        self.par['w2'] = np.random.randn(hide_size,out_size)
        self.par['b1'] = np.zeros(hide_size)
        self.par['b2'] = np.zeros(out_size)
    # 神经网络的推理
    def predict(self, x):
        z1 = sigmoid(np.dot(x, self.par['w1']) + self.par['b1'])
        z2 = softmax(np.dot(z1, self.par['w2']) + self.par['b2'])
        return z2
    # 损失函数
    def loss(self, x, t):
        y = self.predict(x)
        return cross_entropy_error(y, t)

    def accuracy(self,x, t):
        pass
    # 计算梯度
    def num_gradient(self, x, t):
        loss_W = lambda W: self.loss(x, t)
        grads = {}

        grads['w1'] = num_gradient(loss_W, self.par['w1'])
        grads['b1'] = num_gradient(loss_W, self.par['b1'])
        grads['w2'] = num_gradient(loss_W, self.par['w2'])
        grads['b2'] = num_gradient(loss_W, self.par['b2'])
        return grads
