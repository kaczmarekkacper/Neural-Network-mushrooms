"""
    File name: Neuron.py
    Author: Kacper Kaczmarek
    Python Version: 3.6.0
"""
import numpy as np


class Neuron:
    @staticmethod
    def count_value(vec):
        value = sum(vec)
        return Neuron.func(value)

    @staticmethod
    def func(value):
        return 1 / (1 + np.e**(-value))

    @staticmethod
    def der_func(value):
        return np.multiply(value, np.subtract(1, value))

    @staticmethod
    def calculate_value(layer_values):
        for i in range(layer_values.size):
            layer_values[i] = Neuron.func(layer_values[i])
        return layer_values


