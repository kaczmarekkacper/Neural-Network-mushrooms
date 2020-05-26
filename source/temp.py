import source.MushroomLoader as Ml
import source.Mushroom as Mushroom
import source.MushroomInfo as Mi
import source.MushroomNeuralNetwork as Mnn
import random
import sys
import numpy as np


def make_mushrooms(ml, im):
    mushrooms = []
    for i in range(len(im)):
        m = Mushroom.Mushroom(ml.get_mushroom_in_list(im[i]))
        mushrooms.append(m)
    return mushrooms


input_number = 22
output_number = 1

layers = [5]
ml = Ml.MushroomLoader('../data/agaricus-lepiota.data')
im = ml.import_mushrooms()
mushrooms = make_mushrooms(ml, im)

mushrooms_set = []
# mushrooms_set.append([1, 2, 3])
# mushrooms_set.append([4, 5, 6])
# print(mushrooms_set)

# for m in mushrooms:
#     mushrooms_set.append(m.get_vector())

# print(mushrooms_set)

a = [0, 1, 2]
b = [0, 1, 2]
b = np.array(b, dtype=float)

c = np.divide(a, b, out=np.zeros_like(b), where=b != 0)
print(c)
# std = np.std(mushrooms_set, axis=0)
# mean = np.mean(mushrooms_set, axis=0)
# print(std)
# print(mean)
