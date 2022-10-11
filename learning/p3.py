'''
Simple 3 neuron networks with 4 inputs, inputs* weights + bias = output

no numpy, using zip and for loops
'''

inputs  = [1.2, 5.6, 2.8, 5.4]
weights = [[3.1, 5.1, 10.2, 0.8],
    [1, 5.1, 9, 0.8],
    [33.1, 0.1, 11.2, 0.8]]
bias = [3,1,0]

layer_outputs = []
for neuron_weights, neuron_bias in zip(weights, bias):
    current_neuron_output = 0
    for neuron_input, weight in zip(inputs, neuron_weights):
        current_neuron_output += neuron_input*weight
    current_neuron_output += neuron_bias
    layer_outputs.append(current_neuron_output)

print(layer_outputs)