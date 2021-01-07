import json
import sys
import os


class Config:
    def __init__(self, name):
        self.__path = os.path.abspath("File/" + name)
        self.__config = {}

    def load(self):
        with open(self.__path, "r") as read_file:
            self.__config = json.load(read_file)

    def get_color(self, name):
        return tuple(self.__config["Color"][name])

    def get_position(self, name):
        return tuple(self.__config["Position"][name])

    def get_window(self, name):
        return int(self.__config["Window"][name])



