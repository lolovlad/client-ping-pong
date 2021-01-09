import pygame
from Class.Interfase.ISolid import Solide
from Core.Cursor import Cursor
from Core.MainMenuEvents import MainMenuEvents
from Model.DataBase import DataBase

class Picture(pygame.sprite.Sprite):
    def __init__(self, img, group):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(group)
        self.image = img
        self.rect = self.image.get_rect()
        

class MainMenu(metaclass=Solide):
    def __init__(self):
        self.__main_display = None
        self.__main_sprites = pygame.sprite.RenderPlain()
        self.cursor_sprites = pygame.sprite.RenderPlain()
        self.button = 'no_one'
        self.player_name = 'Игрок'
        self.menu_events = None
        self.skin = 0

    def game_init(self):
        self.__main_display = pygame.display.set_mode((DataBase().WINDOW_WIDTH,\
                                                       DataBase().WINDOW_HEIGHT + DataBase().DISPLAY_HEIGHT))
        self.__main_display.fill((0, 0, 0))
        pygame.display.set_caption('Ping-Pong 2.0')
        Picture(pygame.image.load('mainmenu.png'), self.__main_sprites)
        Cursor(self.cursor_sprites)
        self.menu_events = MainMenuEvents(self.cursor_sprites, self.player_name)
        

    def update_game(self):
        self.__main_display.fill((0, 0, 0))
        self.menu_events.player_name = self.player_name
        t = self.menu_events.update()
        if t != None and self.button != 'connection':
            self.button = t
            
        self.__main_sprites.draw(self.__main_display)
        
        if self.button != 'nameedit':
            col = 'white'
        else:
            col = 'yellow'
            text = pygame.font.Font(None, 25).render('Введите свое имя', True, col)
            self.__main_display.blit(text, ((DataBase().WINDOW_WIDTH - 400) // 2, 255))
            self.player_name = self.menu_events.player_name
            
        pygame.draw.rect(self.__main_display, col, ((DataBase().WINDOW_WIDTH - 400) // 2, 200, 400, 50), 3)
        text = pygame.font.Font(None, 50).render(self.player_name, True, col)
        self.__main_display.blit(text, ((DataBase().WINDOW_WIDTH - 400) // 2 + 8, 210))
        
        pygame.draw.rect(self.__main_display, 'white', ((DataBase().WINDOW_WIDTH - 475) // 2, 300, 75, 75), 0)
        pygame.draw.rect(self.__main_display, 'red', ((DataBase().WINDOW_WIDTH - 475) // 2 + 100, 300, 75, 75), 0)
        pygame.draw.rect(self.__main_display, 'green', ((DataBase().WINDOW_WIDTH - 475) // 2 + 200, 300, 75, 75), 0)
        pygame.draw.rect(self.__main_display, 'blue', ((DataBase().WINDOW_WIDTH - 475) // 2 + 300, 300, 75, 75), 0)
        pygame.draw.rect(self.__main_display, 'yellow', ((DataBase().WINDOW_WIDTH - 475) // 2 + 400, 300, 75, 75), 0)
        
        if len(self.button) == 1:
            self.skin = int(self.button)
        pygame.draw.rect(self.__main_display, 'green', (self.skin * 100 + (DataBase().WINDOW_WIDTH - 475) // 2 - 5,\
                                                        295, 85, 85), 3)
        
        pygame.draw.rect(self.__main_display, 'red', ((DataBase().WINDOW_WIDTH - 400) // 2,\
                                                      DataBase().WINDOW_HEIGHT + DataBase().DISPLAY_HEIGHT - 100,\
                                                      400, 50), 0)
        if self.button != 'connection':
            text = pygame.font.Font(None, 50).render('Начать игру', True, 'white')
            self.__main_display.blit(text, ((DataBase().WINDOW_WIDTH - 400) // 2 + 98,\
                                            DataBase().WINDOW_HEIGHT + DataBase().DISPLAY_HEIGHT - 90))
        else:
            text = pygame.font.Font(None, 50).render('Поиск игроков...', True, 'white')
            self.__main_display.blit(text, ((DataBase().WINDOW_WIDTH - 400) // 2 + 68,\
                                            DataBase().WINDOW_HEIGHT + DataBase().DISPLAY_HEIGHT - 90))
        
        if pygame.mouse.get_focused():
            self.cursor_sprites.draw(self.__main_display)