import numpy as np
def rnn_cell_forward(xt,a_prev,parameters):

    Wax = parameters["Wax"]
    Waa = parameters["Waa"]
    ba = parameters["ba"]

    Z = np.dot(Waa,a_prev) + np.dot(Wax,xt) + ba
    a_next = np.tanh(Z)

    cache = (a_next , a_prev , xt , parameters)

    return a_next, cache