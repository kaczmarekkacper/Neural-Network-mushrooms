import source.MushroomLoader as Ml
import source.Mushroom as Mushroom
import source.MushroomInfo as Mi
import source.NeuralNetwork as Nn
import numpy as np
import random
import sys


def main():
    input_number, layers, output_number, method = load_params()
    ml = Ml.MushroomLoader('../data/agaricus-lepiota.data')
    im = ml.import_mushrooms()
    mushrooms = make_mushrooms(ml, im)
    edible_mushrooms, poisonous_mushrooms = split_poisonous(mushrooms)
    training_set, validation_set = make_sets(edible_mushrooms, poisonous_mushrooms)
    nn = Nn.NeuralNetwork(input_number, layers, output_number)
    if method:
        nn.delta_svg(training_set)
    else:
        nn.delta_batch(training_set)
    nn.calculate_set(validation_set)
    print_stats(validation_set)
    #save_mushrooms(validation_set)


def load_params():
    if len(sys.argv) != 5:
        exit(1)
    input_number = int(sys.argv[1])
    layers = []
    second_arg = eval(sys.argv[2])
    for i in range(len(second_arg)):
        layers.append(int(second_arg[i]))
    output_number = int(sys.argv[3])
    method = 0
    if sys.argv[4] == 'batch':
        method = 0
    else:
        if sys.argv[4] == 'svg':
            method = 1
        else:
            exit(2)
    return input_number, layers, output_number, method


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


def print_stats(mushroom_set):
    correct = 0
    for i in range(len(mushroom_set)):
        if mushroom_set[i].check_prediction():
            correct = correct + 1
    print("There are " + str(correct) + " correct predictions from " + str(len(mushroom_set)) + " mushrooms (" + str(correct/len(mushroom_set)*100) + "%).")


def save_mushrooms(mushroom_set):
    mushroom_set = mushroom_set


if __name__ == "__main__":
    main()
