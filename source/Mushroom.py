import MushroomInfo as mi


class Mushroom:
    def __init__(self, vec, bool):
        self.edible = None
        self.capShape = None
        self.capColor = None
        self.bruises = None
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

    def set_edible(self, feature, boolean):
        if boolean:
            if feature == "e":
                self.edible = mi.Edible.Yes
            if feature == "p":
                self.edible = mi.Edible.No
            if feature != "e" and feature != "p":
                raise ValueError("No such value in mi.Edible")
        else:
            self.edible = mi.Edible.NoInfo

    def set_capshape(self, feature):
        if feature == 'b':
            self.capShape = mi.CapShape.Bell
        if feature == 'c':
            self.capShape = mi.CapShape.Conical
