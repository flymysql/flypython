import numpy as np
import matplotlib.pylab as plt

class network:
    def __init__(self):
        self.W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
        self.b1 = np.array([0.1, 0.2, 0.3])
        self.W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
        self.b2 = np.array([0.1, 0.2])
        self.W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
        self.b3 = np.array([0.1, 0.2])

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def indentity_fun(self, x):
        return x

    def for_ward(self, x):
        w1, w2, w3 = self.W1, self.W2, self.W3
        b1, b2, b3 = self.b1, self.b2, self.b3
        a1= np.dot(x, w1) + b1
        z1 = self.sigmoid(a1)
        a2 = np.dot(z1, w2) + b2
        z2 = self.sigmoid(a2)
        a3 = np.dot(z2, w3) + b3
        y = self.indentity_fun(a3)
        return y

net = network()
x = np.array([1.0, 0.5])
print(net.for_ward(x))
