import numpy as np
import source.Neuron as Neuron


class NeuralNetwork:
    def __init__(self, inputs, size, outputs):
        self.input = np.zeros(inputs, 1)
        self.hidden_layers = len(size)
        self.output = np.zeros(outputs, 1)
        self.weights = []
        for i in range(self.hidden_layers):
            if i == 1 and i != self.hidden_layers:
                self.weights.append(np.random.rand(size(1), inputs))
            else:
                if i != 1 and i == self.hidden_layers:
                    self.weights.append(np.random.rand(outputs, size(self.hidden_layers)))
                else:
                    if i == 1 and i == self.hidden_layers:
                        self.weights.append(np.random.rand(outputs, inputs))
                    else:
                        self.weights.append(np.random.rand(size(i), size(i-1)))
    