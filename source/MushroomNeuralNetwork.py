# -*- coding: utf-8 -*-
"""
    File name: MushroomNeuralNetwork.py
    Author: Krzysztof Kobyliński, Kacper Kaczmarek
    Python Version: 3.6.0
"""
import source.NeuralNetwork as Nn


class MushroomNeuralNetwork:
    def __init__(self, inputs, size, outputs):
        self.network = Nn.NeuralNetwork(inputs, size, outputs)

    def calculate_output(self, mushroom_set):
        for i in range(len(mushroom_set)):
            output = self.network.calculate_output(mushroom_set[i].get_normalized_vector())
            mushroom_set[i].set_prediction(output)

    def train_network_svg(self, mushroom_set, learning_rate):
        training_set = []
        labels = []
        for m in mushroom_set:
            training_set.append(m.get_normalized_vector())
            labels.append(m.edible.value)
        self.network.train_network_svg(training_set, learning_rate, labels)

    def train_network_mini_batch(self, mushroom_set, learning_rate, batch_no):
        training_set = []
        labels = []
        for m in mushroom_set:
            training_set.append(m.get_normalized_vector())
            labels.append(m.edible.value)
        self.network.train_network_mini_batch(training_set, learning_rate, labels, batch_no)
