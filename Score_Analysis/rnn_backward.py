import numpy as np
from rnn_cell_backward import rnn_cell_backward

def rnn_backward(daT,caches,T_x):

    (caches,x) = caches
    (a1,a0,x1,parameters) = caches[0]

    n_a,m = daT.shape
    n_x,m = x1.shape

    dx = np.zeros((n_x,m,T_x))
    dWax = np.zeros((n_a,n_x))
    dWaa = np.zeros((n_a,n_a))
    dba = np.zeros((n_a,1))
    da0 = np.zeros((n_a,m))
    """
    这里和deeplearning的那门课里面有些许不同
    因为原本的rnn模型在每一个时间节点都有输出
    而本模型不用，因此就不用考虑用输出Y<t>那边传递过来的da
    直接从最后的L传递梯度即可
    """
    da_prevt = daT

    for t in reversed(range(T_x)):
        gradients = rnn_cell_backward(da_prevt,caches[t])
        dxt,da_prevt,dWaxt,dWaat,dbat = gradients["dxt"],gradients["da_prev"],gradients["dWax"],gradients["dWaa"],gradients["dba"]

        dx[:,:,t] = dxt
        dWax += dWaxt
        dWaa += dWaat
        dba += dbat

    da0 = da_prevt

    gradients = {"dx":dx,"da0":da0,"dWax":dWax,"dWaa":dWaa,"dba":dba}

    return gradients
