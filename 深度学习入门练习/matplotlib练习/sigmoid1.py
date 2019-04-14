import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    if x > 0:
        return 1
    else:
        return 0

def step_function2(x):
    y = x > 1
    return y.astype(np.int)

def show():
    x = np.arange(-5, 5, 0.1)
    y = step_function2(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1) #指定y轴的范围
    plt.show()

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def show_sigmoid():
    x = np.arange(-5, 5, 0.1)
    y = sigmoid(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1) #指定y轴范围
    plt.show()

X = np.array([1.0, 0.5]) 
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]]) 
B1 = np.array([0.1, 0.2, 0.3])
A1 = np.dot(X, W1) + B1
Z1 = sigmoid(A1)

W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])
A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)

print(A2)
print(Z2)


