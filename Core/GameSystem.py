import pygame, sys, time
from pygame.math import Vector2
from Class.Interfase.ISolid import Solide
from Core.Paddle import Paddle
from Core.Ball import Ball
from Core.Map import Map
from Core.EventSystem import EventSystem
from Core.Display import Dispaly
from Model.DataBase import DataBase
from Class.Config import Config
import random


class GameSystem(metaclass=Solide):
    def __init__(self):
        self.__player = {}
        self.__ball = None
        self.__event_system = None
        self.__main_display = None
        self.__paddle_left = None
        self.__paddle_right = None
        self.__ball = None
        self.__map = None
        self.__main_sprites = pygame.sprite.RenderPlain()
        self.__ball_sprites = pygame.sprite.RenderPlain()


    def init(self, player, event_system):
        self.__player[player["side"]] = player["player"]
        self.__event_system = event_system

    def game_init(self):
        clock = pygame.time.Clock()
        config = Config("game.json")
        config.load()

        pygame.mixer.music.load("endofline.ogg")
        sound_effect = pygame.mixer.Sound("beep.wav")

        self.__main_display = pygame.display.set_mode((config.get_window("Width"), config.get_window("Height")), 0, 32)

        DataBase().set_position_ball(config.get_position("Ball"))
        DataBase().set_position_paddles(config.get_position("Left_paddle"), config.get_position("Right_paddle"))

        self.__paddle_left = Paddle(config.get_position("Left_paddle"), [10, 100], DataBase().left_color,
                                    4, 4, 13, 1)
        self.__paddle_right = Paddle(config.get_position("Right_paddle"), [10, 100], DataBase().right_color,
                                     4, 4, 13, 2)

        self.__ball = [Ball(DataBase().get_position_ball(), [10, 10], config.get_color("White"),
                           5, 2, 8, (random.uniform(-0.5, 0.5), random.uniform(-0.2, 0.2)))]

        self.__map = Map(config.get_color("Red"), config.get_color("Turquoise"))

        event_system = EventSystem({"paddle": {"left": self.__paddle_left,
                                               "right": self.__paddle_right}, "ball": self.__ball, "map": self.__map},
                                   self)
        
        Dispaly().init(config.get_window("Height") - 300,
                       config.get_window("Width"), config.get_color("White"), config.get_color("Black"),
                       self.__main_display)
        
        GameSystem().init({"side": "left", "player": self.__paddle_left}, event_system)

        self.__main_sprites.add(*self.__map.get_borders_render())
        self.__main_sprites.add(*self.__map.get_energy_render())
        self.__main_sprites.add(self.__paddle_left, self.__paddle_right)
        self.__ball_sprites.add(*self.__ball)

    def update_game(self):
        self.__main_display.fill((0, 0, 0))      
        self.__event_system.update()
        Dispaly().render_score_bord()
        Dispaly().render_timer()
        Dispaly().render_energy_hud(DataBase().hud_energy[0], DataBase().hud_energy[1])
        self.__ball_sprites.add(*self.__ball)
        self.__main_sprites.draw(self.__main_display)
        self.__ball_sprites.draw(self.__main_display)

    def restart(self):
        config = Config("game.json")
        config.load()        

        self.__paddle_left.energy = 33
        self.__paddle_left.position = DataBase().get_position_paddles()[0]
        self.__paddle_left.direction = (0, 0)
        self.__paddle_left.is_power_hit = False
        self.__ball = [Ball(DataBase().get_position_ball(), [10, 10], config.get_color("White"),
                           5, 2, 8, (random.uniform(-0.5, 0.5), random.uniform(-0.2, 0.2)))]
        
    def new_ball(self):
        for i in self.__ball_sprites:
            self.__ball_sprites.remove(i)


    def game_over(self, i):
        config = Config("game.json")
        config.load()

        DataBase().is_playing = False

        self.__main_display.fill(config.get_color("Black"))

        Dispaly().render_game_over(i, (config.get_window("Height") // 2, config.get_window("Width") // 2))
        pygame.display.update()
        time.sleep(2)
