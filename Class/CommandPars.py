from Core.Network import NetWork
from Model.DataBase import DataBase
from Class.Interfase.IObserver import Observer
from pygame import event


class CommandPars(Observer):
    def update(self, subject):
        subject = subject.pop()
        if subject["Type_message"] == "Server":
            if subject["Type_command"] == "Started_game":
                DataBase().side = subject["Side"]
                if subject["Side"] == 'left':
                    DataBase().left_color = subject["Color"]
                    DataBase().right_color = subject["EnemyColor"]
                else:
                    DataBase().left_color = subject["EnemyColor"]
                    DataBase().right_color = subject["Color"]                    
                DataBase().is_playing = True
            if subject["Type_command"] == "Game_over":
                DataBase().game_over_event.message = subject["Win"]
                event.post(DataBase().game_over_event)
        elif subject["Type_message"] == "Update_position":
            position = subject["Position"]

            DataBase().move_paddle_event.message = position["paddle"]
            event.post(DataBase().move_paddle_event)

            DataBase().move_ball_event.message = position["balls"]
            event.post(DataBase().move_ball_event)

            DataBase().energy_map_event.message = position["energy"]
            event.post(DataBase().energy_map_event)
            DataBase().score = position["score"]
            DataBase().timer = position["timer"]