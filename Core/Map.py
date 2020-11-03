from pygame.sprite import RenderPlain
from pygame import Surface, sprite, Rect
from Model.Border import Border


class Map:
    def __init__(self, color_border, position_borders, size_borders):
        self.__color_border = color_border
        self.__borders = []
        self.__borders_render = []
        self.__position_border = position_borders
        self.__size_borders = size_borders
        self.create_border()

    def create_border(self):
        for i, z in zip(self.__position_border, self.__size_borders):
            border = Border(i, z, self.__color_border)
            self.__borders.append(border.rect)
            self.__borders_render.append(border)

    def get_borders_render(self):
        return self.__borders_render

    def get_borders(self):
        return self.__borders
