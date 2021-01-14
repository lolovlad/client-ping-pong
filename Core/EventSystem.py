import pygame, sys, time
from pygame.locals import *
from pygame.math import Vector2
import random
from Class.Interfase.ISolid import Solide
from Model.DataBase import DataBase
from Core.Network import NetWork
from Core.Display import Dispaly
from Class.Config import Config
from Core.Ball import Ball


class EventSystem(metaclass=Solide):
    def __init__(self, game_objects, game_system):
        self.__game_objects = game_objects
        self.__game_system = game_system

    def update(self):
        event_sps = {"K_z": "False",
                     "K_up": "False",
                     "K_down": "False",
                     "K_lshift": "False",
                     "side": DataBase().side}
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_z:
                    event_sps["K_z"] = "True"
            if event.type == DataBase().restart:
                self.__game_system.restart()
            if event.type == DataBase().game_over:
                self.__game_system.game_over(event.message)

            if event.type == DataBase().move_paddle:
                info = event.message
                self.move_paddle(info["x"], info["y"], info["energy"])

            if event.type == DataBase().move_ball:
                info = event.message
                self.move_ball(info["x"], info["y"])

            if event.type == DataBase().energy_map:
                info = event.message
                self.energy_map(info["id_energy"], info["flag"])

        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            event_sps["K_up"] = "True"
        elif keys[K_DOWN]:
            event_sps["K_down"] = "True"
        if keys[K_LSHIFT]:
            event_sps["K_lshift"] = "True"
        NetWork().send_message(event_sps)

    def move_paddle(self, x, y, energy):
        self.__game_objects["paddle"]["left"].rect.center = x[0], y[0]
        self.__game_objects["paddle"]["right"].rect.center = x[1], y[1]
        self.__game_objects["paddle"]["left"].energy = energy[0]
        self.__game_objects["paddle"]["right"].energy = energy[1]
        DataBase().hud_energy[0] = self.__game_objects["paddle"][DataBase().side].energy
        DataBase().hud_energy[1] = self.__game_objects["paddle"][DataBase().side].position.x

    def move_ball(self, x, y):
        config = Config("game.json")
        config.load()
        if len(self.__game_objects["ball"]) < len(x):          
            t = len(self.__game_objects["ball"])
            for i in range(len(self.__game_objects["ball"])):
                self.__game_objects["ball"].append(Ball((self.__game_objects["ball"][i].rect.center), [10, 10], config.get_color("White"),
                               5, 2, 8, (x[t + 2 * i], y[t + 2 * i])))
                self.__game_objects["ball"].append(Ball((self.__game_objects["ball"][i].rect.center), [10, 10], config.get_color("White"),
                               5, 2, 8, (x[t + 1 + 2 * i], y[t + 1 + 2 * i])))
        try:
            for i in range(len(self.__game_objects["ball"])):
                self.__game_objects["ball"][i].rect.center = x[i], y[i]
        except:
            for i in self.__game_objects["ball"]:
                self.__game_objects["ball"].remove(i)
            self.__game_system.new_ball()

    def energy_map(self, id_energy, flag):
        config = Config("game.json")
        config.load()
        for i, z in zip(id_energy, flag):
            energy = self.__game_objects["map"].get_energy_render()[i]
            energy.is_energy = z
            if z:
                energy.image.fill(config.get_color("Turquoise"))
            else:
                energy.image.fill(config.get_color("Black"))