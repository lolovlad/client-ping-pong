import pygame
from pygame.locals import *
from Class.Interfase.ISolid import Solide
from Model.DataBase import DataBase


class MainMenuEvents(metaclass=Solide):
    def __init__(self, objects, name):
        self.player_name = name
        self.objects = objects

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                self.objects.update(x, y)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x in range((DataBase().WINDOW_WIDTH - 475) // 2, (DataBase().WINDOW_WIDTH - 475) // 2 + 401)\
                   and y in range(200, 251):
                    return 'nameedit'
                elif x in range((DataBase().WINDOW_WIDTH - 475) // 2, (DataBase().WINDOW_WIDTH - 475) // 2 + 401)\
                     and y in range(DataBase().WINDOW_HEIGHT + DataBase().DISPLAY_HEIGHT - 100,\
                                    DataBase().WINDOW_HEIGHT + DataBase().DISPLAY_HEIGHT - 49):
                    return 'connection'
                elif (x in range((DataBase().WINDOW_WIDTH - 475) // 2, (DataBase().WINDOW_WIDTH - 475) // 2 + 76) or\
                      x in range((DataBase().WINDOW_WIDTH - 475) // 2 + 100, (DataBase().WINDOW_WIDTH - 475) // 2 + 176) or\
                      x in range((DataBase().WINDOW_WIDTH - 475) // 2 + 200, (DataBase().WINDOW_WIDTH - 475) // 2 + 276) or\
                      x in range((DataBase().WINDOW_WIDTH - 475) // 2 + 300, (DataBase().WINDOW_WIDTH - 475) // 2 + 376) or\
                      x in range((DataBase().WINDOW_WIDTH - 475) // 2 + 400, (DataBase().WINDOW_WIDTH - 475) // 2 + 476)) and\
                     y in range(300, 376):
                    return str((x - (DataBase().WINDOW_WIDTH - 475) // 2) // 100)
                else:
                    return 'no_one'
            if event.type == pygame.KEYDOWN:
                if event.key == K_BACKSPACE:
                    if len(self.player_name) > 0:
                        self.player_name = self.player_name[:-1]
                elif event.unicode.isalpha():
                    if len(self.player_name) < 12:
                        self.player_name += event.unicode
                
