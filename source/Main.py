import source.MushroomLoader as Ml
import source.Mushroom as Mushroom
import source.MushroomInfo as Mi
import source.NeuralNetwork as Nn
import numpy as np
import random

input_number = 22
output_number = 1


def main():
    ml = Ml.MushroomLoader('../data/agaricus-lepiota.data')
    im = ml.import_mushrooms()
    mushrooms = make_mushrooms(ml, im)
    edible_mushrooms, poisonous_mushrooms = split_poisonous(mushrooms)
    training_set, validation_set = make_sets(edible_mushrooms, poisonous_mushrooms)
    nn = Nn.NeuralNetwork(input_number, [3, 2], output_number)
    training_arr = set_to_array(training_set)


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


def set_to_array(mushroom_set):
    arr = np.empty((len(mushroom_set), input_number))
    for i in range(len(mushroom_set)):
        vec = mushroom_set[i].get_vector()
        arr[i] = np.array(vec)
    return arr


if __name__ == "__main__":
    main()
