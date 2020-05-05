import unittest
import source.Mushroom as Mushroom
import source.MushroomInfo as Mi


class TestGetVector(unittest.TestCase):
    def test_getVector(self):
        vec = ['e', 'x', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        vec = [3, 4, 1, 1, 8, 3, 1, 2, 1, 1, 4, 4, 4, 8, 8, 1, 3, 2, 6, 1, 4, 5]
        self.assertListEqual(mushroom.get_vector(), vec)


class TestSetEdible(unittest.TestCase):
    def test_set_edible_yes(self):
        vec = ['e', 'x', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.edible == Mi.Edible.Yes, True)

    def test_set_edible_no(self):
        vec = ['p', 'x', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.edible == Mi.Edible.No, True)

    def test_set_edible_wrong_value(self):
        vec = ['g', 'x', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        with self.assertRaises(ValueError):
            Mushroom.Mushroom(vec)


class TestSetCapShape(unittest.TestCase):
    def test_set_capshape_bell(self):
        vec = ['p', 'b', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.capShape == Mi.CapShape.Bell, True)

    def test_set_capshape_conical(self):
        vec = ['p', 'c', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.capShape == Mi.CapShape.Conical, True)

    def test_set_capshape_convex(self):
        vec = ['p', 'x', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.capShape == Mi.CapShape.Convex, True)

    def test_set_capshape_flat(self):
        vec = ['p', 'f', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.capShape == Mi.CapShape.Flat, True)

    def test_set_capshape_knobbed(self):
        vec = ['p', 'k', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.capShape == Mi.CapShape.Knobbed, True)

    def test_set_capshape_sunken(self):
        vec = ['p', 's', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.capShape == Mi.CapShape.Sunken, True)

    def test_set_capshape_wrong_value(self):
        vec = ['p', 'g', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        with self.assertRaises(ValueError):
            Mushroom.Mushroom(vec)


class TestSetCapSurface(unittest.TestCase):
    def test_set_cap_surface_fibrous(self):
        vec = ['p', 'b', 'f', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.capSurface == Mi.CapSurface.Fibrous, True)

    def test_set_cap_surface_grooves(self):
        vec = ['p', 'c', 'g', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.capSurface == Mi.CapSurface.Grooves, True)

    def test_set_cap_surface_scaly(self):
        vec = ['p', 'x', 'y', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.capSurface == Mi.CapSurface.Scaly, True)

    def test_set_cap_surface_smooth(self):
        vec = ['p', 'f', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.capSurface == Mi.CapSurface.Smooth, True)

    def test_set_cap_surface_wrong_value(self):
        vec = ['p', 's', 'b', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        with self.assertRaises(ValueError):
            Mushroom.Mushroom(vec)


class TestSetCapColor(unittest.TestCase):
    def test_set_cap_color_brown(self):
        vec = ['p', 'b', 's', 'n', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.capColor == Mi.CapColor.Brown, True)

    def test_set_cap_color_buff(self):
        vec = ['p', 'c', 's', 'b', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.capColor == Mi.CapColor.Buff, True)

    def test_set_cap_color_cinnamon(self):
        vec = ['p', 'x', 's', 'c', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.capColor == Mi.CapColor.Cinnamon, True)

    def test_set_cap_color_gray(self):
        vec = ['p', 'f', 's', 'g', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.capColor == Mi.CapColor.Gray, True)

    def test_set_cap_color_green(self):
        vec = ['p', 'k', 's', 'r', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.capColor == Mi.CapColor.Green, True)

    def test_set_cap_color_pink(self):
        vec = ['p', 's', 's', 'p', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.capColor == Mi.CapColor.Pink, True)

    def test_set_cap_color_purple(self):
        vec = ['p', 'b', 's', 'u', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.capColor == Mi.CapColor.Purple, True)

    def test_set_cap_color_red(self):
        vec = ['p', 'c', 's', 'e', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.capColor == Mi.CapColor.Red, True)

    def test_set_cap_color_white(self):
        vec = ['p', 'x', 's', 'w', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.capColor == Mi.CapColor.White, True)

    def test_set_cap_color_yellow(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.capColor == Mi.CapColor.Yellow, True)

    def test_set_cap_color_wrong_value(self):
        vec = ['p', 'g', 's', 'f', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        with self.assertRaises(ValueError):
            Mushroom.Mushroom(vec)


class TestSetBruises(unittest.TestCase):
    def test_set_bruices_yes(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.bruises == Mi.Bruises.Yes, True)

    def test_set_bruices_no(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec,)
        self.assertEqual(mushroom.bruises == Mi.Bruises.No, True)

    def test_set_bruices_wrong_value(self):
        vec = ['p', 'k', 's', 'y', 'g', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        with self.assertRaises(ValueError):
            Mushroom.Mushroom(vec)


class TestSetOdor(unittest.TestCase):
    def test_set_odor_almond(self):
        vec = ['p', 'b', 's', 'n', 't', 'a', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.odor == Mi.Odor.Almond, True)

    def test_set_odor_anise(self):
        vec = ['p', 'c', 's', 'b', 't', 'l', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.odor == Mi.Odor.Anise, True)

    def test_set_odor_creosote(self):
        vec = ['p', 'x', 's', 'c', 't', 'c', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.odor == Mi.Odor.Creosote, True)

    def test_set_odor_fishy(self):
        vec = ['p', 'f', 's', 'g', 't', 'y', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.odor == Mi.Odor.Fishy, True)

    def test_set_odor_foul(self):
        vec = ['p', 'k', 's', 'r', 't', 'f', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.odor == Mi.Odor.Foul, True)

    def test_set_odor_musty(self):
        vec = ['p', 's', 's', 'p', 't', 'm', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.odor == Mi.Odor.Musty, True)

    def test_set_odor_without(self):
        vec = ['p', 'b', 's', 'u', 't', 'n', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.odor == Mi.Odor.Without, True)

    def test_set_odor_pungent(self):
        vec = ['p', 'c', 's', 'e', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.odor == Mi.Odor.Pungent, True)

    def test_set_odor_spicy(self):
        vec = ['p', 'x', 's', 'w', 't', 's', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.odor == Mi.Odor.Spicy, True)

    def test_set_odor_wrong_value(self):
        vec = ['p', 'g', 's', 'f', 't', 'b', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        with self.assertRaises(ValueError):
            Mushroom.Mushroom(vec)


class TestSetGillAttachment(unittest.TestCase):
    def test_set_gill_attachment_attached(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.gillAttachment == Mi.GillAttachment.Attached, True)

    def test_set_gill_attachment_descending(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.gillAttachment == Mi.GillAttachment.Descending, True)

    def test_set_gill_attachment_free(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'f', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.gillAttachment == Mi.GillAttachment.Free, True)

    def test_set_gill_attachment_nothced(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'n', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.gillAttachment == Mi.GillAttachment.Notched, True)

    def test_set_gill_attachment_wrong_value(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'b', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        with self.assertRaises(ValueError):
            Mushroom.Mushroom(vec)


class TestSetGillSpacing(unittest.TestCase):
    def test_set_gill_spacing_close(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.gillSpacing == Mi.GillSpacing.Close, True)

    def test_set_gill_spacing_crowded(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.gillSpacing == Mi.GillSpacing.Crowded, True)

    def test_set_gill_spacing_distant(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'f', 'd', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.gillSpacing == Mi.GillSpacing.Distant, True)

    def test_set_gill_spacing_wrong_value(self):
        vec = ['p', 'k', 's', 'y', 't', 'p', 'n', 'b', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        with self.assertRaises(ValueError):
            Mushroom.Mushroom(vec)


class TestSetGillSize(unittest.TestCase):
    def test_set_gill_size_broad(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'b', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.gillSize == Mi.GillSize.Broad, True)

    def test_set_gill_size_narrow(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.gillSize == Mi.GillSize.Narrow, True)

    def test_set_gill_spacing_wrong_value(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'n', 'd', 'g', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        with self.assertRaises(ValueError):
            Mushroom.Mushroom(vec)


class TestSetGillColor(unittest.TestCase):
    def test_set_gill_color_black(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.gillColor == Mi.GillColor.Black, True)

    def test_set_gill_color_brown(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.gillColor == Mi.GillColor.Brown, True)

    def test_set_gill_color_buff(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'f', 'd', 'n', 'b',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.gillColor == Mi.GillColor.Buff, True)

    def test_set_gill_color_chocolate(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'h',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.gillColor == Mi.GillColor.Chocolate, True)

    def test_set_gill_color_gray(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'g',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.gillColor == Mi.GillColor.Gray, True)

    def test_set_gill_color_green(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'f', 'd', 'n', 'r',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.gillColor == Mi.GillColor.Green, True)

    def test_set_gill_color_orange(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'o',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.gillColor == Mi.GillColor.Orange, True)

    def test_set_gill_color_pink(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'p',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.gillColor == Mi.GillColor.Pink, True)

    def test_set_gill_color_purple(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'f', 'd', 'n', 'u',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.gillColor == Mi.GillColor.Purple, True)

    def test_set_gill_color_red(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'e',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.gillColor == Mi.GillColor.Red, True)

    def test_set_gill_color_white(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'w',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.gillColor == Mi.GillColor.White, True)

    def test_set_gill_color_yellow(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'f', 'd', 'n', 'y',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.gillColor == Mi.GillColor.Yellow, True)

    def test_set_gill_color_wrong_value(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'f', 'd', 'n', 'x',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        with self.assertRaises(ValueError):
            Mushroom.Mushroom(vec)


class TestSetStalkShape(unittest.TestCase):
    def test_set_stalk_shape_enlarging(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkShape == Mi.StalkShape.Enlarging, True)

    def test_set_stalk_shape_tapering(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkShape == Mi.StalkShape.Tapering, True)

    def test_set_stalk_shape_wrong_value(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'f', 'd', 'n', 'k',
               'x', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        with self.assertRaises(ValueError):
            Mushroom.Mushroom(vec)


class TestSetStalkRoot(unittest.TestCase):
    def test_set_stalk_root_bulbous(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkRoot == Mi.StalkRoot.Bulbous, True)

    def test_set_stalk_root_club(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'c', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkRoot == Mi.StalkRoot.Club, True)

    def test_set_stalk_root_cup(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'u', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkRoot == Mi.StalkRoot.Cup, True)

    def test_set_stalk_root_equal(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkRoot == Mi.StalkRoot.Equal, True)

    def test_set_stalk_root_rhizomorphs(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'z', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkRoot == Mi.StalkRoot.Rhizomorphs, True)

    def test_set_stalk_root_rooted(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'r', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkRoot == Mi.StalkRoot.Rooted, True)

    def test_set_stalk_root_missing(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', '?', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkRoot == Mi.StalkRoot.Missing, True)

    def test_set_stalk_root_wrong_value(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'f', 'd', 'n', 'k',
               'e', 'x', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        with self.assertRaises(ValueError):
            Mushroom.Mushroom(vec)


class TestSetStalkSurfaceAboveRing(unittest.TestCase):
    def test_set_stalk_surface_above_ring_fibrous(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkSurfaceAboveRing == Mi.StalkSurfaceAboveRing.Fibrous, True)

    def test_set_stalk_surface_above_ring_scaly(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'c', 'y', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkSurfaceAboveRing == Mi.StalkSurfaceAboveRing.Scaly, True)

    def test_set_stalk_surface_above_ring_silky(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'u', 'k', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkSurfaceAboveRing == Mi.StalkSurfaceAboveRing.Silky, True)

    def test_set_stalk_surface_above_ring_smooth(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkSurfaceAboveRing == Mi.StalkSurfaceAboveRing.Smooth, True)

    def test_set_stalk_surface_above_ring_wrong_value(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'f', 'd', 'n', 'k',
               'e', 'e', 'e', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        with self.assertRaises(ValueError):
            Mushroom.Mushroom(vec)


class TestSetStalkSurfaceBelowRing(unittest.TestCase):
    def test_set_stalk_surface_below_ring_fibrous(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 'f', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkSurfaceBelowRing == Mi.StalkSurfaceBelowRing.Fibrous, True)

    def test_set_stalk_surface_below_ring_scaly(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'c', 'y', 'y', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkSurfaceBelowRing == Mi.StalkSurfaceBelowRing.Scaly, True)

    def test_set_stalk_surface_below_ring_silky(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'u', 'k', 'k', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkSurfaceBelowRing == Mi.StalkSurfaceBelowRing.Silky, True)

    def test_set_stalk_surface_below_ring_smooth(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkSurfaceBelowRing == Mi.StalkSurfaceBelowRing.Smooth, True)

    def test_set_stalk_surface_below_ring_wrong_value(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'f', 'd', 'n', 'k',
               't', 'e', 's', 'e', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        with self.assertRaises(ValueError):
            Mushroom.Mushroom(vec)


class TestSetStalkColorAboveRing(unittest.TestCase):
    def test_set_stalk_color_above_ring_brown(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 'f', 'n', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkColorAboveRing == Mi.StalkColorAboveRing.Brown, True)

    def test_set_stalk_color_above_ring_buff(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'c', 'y', 'y', 'b', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkColorAboveRing == Mi.StalkColorAboveRing.Buff, True)

    def test_set_stalk_color_above_ring_cinnamon(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'u', 'k', 'k', 'c', 'c', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkColorAboveRing == Mi.StalkColorAboveRing.Cinnamon, True)

    def test_set_stalk_color_above_ring_gray(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'e', 's', 's', 'g', 'g', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkColorAboveRing == Mi.StalkColorAboveRing.Gray, True)

    def test_set_stalk_color_above_ring_orange(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 'f', 'o', 'o', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkColorAboveRing == Mi.StalkColorAboveRing.Orange, True)

    def test_set_stalk_color_above_ring_pink(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'c', 'y', 'y', 'p', 'p', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkColorAboveRing == Mi.StalkColorAboveRing.Pink, True)

    def test_set_stalk_color_above_ring_red(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'u', 'k', 'k', 'e', 'e', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkColorAboveRing == Mi.StalkColorAboveRing.Red, True)

    def test_set_stalk_color_above_ring_white(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'c', 'y', 'y', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkColorAboveRing == Mi.StalkColorAboveRing.White, True)

    def test_set_stalk_color_below_ring_yellow(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'u', 'k', 'k', 'y', 'y', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkColorAboveRing == Mi.StalkColorAboveRing.Yellow, True)

    def test_set_stalk_color_above_ring_wrong_value(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'f', 'd', 'n', 'k',
               't', 'e', 's', 'k', 'x', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        with self.assertRaises(ValueError):
            Mushroom.Mushroom(vec)


class TestSetStalkColorBelowRing(unittest.TestCase):
    def test_set_stalk_color_below_ring_brown(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 'f', 'n', 'n', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkColorBelowRing == Mi.StalkColorBelowRing.Brown, True)

    def test_set_stalk_color_below_ring_buff(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'c', 'y', 'y', 'b', 'b', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkColorBelowRing == Mi.StalkColorBelowRing.Buff, True)

    def test_set_stalk_color_below_ring_cinnamon(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'u', 'k', 'k', 'c', 'c', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkColorBelowRing == Mi.StalkColorBelowRing.Cinnamon, True)

    def test_set_stalk_color_below_ring_gray(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'e', 's', 's', 'g', 'g', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkColorBelowRing == Mi.StalkColorBelowRing.Gray, True)

    def test_set_stalk_color_below_ring_orange(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 'f', 'o', 'o', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkColorBelowRing == Mi.StalkColorBelowRing.Orange, True)

    def test_set_stalk_color_below_ring_pink(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'c', 'y', 'y', 'p', 'p', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkColorBelowRing == Mi.StalkColorBelowRing.Pink, True)

    def test_set_stalk_color_below_ring_red(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'u', 'k', 'k', 'e', 'e', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkColorBelowRing == Mi.StalkColorBelowRing.Red, True)

    def test_set_stalk_color_below_ring_white(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'c', 'y', 'y', 'w', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkColorBelowRing == Mi.StalkColorBelowRing.White, True)

    def test_set_stalk_color_below_ring_yellow(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'u', 'k', 'k', 'y', 'y', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.stalkColorBelowRing == Mi.StalkColorBelowRing.Yellow, True)

    def test_set_stalk_color_below_ring_wrong_value(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'f', 'd', 'n', 'k',
               't', 'e', 's', 'k', 'w', 'x', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        with self.assertRaises(ValueError):
            Mushroom.Mushroom(vec)


class TestSetVeilType(unittest.TestCase):
    def test_set_veil_type_partial(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 'f', 'n', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.veilType == Mi.VeilType.Partial, True)

    def test_set_veil_type_universal(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'c', 'y', 'y', 'b', 'w', 'u', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.veilType == Mi.VeilType.Universal, True)

    def test_set_veil_type_wrong_value(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'f', 'd', 'n', 'k',
               't', 'c', 'y', 'y', 'w', 'w', 'x', 'w', 'o', 'p',
               'k', 's', 'u']
        with self.assertRaises(ValueError):
            Mushroom.Mushroom(vec)


class TestSetVeilColor(unittest.TestCase):
    def test_set_veil_color_brown(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 'f', 'n', 'w', 'p', 'n', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.veilColor == Mi.VeilColor.Brown, True)

    def test_set_veil_color_orange(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'c', 'y', 'y', 'b', 'w', 'u', 'o', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.veilColor == Mi.VeilColor.Orange, True)

    def test_set_veil_color_white(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 'f', 'n', 'w', 'p', 'w', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.veilColor == Mi.VeilColor.White, True)

    def test_set_veil_color_yellow(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'c', 'y', 'y', 'b', 'w', 'u', 'y', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.veilColor == Mi.VeilColor.Yellow, True)

    def test_set_stalk_color_below_ring_wrong_value(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'f', 'd', 'n', 'k',
               't', 'c', 'y', 'y', 'w', 'w', 'u', 'x', 'o', 'p',
               'k', 's', 'u']
        with self.assertRaises(ValueError):
            Mushroom.Mushroom(vec)


class TestSetRingNumber(unittest.TestCase):
    def test_set_ring_number_none(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 'f', 'n', 'w', 'p', 'n', 'n', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.ringNumber == Mi.RingNumber.Zero, True)

    def test_set_ring_number_one(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'c', 'y', 'y', 'b', 'w', 'u', 'o', 'o', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.ringNumber == Mi.RingNumber.One, True)

    def test_set_ring_number_two(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 'f', 'n', 'w', 'p', 'w', 't', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.ringNumber == Mi.RingNumber.Two, True)

    def test_set_ring_number_wrong_value(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'f', 'd', 'n', 'k',
               't', 'c', 'y', 'y', 'w', 'w', 'u', 'w', 'g', 'p',
               'k', 's', 'u']
        with self.assertRaises(ValueError):
            Mushroom.Mushroom(vec)


class TestSetRingType(unittest.TestCase):
    def test_set_ring_type_cobwebby(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 'f', 'n', 'w', 'p', 'n', 'n', 'c',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.ringType == Mi.RingType.Cobwebby, True)

    def test_set_ring_type_evanescent(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'c', 'y', 'y', 'b', 'w', 'u', 'o', 'o', 'e',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.ringType == Mi.RingType.Evanescent, True)

    def test_set_ring_type_flaring(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 'f', 'n', 'w', 'p', 'w', 't', 'f',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.ringType == Mi.RingType.Flaring, True)

    def test_set_ring_type_large(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 'f', 'n', 'w', 'p', 'n', 'n', 'l',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.ringType == Mi.RingType.Large, True)

    def test_set_ring_type_no(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'c', 'y', 'y', 'b', 'w', 'u', 'o', 'o', 'n',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.ringType == Mi.RingType.No, True)

    def test_set_ring_type_pendant(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 'f', 'n', 'w', 'p', 'w', 't', 'p',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.ringType == Mi.RingType.Pendant, True)

    def test_set_ring_type_sheathing(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 'f', 'n', 'w', 'p', 'n', 'n', 's',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.ringType == Mi.RingType.Sheathing, True)

    def test_set_ring_type_zone(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'c', 'y', 'y', 'b', 'w', 'u', 'o', 'o', 'z',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.ringType == Mi.RingType.Zone, True)

    def test_set_ring_type_wrong_value(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'f', 'd', 'n', 'k',
               't', 'c', 'y', 'y', 'w', 'w', 'u', 'w', 'n', 'x',
               'k', 's', 'u']
        with self.assertRaises(ValueError):
            Mushroom.Mushroom(vec)


class TestSetSporePrintColor(unittest.TestCase):
    def test_set_spore_print_color_black(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 'f', 'n', 'w', 'p', 'n', 'n', 'c',
               'k', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.sporePrintColor == Mi.SporePrintColor.Black, True)

    def test_set_spore_print_color_brown(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'c', 'y', 'y', 'b', 'w', 'u', 'o', 'o', 'e',
               'n', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.sporePrintColor == Mi.SporePrintColor.Brown, True)

    def test_set_spore_print_color_buff(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 'f', 'n', 'w', 'p', 'w', 't', 'f',
               'b', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.sporePrintColor == Mi.SporePrintColor.Buff, True)

    def test_set_spore_print_color_chocolate(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 'f', 'n', 'w', 'p', 'n', 'n', 'l',
               'h', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.sporePrintColor == Mi.SporePrintColor.Chocolate, True)

    def test_set_spore_print_color_green(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'c', 'y', 'y', 'b', 'w', 'u', 'o', 'o', 'n',
               'r', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.sporePrintColor == Mi.SporePrintColor.Green, True)

    def test_set_spore_print_color_orange(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 'f', 'n', 'w', 'p', 'w', 't', 'p',
               'o', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.sporePrintColor == Mi.SporePrintColor.Orange, True)

    def test_set_spore_print_color_purple(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 'f', 'n', 'w', 'p', 'n', 'n', 's',
               'u', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.sporePrintColor == Mi.SporePrintColor.Purple, True)

    def test_set_spore_print_color_white(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'c', 'y', 'y', 'b', 'w', 'u', 'o', 'o', 'z',
               'w', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.sporePrintColor == Mi.SporePrintColor.White, True)

    def test_set_spore_print_color_yellow(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'c', 'y', 'y', 'b', 'w', 'u', 'o', 'o', 'z',
               'y', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.sporePrintColor == Mi.SporePrintColor.Yellow, True)

    def test_set_spore_print_color_wrong_value(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'f', 'd', 'n', 'k',
               't', 'c', 'y', 'y', 'w', 'w', 'u', 'w', 'n', 'z',
               'x', 's', 'u']
        with self.assertRaises(ValueError):
            Mushroom.Mushroom(vec)


class TestSetPopulation(unittest.TestCase):
    def test_set_population_abundant(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 'f', 'n', 'w', 'p', 'n', 'n', 'c',
               'k', 'a', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.population == Mi.Population.Abundant, True)

    def test_set_population_clustered(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'c', 'y', 'y', 'b', 'w', 'u', 'o', 'o', 'e',
               'n', 'c', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.population == Mi.Population.Clustered, True)

    def test_set_population_numerous(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 'f', 'n', 'w', 'p', 'w', 't', 'f',
               'b', 'n', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.population == Mi.Population.Numerous, True)

    def test_set_population_scattered(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 'f', 'n', 'w', 'p', 'n', 'n', 'l',
               'h', 's', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.population == Mi.Population.Scattered, True)

    def test_set_population_several(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 'f', 'n', 'w', 'p', 'n', 'n', 'l',
               'w', 'v', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.population == Mi.Population.Several, True)

    def test_set_population_solitary(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'c', 'y', 'y', 'b', 'w', 'u', 'o', 'o', 'n',
               'r', 'y', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.population == Mi.Population.Solitary, True)

    def test_set_population_wrong_value(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'f', 'd', 'n', 'k',
               't', 'c', 'y', 'y', 'w', 'w', 'u', 'w', 'n', 'z',
               'r', 'x', 'u']
        with self.assertRaises(ValueError):
            Mushroom.Mushroom(vec)


class TestSetHabitat(unittest.TestCase):
    def test_set_habitat_grassed(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 'f', 'n', 'w', 'p', 'n', 'n', 'c',
               'k', 'a', 'g']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.habitat == Mi.Habitat.Grasses, True)

    def test_set_habitat_leaves(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'c', 'y', 'y', 'b', 'w', 'u', 'o', 'o', 'e',
               'n', 'c', 'l']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.habitat == Mi.Habitat.Leaves, True)

    def test_set_habitat_meadows(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 'f', 'n', 'w', 'p', 'w', 't', 'f',
               'b', 'n', 'm']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.habitat == Mi.Habitat.Meadows, True)

    def test_set_habitat_paths(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 'f', 'n', 'w', 'p', 'n', 'n', 'l',
               'h', 's', 'p']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.habitat == Mi.Habitat.Paths, True)

    def test_set_habitat_urban(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'a', 'c', 'n', 'k',
               'e', 'b', 'f', 'f', 'n', 'w', 'p', 'n', 'n', 'l',
               'w', 'y', 'u']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.habitat == Mi.Habitat.Urban, True)

    def test_set_habitat_waste(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'c', 'y', 'y', 'b', 'w', 'u', 'o', 'o', 'n',
               'r', 'y', 'w']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.habitat == Mi.Habitat.Waste, True)

    def test_set_habitat_woods(self):
        vec = ['p', 'k', 's', 'y', 'f', 'p', 'd', 'w', 'n', 'n',
               't', 'c', 'y', 'y', 'b', 'w', 'u', 'o', 'o', 'n',
               'r', 'y', 'd']
        mushroom = Mushroom.Mushroom(vec)
        self.assertEqual(mushroom.habitat == Mi.Habitat.Woods, True)

    def test_set_habitat_wrong_value(self):
        vec = ['p', 'f', 's', 'y', 't', 'p', 'f', 'd', 'n', 'k',
               't', 'c', 'y', 'y', 'w', 'w', 'u', 'w', 'n', 'z',
               'r', 'y', 'x']
        with self.assertRaises(ValueError):
            Mushroom.Mushroom(vec)


if __name__ == '__main__':
    unittest.main()
