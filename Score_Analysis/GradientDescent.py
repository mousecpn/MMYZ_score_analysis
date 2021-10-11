import numpy as np

def GradientDescent(a0,rnn_parameters,fc_parameters,fc_grads,rnn_grads,learning_rate):

    L = len(fc_parameters) // 2

    for l in range(L):
        fc_parameters["W"+str(l+1)] = fc_parameters["W"+str(l+1)] - learning_rate*fc_grads["dW"+str(l+1)]
        fc_parameters["W"+str(l+1)] = fc_parameters["W"+str(l+1)] - learning_rate*fc_grads["dW"+str(l+1)]

    rnn_parameters["Waa"] = rnn_parameters["Waa"] - learning_rate * rnn_grads["dWaa"]
    rnn_parameters["Wax"] = rnn_parameters["Wax"] - learning_rate * rnn_grads["dWax"]
    rnn_parameters["ba"] = rnn_parameters["ba"] - learning_rate * rnn_grads["dba"]
    a0 = a0 - learning_rate*rnn_grads["da0"]
    return a0,rnn_parameters,fc_parameters


