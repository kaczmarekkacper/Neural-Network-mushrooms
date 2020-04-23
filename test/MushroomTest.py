import unittest
import source.Mushroom as Mushroom
import source.MushroomInfo as Mi


class TestSetEdible(unittest.TestCase):
    def test_set_edible_yes(self):
        vec = ['e', 'x', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec, True)
        self.assertEqual(mushroom.edible == Mi.Edible.Yes, True)

    def test_set_edible_no(self):
        vec = ['p', 'x', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec, True)
        self.assertEqual(mushroom.edible == Mi.Edible.No, True)

    def test_set_ediable_noinfo(self):
        vec = ['e', 'x', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec, False)
        self.assertEqual(mushroom.edible == Mi.Edible.NoInfo, True)

        vec = ['p', 'x', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec, False)
        self.assertEqual(mushroom.edible == Mi.Edible.NoInfo, True)

    def test_set_edible_wrong_value(self):
        vec = ['g', 'x', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        with self.assertRaises(ValueError):
            Mushroom.Mushroom(vec, True)


class TestSetCapShape(unittest.TestCase):
    def test_set_capshape_bell(self):
        vec = ['p', 'b', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec, True)
        self.assertEqual(mushroom.capShape == Mi.CapShape.Bell, True)

    def test_set_capshape_conical(self):
        vec = ['p', 'c', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec, True)
        self.assertEqual(mushroom.capShape == Mi.CapShape.Conical, True)

    def test_set_capshape_convex(self):
        vec = ['p', 'x', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec, True)
        self.assertEqual(mushroom.capShape == Mi.CapShape.Convex, True)

    def test_set_capshape_flat(self):
        vec = ['p', 'f', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec, True)
        self.assertEqual(mushroom.capShape == Mi.CapShape.Flat, True)

    def test_set_capshape_knobbed(self):
        vec = ['p', 'k', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec, True)
        self.assertEqual(mushroom.capShape == Mi.CapShape.Knobbed, True)

    def test_set_capshape_sunken(self):
        vec = ['p', 's', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec, True)
        self.assertEqual(mushroom.capShape == Mi.CapShape.Sunken, True)

    def test_set_capshape_wrong_value(self):
        vec = ['p', 'g', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        with self.assertRaises(ValueError):
            Mushroom.Mushroom(vec, True)


class TestSetCapsurface(unittest.TestCase):
    def test_set_capsurface_fibrous(self):
        vec = ['p', 'b', 'f', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec, True)
        self.assertEqual(mushroom.capSurface == Mi.CapSurface.Fibrous, True)

    def test_set_capsurface_grooves(self):
        vec = ['p', 'c', 'g', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec, True)
        self.assertEqual(mushroom.capSurface == Mi.CapSurface.Grooves, True)

    def test_set_capsurface_scaly(self):
        vec = ['p', 'x', 'y', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec, True)
        self.assertEqual(mushroom.capSurface == Mi.CapSurface.Scaly, True)

    def test_set_capsurface_smooth(self):
        vec = ['p', 'f', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec, True)
        self.assertEqual(mushroom.capSurface == Mi.CapSurface.Smooth, True)

    def test_set_capsurface_wrong_value(self):
        vec = ['p', 'g', 'b', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        with self.assertRaises(ValueError):
            Mushroom.Mushroom(vec, True)

class TestSetCapColor(unittest.TestCase):
    def test_set_capcolor_brown(self):
        vec = ['p', 'b', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec, True)
        self.assertEqual(mushroom.capColor == Mi.CapColor.Brown, True)

    def test_set_capcolor_buff(self):
        vec = ['p', 'c', 's', 'b', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec, True)
        self.assertEqual(mushroom.capColor == Mi.CapColor.Buff, True)

    def test_set_capcolor_cinnamon(self):
        vec = ['p', 'x', 's', 'c', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec, True)
        self.assertEqual(mushroom.capColor == Mi.CapColor.Cinnamon, True)

    def test_set_capcolor_gray(self):
        vec = ['p', 'f', 's', 'g', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec, True)
        self.assertEqual(mushroom.capColor == Mi.CapColor.Gray, True)

    def test_set_capcolor_green(self):
        vec = ['p', 'k', 's', 'r', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec, True)
        self.assertEqual(mushroom.capColor == Mi.CapColor.Green, True)

    def test_set_capcolor_pink(self):
        vec = ['p', 's', 's', 'p', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec, True)
        self.assertEqual(mushroom.capColor == Mi.CapColor.Pink, True)

    def test_set_capcolor_purple(self):
        vec = ['p', 'b', 's', 'u', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec, True)
        self.assertEqual(mushroom.capColor == Mi.CapColor.Purple, True)

    def test_set_capcolor_red(self):
        vec = ['p', 'c', 's', 'e', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec, True)
        self.assertEqual(mushroom.capColor == Mi.CapColor.Red, True)

    def test_set_capcolor_white(self):
        vec = ['p', 'x', 's', 'w', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec, True)
        self.assertEqual(mushroom.capColor == Mi.CapColor.White, True)

    def test_set_capcolor_yellow(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec, True)
        self.assertEqual(mushroom.capColor == Mi.CapColor.Yellow, True)

    def test_set_capcolor_wrong_value(self):
        vec = ['p', 'g', 's', 'f', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        with self.assertRaises(ValueError):
            Mushroom.Mushroom(vec, True)


class TestSetBruises(unittest.TestCase):
    def test_set_bruices_yes(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec, True)
        self.assertEqual(mushroom.bruises == Mi.Bruises.Yes, True)

    def test_set_bruices_no(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec, True)
        self.assertEqual(mushroom.bruises == Mi.Bruises.No, True)


if __name__ == '__main__':
    unittest.main()
