from pygame.math import Vector2
from Model.Enemy import Enemy
from pygame import Rect


class Ball(Enemy):
    def __init__(self, start_position, size, color, speed, direction):
        super().__init__(start_position, size, color, speed)
        self.__direction = Vector2(direction).normalize()

    def reflect(self, new_dir):
        self.__direction = self.__direction.reflect(Vector2(new_dir))

    def move(self, e):
        hit = self.rect.collidelist(e) + 1
        print(hit)
        if hit == 3:
            self.reflect((1, 0))
        if hit == 2:
            self.reflect((-1, 0))
        if hit == 1:
            self.reflect((0, 1))
        if hit == 0:
            self.reflect((0, -1))
        self.position += self.__direction * self.speed
        self.rect.center = round(self.position.x), round(self.position.y)
