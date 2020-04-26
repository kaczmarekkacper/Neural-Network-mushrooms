import unittest
import source.MushroomLoader as Ml
import source.Main as Main


class TestMain(unittest.TestCase):
    def test_making_mushrooms(self):
        ml = Ml.MushroomLoader('../data/agaricus-lepiota.data')
        im = ml.import_mushrooms()
        mushrooms = Main.make_mushrooms(ml, im)
        self.assertEqual(mushrooms.__len__(), 8124)

    def test_split_mushrooms_edible(self):
        ml = Ml.MushroomLoader('../data/agaricus-lepiota.data')
        im = ml.import_mushrooms()
        mushrooms = Main.make_mushrooms(ml, im)
        edible_mushrooms, poisonous_mushrooms = Main.split_poisonous(mushrooms)
        self.assertEqual(edible_mushrooms.__len__(), 4208)

    def test_split_mushrooms_poisonous(self):
        ml = Ml.MushroomLoader('../data/agaricus-lepiota.data')
        im = ml.import_mushrooms()
        mushrooms = Main.make_mushrooms(ml, im)
        edible_mushrooms, poisonous_mushrooms = Main.split_poisonous(mushrooms)
        self.assertEqual(poisonous_mushrooms.__len__(), 3916)

    def test_make_sets_training_len(self):
        ml = Ml.MushroomLoader('../data/agaricus-lepiota.data')
        im = ml.import_mushrooms()
        mushrooms = Main.make_mushrooms(ml, im)
        edible_mushrooms, poisonous_mushrooms = Main.split_poisonous(mushrooms)
        training_set, validation_set = Main.make_sets(edible_mushrooms, poisonous_mushrooms)
        self.assertEqual(training_set.__len__(), 8124/2)

    def test_make_sets_validation_len(self):
        ml = Ml.MushroomLoader('../data/agaricus-lepiota.data')
        im = ml.import_mushrooms()
        mushrooms = Main.make_mushrooms(ml, im)
        edible_mushrooms, poisonous_mushrooms = Main.split_poisonous(mushrooms)
        training_set, validation_set = Main.make_sets(edible_mushrooms, poisonous_mushrooms)
        self.assertEqual(validation_set.__len__(), 8124/2)


if __name__ == '__main__':
    unittest.main()
