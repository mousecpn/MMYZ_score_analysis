from fc_layer_backward import L_model_backward
from rnn_backward import rnn_backward

def backward(fcAL,Y,fc_caches,rnn_caches,T_x):
    fc_grads = L_model_backward(fcAL, Y, fc_caches)
    dA1 = fc_grads["dA1"]
    rnn_grads = rnn_backward(dA1, rnn_caches, T_x)
    return fc_grads,rnn_grads

