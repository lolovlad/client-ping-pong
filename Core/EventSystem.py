import pygame, sys, time
from pygame.locals import *
from pygame.math import Vector2
from random import randint
from Class.Interfase.ISolid import Solide


class EventSystem(metaclass=Solide):
    def __init__(self, game_objects):
        self.__game_objects = game_objects

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        self.__move_player()
        self.__ball_reflect_map()
        self.__paddle_hit_map()
        self.__paddle_hit_ball()

    def __move_player(self):
        keys = pygame.key.get_pressed()
        direction = (0, 0)
        if keys[K_UP]:
            direction = (0, -1)
        elif keys[K_DOWN]:
            direction = (0, 1)
        if keys[K_LSHIFT]:
            self.__game_objects["paddle"].set_speed(10)
        else:
            self.__game_objects["paddle"].set_speed(4)
        self.__game_objects["paddle"].direction = Vector2(direction)
        self.__game_objects["paddle"].move()

    def __ball_reflect_map(self):
        hit = self.__game_objects["ball"].rect.collidelist(self.__game_objects["map"].get_borders()) + 1
        if hit == 3:
            self.__game_objects["ball"].reflect((1, 0))
        if hit == 4:
            self.__game_objects["ball"].reflect((-1, 0))
        if hit == 2:
            self.__game_objects["ball"].reflect((0, 1))
        if hit == 1:
            self.__game_objects["ball"].reflect((0, -1))

    def __paddle_hit_map(self):
        hit = self.__game_objects["paddle"].rect.collidelist(self.__game_objects["map"].get_borders()) + 1
        if hit == 2:
            self.__game_objects["paddle"].reflect((0, 1))
            self.__game_objects["paddle"].direction = Vector2((0, 0))
        if hit == 1:
            self.__game_objects["paddle"].reflect((0, -1))
            self.__game_objects["paddle"].direction = Vector2((0, 0))

    def __paddle_hit_ball(self):
        hit = self.__game_objects["ball"].rect.colliderect(self.__game_objects["paddle"].rect)
        if hit:
            self.__game_objects["ball"].direction += self.__game_objects["paddle"].is_ball_direction + \
                                                     self.__game_objects["paddle"].direction

            self.__game_objects["ball"].set_speed(1)

    def add_game_object(self, name_object, game_object):
        self.__game_objects[name_object] = game_object
