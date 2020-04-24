from enum import Enum


class Edible(Enum):
    Yes = 1
    No = 2
    NoInfo = 3


class CapShape(Enum):
    Bell = 1
    Conical = 2
    Convex = 3
    Flat = 4
    Knobbed = 5
    Sunken = 6


class CapSurface(Enum):
    Fibrous = 1
    Grooves = 2
    Scaly = 3
    Smooth = 4


class CapColor(Enum):
    Brown = 1
    Buff = 2
    Cinnamon = 3
    Gray = 4
    Green = 5
    Pink = 6
    Purple = 7
    Red = 8
    White = 9
    Yellow = 10


class Bruises(Enum):
    Yes = 1
    No = 2


class Odor(Enum):
    Almond = 1
    Anise = 2
    Creosote = 3
    Fishy = 4
    Foul = 5
    Musty = 6
    Without = 7
    Pungent = 8
    Spicy = 9


class GillAttachment(Enum):
    Attached = 1
    Descending = 2
    Free = 3
    Notched = 4


class GillSpacing(Enum):
    Close = 1
    Crowded = 2
    Distant = 3


class GillSize(Enum):
    Broad = 1
    Narrow = 2


class GillColor(Enum):
    Black = 1
    Brown = 2
    Buff = 3
    Chocolate = 4
    Gray = 5
    Green = 6
    Orange = 7
    Pink = 8
    Purple = 9
    Red = 10
    White = 11
    Yellow = 12


class StalkShape(Enum):
    Enlarging = 1
    Tapering = 2


class StalkRoot(Enum):
    Bulbous = 1
    Club = 2
    Cup = 3
    Equal = 4
    Rhizomorphs = 5
    Rooted = 6
    Missing = 7


class StalkSurfaceAboveRing(Enum):
    Fibrous = 1
    Scaly = 2
    Silky = 3
    Smooth = 4


class StalkSurfaceBelowRing(Enum):
    Fibrous = 1
    Scaly = 2
    Silky = 3
    Smooth = 4


class StalkColorAboveRing(Enum):
    Brown = 1
    Buff = 2
    Cinnamon = 3
    Gray = 4
    Orange = 5
    Pink = 6
    Red = 7
    White = 8
    Yellow = 9


class StalkColorBelowRing(Enum):
    Brown = 1
    Buff = 2
    Cinnamon = 3
    Gray = 4
    Orange = 5
    Pink = 6
    Red = 7
    White = 8
    Yellow = 9


class VeilType(Enum):
    Partial = 1
    Universal = 2


class VeilColor(Enum):
    Brown = 1
    Orange = 2
    White = 3
    Yellow = 4


class RingNumber(Enum):
    Zero = 1
    One = 2
    Two = 3


class RingType(Enum):
    Cobwebby = 1
    Evanescent = 2
    Flaring = 3
    Large = 4
    No = 5
    Pendant = 6
    Sheathing = 7
    Zone = 8


class SporePrintColor(Enum):
    Black = 1
    Brown = 2
    Buff = 3
    Chocolate = 4
    Gray = 5
    Green = 6
    Orange = 7
    Pink = 8
    Purple = 9
    Red = 10
    White = 11
    Yellow = 12


class Population(Enum):
    Abundant = 1
    Clustered = 2
    Numerous = 3
    Scattered = 4
    Several = 5
    Solitary = 6


class Habitat(Enum):
    Grasses = 1
    Leaves = 2
    Meadows = 3
    Paths = 4
    Urban = 5
    Waste = 6
    Woods = 7
