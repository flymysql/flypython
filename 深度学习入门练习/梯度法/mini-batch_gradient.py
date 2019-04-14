import numpy as np
import sys, os
sys.path.append(os.pardir)
from data.dataset.mnist import load_mnist
from TwoLayerNet import TwolayerNet

(x_train,t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

train_loss_list = []

step_num = 10
train_size = x_train.shape[0]
batch_size = 100
lr = 0.1

network = TwolayerNet(in_size=784, hide_size=50, out_size=10)

for i in range(step_num):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    grad = network.num_gradient(x_batch, t_batch)
    for key in ('w1', 'w2', 'b1', 'b2'):
        network.par[key] -= lr * grad[key]
    
    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)

print(train_loss_list.shape())
