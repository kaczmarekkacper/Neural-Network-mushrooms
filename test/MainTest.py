import unittest
import source.MushroomLoader as Ml
import source.Main as Main


NUMBER_OF_MUSHROOMS = 8124
NUMBER_OF_POISONOUS = 3916
NUMBER_OF_EDIBLE = 4208


class TestMain(unittest.TestCase):
    def test_making_mushrooms(self):
        ml = Ml.MushroomLoader('../data/agaricus-lepiota.data')
        im = ml.import_mushrooms()
        mushrooms = Main.make_mushrooms(ml, im)
        self.assertEqual(mushrooms.__len__(), NUMBER_OF_MUSHROOMS)

    def test_split_mushrooms_edible(self):
        ml = Ml.MushroomLoader('../data/agaricus-lepiota.data')
        im = ml.import_mushrooms()
        mushrooms = Main.make_mushrooms(ml, im)
        edible_mushrooms, poisonous_mushrooms = Main.split_poisonous(mushrooms)
        self.assertEqual(edible_mushrooms.__len__(), NUMBER_OF_EDIBLE)

    def test_split_mushrooms_poisonous(self):
        ml = Ml.MushroomLoader('../data/agaricus-lepiota.data')
        im = ml.import_mushrooms()
        mushrooms = Main.make_mushrooms(ml, im)
        edible_mushrooms, poisonous_mushrooms = Main.split_poisonous(mushrooms)
        self.assertEqual(poisonous_mushrooms.__len__(), NUMBER_OF_POISONOUS)

    def test_make_sets_training_len(self):
        ml = Ml.MushroomLoader('../data/agaricus-lepiota.data')
        im = ml.import_mushrooms()
        mushrooms = Main.make_mushrooms(ml, im)
        edible_mushrooms, poisonous_mushrooms = Main.split_poisonous(mushrooms)
        training_set, validation_set = Main.make_sets(edible_mushrooms, poisonous_mushrooms)
        self.assertEqual(training_set.__len__(), NUMBER_OF_MUSHROOMS/2)

    def test_make_sets_validation_len(self):
        ml = Ml.MushroomLoader('../data/agaricus-lepiota.data')
        im = ml.import_mushrooms()
        mushrooms = Main.make_mushrooms(ml, im)
        edible_mushrooms, poisonous_mushrooms = Main.split_poisonous(mushrooms)
        training_set, validation_set = Main.make_sets(edible_mushrooms, poisonous_mushrooms)
        self.assertEqual(validation_set.__len__(), NUMBER_OF_MUSHROOMS/2)


if __name__ == '__main__':
    unittest.main()
