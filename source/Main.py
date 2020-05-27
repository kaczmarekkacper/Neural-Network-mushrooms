"""
    File name: Main.py
    Author: Kacper Kaczmarek
    Python Version: 3.6.0
"""
import source.MushroomLoader as Ml
import source.Mushroom as Mushroom
import source.MushroomInfo as Mi
import source.MushroomNeuralNetwork as Mnn
import random
import sys

input_number = 22
output_number = 1


def main():
    layers = eval(sys.argv[1])
    epochs = eval(sys.argv[2])
    method = sys.argv[3]
    learning_rate = 0.9
    if method == "batch":
        batch_no = eval(sys.argv[4])
    ml = Ml.MushroomLoader('../data/agaricus-lepiota.data')
    im = ml.import_mushrooms()
    mushrooms = make_mushrooms(ml, im)
    Mushroom.Mushroom.set_std_and_mean_values(mushrooms)
    edible_mushrooms, poisonous_mushrooms = split_poisonous(mushrooms)
    training_set, validation_set = make_sets(edible_mushrooms, poisonous_mushrooms)
    mnn = Mnn.MushroomNeuralNetwork(input_number, layers, output_number)
    for i in range(epochs):
        if method == "svg":
            mnn.train_network_svg(training_set, learning_rate)
        elif method == "batch":
            mnn.train_network_mini_batch(training_set, learning_rate, batch_no)
        else:
            raise Exception("Method name should be 'svg' or 'batch'")
        mnn.calculate_output(training_set)
        mnn.calculate_output(validation_set)
        [train_per, valid_per] = print_stats(training_set, validation_set)
        if valid_per == 100:
            break


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
    training_percent = correct/len(training_set)*100
    print("Training: There are " + str(correct) + " correct predictions from "
          + str(len(training_set)) + " mushrooms (" + str(training_percent) + "%).")

    correct = 0
    for i in range(len(validation_set)):
        if validation_set[i].check_prediction():
            correct = correct + 1
    validation_percent = correct/len(validation_set)*100
    print("Validation: There are " + str(correct) + " correct predictions from "
          + str(len(validation_set)) + " mushrooms (" + str(validation_percent) + "%).")

    return training_percent, validation_percent


if __name__ == "__main__":
    main()
