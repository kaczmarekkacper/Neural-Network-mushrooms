import source.NeuralNetwork as Nn


class MushroomNeuralNetwork:
    def __init__(self, inputs, size, outputs):
        self.network = Nn.NeuralNetwork(inputs, size, outputs)

    def calculate_output(self, mushroom_set):
        for i in range(len(mushroom_set)):
            output = self.network.calculate_output(mushroom_set[i].get_normalized_vector())
            mushroom_set[i].set_prediction(output)

    def train_network(self, mushroom_set, learning_rate):
        for mushroom in mushroom_set:
            self.network.train_network(mushroom.get_normalized_vector(), learning_rate, mushroom.edible.value)
