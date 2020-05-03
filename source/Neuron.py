import numpy as np


class Neuron:
    @staticmethod
    def count_value(vec):
        value = sum(vec) + 1
        return Neuron.func(value)

    @staticmethod
    def func(value):
        return 1 / (1 + np.e**(-value))

    @staticmethod
    def calculate_value(layer_values):
        for i in range(layer_values.size):
            layer_values[i] = Neuron.func(layer_values[i])
        return layer_values


