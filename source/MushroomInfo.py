from enum import Enum


class Edible(Enum):
    Yes = 1  # e
    No = 2  # p
    NoInfo = 3


class CapShape(Enum):  # kształt kapelusza
    Bell = -1.3363  # b Dzwon
    Conical = -0.8018  # c Stożkowy
    Convex = -0.2673  # x Wypukły
    Flat = 0.2673  # f Płaski
    Knobbed = 0.8018  # k Wybrzuszony
    Sunken = 1.3363  # s Wklęsły


class CapSurface(Enum):  # Powierzchnia kapelusza
    Fibrous = -1.1619  # f Włóknisty
    Grooves = -0.3873 # g Wypustkowaty
    Scaly = 0.3873  # t Łuskowaty
    Smooth = 1.1619 # s Gładki


class CapColor(Enum):
    Brown = -1.4863  # n Brązowy
    Buff = -1.1560  # b Kolor skóry (brązowo-żółtyO
    Cinnamon = -0.8257  # c Cynamonowy
    Gray = -0.4954  # g Szary
    Green = -0.1651  # r Zielony
    Pink = 0.1651  # p Różowy
    Purple = 0.4954   # u Fioletowy
    Red = 0.8257  # e Czerwony
    White = 1.1560  # w Biały
    Yellow = 1.4863  # y Żółty


class Bruises(Enum):  # Siniaki
    Yes = -0.7071  # t Tak
    No = 0.7071  # f Nie


class Odor(Enum):  # Zapach
    Almond = -1.4606   # a Migdałowy
    Anise = -1.0954   # l Anyż
    Creosote = -0.7303  # c Kreozot
    Fishy = -0.3651  # y Rybny(podejrzany)
    Foul = 0  # f Mdły
    Musty = 0.3651  # m Stęchły
    Without = 0.7303  # n Bez
    Pungent = 1.0954   # p Cierpki, Ostry, Gryzący
    Spicy = 1.4606   # s Pikantny, Korzenny


class GillAttachment(Enum):  # Załącznik blaszek
    Attached = -1.1619  # a Przywiązane
    Descending = -0.3873  # d Schodzące
    Free = 0.3873   # f Wolne
    Notched = 1.1619 # n Zaząbkowane


class GillSpacing(Enum):  # Odległości blaszek
    Close = -1  # c Blisko
    Crowded = 0  # w Tłoczno
    Distant = 1  # d Odległe


class GillSize(Enum):  # Wielkości blaszek
    Broad = -0.7071  # b Szerokie
    Narrow = 0.7071  # n Wąskie


class GillColor(Enum):  # Kolory blaszek
    Black = -1.5254   # k
    Brown = -1.2481  # n
    Buff = -0.9707  # b
    Chocolate = -0.6934  # h
    Gray = -0.4160  # g
    Green = -0.1387  # r
    Orange = 0.1387  # o
    Pink = 0.4160  # p
    Purple = 0.6934  # u
    Red = 0.9707  # e
    White = 1.2481  # w
    Yellow = 1.5254   # y


class StalkShape(Enum):  # Kształt łodygi
    Enlarging = -0.7071  # e Powiększająca się
    Tapering = 0.7071  # t Zmniejszająca się


class StalkRoot(Enum):  # Korzeń łodygi
    Bulbous = -1.3887  # b Bulwa
    Club = -0.9258  # c Maczuga
    Cup = -0.4629 # u Puchar
    Equal = 0  # e Równa
    Rhizomorphs = 0.4629  # z Ryzomorfy(takie długie czarne korzenie)
    Rooted = 0.9258  # r Normalne
    Missing = 1.3887  # ? Bez


class StalkSurfaceAboveRing(Enum):  # Powierzchnia łodyg powyżej pierścienia
    Fibrous = -1.1619  # f Włoknisty
    Scaly = -0.3873  # y Łuszczący się
    Silky = 0.3873   # k Jedwabisty
    Smooth = 1.1619  # s Gładki


class StalkSurfaceBelowRing(Enum):  # Powierzchnia łodyg poniżej pierwscienia
    Fibrous = -1.1619  # f Włoknisty
    Scaly = -0.3873   # y Łuszczący się
    Silky = 0.3873  # k Jedwabisty
    Smooth = 1.1619   # s Gładki


class StalkColorAboveRing(Enum):  # Kolor łodygi powyżej pierścienia
    Brown = -1.4606  # n
    Buff = -1.0954  # b
    Cinnamon = -0.7303  # c
    Gray = -0.3651  # g
    Orange = 0  # o
    Pink = 0.3651  # p
    Red = 0.7303  # e
    White = 1.0954  # w
    Yellow = 1.4606  # y


class StalkColorBelowRing(Enum):  # Kolor łodygi powyżej pierścienia
    Brown = -1.4606  # n
    Buff = -1.0954  # b
    Cinnamon = -0.7303  # c
    Gray = -0.3651  # g
    Orange = 0  # o
    Pink = 0.3651  # p
    Red = 0.7303  # e
    White = 1.0954  # w
    Yellow = 1.4606  # y


class VeilType(Enum):  # Rodzaj osłony
    Partial = -0.7071  # p Częściowy
    Universal = 0.7071  # u https://en.wikipedia.org/wiki/Universal_veil


class VeilColor(Enum):  # Kolor osłony
    Brown = -1.1619  # n
    Orange = -0.3873  # o
    White = 0.3873  # w
    Yellow = 1.1619  # y


class RingNumber(Enum):  # Liczba pierścieni
    Zero = -1  # n
    One = 0  # o
    Two = 1  # t


class RingType(Enum):  # Rodzaj pierścienia
    Cobwebby = -1.4289  # c Pajęczynowy
    Evanescent = -1.4289  # e Zanikający
    Flaring = -0.6124 # f Kloszowy
    Large = -0.2041   # l Duży
    No = 0.2041  # n Bez
    Pendant = 0.6124  # p Wisiorek
    Sheathing = 1.0206   # s Poszycie
    Zone = 1.4289  # z Strefowy


class SporePrintColor(Enum):
    Black =  -1.4606   # k
    Brown = -1.0954  # n
    Buff = -0.7303   # b
    Chocolate = -0.3651  # h
    Green = 0  # r
    Orange = 0.3651  # o
    Purple = 0.7303   # u
    White = 1.0954  # w
    Yellow = 1.4606   # y


class Population(Enum):  # Populacja
    Abundant = -1.3363  # a Obfita
    Clustered = -0.8018  # c Zgrupowane
    Numerous = -0.2673  # n Liczna
    Scattered = 0.2673 # s Rozsiana
    Several = 0.8018   # v Kilka
    Solitary = 1.3363  # y Samotny


class Habitat(Enum):  # Siedlisko
    Grasses = -1.3887  # g Trawy
    Leaves = -0.9258  # l Liście
    Meadows = -0.4629  # m Łąki
    Paths = 0  # p Ścieżki
    Urban = 0.4629  # u Miasto
    Waste = 0.9258  # w Pustkowie
    Woods = 1.3887  # d Las
