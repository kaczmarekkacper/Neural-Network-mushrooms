import source.MushroomInfo as mi


class Mushroom:
    def __init__(self, vec, boolean):
        self.edible = self.set_edible(vec[0], boolean)
        self.capShape = self.set_capshape(vec[1])
        self.capSurface = self.set_capsurface(vec[2])
        self.capColor = self.set_capcolor(vec[3])
        self.bruises = self.set_bruises(vec[4])
        self.odor = None
        self.gillAttachment = None
        self.gillSpacing = None
        self.gillSize = None
        self.gillColor = None
        self.stalkShape = None
        self.stalkRoot = None
        self.stalkSurfaceAboveRing = None
        self.stalkSurfaceBelowRing = None
        self.veilType = None
        self.veilColor = None
        self.ringNumber = None
        self.ringType = None
        self.sporePrintColor = None
        self.population = None
        self.habitat = None

    @staticmethod
    def set_edible(feature, boolean):
        if boolean:
            if feature == "e":
                return mi.Edible.Yes
            if feature == "p":
                return mi.Edible.No
            raise ValueError("No such value in mi.Edible")
        else:
            return mi.Edible.NoInfo

    @staticmethod
    def set_capshape(feature):
        if feature == 'b':
            return mi.CapShape.Bell
        if feature == 'c':
            return mi.CapShape.Conical
        if feature == 'x':
            return mi.CapShape.Convex
        if feature == 'f':
            return mi.CapShape.Flat
        if feature == 'k':
            return mi.CapShape.Knobbed
        if feature == 's':
            return mi.CapShape.Sunken
        raise ValueError('No such value in mi.CapShape')

    @staticmethod
    def set_capsurface(feature):
        if feature == 'f':
            return mi.CapSurface.Fibrous
        if feature == 'g':
            return mi.CapSurface.Grooves
        if feature == 'y':
            return mi.CapSurface.Scaly
        if feature == 's':
            return mi.CapSurface.Smooth
        raise ValueError('No such value in mi.CapSurface')

    @staticmethod
    def set_capcolor(feature):
        if feature == 'n':
            return mi.CapColor.Brown
        if feature == 'b':
            return mi.CapColor.Buff
        if feature == 'c':
            return mi.CapColor.Cinnamon
        if feature == 'g':
            return mi.CapColor.Gray
        if feature == 'r':
            return mi.CapColor.Green
        if feature == 'p':
            return mi.CapColor.Pink
        if feature == 'u':
            return mi.CapColor.Purple
        if feature == 'e':
            return mi.CapColor.Red
        if feature == 'w':
            return mi.CapColor.White
        if feature == 'y':
            return mi.CapColor.Yellow
        raise ValueError('No such value in mi.CapColor')

    @staticmethod
    def set_bruises(feature):
        if feature == 't':
            return mi.Bruises.Yes
        if feature == 'f':
            return mi.Bruises.No
        raise ValueError('No such value in mi.Bruises')