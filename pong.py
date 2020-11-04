import pygame, sys, time
from pygame.locals import *
from pygame.math import Vector2
from random import randint
from Core.Paddle import Paddle
from Core.Ball import Ball
from Core.Map import Map
from Core.EventSystem import EventSystem
import random

pygame.init()

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 600

clock = pygame.time.Clock()

player1_win = False
player2_win = False

PADDLE_SPEED = 10

pygame.mixer.music.load("endofline.ogg")
sound_effect = pygame.mixer.Sound("beep.wav")

### colors ###
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


border_position = ((0, 0), (0, WINDOW_HEIGHT - 5), (0, 0), (WINDOW_WIDTH - 5, 0))
border_size = ([WINDOW_WIDTH, 5], [WINDOW_WIDTH, 5], [5, WINDOW_HEIGHT], [5, WINDOW_HEIGHT])

energy_position = ((45, 100), (45, 500), (WINDOW_WIDTH - 55, 100), (WINDOW_WIDTH - 45, 500))
energy_size = ([10, 10], [10, 10], [10, 10], [10, 10])

### Creating the main surface ###
main_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
surface_rect = main_surface.get_rect()

basic_font = pygame.font.SysFont("Helvetica", 120)
game_over_font_big = pygame.font.SysFont("Helvetica", 72)
game_over_font_small = pygame.font.SysFont("Helvetica", 50)

paddle1 = Paddle((main_surface.get_rect().left + 50, main_surface.get_rect().centery), [10, 100], WHITE, 4, 4, 13, 1)
ball = Ball(main_surface.get_rect().center, [10, 10], WHITE, 5, 2, 8, (random.random(), random.random()))
main_map = Map((255, 0, 0), border_position, border_size, (0, 255, 255), energy_position, energy_size)

event_system = EventSystem({"paddle": paddle1, "ball": ball, "map": main_map})


all_sprites = pygame.sprite.RenderPlain()
all_sprites.add(*main_map.get_borders_render())
all_sprites.add(*main_map.get_energy_render())
all_sprites.add(paddle1, ball)


player1_score = 0
player2_score = 0

counter = 0

while True:

    clock.tick(60)

    event_system.update()
    ball.move()
    keys = pygame.key.get_pressed()
    score_board = basic_font.render(str(player1_score) + "           " + str(player2_score), True, WHITE, BLACK) 
    score_board_rect = score_board.get_rect()
    score_board_rect.centerx = surface_rect.centerx 
    score_board_rect.y = 10

    main_surface.fill(BLACK)

    main_surface.blit(score_board, score_board_rect)

    netx = surface_rect.centerx

    net_rect0 = pygame.Rect(netx, 0, 5, 5)
    net_rect1 = pygame.Rect(netx, 60, 5, 5)
    net_rect2 = pygame.Rect(netx, 120, 5, 5)
    net_rect3 = pygame.Rect(netx, 180, 5, 5)
    net_rect4 = pygame.Rect(netx, 240, 5, 5)
    net_rect5 = pygame.Rect(netx, 300, 5, 5)
    net_rect6 = pygame.Rect(netx, 360, 5, 5)
    net_rect7 = pygame.Rect(netx, 420, 5, 5)
    net_rect8 = pygame.Rect(netx, 480, 5, 5)
    net_rect9 = pygame.Rect(netx, 540, 5, 5)
    net_rect10 = pygame.Rect(netx, 595, 5, 5)



    pygame.draw.rect(main_surface, WHITE, (net_rect0.left, net_rect0.top, net_rect0.width, net_rect0.height))
    pygame.draw.rect(main_surface, WHITE, (net_rect1.left, net_rect1.top, net_rect1.width, net_rect1.height))
    pygame.draw.rect(main_surface, WHITE, (net_rect2.left, net_rect2.top, net_rect2.width, net_rect2.height))
    pygame.draw.rect(main_surface, WHITE, (net_rect3.left, net_rect3.top, net_rect3.width, net_rect3.height))
    pygame.draw.rect(main_surface, WHITE, (net_rect4.left, net_rect4.top, net_rect4.width, net_rect4.height))
    pygame.draw.rect(main_surface, WHITE, (net_rect5.left, net_rect5.top, net_rect5.width, net_rect5.height))
    pygame.draw.rect(main_surface, WHITE, (net_rect6.left, net_rect6.top, net_rect6.width, net_rect6.height))
    pygame.draw.rect(main_surface, WHITE, (net_rect7.left, net_rect7.top, net_rect7.width, net_rect7.height))
    pygame.draw.rect(main_surface, WHITE, (net_rect8.left, net_rect8.top, net_rect8.width, net_rect8.height))
    pygame.draw.rect(main_surface, WHITE, (net_rect9.left, net_rect9.top, net_rect9.width, net_rect9.height))
    pygame.draw.rect(main_surface, WHITE, (net_rect10.left, net_rect10.top, net_rect10.width, net_rect10.height))


    all_sprites.draw(main_surface)

    if ball.rect.x > WINDOW_WIDTH:
        player1_score += 1
    elif ball.rect.x < 0:
        player2_score += 1

    

    pygame.display.update()

    if counter == 0:
        time.sleep(1.5)
        pygame.mixer.music.play(-1, 0.5)

    if player1_score == 5:
        player1_win = True
        break
    elif player2_score == 5:
        player2_win = True
        break

    counter += 1

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    main_surface.fill(BLACK)

    if player1_win == True:
        game_over = game_over_font_big.render("GAME OVER", True, WHITE, BLACK)
        game_over1 = game_over_font_small.render("Player 1 Wins", True, WHITE, BLACK)
    elif player2_win == True:
        game_over = game_over_font_big.render("GAME OVER", True, WHITE, BLACK)
        game_over1 = game_over_font_small.render("Player 2 Wins", True, WHITE, BLACK)

    game_over_rect = game_over.get_rect()
    game_over_rect.centerx = surface_rect.centerx
    game_over_rect.centery = surface_rect.centery - 50
    game_over1_rect = game_over1.get_rect()
    game_over1_rect.centerx = game_over_rect.centerx
    game_over1_rect.centery = game_over_rect.centery + 75

    main_surface.blit(game_over, game_over_rect)
    main_surface.blit(game_over1, game_over1_rect)

    pygame.display.update()

    







