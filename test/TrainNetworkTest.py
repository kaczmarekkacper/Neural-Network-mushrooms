"""
    File name: TrainNetworkTest.py
    Author: Krzysztof Kobyliński
    Python Version: 3.6.0
"""
import unittest
import source.NeuralNetwork as Nn
import numpy as np


class TestNetworkTraining(unittest.TestCase):
    def test_back_propagation_svg(self):
        nn = Nn.NeuralNetwork(3, [2], 2)
        desire = np.asarray([[[0.1], [0.05]]])
        x = np.asarray([[1, 4, 5]])
        self.set_network_weights(nn)

        out1 = nn.calculate_output(x[0])
        self.assertEqual(out1[0][0], 0.8288270126411345)
        self.assertEqual(out1[1][0], 0.707169973572705)
        nn.train_network_svg(x, 0.9, desire)
        out2 = nn.calculate_output(x[0])
        self.assertEqual(out2[0][0], 0.7860654588268334)
        self.assertEqual(out2[1][0], 0.6269588539666903)

    def test_back_propagation_mini_batch_1(self):
        nn = Nn.NeuralNetwork(3, [2], 2)
        desire = np.asarray([[[0.1], [0.05]],
                             [[0.2], [0.1]],
                             [[0.3], [0.15]],
                             [[0.4], [0.2]],
                             [[0.5], [0.25]]])

        x = np.asarray([[1, 4, 5],
                        [2, 2, 2],
                        [7, 8, 1],
                        [8, 8, 8],
                        [1, 2, 1]])
        self.set_network_weights(nn)

        out1 = nn.calculate_output(x[0])
        self.assertEqual(out1[0][0], 0.8288270126411345)
        self.assertEqual(out1[1][0], 0.707169973572705)
        nn.train_network_mini_batch(x, 0.9, desire, 2)
        out2 = nn.calculate_output(x[1])
        self.assertEqual(out2[0][0], 0.7082007164237192)
        self.assertEqual(out2[1][0], 0.5058618164355518)

    @staticmethod
    def set_network_weights(nn):
        nn.weights[0][0, 0] = 0.1
        nn.weights[0][0, 1] = 0.3
        nn.weights[0][0, 2] = 0.5
        nn.weights[0][0, 3] = 0

        nn.weights[0][1, 0] = 0.2
        nn.weights[0][1, 1] = 0.4
        nn.weights[0][1, 2] = 0.6
        nn.weights[0][1, 3] = 0

        nn.weights[1][0, 0] = 0.7
        nn.weights[1][0, 1] = 0.9
        nn.weights[1][0, 2] = 0

        nn.weights[1][1, 0] = 0.8
        nn.weights[1][1, 1] = 0.1
        nn.weights[1][1, 2] = 0
