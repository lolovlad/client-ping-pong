import pygame, sys, time
from pygame.locals import *
from pygame.math import Vector2
from random import randint
from Class.Interfase.ISolid import Solide


class EventSystem(metaclass=Solide):
    def __init__(self, game_objects):
        self.__game_objects = game_objects
        pygame.time.set_timer(self.__game_objects["paddle"].power_hit, 0)

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == self.__game_objects["paddle"].power_hit:
                self.__game_objects["paddle"].is_power_hit = False
                pygame.time.set_timer(self.__game_objects["paddle"].power_hit, 0)
            if event.type == KEYDOWN:
                if event.key == K_z:
                    self.__game_objects["paddle"].is_power_hit = True
                    self.__game_objects["paddle"].punch()
                    pygame.time.set_timer(self.__game_objects["paddle"].power_hit, 100)
            for i in self.__game_objects["map"].get_energy_render():
                if event.type == i.energy_take:
                    i.is_energy = True
                    i.image.fill((0, 255, 255))
                    pygame.time.set_timer(i.energy_take, 0)

        self.__move_player()
        self.__ball_reflect_map()
        self.__paddle_hit_map()
        self.__paddle_hit_ball()
        self.__hit_energy()

    def __move_player(self):
        keys = pygame.key.get_pressed()
        direction = (0, 0)
        if keys[K_UP]:
            direction = (0, -1)
        elif keys[K_DOWN]:
            direction = (0, 1)
        self.__game_objects["paddle"].run(keys[K_LSHIFT])
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

            speed_punch = self.__game_objects["paddle"].punch()
            self.__game_objects["ball"].set_speed(speed_punch)

    def add_game_object(self, name_object, game_object):
        self.__game_objects[name_object] = game_object

    def __hit_energy(self):
        hit = self.__game_objects["paddle"].rect.collidelist(self.__game_objects["map"].get_energy())
        if hit != -1:
            energy = self.__game_objects["map"].get_energy_render()[hit]
            if energy.is_energy:
                energy.is_energy = False
                energy.image.fill((0, 0, 0))
                pygame.time.set_timer(energy.energy_take, 10000)
                self.__game_objects["paddle"].set_energy(energy.energy)
