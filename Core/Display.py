from pygame import font
from Class.Interfase.ISolid import Solide
from Model.DataBase import DataBase


class Dispaly(metaclass=Solide):
    def __init__(self):
        self.__basic_font = font.SysFont("Helvetica", 120)
        self.__game_over_font_big = font.SysFont("Helvetica", 72)
        self.__score = font.SysFont("Helvetica", 50)
        self.__energy = font.SysFont("Helvetica", 30)
        self.__height = 0
        self.__width = 0
        self.__color_text = 0
        self.__color_font = 0
        self.__display = None

    def init(self, height, width, color_text, color_font, display):
        self.__height = height
        self.__width = width
        self.__color_text = color_text
        self.__color_font = color_font
        self.__display = display

    def render_score_bord(self):
        score_board = self.__score.render('{0}    :    {1}'.format(DataBase().score[1] // 2, DataBase().score[0] // 2),
                                          True, self.__color_text, self.__color_font)
        score_board_rect = score_board.get_rect()
        score_board_rect.centerx = self.__width // 2
        score_board_rect.y = self.__height + (300 // 2)
        self.__display.blit(score_board, score_board_rect)

    def render_timer(self):
        score_board = self.__score.render('{0}'.format(DataBase().timer), True, self.__color_text, self.__color_font)
        score_board_rect = score_board.get_rect()
        score_board_rect.centerx = self.__width // 2
        score_board_rect.y = self.__height + 75
        self.__display.blit(score_board, score_board_rect)

    def render_energy_hud(self, energy, x):
        energy_board = self.__energy.render('{0}'.format(round(energy)), True, self.__color_text, self.__color_font)
        energy_board_rect = energy_board.get_rect()
        energy_board_rect.centerx = x
        energy_board_rect.y = self.__height + (300 // 2)
        self.__display.blit(energy_board, energy_board_rect)

    def render_game_over(self, player, coord):
        game_over_board = self.__game_over_font_big.render(str(player), True, self.__color_text, self.__color_font)
        game_over_board_rect = game_over_board.get_rect()
        game_over_board_rect.center = coord
        self.__display.blit(game_over_board, game_over_board_rect)

