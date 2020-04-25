import source.MushroomLoader as Ml
import source.Mushroom as Mushroom
import source.MushroomInfo as Mi
import random


def main():
    ml = Ml.MushroomLoader('../data/agaricus-lepiota.data')
    im = ml.import_mushrooms()
    mushrooms = make_mushrooms(ml, im)
    edible_mushrooms, poisonous_mushrooms = split_poisonous(mushrooms)
    training_set, validation_set = make_sets(edible_mushrooms, poisonous_mushrooms)


def split_poisonous(mushrooms):
    edible_mushrooms = []
    poisonous_mushrooms = []
    for i in range(len(mushrooms)):
        if mushrooms[i].edible == Mi.Edible.Yes:
            edible_mushrooms.append(mushrooms[i])
        else:
            poisonous_mushrooms.append(mushrooms[i])
    return edible_mushrooms, poisonous_mushrooms


def make_mushrooms(ml, im):
    mushrooms = []
    for i in range(len(im)):
        m = Mushroom.Mushroom(ml.get_mushroom_in_list(im[i]))
        mushrooms.append(m)
    return mushrooms


def make_sets(edible_mushrooms, poisonous_mushrooms):
    training_set = []
    validation_set = []
    random.shuffle(edible_mushrooms)
    edible_half = round(len(edible_mushrooms)/2)
    random.shuffle(poisonous_mushrooms)
    poisonous_half = round(len(poisonous_mushrooms)/2)
    # split edible
    for i in range(edible_half):
        edible_mushrooms[i].set_edible_no_info()
        training_set.append(edible_mushrooms[i])
    for i in range(edible_half, len(edible_mushrooms)-1):
        validation_set.append(edible_mushrooms[i])
    # split poisonous
    for i in range(poisonous_half):
        poisonous_mushrooms[i].set_edible_no_info()
        training_set.append(poisonous_mushrooms[i])
    for i in range(poisonous_half, len(poisonous_mushrooms)-1):
        validation_set.append(poisonous_mushrooms[i])
    return training_set, validation_set


if __name__ == "__main__":
    main()
