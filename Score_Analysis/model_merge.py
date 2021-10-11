import numpy as np
import pandas as pd
from fc_layer_init import fc_layer_init
from rnn_init import rnn_init
from forward import forward
from forward import error
from backward import backward
from GradientDescent import GradientDescent
from Data_Setup import Data_Input
from Data_Setup import Data_Setup
from basicFun import normalize

datList = Data_Input(r'C:\Users\mouse\Desktop\score\training_data_1.xlsx')
Y_label = pd.read_excel(r'C:\Users\mouse\Desktop\score\train_data_1_label.xlsx',sheetname=0)
dat,dat_matrix = Data_Setup(datList)
X = np.ones((6,2087,4)) #2090个样本，6个feature，4个时间
X[:,:,1] = normalize(dat_matrix[:,2:8,1]).T
X[:,:,2] = normalize(dat_matrix[:,2:8,2]).T
X[:,:,3] = normalize(dat_matrix[:,2:8,3]).T
X[:,:,0] = normalize(dat_matrix[:,2:8,0]).T

Y = Y_label.values[:,3].T
n_x,m,T_x = X.shape
learning_rate = 1
#定义rnn起始参数，a0(n_a,m)
n_a = 6 #这个超参数还要再调调
a0 = np.zeros((n_a,m))

layer_dims=[6,5,1]
fc_parameters = fc_layer_init(layer_dims)
rnn_parameters = rnn_init(n_a,n_x,m)
E = np.zeros((1,10000))
for i in range(100000):
    a,rnn_caches,fcAL,fc_caches = forward(X,a0,rnn_parameters,fc_parameters)
    fc_grads,rnn_grads = backward(fcAL,Y,fc_caches,rnn_caches,T_x)
    a0,rnn_parameters,fc_parameters = GradientDescent(a0,rnn_parameters,fc_parameters,fc_grads,rnn_grads,learning_rate)
    e = error(fcAL,Y)
x=e
print(x)
while x==1:
    x=1

