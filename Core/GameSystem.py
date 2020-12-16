import pygame, sys, time
from pygame.math import Vector2
from Class.Interfase.ISolid import Solide
from Core.Paddle import Paddle
from Core.Ball import Ball
from Core.Map import Map
from Core.EventSystem import EventSystem
from Core.Display import Dispaly
from Model.DataBase import DataBase
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

    def init(self, player, event_system):
        self.__player[player["side"]] = player["player"]
        self.__event_system = event_system

    def game_init(self):
        clock = pygame.time.Clock()

        pygame.mixer.music.load("endofline.ogg")
        sound_effect = pygame.mixer.Sound("beep.wav")

        self.__main_display = pygame.display.set_mode((DataBase().WINDOW_WIDTH,
                                                DataBase().WINDOW_HEIGHT + DataBase().DISPLAY_HEIGHT), 0, 32)

        DataBase().set_position_ball((self.__main_display.get_rect().centerx,
                                      self.__main_display.get_rect().centery - DataBase().DISPLAY_HEIGHT))

        self.__paddle_left = Paddle(DataBase().get_position_paddles()[0], [10, 100], DataBase().WHITE, 4, 4, 13, 1)
        self.__paddle_right = Paddle(DataBase().get_position_paddles()[1], [10, 100], DataBase().WHITE, 4, 4, 13, 2)

        self.__ball = Ball(DataBase().get_position_ball(), [10, 10], DataBase().WHITE,
                           5, 2, 8, (random.uniform(-0.5, 0.5), random.uniform(-0.2, 0.2)))
        self.__map = Map(DataBase().RED, DataBase().border_position, DataBase().border_size,
                         DataBase().BUR, DataBase().energy_position, DataBase().energy_size)

        event_system = EventSystem({"paddle": {"left": self.__paddle_left,
                                               "right": self.__paddle_right}, "ball": self.__ball, "map": self.__map},
                                   self)
        Dispaly().init(DataBase().WINDOW_HEIGHT + DataBase().DISPLAY_HEIGHT,
                       DataBase().WINDOW_WIDTH, DataBase().WHITE, DataBase().BLACK, self.__main_display)
        GameSystem().init({"side": "left", "player": self.__paddle_left}, event_system)

        self.__main_sprites.add(*self.__map.get_borders_render())
        self.__main_sprites.add(*self.__map.get_energy_render())
        self.__main_sprites.add(self.__paddle_left, self.__ball, self.__paddle_right)

    def update_game(self):
        self.__main_display.fill((0, 0, 0))
        self.__event_system.update()
        Dispaly().render_score_bord()
        Dispaly().render_energy_hud(DataBase().hud_energy[0], DataBase().hud_energy[1])
        self.__main_sprites.draw(self.__main_display)

    def restart(self):
        self.__paddle_left.energy = 33
        self.__paddle_left.position = DataBase().get_position_paddles()[0]
        self.__paddle_left.direction = (0, 0)
        self.__paddle_left.is_power_hit = False
        self.__ball.position = DataBase().get_position_ball()
        self.__ball.direction = Vector2((random.uniform(-0.5, 0.5), random.uniform(-0.2, 0.2)))

    def game_over(self, i):
        DataBase().is_playing = False
        self.__main_display.fill(DataBase().BLACK)
        Dispaly().render_game_over(i, ((DataBase().WINDOW_HEIGHT + DataBase().DISPLAY_HEIGHT) // 2,
                                       DataBase().WINDOW_WIDTH // 2))
        pygame.display.update()
        time.sleep(2)
