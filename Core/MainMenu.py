import pygame
from Class.Interfase.ISolid import Solide
from Core.Cursor import Cursor
from Core.MainMenuEvents import MainMenuEvents
from Model.DataBase import DataBase
from Class.Config import Config

class Picture(pygame.sprite.Sprite):
    def __init__(self, img, group):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(group)
        self.image = img
        self.rect = self.image.get_rect()
        

class MainMenu(metaclass=Solide):
    def __init__(self, name):
        self.__main_display = None
        self.__main_sprites = pygame.sprite.RenderPlain()
        self.cursor_sprites = pygame.sprite.RenderPlain()
        self.button = 'no_one'
        self.player_name = name
        self.menu_events = None
        self.skin = 0

    def game_init(self):
        config = Config("game.json")
        config.load()

        self.button = 'no_one'
        self.__main_display = pygame.display.set_mode((config.get_window("Width"), config.get_window("Height")))
        self.__main_display.fill((0, 0, 0))
        pygame.display.set_caption('Ping-Pong 2.0')
        Picture(pygame.image.load('mainmenu.png'), self.__main_sprites)
        Cursor(self.cursor_sprites)
        self.menu_events = MainMenuEvents(self.cursor_sprites, self.player_name)
        

    def update_game(self):
        config = Config("game.json")
        config.load()
        
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
            self.__main_display.blit(text, ((config.get_window("Width") - 400) // 2, 255))
            self.player_name = self.menu_events.player_name
            
        pygame.draw.rect(self.__main_display, col, ((config.get_window("Width") - 400) // 2, 200, 400, 50), 3)
        text = pygame.font.Font(None, 50).render(self.player_name, True, col)
        self.__main_display.blit(text, ((config.get_window("Width") - 400) // 2 + 8, 210))
        
        pygame.draw.rect(self.__main_display, 'white', ((config.get_window("Width") - 475) // 2, 300, 75, 75), 0)
        pygame.draw.rect(self.__main_display, 'red', ((config.get_window("Width") - 475) // 2 + 100, 300, 75, 75), 0)
        pygame.draw.rect(self.__main_display, 'green', ((config.get_window("Width") - 475) // 2 + 200, 300, 75, 75), 0)
        pygame.draw.rect(self.__main_display, 'blue', ((config.get_window("Width") - 475) // 2 + 300, 300, 75, 75), 0)
        pygame.draw.rect(self.__main_display, 'yellow', ((config.get_window("Width") - 475) // 2 + 400, 300, 75, 75), 0)
        
        if len(self.button) == 1:
            self.skin = int(self.button)
        pygame.draw.rect(self.__main_display, 'green', (self.skin * 100 + (config.get_window("Width")- 475) // 2 - 5,\
                                                        295, 85, 85), 3)
        
        pygame.draw.rect(self.__main_display, 'red', ((config.get_window("Width") - 400) // 2,\
                                                      config.get_window("Height") - 100,\
                                                      400, 50), 0)
        if self.button != 'connection':
            text = pygame.font.Font(None, 50).render('Начать игру', True, 'white')
            self.__main_display.blit(text, ((config.get_window("Width") - 400) // 2 + 98,\
                                            config.get_window("Height") - 90))
        else:
            text = pygame.font.Font(None, 50).render('Поиск игроков...', True, 'white')
            self.__main_display.blit(text, ((config.get_window("Width") - 400) // 2 + 68,\
                                            config.get_window("Height") - 90))
        
        if pygame.mouse.get_focused():
            self.cursor_sprites.draw(self.__main_display)