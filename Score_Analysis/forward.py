import numpy as np
from fc_layer_forward import L_model_forward
from rnn_forward import rnn_forward
def forward(X,a0,rnn_parameters,fc_parameters):
    n_x, m, T_x = X.shape
    a,rnn_caches = rnn_forward(X,a0,rnn_parameters)
    fcAL,fc_caches = L_model_forward(a[:,:,T_x-1], fc_parameters)
    return a,rnn_caches,fcAL,fc_caches

# Y是一个(4,m)矩阵，1代表第一梯队学校，2代表985大学，3代表一本，4是非一本
def error(fcAL,Y):
    err = 0
    for i in range(Y.shape[0]):
        if(fcAL[0,i] > 0.5):
            pred = 1
        else:
            pred = 0
        if Y[i] != pred:
            err += 1
    err = err / Y.shape[0]
    return err