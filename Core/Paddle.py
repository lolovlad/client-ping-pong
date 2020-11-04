from pygame.sprite import Sprite
from pygame import Surface
from pygame import K_UP, K_DOWN, transform
from pygame.math import Vector2
from Model.Enemy import GameObject


class Paddle(GameObject):
    def __init__(self, start_point, size, color, speed,  min_speed, max_speed):
        super().__init__(start_point, size, color, speed, min_speed, max_speed, (0, 0))
        self.is_ball_direction = Vector2((1, 0))

    def move(self):
        print(self.direction * self.speed)
        self.position += (self.direction * self.speed)
        self.rect.center = round(self.position.x), round(self.position.y)

    def reflect(self, new_dir):
        self.direction = self.direction.reflect(Vector2(new_dir))
        self.move()

    def set_speed(self, speed):
        self.speed = speed

