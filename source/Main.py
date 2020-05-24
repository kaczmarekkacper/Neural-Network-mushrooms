import source.MushroomLoader as Ml
import source.Mushroom as Mushroom
import source.MushroomInfo as Mi
import source.MushroomNeuralNetwork as Mnn
import random
import sys

input_number = 22
output_number = 1


def main():
    layers = load_layers()
    ml = Ml.MushroomLoader('../data/agaricus-lepiota.data')
    im = ml.import_mushrooms()
    mushrooms = make_mushrooms(ml, im)
    edible_mushrooms, poisonous_mushrooms = split_poisonous(mushrooms)
    training_set, validation_set = make_sets(edible_mushrooms, poisonous_mushrooms)
    mnn = Mnn.MushroomNeuralNetwork(input_number, layers, output_number)
    for i in range(10):
        mnn.train_network(training_set, 0.9)
        mnn.calculate_output(training_set)
        mnn.calculate_output(validation_set)
        print_stats(training_set, validation_set)


def load_layers():
    layers = []
    layers_arg = eval(sys.argv[1])
    for i in range(len(layers_arg)):
        layers.append(int(layers_arg[i]))
    return layers


def make_mushrooms(ml, im):
    mushrooms = []
    for i in range(len(im)):
        m = Mushroom.Mushroom(ml.get_mushroom_in_list(im[i]))
        mushrooms.append(m)
    return mushrooms


def split_poisonous(mushrooms):
    edible_mushrooms = []
    poisonous_mushrooms = []
    for i in range(len(mushrooms)):
        if mushrooms[i].edible == Mi.Edible.Yes:
            edible_mushrooms.append(mushrooms[i])
        else:
            poisonous_mushrooms.append(mushrooms[i])
    return edible_mushrooms, poisonous_mushrooms


def make_sets(edible_mushrooms, poisonous_mushrooms):
    training_set = []
    validation_set = []
    number_of_edible = len(edible_mushrooms)
    edible_half = round(number_of_edible / 2)
    number_of_poisonous = len(poisonous_mushrooms)
    poisonous_half = round(number_of_poisonous / 2)

    # shuffle mushrooms
    random.shuffle(edible_mushrooms)
    random.shuffle(poisonous_mushrooms)

    # split edible
    for i in range(edible_half):
        training_set.append(edible_mushrooms[i])
    for i in range(edible_half, len(edible_mushrooms)):
        validation_set.append(edible_mushrooms[i])

    # split poisonous
    for i in range(poisonous_half):
        training_set.append(poisonous_mushrooms[i])
    for i in range(poisonous_half, len(poisonous_mushrooms)):
        validation_set.append(poisonous_mushrooms[i])

    # shuffle sets
    random.shuffle(training_set)
    random.shuffle(validation_set)
    return training_set, validation_set


def print_stats(training_set, validation_set):
    correct = 0
    for i in range(len(training_set)):
        if training_set[i].check_prediction():
            correct = correct + 1
    print("Training: There are " + str(correct) + " correct predictions from "
          + str(len(training_set)) + " mushrooms (" + str(correct/len(training_set)*100) + "%).")

    correct = 0
    for i in range(len(validation_set)):
        if validation_set[i].check_prediction():
            correct = correct + 1
    print("Validation: There are " + str(correct) + " correct predictions from "
          + str(len(validation_set)) + " mushrooms (" + str(correct/len(validation_set)*100) + "%).")


if __name__ == "__main__":
    main()
