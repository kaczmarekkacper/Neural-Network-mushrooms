import unittest
import source.MushroomLoader as Ml
import source.Mushroom as Mushroom


class TestImportParams(unittest.TestCase):
    def test_import_mushrooms(self):
        ml = Ml.MushroomLoader('../data/agaricus-lepiota.data')
        mushrooms = None
        mushrooms = ml.import_mushrooms()
        self.assertIsNotNone(mushrooms)

    def test_import_wrong_file(self):
        ml = Ml.MushroomLoader('data/aaa.data')
        with self.assertRaises(IOError):
            mushrooms = ml.import_mushrooms()


class TestGetMushroomInList(unittest.TestCase):
    def test_import_mushrooms_length(self):
        vec = ['p', 'x', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        ml = Ml.MushroomLoader('../data/agaricus-lepiota.data')
        mushrooms = ml.import_mushrooms()
        mushroom = ml.get_mushroom_in_list(mushrooms[0])
        self.assertCountEqual(mushroom, vec)

    def test_import_mushrooms_equal(self):
        vec = ['p', 'x', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        ml = Ml.MushroomLoader('../data/agaricus-lepiota.data')
        mushrooms = ml.import_mushrooms()
        mushroom = ml.get_mushroom_in_list(mushrooms[0])
        self.assertEqual(mushroom, vec)

    def test_import_mushrooms_everything(self):
        ml = Ml.MushroomLoader('../data/agaricus-lepiota.data')
        mushrooms = ml.import_mushrooms()
        self.assertEqual(mushrooms.__len__(), 8124)


class TestCreateAMushroom(unittest.TestCase):
    def test_create_a_mushroom(self):
        vec = ['p', 'x', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        ml = Ml.MushroomLoader('../data/agaricus-lepiota.data')
        mushrooms = ml.import_mushrooms()
        mushroom = ml.get_mushroom_in_list(mushrooms[0])
        m1 = Mushroom.Mushroom(mushroom)
        m2 = Mushroom.Mushroom(vec)
        self.assertEqual(m1.edible, m2.edible)
        self.assertEqual(m1.capShape, m2.capShape)
        self.assertEqual(m1.capSurface, m2.capSurface)
        self.assertEqual(m1.capColor, m2.capColor)
        self.assertEqual(m1.bruises, m2.bruises)
        self.assertEqual(m1.odor, m2.odor)
        self.assertEqual(m1.gillAttachment, m2.gillAttachment)
        self.assertEqual(m1.gillSpacing, m2.gillSpacing)
        self.assertEqual(m1.gillSize, m2.gillSize)
        self.assertEqual(m1.gillColor, m2.gillColor)
        self.assertEqual(m1.stalkShape, m2.stalkShape)
        self.assertEqual(m1.stalkRoot, m2.stalkRoot)
        self.assertEqual(m1.stalkSurfaceAboveRing, m2.stalkSurfaceAboveRing)
        self.assertEqual(m1.stalkSurfaceBelowRing, m2.stalkSurfaceBelowRing)
        self.assertEqual(m1.stalkColorAboveRing, m2.stalkColorAboveRing)
        self.assertEqual(m1.stalkColorBelowRing, m2.stalkColorBelowRing)
        self.assertEqual(m1.veilType, m2.veilType)
        self.assertEqual(m1.veilColor, m2.veilColor)
        self.assertEqual(m1.ringNumber, m2.ringNumber)
        self.assertEqual(m1.ringType, m2.ringType)
        self.assertEqual(m1.sporePrintColor, m2.sporePrintColor)
        self.assertEqual(m1.population, m2.population)
        self.assertEqual(m1.habitat, m2.habitat)


if __name__ == '__main__':
    unittest.main()
