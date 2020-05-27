"""
    File name: NeuralNetwork.py
    Author: Kacper Kaczmarek, Krzysztof Kobyliński
    Python Version: 3.6.0
"""
import numpy as np
import source.Neuron as Neuron


class NeuralNetwork:
    def __init__(self, inputs, size, outputs):
        self.sizes = size  # for set_weights_one()
        self.input = np.zeros((inputs+1, 1))
        self.neurons = []
        self.hidden_layers = len(size)
        self.output = np.zeros((outputs, 1))
        self.weights = []
        if self.hidden_layers == 0:
            self.weights.append(np.random.rand(outputs, inputs+1))
        else:
            self.weights.append(np.random.rand(size[0], inputs+1))
            for i in range(1, self.hidden_layers):
                self.weights.append(np.random.rand(size[i], size[i - 1]+1))
            self.weights.append(np.random.rand(outputs, size[self.hidden_layers-1]+1))

    def calculate_output(self, vec):
        self.neurons = []
        self.fill_input(vec)
        self.neurons.append(self.input)
        for i in range(self.hidden_layers+1):
            layers_neuron = NeuralNetwork.calculate_layer(self.weights[i], self.neurons[i])
            if i != self.hidden_layers:
                layers_neuron = NeuralNetwork.fill_layer(layers_neuron)
            self.neurons.append(layers_neuron)
        self.output = self.neurons[self.hidden_layers+1]
        return self.output

    def fill_input(self, vec):
        for i in range(len(vec)):
            self.input[i] = vec[i]
        self.input[len(vec)] = 1

    @staticmethod
    def fill_layer(layer):
        new_layer = np.zeros((layer.size+1, 1))
        for i in range(layer.size):
            new_layer[i] = layer[i]
        new_layer[layer.size] = 1
        return new_layer

    @staticmethod
    def calculate_layer(weights, layer):
        layer_values = np.dot(weights, layer)
        layer_output = Neuron.Neuron.calculate_value(layer_values)
        return layer_output

    def set_weights_one(self):
        self.weights = []
        if self.hidden_layers == 0:
            self.weights.append(np.ones((self.output.size, self.input.size)))
        else:
            self.weights.append(np.ones((self.sizes[0], self.input.size)))
            for i in range(1, self.hidden_layers):
                self.weights.append(np.ones((self.sizes[i], self.sizes[i - 1]+1)))
            self.weights.append(np.ones((self.output.size, self.sizes[self.hidden_layers - 1]+1)))

    def train_network_svg(self, train_set, learning_rate, desire_outputs):
        sum_error = 0
        for i in range(len(train_set)):
            [weights_change, error] = self.compute_weights(train_set[i], learning_rate, desire_outputs[i])
            sum_error += error
            for layer in range(self.hidden_layers + 1):
                self.weights[layer] = np.add(self.weights[layer], weights_change[layer])
        return sum_error

    def train_network_mini_batch(self, train_set, learning_rate, desire_outputs, batch_no):
        sum_error = 0
        weights_batch = []
        for i in range(len(train_set)):
            [weights_change, error] = self.compute_weights(train_set[i], learning_rate, desire_outputs[i])
            sum_error += error
            if len(weights_batch) == 0:
                weights_batch = weights_change
            else:
                for layer in range(self.hidden_layers + 1):
                    weights_batch[layer] = np.add(weights_batch[layer], weights_change[layer])
            if (i+1) % batch_no == 0:
                for layer in range(self.hidden_layers + 1):
                    self.weights[layer] = np.add(self.weights[layer], np.divide(weights_batch[layer], batch_no))
                weights_batch = []
        if len(weights_batch) != 0:
            for l in range(self.hidden_layers + 1):
                self.weights[l] = np.add(self.weights[l], np.divide(weights_batch[l], len(train_set) % batch_no))
        return sum_error

    def compute_weights(self, vec, learning_rate, desire_output):
        # Forward propagation - outputs of layers in neurons
        self.calculate_output(vec)
        out = self.output
        sum_error = 0.5 * (sum(np.subtract(desire_output, out)**2))
        # Compute delta error of the output layer
        out_delta = np.multiply(np.subtract(desire_output, out), Neuron.Neuron.der_func(out))
        # Compute delta of the hidden layers
        next_weights = self.weights[-1]  # output layer weights
        next_delta = np.transpose(out_delta)
        hidden_delta = []
        for i in reversed(range(1, self.hidden_layers + 1)):
            inputs_nr = np.size(next_weights, 1)
            hid_lay_out = self.neurons[i]
            hid_lay_out = np.transpose(hid_lay_out[0:inputs_nr - 1, :])
            hid_lay_out = Neuron.Neuron.der_func(hid_lay_out)
            error = np.matmul(next_delta, next_weights[:, 0:inputs_nr - 1])
            hidden_delta.insert(0, np.multiply(error, hid_lay_out))
            next_weights = self.weights[i - 1]
            next_delta = hidden_delta[0]

        computed_weights_change = []
        # Output layers weights
        weights_change = np.matmul(self.neurons[-2], np.transpose(out_delta))
        weights_change = np.multiply(weights_change, learning_rate)
        computed_weights_change.insert(0, np.transpose(weights_change))

        # Hidden layers weights
        for i in reversed(range(1, self.hidden_layers + 1)):
            weights_change = np.matmul(self.neurons[i - 1], hidden_delta[i - 1])
            weights_change = np.multiply(weights_change, learning_rate)
            computed_weights_change.insert(0, np.transpose(weights_change))

        return [computed_weights_change, sum_error]
