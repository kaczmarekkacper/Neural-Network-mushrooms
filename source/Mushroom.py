# -*- coding: utf-8 -*-
"""
    File name: Mushroom.py
    Author: Kacper Kaczmarek, Krzysztof Kobyliński
    Python Version: 3.6.0
"""
import MushroomInfo as Mi
import numpy as np


class Mushroom:

    mean_values = []
    std_values = []

    def __init__(self, vec):
        self.prediction = Mi.Edible.NoInfo
        self.edible = self.set_edible(vec[0])
        self.capShape = self.set_capshape(vec[1])
        self.capSurface = self.set_capsurface(vec[2])
        self.capColor = self.set_capcolor(vec[3])
        self.bruises = self.set_bruises(vec[4])
        self.odor = self.set_odor(vec[5])
        self.gillAttachment = self.set_gill_attachment(vec[6])
        self.gillSpacing = self.set_gill_spacing(vec[7])
        self.gillSize = self.set_gill_size(vec[8])
        self.gillColor = self.set_gill_color(vec[9])
        self.stalkShape = self.set_stalk_shape(vec[10])
        self.stalkRoot = self.set_stalk_root(vec[11])
        self.stalkSurfaceAboveRing = self.set_stalk_surface_above_ring(vec[12])
        self.stalkSurfaceBelowRing = self.set_stalk_surface_below_ring(vec[13])
        self.stalkColorAboveRing = self.set_stalk_color_above_ring(vec[14])
        self.stalkColorBelowRing = self.set_stalk_color_below_ring(vec[15])
        self.veilType = self.set_veil_type(vec[16])
        self.veilColor = self.set_veil_color(vec[17])
        self.ringNumber = self.set_ring_number(vec[18])
        self.ringType = self.set_ring_type(vec[19])
        self.sporePrintColor = self.set_spore_print_color(vec[20])
        self.population = self.set_population(vec[21])
        self.habitat = self.set_habitat(vec[22])
        self.error = 0

    def get_vector(self):
        vec = [self.capShape.value, self.capSurface.value, self.capColor.value, self.bruises.value,
               self.odor.value, self.gillAttachment.value, self.gillSpacing.value, self.gillSize.value,
               self.gillColor.value, self.stalkShape.value, self.stalkRoot.value,
               self.stalkSurfaceAboveRing.value, self.stalkSurfaceBelowRing.value, self.stalkColorAboveRing.value,
               self.stalkColorBelowRing.value, self.veilType.value, self.veilColor.value, self.ringNumber.value,
               self.ringType.value, self.sporePrintColor.value, self.population.value, self.habitat.value]
        return vec

    def get_normalized_vector(self):
        vec = self.get_vector()
        vec = Mushroom.normalize_vector(vec)
        return vec

    @staticmethod
    def set_std_and_mean_values(mushrooms):
        mushrooms_set = []
        for m in mushrooms:
            mushrooms_set.append(m.get_vector())
        Mushroom.std_values = np.std(mushrooms_set, axis=0)
        Mushroom.std_values = np.array(Mushroom.std_values, dtype=float)
        Mushroom.mean_values = np.mean(mushrooms_set, axis=0)
        Mushroom.mean_values = np.array(Mushroom.mean_values, dtype=float)

    @staticmethod
    def normalize_vector(vec):
        vec = np.subtract(vec, Mushroom.mean_values)
        vec = np.divide(vec, Mushroom.std_values, out=np.zeros_like(Mushroom.std_values), where=Mushroom.std_values != 0)
        return vec

    def set_prediction(self, output):
        if output > 0.5:
            self.prediction = Mi.Edible.Yes
            self.error = 1 - output
        else:
            self.prediction = Mi.Edible.No
            self.error = 0 - output

    def check_prediction(self):
        return not abs(self.prediction.value - self.edible.value)

    @staticmethod
    def set_edible(feature):
        if feature == "e":
            return Mi.Edible.Yes
        if feature == "p":
            return Mi.Edible.No
        raise ValueError("No such value in mi.Edible")

    @staticmethod
    def set_capshape(feature):
        if feature == 'b':
            return Mi.CapShape.Bell
        if feature == 'c':
            return Mi.CapShape.Conical
        if feature == 'x':
            return Mi.CapShape.Convex
        if feature == 'f':
            return Mi.CapShape.Flat
        if feature == 'k':
            return Mi.CapShape.Knobbed
        if feature == 's':
            return Mi.CapShape.Sunken
        raise ValueError('No such value in mi.CapShape')

    @staticmethod
    def set_capsurface(feature):
        if feature == 'f':
            return Mi.CapSurface.Fibrous
        if feature == 'g':
            return Mi.CapSurface.Grooves
        if feature == 'y':
            return Mi.CapSurface.Scaly
        if feature == 's':
            return Mi.CapSurface.Smooth
        raise ValueError('No such value in mi.CapSurface')

    @staticmethod
    def set_capcolor(feature):
        if feature == 'n':
            return Mi.CapColor.Brown
        if feature == 'b':
            return Mi.CapColor.Buff
        if feature == 'c':
            return Mi.CapColor.Cinnamon
        if feature == 'g':
            return Mi.CapColor.Gray
        if feature == 'r':
            return Mi.CapColor.Green
        if feature == 'p':
            return Mi.CapColor.Pink
        if feature == 'u':
            return Mi.CapColor.Purple
        if feature == 'e':
            return Mi.CapColor.Red
        if feature == 'w':
            return Mi.CapColor.White
        if feature == 'y':
            return Mi.CapColor.Yellow
        raise ValueError('No such value in mi.CapColor')

    @staticmethod
    def set_bruises(feature):
        if feature == 't':
            return Mi.Bruises.Yes
        if feature == 'f':
            return Mi.Bruises.No
        raise ValueError('No such value in mi.Bruises')

    @staticmethod
    def set_odor(feature):
        if feature == 'a':
            return Mi.Odor.Almond
        if feature == 'l':
            return Mi.Odor.Anise
        if feature == 'c':
            return Mi.Odor.Creosote
        if feature == 'y':
            return Mi.Odor.Fishy
        if feature == 'f':
            return Mi.Odor.Foul
        if feature == 'm':
            return Mi.Odor.Musty
        if feature == 'n':
            return Mi.Odor.Without
        if feature == 'p':
            return Mi.Odor.Pungent
        if feature == 's':
            return Mi.Odor.Spicy
        raise ValueError('No such value in mi.Odor')

    @staticmethod
    def set_gill_attachment(feature):
        if feature == 'a':
            return Mi.GillAttachment.Attached
        if feature == 'd':
            return Mi.GillAttachment.Descending
        if feature == 'f':
            return Mi.GillAttachment.Free
        if feature == 'n':
            return Mi.GillAttachment.Notched
        raise ValueError('No such value in mi.GillAttachment')

    @staticmethod
    def set_gill_spacing(feature):
        if feature == 'c':
            return Mi.GillSpacing.Close
        if feature == 'w':
            return Mi.GillSpacing.Crowded
        if feature == 'd':
            return Mi.GillSpacing.Distant
        raise ValueError('No such value in mi.GillSpacing')

    @staticmethod
    def set_gill_size(feature):
        if feature == 'b':
            return Mi.GillSize.Broad
        if feature == 'n':
            return Mi.GillSize.Narrow
        raise ValueError('No such value in mi.GillSize')

    @staticmethod
    def set_gill_color(feature):
        if feature == 'k':
            return Mi.GillColor.Black
        if feature == 'n':
            return Mi.GillColor.Brown
        if feature == 'b':
            return Mi.GillColor.Buff
        if feature == 'h':
            return Mi.GillColor.Chocolate
        if feature == 'g':
            return Mi.GillColor.Gray
        if feature == 'r':
            return Mi.GillColor.Green
        if feature == 'o':
            return Mi.GillColor.Orange
        if feature == 'p':
            return Mi.GillColor.Pink
        if feature == 'u':
            return Mi.GillColor.Purple
        if feature == 'e':
            return Mi.GillColor.Red
        if feature == 'w':
            return Mi.GillColor.White
        if feature == 'y':
            return Mi.GillColor.Yellow
        raise ValueError('No such value in mi.GillColor')

    @staticmethod
    def set_stalk_shape(feature):
        if feature == 'e':
            return Mi.StalkShape.Enlarging
        if feature == 't':
            return Mi.StalkShape.Tapering
        raise ValueError('No such value in mi.StalkShape')

    @staticmethod
    def set_stalk_root(feature):
        if feature == 'b':
            return Mi.StalkRoot.Bulbous
        if feature == 'c':
            return Mi.StalkRoot.Club
        if feature == 'u':
            return Mi.StalkRoot.Cup
        if feature == 'e':
            return Mi.StalkRoot.Equal
        if feature == 'z':
            return Mi.StalkRoot.Rhizomorphs
        if feature == 'r':
            return Mi.StalkRoot.Rooted
        if feature == '?':
            return Mi.StalkRoot.Missing
        raise ValueError('No such value in mi.StalkRoot')

    @staticmethod
    def set_stalk_surface_above_ring(feature):
        if feature == 'f':
            return Mi.StalkSurfaceAboveRing.Fibrous
        if feature == 'y':
            return Mi.StalkSurfaceAboveRing.Scaly
        if feature == 'k':
            return Mi.StalkSurfaceAboveRing.Silky
        if feature == 's':
            return Mi.StalkSurfaceAboveRing.Smooth
        raise ValueError('No such value in mi.StalkSurfaceAboveRing')

    @staticmethod
    def set_stalk_surface_below_ring(feature):
        if feature == 'f':
            return Mi.StalkSurfaceBelowRing.Fibrous
        if feature == 'y':
            return Mi.StalkSurfaceBelowRing.Scaly
        if feature == 'k':
            return Mi.StalkSurfaceBelowRing.Silky
        if feature == 's':
            return Mi.StalkSurfaceBelowRing.Smooth
        raise ValueError('No such value in mi.StalkSurfaceBelowRing')

    @staticmethod
    def set_stalk_color_above_ring(feature):
        if feature == 'n':
            return Mi.StalkColorAboveRing.Brown
        if feature == 'b':
            return Mi.StalkColorAboveRing.Buff
        if feature == 'c':
            return Mi.StalkColorAboveRing.Cinnamon
        if feature == 'g':
            return Mi.StalkColorAboveRing.Gray
        if feature == 'o':
            return Mi.StalkColorAboveRing.Orange
        if feature == 'p':
            return Mi.StalkColorAboveRing.Pink
        if feature == 'e':
            return Mi.StalkColorAboveRing.Red
        if feature == 'w':
            return Mi.StalkColorAboveRing.White
        if feature == 'y':
            return Mi.StalkColorAboveRing.Yellow
        raise ValueError('No such value in mi.StalkColorAboveRing')

    @staticmethod
    def set_stalk_color_below_ring(feature):
        if feature == 'n':
            return Mi.StalkColorBelowRing.Brown
        if feature == 'b':
            return Mi.StalkColorBelowRing.Buff
        if feature == 'c':
            return Mi.StalkColorBelowRing.Cinnamon
        if feature == 'g':
            return Mi.StalkColorBelowRing.Gray
        if feature == 'o':
            return Mi.StalkColorBelowRing.Orange
        if feature == 'p':
            return Mi.StalkColorBelowRing.Pink
        if feature == 'e':
            return Mi.StalkColorBelowRing.Red
        if feature == 'w':
            return Mi.StalkColorBelowRing.White
        if feature == 'y':
            return Mi.StalkColorBelowRing.Yellow
        raise ValueError('No such value in mi.StalkColorBelowRing')

    @staticmethod
    def set_veil_type(feature):
        if feature == 'p':
            return Mi.VeilType.Partial
        if feature == 'u':
            return Mi.VeilType.Universal
        raise ValueError('No such value in mi.VeilType')

    @staticmethod
    def set_veil_color(feature):
        if feature == 'n':
            return Mi.VeilColor.Brown
        if feature == 'o':
            return Mi.VeilColor.Orange
        if feature == 'w':
            return Mi.VeilColor.White
        if feature == 'y':
            return Mi.VeilColor.Yellow
        raise ValueError('No such value in mi.VeilColor')

    @staticmethod
    def set_ring_number(feature):
        if feature == 'n':
            return Mi.RingNumber.Zero
        if feature == 'o':
            return Mi.RingNumber.One
        if feature == 't':
            return Mi.RingNumber.Two
        raise ValueError('No such value in mi.RingNumber')

    @staticmethod
    def set_ring_type(feature):
        if feature == 'c':
            return Mi.RingType.Cobwebby
        if feature == 'e':
            return Mi.RingType.Evanescent
        if feature == 'f':
            return Mi.RingType.Flaring
        if feature == 'l':
            return Mi.RingType.Large
        if feature == 'n':
            return Mi.RingType.No
        if feature == 'p':
            return Mi.RingType.Pendant
        if feature == 's':
            return Mi.RingType.Sheathing
        if feature == 'z':
            return Mi.RingType.Zone
        raise ValueError('No such value in mi.RingType')

    @staticmethod
    def set_spore_print_color(feature):
        if feature == 'k':
            return Mi.SporePrintColor.Black
        if feature == 'n':
            return Mi.SporePrintColor.Brown
        if feature == 'b':
            return Mi.SporePrintColor.Buff
        if feature == 'h':
            return Mi.SporePrintColor.Chocolate
        if feature == 'r':
            return Mi.SporePrintColor.Green
        if feature == 'o':
            return Mi.SporePrintColor.Orange
        if feature == 'u':
            return Mi.SporePrintColor.Purple
        if feature == 'w':
            return Mi.SporePrintColor.White
        if feature == 'y':
            return Mi.SporePrintColor.Yellow
        raise ValueError('No such value in mi.SporePrintColor')

    @staticmethod
    def set_population(feature):
        if feature == 'a':
            return Mi.Population.Abundant
        if feature == 'c':
            return Mi.Population.Clustered
        if feature == 'n':
            return Mi.Population.Numerous
        if feature == 's':
            return Mi.Population.Scattered
        if feature == 'v':
            return Mi.Population.Several
        if feature == 'y':
            return Mi.Population.Solitary
        raise ValueError('No such value in mi.Population')

    @staticmethod
    def set_habitat(feature):
        if feature == 'g':
            return Mi.Habitat.Grasses
        if feature == 'l':
            return Mi.Habitat.Leaves
        if feature == 'm':
            return Mi.Habitat.Meadows
        if feature == 'p':
            return Mi.Habitat.Paths
        if feature == 'u':
            return Mi.Habitat.Urban
        if feature == 'w':
            return Mi.Habitat.Waste
        if feature == 'd':
            return Mi.Habitat.Woods
        raise ValueError('No such value in mi.Habitat')
