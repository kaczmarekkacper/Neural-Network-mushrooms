import unittest
import source.NeuralNetwork as NN
import numpy as np
import source.Neuron as Neuron


class TestNNSizes(unittest.TestCase):
    def test_init_zero_hidden(self):
        nn = NN.NeuralNetwork(1, [], 1)
        self.assertEqual(nn.input.size, 1)
        self.assertEqual(nn.weights[0].size, 1)
        self.assertEqual(nn.hidden_layers, 0)
        self.assertEqual(nn.output.size, 1)

    def test_init_one_hidden(self):
        nn = NN.NeuralNetwork(1, [2], 1)
        self.assertEqual(nn.input.size, 1)
        self.assertEqual(nn.weights[0].size, 2)
        self.assertEqual(nn.weights[1].size, 2)
        self.assertEqual(nn.hidden_layers, 1)
        self.assertEqual(nn.output.size, 1)

    def test_init_two_hidden(self):
        nn = NN.NeuralNetwork(1, [2, 2], 1)
        self.assertEqual(nn.input.size, 1)
        self.assertEqual(nn.weights[0].size, 1 * 2)
        self.assertEqual(nn.weights[1].size, 2 * 2)
        self.assertEqual(nn.weights[2].size, 2)
        self.assertEqual(nn.hidden_layers, 2)
        self.assertEqual(nn.output.size, 1)

    def test_init_three_hidden(self):
        nn = NN.NeuralNetwork(1, [7, 6, 4], 1)
        self.assertEqual(nn.input.size, 1)
        self.assertEqual(nn.weights[0].size, 1 * 7)
        self.assertEqual(nn.weights[1].size, 7 * 6)
        self.assertEqual(nn.weights[2].size, 6 * 4)
        self.assertEqual(nn.weights[3].size, 4 * 1)
        self.assertEqual(nn.hidden_layers, 3)
        self.assertEqual(nn.output.size, 1)


class TestNNCalculations(unittest.TestCase):
    def test_calc_zero(self):
        nn = NN.NeuralNetwork(1, [], 1)
        nn.calculate_output([0])
        self.assertEqual(nn.output[0][0], 1/2)
        nn.set_weights_one()
        nn.calculate_output([100])
        self.assertAlmostEqual(nn.output[0][0], 1, 7)
        nn.set_weights_one()
        nn.calculate_output([-100])
        self.assertAlmostEqual(nn.output[0][0], 0, 7)

    def test_calc_one(self):
        nn = NN.NeuralNetwork(1, [1], 1)
        nn.set_weights_one()
        nn.calculate_output([0])
        value = Neuron.Neuron.func(Neuron.Neuron.func(0))
        self.assertEqual(nn.output[0][0], value)

        nn = NN.NeuralNetwork(1, [2], 1)
        nn.set_weights_one()
        nn.calculate_output([0])
        value = Neuron.Neuron.func(Neuron.Neuron.func(0)*2)
        self.assertEqual(nn.output[0][0], value)

        nn = NN.NeuralNetwork(1, [3], 1)
        nn.set_weights_one()
        nn.calculate_output([0])
        value = Neuron.Neuron.func(Neuron.Neuron.func(0) * 3)
        self.assertEqual(nn.output[0][0], value)

    def test_calc_two(self):
        nn = NN.NeuralNetwork(1, [1, 1], 1)
        nn.set_weights_one()
        nn.calculate_output([0])
        value = Neuron.Neuron.func(Neuron.Neuron.func(Neuron.Neuron.func(0)))
        self.assertEqual(nn.output[0][0], value)

        nn = NN.NeuralNetwork(1, [2, 2], 1)
        nn.set_weights_one()
        nn.calculate_output([0])
        value = Neuron.Neuron.func(2*Neuron.Neuron.func(Neuron.Neuron.func(0)*2))
        self.assertEqual(nn.output[0][0], value)

        nn = NN.NeuralNetwork(1, [3, 3], 1)
        nn.set_weights_one()
        nn.calculate_output([0])
        value = Neuron.Neuron.func(3*Neuron.Neuron.func(Neuron.Neuron.func(0)*3))
        self.assertEqual(nn.output[0][0], value)


if __name__ == '__main__':
    unittest.main()
