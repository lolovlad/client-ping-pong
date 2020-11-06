from Class.Interfase.ISolid import Solide
from Class.Interfase.IObserver import Subject


class DataBaseNetwork(Subject):
    __list_command = []
    __observers = []
    __metaclass__ = Solide

    def attach(self, observer):
        self.__observers.append(observer)

    def detach(self, observer):
        self.__observers.remove(observer)

    def notify(self, message):
        for i in self.__observers:
            i.update(message)

    def get_list_command(self):
        return self.__list_command

    def add_list_command(self, command):
        self.__list_command.append(command)
        self.notify(self.__list_command)