'''
Simple 3 neuron networks with 4 inputs, inputs* weights + bias = output

no numpy and for loops yet
'''

inputs  = [1.2, 5.6, 2.8, 5.4]
weights1 = [3.1, 5.1, 10.2, 0.8]
weights2 = [1, 5.1, 9, 0.8]
weights3 = [33.1, 0.1, 11.2, 0.8]
bias1 = 3
bias2 = 1
bias3 = 0

output1 = inputs[0]*weights1[0] + inputs[1]*weights1[1] + inputs[2]*weights1[2] + inputs[3]*weights1[3] + bias1
output2 = inputs[0]*weights2[0] + inputs[1]*weights2[1] + inputs[2]*weights2[2] + inputs[3]*weights2[3] + bias1
output3 = inputs[0]*weights3[0] + inputs[1]*weights3[1] + inputs[2]*weights3[2] + inputs[3]*weights3[3] + bias1
print(output1)
print(output2)
print(output3)