import unittest
import source.NeuralNetwork as Nn


class TestNetworkTraining(unittest.TestCase):
    def test_init_zero_hidden(self):
        nn = Nn.NeuralNetwork(3, [2], 2)