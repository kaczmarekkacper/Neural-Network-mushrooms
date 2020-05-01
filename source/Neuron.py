import numpy as np


class Neuron:
    @staticmethod
    def count_value(vec):
        value = sum(vec) + 1
        return Neuron.func(value)

    @staticmethod
    def func(value):
        return 1 / (1 + np.e**(-value))
