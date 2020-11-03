from pygame.sprite import Sprite
from pygame import Surface
from pygame.math import Vector2


class Enemy(Sprite):
    def __init__(self, start_point, size, color, speed):
        Sprite.__init__(self)

        self.image = Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.position = Vector2(start_point)

        self.rect.centerx, self.rect.centery = self.position.x, self.position.y

    def move(self, e):
        pass
