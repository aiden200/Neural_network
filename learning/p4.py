'''
Simple 1 neuron networks with 4 inputs, inputs* weights + bias = output

using numpy now
'''
import numpy as np

inputs  = [[1.2, 5.6, 2.8, 5.4],
    [5,6,8,1],
    [2,2,1,5]]
weights = [[3.1, 5.1, 10.2, 0.8],
    [1, 5.1, 9, 0.8],
    [33.1, 0.1, 11.2, 0.8]]
bias = [3,1,0]

weights2 = [[0.1, -0.14, 0.5],
    [-0.5, 0.12, -0.33],
    [33.1, 0.1, 11.2]]
bias2 = [-1,2,0.5]

layer1_output = output = np.dot(inputs, np.array(weights).T) + bias
layer2_output = output = np.dot(layer1_output, np.array(weights2).T) + bias

print(layer2_output)