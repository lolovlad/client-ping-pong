import pygame
import time
from Core.GameSystem import GameSystem
from Model.DataBase import DataBase


counter = 0


def game_start(co=0):
    pygame.init()
    clock = pygame.time.Clock()

    pygame.mixer.music.load("endofline.ogg")
    sound_effect = pygame.mixer.Sound("beep.wav")
    GameSystem().game_init()
    while DataBase().is_playing:
        clock.tick(60)
        GameSystem().update_game()
        pygame.display.update()

        if co == 0:
            time.sleep(1.5)
            pygame.mixer.music.play(-1, 0.5)
        co += 1

    while True:
        clock.tick(60)
        GameSystem().game_over()
        pygame.display.update()


game_start(counter)
