import pygame
import time
from Core.GameSystem import GameSystem
from Model.DataBase import DataBase
from threading import Thread
from Core.Network import NetWork
from Model.DataBaseNetwork import DataBaseNetwork
from Class.CommandPars import CommandPars

counter = 0


user_name = input()
ip = int(input())


def network_core(net, mmr):
    net.send_message({"Type_Command": "Login", "Name_user": user_name, "Ip_user": ip, "Mmr_user": mmr})
    while True:
        command = net.listener()
        if command is not None:
            DataBaseNetwork().add_list_command(command)
        else:
            break
    net.close()


socket = NetWork()
socket('192.168.0.108', 2510)
DataBaseNetwork().attach(CommandPars())
Thread(target=network_core, args=(socket, 1000,), daemon=True).start()


def game_start(co=0):
    pygame.init()
    clock = pygame.time.Clock()

    pygame.mixer.music.load("endofline.ogg")
    GameSystem().game_init()
    while DataBase().is_playing:
        clock.tick(120)
        GameSystem().update_game()
        pygame.display.update()

        if co == 0:
            pygame.mixer.music.play(-1, 0.5)
        co += 1
    pygame.quit()


while True:
    if DataBase().is_playing:
        game_start(counter)
