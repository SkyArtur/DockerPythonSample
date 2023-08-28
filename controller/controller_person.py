import os
from functions import input_numeric
from views import ViewPerson
from pathlib import Path
from datetime import datetime


class ControllerPerson:
    def __init__(self):
        self.__templates = Path(__file__).resolve().parent.parent.joinpath('templates')
        self.__view = ViewPerson()
        self.__execute = True

    def __read_file(self, filename):
        with open(self.__templates.joinpath(filename), encoding='utf8') as file:
            return file.read()

    @property
    def execute(self):
        return self.__execute

    @staticmethod
    def clear_screen():
        return os.system('cls' if os.name in 'nt' else 'clear')

    def opening(self):
        date_hour = datetime.today()
        self.clear_screen()
        print(
            self.__read_file('opening.txt').format(
                date_hour.strftime('%d/%m/%Y'),
                date_hour.strftime('%H:%M:%S')
            )
        )

    def menu(self):
        resp = input_numeric(self.__read_file('menu.txt'), minn=0, maxx=5)
        if resp == 1:
            self.clear_screen()
            self.__view.new_person()
        elif resp == 2:
            self.clear_screen()
            self.__view.update_person()
        elif resp == 3:
            self.clear_screen()
            self.__view.get_one_person()
        elif resp == 4:
            self.clear_screen()
            self.__view.get_all_persons()
        elif resp == 5:
            self.clear_screen()
            self.__view.delete_person()
        else:
            self.__execute = False
            self.clear_screen()
            return
        input('\n\nDigite qualquer tecla para continuar....')
        self.clear_screen()
