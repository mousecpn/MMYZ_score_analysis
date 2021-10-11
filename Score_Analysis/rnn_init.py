import numpy as np

def rnn_init(n_a,n_x,m):
    Waa = np.zeros((n_a,n_a))
    Wax = np.zeros((n_a,n_x))
    ba = np.zeros((n_a,1))

    parameters = {"Waa":Waa,"Wax":Wax,"ba":ba}
    return parameters