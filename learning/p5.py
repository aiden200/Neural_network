'''
Simple 1 neuron networks with 4 inputs, inputs* weights + bias = output

using numpy now and OOP
'''
from socket import NI_NUMERICHOST
import numpy as np

X  = [[1.2, 5.6, 2.8, 5.4],
    [5,6,8,1],
    [2,2,1,5]]


class Layer_dense:
    def __init__(self, n_inputs, n_neurons):
        self.weight = 0.1*np.random.randn(n_inputs, n_neurons) #0.1 to make the values less than 1
        self.biases = np.zeros((1, n_neurons)) #first param is the shape so we have brackets
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weight) + self.biases

layer1 = Layer_dense(4, 5)
layer2 = Layer_dense(5, 2) #output of first needs to be input of second, hence the five

layer1.forward(X)
print(layer1.output)
layer2.forward(layer1.output)
print(layer2.output)