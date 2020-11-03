from pygame.sprite import Sprite
from pygame import Surface
from pygame import K_UP, K_DOWN
from pygame.math import Vector2
from Model.Enemy import Enemy


class Paddle(Enemy):
    def __init__(self, start_point, size, color, speed):
        super().__init__(start_point, size, color, speed)

    def move(self, e):
        direction = Vector2((0, 0))
        if e[K_UP]:
            direction = Vector2((0, -1))
        elif e[K_DOWN]:
            direction = Vector2((0, 1))
        self.position += (direction * self.speed)
        self.rect.center = round(self.position.x), round(self.position.y)

