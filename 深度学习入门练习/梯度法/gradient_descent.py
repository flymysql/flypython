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

def gradient_descent(fun, init_x, lr=0.01, setp_num=100):
    x =init_x
    for i in range(setp_num):
        grad = num_gradient(fun, x)
        x -= lr * grad
    return x

def function1(x):
    return x[0]**2 + x[1]**2 - 5 * x[2]

# init_x = np.array([-3.0, 4.0, 6.0])
# grad1 = gradient_descent(function1, init_x, lr=0.01, setp_num=10000)
# print(grad1)