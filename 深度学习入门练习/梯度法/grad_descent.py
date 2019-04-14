import sys, os
import numpy as np

# 求中心差分
def num_gradient(f, x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x)
    
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x) # f(x+h)
        
        x[idx] = tmp_val - h 
        fxh2 = f(x) # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2*h)
        
        x[idx] = tmp_val # 还原值
        it.iternext()   
        
    return grad
# 批处理交叉熵误差
def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
        
    # 监督数据是one-hot-vector的情况下，转换为正确解标签的索引
    if t.size == y.size:
        t = t.argmax(axis=1)

    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size

# softmax激活函数
def softmax(a):
    c = np.max(a)
    # 减去最大值，简化运算
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

# 一个简单的一层神经网络
class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3)   # 用高斯分布进行初始化
    def predict(self, x):
        return np.dot(x, self.W)
    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)
        return loss

if __name__ == "__main__":
    net = simpleNet()
    print(net.W)
    x = np.array([0.6, 0.9])
    p = net.predict(x)
    print(p)
    t = np.array([0, 0, 1])
    print(net.loss(x, t))

    def f(w):
        return net.loss(x, t)

    dw = ng(f, net.W)
    print(dw)