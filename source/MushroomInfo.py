# -*- coding: utf-8 -*-
"""
    File name: MushroomInfo.py
    Author: Kacper Kaczmarek
    Python Version: 3.6.0
"""
from enum import Enum


class Edible(Enum):
    No = 0  # p
    Yes = 1  # e
    NoInfo = 2


class CapShape(Enum):  # kształt kapelusza
    Bell = 1  # b Dzwon
    Conical = 2  # c Stożkowy
    Convex = 3  # x Wypukły
    Flat = 4  # f Płaski
    Knobbed = 5  # k Wybrzuszony
    Sunken = 6  # s Wklęsły


class CapSurface(Enum):  # Powierzchnia kapelusza
    Fibrous = 1  # f Włóknisty
    Grooves = 2  # g Wypustkowaty
    Scaly = 3  # t Łuskowaty
    Smooth = 4  # s Gładki


class CapColor(Enum):
    Brown = 1  # n Brązowy
    Buff = 2  # b Kolor skóry (brązowo-żółtyO
    Cinnamon = 3  # c Cynamonowy
    Gray = 4  # g Szary
    Green = 5  # r Zielony
    Pink = 6  # p Różowy
    Purple = 7  # u Fioletowy
    Red = 8  # e Czerwony
    White = 9  # w Biały
    Yellow = 10  # y Żółty


class Bruises(Enum):  # Siniaki
    Yes = 1  # t Tak
    No = 2  # f Nie


class Odor(Enum):  # Zapach
    Almond = 1  # a Migdałowy
    Anise = 2  # l Anyż
    Creosote = 3  # c Kreozot
    Fishy = 4  # y Rybny(podejrzany)
    Foul = 5  # f Mdły
    Musty = 6  # m Stęchły
    Without = 7  # n Bez
    Pungent = 8  # p Cierpki, Ostry, Gryzący
    Spicy = 9  # s Pikantny, Korzenny


class GillAttachment(Enum):  # Załącznik blaszek
    Attached = 1  # a Przywiązane
    Descending = 2  # d Schodzące
    Free = 3  # f Wolne
    Notched = 4  # n Zaząbkowane


class GillSpacing(Enum):  # Odległości blaszek
    Close = 1  # c Blisko
    Crowded = 2  # w Tłoczno
    Distant = 3  # d Odległe


class GillSize(Enum):  # Wielkości blaszek
    Broad = 1  # b Szerokie
    Narrow = 2  # n Wąskie


class GillColor(Enum):  # Kolory blaszek
    Black = 1  # k
    Brown = 2  # n
    Buff = 3  # b
    Chocolate = 4  # h
    Gray = 5  # g
    Green = 6  # r
    Orange = 7  # o
    Pink = 8  # p
    Purple = 9  # u
    Red = 10  # e
    White = 11  # w
    Yellow = 12  # y


class StalkShape(Enum):  # Kształt łodygi
    Enlarging = 1  # e Powiększająca się
    Tapering = 2  # t Zmniejszająca się


class StalkRoot(Enum):  # Korzeń łodygi
    Bulbous = 1  # b Bulwa
    Club = 2  # c Maczuga
    Cup = 3  # u Puchar
    Equal = 4  # e Równa
    Rhizomorphs = 5  # z Ryzomorfy(takie długie czarne korzenie)
    Rooted = 6  # r Normalne
    Missing = 7  # ? Bez


class StalkSurfaceAboveRing(Enum):  # Powierzchnia łodyg powyżej pierścienia
    Fibrous = 1  # f Włoknisty
    Scaly = 2  # y Łuszczący się
    Silky = 3  # k Jedwabisty
    Smooth = 4  # s Gładki


class StalkSurfaceBelowRing(Enum):  # Powierzchnia łodyg poniżej pierwscienia
    Fibrous = 1  # f Włoknisty
    Scaly = 2  # y Łuszczący się
    Silky = 3  # k Jedwabisty
    Smooth = 4  # s Gładki


class StalkColorAboveRing(Enum):  # Kolor łodygi powyżej pierścienia
    Brown = 1  # n
    Buff = 2  # b
    Cinnamon = 3  # c
    Gray = 4  # g
    Orange = 5  # o
    Pink = 6  # p
    Red = 7  # e
    White = 8  # w
    Yellow = 9  # y


class StalkColorBelowRing(Enum):  # Kolor łodygi powyżej pierścienia
    Brown = 1  # n
    Buff = 2  # b
    Cinnamon = 3  # c
    Gray = 4  # g
    Orange = 5  # o
    Pink = 6  # p
    Red = 7  # e
    White = 8  # w
    Yellow = 9  # y


class VeilType(Enum):  # Rodzaj osłony
    Partial = 1  # p Częściowy
    Universal = 2  # u https://en.wikipedia.org/wiki/Universal_veil


class VeilColor(Enum):  # Kolor osłony
    Brown = 1  # n
    Orange = 2  # o
    White = 3  # w
    Yellow = 4  # y


class RingNumber(Enum):  # Liczba pierścieni
    Zero = 1  # n
    One = 2  # o
    Two = 3  # t


class RingType(Enum):  # Rodzaj pierścienia
    Cobwebby = 1  # c Pajęczynowy
    Evanescent = 2  # e Zanikający
    Flaring = 3  # f Kloszowy
    Large = 4  # l Duży
    No = 5  # n Bez
    Pendant = 6  # p Wisiorek
    Sheathing = 7  # s Poszycie
    Zone = 8  # z Strefowy


class SporePrintColor(Enum):
    Black = 1  # k
    Brown = 2  # n
    Buff = 3  # b
    Chocolate = 4  # h
    Green = 5  # r
    Orange = 6  # o
    Purple = 7  # u
    White = 8  # w
    Yellow = 9  # y


class Population(Enum):  # Populacja
    Abundant = 1  # a Obfita
    Clustered = 2  # c Zgrupowane
    Numerous = 3  # n Liczna
    Scattered = 4  # s Rozsiana
    Several = 5  # v Kilka
    Solitary = 6  # y Samotny


class Habitat(Enum):  # Siedlisko
    Grasses = 1  # g Trawy
    Leaves = 2  # l Liście
    Meadows = 3  # m Łąki
    Paths = 4  # p Ścieżki
    Urban = 5  # u Miasto
    Waste = 6  # w Pustkowie
    Woods = 7  # d Las
