import pygame
from Model.DataBase import DataBase

class Cursor(pygame.sprite.Sprite):
    
    img1 = pygame.image.load('cursor1.png')
    img2 = pygame.image.load('cursor2.png')
    
    def __init__(self, group):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(group)
        self.image = self.img1
        self.rect = self.image.get_rect()
        
    def update(self, x, y):
        if (x in range((DataBase().WINDOW_WIDTH - 400) // 2, (DataBase().WINDOW_WIDTH - 400) // 2 + 401)\
            and (y in range(200, 251) or y in range(DataBase().WINDOW_HEIGHT + DataBase().DISPLAY_HEIGHT - 100,\
                                                    DataBase().WINDOW_HEIGHT + DataBase().DISPLAY_HEIGHT - 100 + 51))) or\
           ((x in range((DataBase().WINDOW_WIDTH - 475) // 2, (DataBase().WINDOW_WIDTH - 475) // 2 + 76) or\
             x in range((DataBase().WINDOW_WIDTH - 475) // 2 + 100, (DataBase().WINDOW_WIDTH - 475) // 2 + 176) or\
             x in range((DataBase().WINDOW_WIDTH - 475) // 2 + 200, (DataBase().WINDOW_WIDTH - 475) // 2 + 276) or\
             x in range((DataBase().WINDOW_WIDTH - 475) // 2 + 300, (DataBase().WINDOW_WIDTH - 475) // 2 + 376) or\
             x in range((DataBase().WINDOW_WIDTH - 475) // 2 + 400, (DataBase().WINDOW_WIDTH - 475) // 2 + 476)) and\
            y in range(300, 376)):
            self.image = self.img2
        else:
            self.image = self.img1
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y