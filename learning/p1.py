'''
Simple single neuron network with 4 inputs, inputs* weights + bias = output
'''

inputs  = [1.2, 5.6, 2.8, 5.4]
weights = [3.1, 5.1, 10.2, 0.8]
bias = 3

output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + inputs[3]*weights[3] + bias
print(output)