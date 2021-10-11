import numpy as np

def rnn_cell_backward(da_next,cache):

    (a_next,a_prev,xt,parameters) = cache

    Wax = parameters["Wax"]
    Waa = parameters["Waa"]
    ba = parameters["ba"]

    dtanh = (1-a_next**2)*da_next

    dxt = np.dot(Wax.T,dtanh)
    dWax = np.dot(dtanh,xt.T)

    da_prev = np.dot(Waa.T,dtanh)
    dWaa = np.dot(dtanh,a_prev.T)

    dba = np.sum(dtanh,keepdims=True,axis=-1)

    gradients = {"dxt":dxt,"da_prev":da_prev,"dWax":dWax,"dWaa":dWaa,"dba":dba}

    return gradients