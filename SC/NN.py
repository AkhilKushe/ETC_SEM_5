import numpy as np

class Neuron:
    def __init__(self, n_inputs, weights, activation, b=0):
        self.n_inputs = n_inputs
        self.weights = np.array(weights, dtype=np.float32)
        self.activation = activation
        self.b = b
    
    def __str__(self):
        return f"<Neuron(n_inputs={self.n_inputs}, weights={self.weights}, activation={self.activation})>"
    
    def get_net(self, inputs):
        if len(inputs) != self.n_inputs:
            print("Expected input of length : %d, got %d", self.n_inputs, len(inputs))
        
        inputs = np.array(inputs, dtype=np.float32)

        net = self.weights.T.dot(inputs) + self.b

        return net

    
    def get_output(self, inputs):
        if len(inputs) != self.n_inputs:
            print("Expected input of length : %d, got %d", self.n_inputs, len(inputs))
        
        net = self.get_net(inputs)

        output = self.activation(net)

        return output



class Layer:
    def __init__(self, n_inputs, neurons):
        self.n_inputs = n_inputs
        for neuron in neurons:
            if neuron.n_inputs != n_inputs:
                raise f"Expected neuron of input length {self.n_inputs} got {neuron.n_inputs}"
        self.neurons = neurons
        self.n_outputs = len(neurons)
    
    def get_net(self, inputs):
        if len(inputs) != self.n_inputs:
            print("Expected input of length : %d, got %d", self.n_inputs, len(inputs))
        
        inputs = np.array(inputs, dtype=np.float32)

        nets = []
        for neuron in self.neurons:
            nets.append(neuron.get_net(inputs))

        nets = np.array(nets)
        return nets
    
    def get_outputs(self, inputs):
        if len(inputs) != self.n_inputs:
            print("Expected input of length : %d, got %d", self.n_inputs, len(inputs))
        
        inputs = np.array(inputs, dtype=np.float32)

        outputs = []
        for neuron in self.neurons:
            outputs.append(neuron.get_output(inputs))

        outputs = np.array(outputs)
        return outputs
        
class Sequential:
    def __init__(self, layers):
        self.layers = layers
        for i in range(len(self.layers)-1):
            if self.layers[i].n_outputs != self.layers[i+1].n_inputs:
                raise f"The output of {i}th neuron does not match the input of {i+1}th neuron"
    
    def get_outputs(self, inputs):
        output = np.array(inputs)
        for layer in self.layers:
            output = layer.get_outputs(output)
        
        return output


