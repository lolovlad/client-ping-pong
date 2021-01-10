import pygame
from Model.DataBase import DataBase
from Class.Config import Config

class Cursor(pygame.sprite.Sprite):
    
    img1 = pygame.image.load('cursor1.png')
    img2 = pygame.image.load('cursor2.png')
    
    def __init__(self, group):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(group)
        self.image = self.img1
        self.rect = self.image.get_rect()
        
    def update(self, x, y):
        config = Config("game.json")
        config.load()        
        if (x in range((config.get_window("Width") - 400) // 2, (config.get_window("Width") - 400) // 2 + 401)\
            and (y in range(200, 251) or y in range(config.get_window("Height") - 100,\
                                                    config.get_window("Height") - 100 + 51))) or\
           ((x in range((config.get_window("Width") - 475) // 2, (config.get_window("Width") - 475) // 2 + 76) or\
             x in range((config.get_window("Width") - 475) // 2 + 100, (config.get_window("Width") - 475) // 2 + 176) or\
             x in range((config.get_window("Width") - 475) // 2 + 200, (config.get_window("Width") - 475) // 2 + 276) or\
             x in range((config.get_window("Width") - 475) // 2 + 300, (config.get_window("Width") - 475) // 2 + 376) or\
             x in range((config.get_window("Width") - 475) // 2 + 400, (config.get_window("Width") - 475) // 2 + 476)) and\
            y in range(300, 376)):
            self.image = self.img2
        else:
            self.image = self.img1
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y