# -*- coding: utf-8 -*-
"""
    File name: MushroomLoader.py
    Author: Kacper Kaczmarek
    Python Version: 3.6.0
"""
import re


class MushroomLoader:

    def __init__(self, path):
        self.path = path
        self.inputFile = None
        self.mushrooms = []

    def import_mushrooms(self):
        self.inputFile = open(self.path)
        self.mushrooms = self.inputFile.readlines()
        self.inputFile.close()
        return self.mushrooms

    @staticmethod
    def get_mushroom_in_list(mushroom):
        mushroom = re.sub('\n', '', mushroom)
        mushroom_list = mushroom.split(",")
        return mushroom_list
