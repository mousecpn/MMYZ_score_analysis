import numpy as np
from rnn_cell_forward import rnn_cell_forward
def rnn_forward(x,a0,parameters):
    caches = []

    n_x,m,T_x = x.shape
    n_a,n_a = parameters["Waa"].shape

    a = np.zeros((n_a,m,T_x))
    a_next = np.zeros((n_a,m))

    for t in range(T_x):
        a_next,cache = rnn_cell_forward(x[:,:,t],a[:,:,t],parameters)
        a[:,:,t] = a_next
        caches.append(cache)

    caches = (caches , x)

    return a,caches