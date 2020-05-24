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

    def calculate_set(self, mushroom_set):
        for i in range(len(mushroom_set)):
            output = self.calculate_output(mushroom_set[i].get_normalized_vector())
            mushroom_set[i].set_prediction(output)

    # Dziala na liczbach
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

    def delta_batch(self, mushroom_set):
        for i in range(len(mushroom_set)):
            self.weights = self.weights
    # mushroom_set[0].get_vector()
    # mushroom_set[0].edible
    # self.weights
    # wsp.uczenia

    def delta_svg(self, mushroom_set, learning_rate):
        error = 0
        # print(self.weights[0][0][0])
        for mushroom in mushroom_set:
            desire_output = 0 if mushroom.edible == mushroom.edible.Yes else 1
            # Forward propagation - outputs of layers in neurons
            self.calculate_output(mushroom.get_normalized_vector())
            out = self.output
            error += 0.5 * (desire_output - out)**2
            # Compute delta error of the output layer
            out_delta = (desire_output - out) * Neuron.Neuron.der_func(out)
            # Compute delta of the hidden layers
            next_weights = self.weights[-1]  # output layer weights
            next_delta = out_delta
            hidden_delta = []
            # neurons - inputs, hidden1, hidden2, output (outputs)
            for l in reversed(range(1, self.hidden_layers + 1)):
                inputs_nr = np.size(next_weights, 1)
                hid_lay_out = self.neurons[l]
                hid_lay_out = np.transpose(hid_lay_out[0:inputs_nr - 1, :])
                hid_lay_out = Neuron.Neuron.der_func(hid_lay_out)
                error = np.matmul(next_delta, next_weights[:, 0:inputs_nr - 1])
                hidden_delta.insert(0, np.multiply(error, hid_lay_out))
                # weights - hidden1, hidden2, output
                next_weights = self.weights[l - 1]
                next_delta = hidden_delta[0]

            # Update output layer weights
            weights_change = np.matmul(self.neurons[-2], out_delta)
            weights_change = np.multiply(weights_change, learning_rate)
            self.weights[-1] += np.transpose(weights_change)

            # Update hidden layers weights
            for l in reversed(range(1, self.hidden_layers + 1)):
                weights_change = np.matmul(self.neurons[l - 1], hidden_delta[l - 1])
                weights_change = np.multiply(weights_change, learning_rate)
                # Debugging
                # if l - 1 == 0:
                #     print("Change {}".format(np.transpose(weights_change)[0][0]))
                self.weights[l - 1] += np.transpose(weights_change)
        # print(self.weights[0][0])
        return error


