import pygame
import time
import os
import sys
from Core.GameSystem import GameSystem
from Core.MainMenu import MainMenu
from Model.DataBase import DataBase
from threading import Thread
from Core.Network import NetWork
from Model.DataBaseNetwork import DataBaseNetwork
from Class.CommandPars import CommandPars

counter = 0

user_name = 'Игрок'
ip = 42
color = 'white'
    
def network_core(net, mmr):
    net.send_message({"Type_Command": "Login", "Name_user": user_name, "Color": color, "Ip_user": ip, "Mmr_user": mmr})
    while True:
        command = net.listener()
        if command is not None:
            DataBaseNetwork().add_list_command(command)
        else:
            break
    net.close()


def game_start(co=0):
    global user_name
    pygame.init()
    clock = pygame.time.Clock()

    pygame.mixer.music.load("endofline.ogg")
    GameSystem().game_init()
    pygame.display.set_caption(f'Ping-Pong 2.0 {user_name}')

    while DataBase().is_playing:
        clock.tick(120)
        GameSystem().update_game()
        pygame.display.update()

        if co == 0:
            pygame.mixer.music.play(-1, 0.5)
        co += 1
    pygame.quit()

    
def game_menu():
    global user_name, color
    co = 0
    pygame.init()
    clock = pygame.time.Clock()
    pygame.mixer.music.load("Tron_legacy_end.ogg")
    pygame.mixer.music.play(-1, 0.5)
    mm = MainMenu(user_name)
    mm.game_init()
    pygame.mouse.set_visible(False)
    while not DataBase().is_playing:
        clock.tick(120)
        mm.update_game()
        pygame.display.update()
        if mm.button == 'connection' and co == 0:
            user_name = mm.player_name
            color = ['white', 'red', 'green', 'blue', 'yellow'][mm.skin]
            socket = NetWork()
            socket('localhost', 2510)
            DataBaseNetwork().attach(CommandPars())
            Thread(target=network_core, args=(socket, 1000,), daemon=True).start()
            co += 1
    pygame.quit()

while True:
    game_menu()
    if DataBase().is_playing:
        game_start(counter)
    os.execl(sys.executable, 'python', __file__, *sys.argv[1:])