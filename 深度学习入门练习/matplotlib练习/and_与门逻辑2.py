import numpy as np
def And(x):
    w = np.array([0.5, 0.5])
    b = -1
    tmp = np.sum(w*x) + b
    if tmp >= 0:
        return 1
    else:
        return 0

def NAnd(x):
    if And(x) == 1:
        return 0
    else:
        return 1

def OR(x):
    w = np.array([0.5, 0.5])
    b = -0.5
    tmp = np.sum(w*x) + b
    if tmp >= 0:
        return 1
    else:
        return 0

def XOR(x):
    s1 = NAnd(x)
    s2 = OR(x)
    s = np.array([s1, s2])
    y = And(s)
    return y

print(XOR(np.array([0, 0])))
print(XOR(np.array([1, 0])))
print(XOR(np.array([0, 1])))
print(XOR(np.array([1, 1])))