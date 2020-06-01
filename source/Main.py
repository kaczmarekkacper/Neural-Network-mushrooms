"""
    File name: Main.py
    Author: Kacper Kaczmarek
    Python Version: 3.6.0
"""
import MushroomLoader as Ml
import Mushroom as Mushroom
import MushroomInfo as Mi
import MushroomNeuralNetwork as Mnn
import random
import sys
import matplotlib.pyplot as plt
import numpy as np
import time

input_number = 22
output_number = 1


def main():
    layers = eval(sys.argv[1])
    epochs = eval(sys.argv[2])
    learning_rate = eval(sys.argv[3])
    method = sys.argv[4]
    if method == "batch":
        batch_no = eval(sys.argv[5])
    else:
        batch_no = 0
    ml = Ml.MushroomLoader('../data/agaricus-lepiota.data')
    im = ml.import_mushrooms()
    mushrooms = make_mushrooms(ml, im)
    Mushroom.Mushroom.set_std_and_mean_values(mushrooms)
    edible_mushrooms, poisonous_mushrooms = split_poisonous(mushrooms)
    results_matrix = []

    # launch 10 times
    for iteration in range(10):
        # Shuffle data again, another initial weights in neural network
        training_set, validation_set = make_sets(edible_mushrooms, poisonous_mushrooms)
        mnn = Mnn.MushroomNeuralNetwork(input_number, layers, output_number)
        train_err = []
        valid_err = []
        # Initial error
        mnn.calculate_output(training_set)
        mnn.calculate_output(validation_set)
        [train_per, valid_per] = print_stats(training_set, validation_set)
        train_err.append(100 - train_per)
        valid_err.append(100 - valid_per)
        start = []
        stop = []

        # Learning
        for i in range(epochs):
            start.append(time.time())
            if method == "svg":
                mnn.train_network_svg(training_set, learning_rate)
            elif method == "batch":
                mnn.train_network_mini_batch(training_set, learning_rate, batch_no)
            else:
                raise Exception("Method name should be 'svg' or 'batch'")
            stop.append(time.time())
            mnn.calculate_output(training_set)
            mnn.calculate_output(validation_set)
            [train_per, valid_per] = print_stats(training_set, validation_set)
            train_err.append(100 - train_per)
            valid_err.append(100 - valid_per)
            if valid_per == 100:
                break

        r_epochs = len(train_err)
        # Last train error, last test error, number of epochs, time per epoch
        results_matrix.append([train_err[r_epochs - 1], valid_err[r_epochs - 1], r_epochs, np.mean(np.subtract(stop, start))])
        t = np.arange(0., r_epochs, 1.)
        plt.plot(t, train_err, t, valid_err)
        # plt.xticks(np.arange(min(t), max(t) + 1, 1.0))
        plt.xlabel('Epoch of learning')
        plt.ylabel('Classification error [%]')
        plt.legend(['Train error', 'Test error'])
        plt.savefig('../results/{}_e{}_lr{}_{}_bno_{}_{}.png'.format(layers, epochs, learning_rate, method, batch_no, iteration))
        plt.show()
        plt.close('all')
    output = open('../results/{}_e{}_lr{}_{}_bno_{}.txt'.format(layers, epochs, learning_rate, method, batch_no), "w")
    output.write(str(results_matrix) + '\n')
    output.write(str(np.mean(results_matrix, axis=0)) + '\n')
    output.close()


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
    format_train_per = "{:.2f}".format(training_percent)
    print("Training: There are " + str(correct) + " correct predictions from "
          + str(len(training_set)) + " mushrooms (" + str(format_train_per) + "%).")

    correct = 0
    for i in range(len(validation_set)):
        if validation_set[i].check_prediction():
            correct = correct + 1
    validation_percent = correct/len(validation_set)*100
    format_val_per = "{:.2f}".format(validation_percent)
    print("Validation: There are " + str(correct) + " correct predictions from "
          + str(len(validation_set)) + " mushrooms (" + str(format_val_per) + "%).")

    return training_percent, validation_percent


if __name__ == "__main__":
    main()
