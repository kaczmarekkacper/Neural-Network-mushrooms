import unittest
import Mushroom
import MushroomInfo as mi


class MyEdible(unittest.TestCase):
    def test_set_edibleYes(self):
        mushroom = Mushroom.Mushroom([], True)
        mushroom.set_edible("e", True)
        self.assertEqual(mushroom.edible == mi.Edible.Yes, True)

    def test_set_edibleNo(self):
        mushroom = Mushroom.Mushroom([], True)
        mushroom.set_edible("p", True)
        self.assertEqual(mushroom.edible == mi.Edible.No, True)

    def test_set_ediableNoInfo(self):
        mushroom = Mushroom.Mushroom([], True)
        mushroom.set_edible("e", False)
        self.assertEqual(mushroom.edible == mi.Edible.NoInfo, True)
        mushroom.set_edible("p", False)
        self.assertEqual(mushroom.edible == mi.Edible.NoInfo, True)

class MyEdible(unittest.TestCase):
    def test_set_edible_yes(self):
        mushroom = Mushroom.Mushroom([], True)
        mushroom.set_edible("e", True)
        self.assertEqual(mushroom.edible == mi.Edible.Yes, True)

    def test_set_edible_no(self):
        mushroom = Mushroom.Mushroom([], True)
        mushroom.set_edible("p", True)
        self.assertEqual(mushroom.edible == mi.Edible.No, True)

    def test_set_ediable_no_info(self):
        mushroom = Mushroom.Mushroom([], True)
        mushroom.set_edible("e", False)
        self.assertEqual(mushroom.edible == mi.Edible.NoInfo, True)
        mushroom.set_edible("p", False)
        self.assertEqual(mushroom.edible == mi.Edible.NoInfo, True)

    def test_set_ediable_wrong_value(self):
        mushroom = Mushroom.Mushroom([], True)
        with self.assertRaises(ValueError):
            mushroom.set_edible("b", True)


if __name__ == '__main__':
    unittest.main()
