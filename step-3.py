"""
Задание:
В данном шаге реализации необходимо реализовать оптимальное создание
объектов подходящих классов, исходя из информации, полученной
от пользователя из консоли. Также необходимо доработать
строковые отображения объектов новых классов.
"""


class Liquid:
    id: int  # номер жижи, реализовать автоинкремент
    title: str  # название
    density: float  # плотность

    def __init__(self, title, density):
        """ Должно быть реализовано на прошлом шаге """
        pass

    def __str__(self):
        """ Должно быть реализовано на прошлом шаге """
        pass


class Eatable(Liquid):

    def __str__(self):
        """ Добавить уточнение, можно пить или нет и вывести признак вкуса """
        pass


class Technical(Liquid):

    def __str__(self):
        """ Добавить уточнение, можно пить или нет и вывести признак вкуса """
        pass


def sorting(sorting_list):
    """ Функция сортировки по плотности жидкости """
    pass


if __name__ == '__main__':
    liquid_list = list()
    while True:
        print('Предлагаю вам ввести параметры жидкости')
        title = input('Введите название: ')
        density = input('Введите плотность: ')
        type_of_liquid = input('Это можно пить? [Y/n]: ')
        new_item = ... # создать объект подходящего класса
        liquid_list.append(new_item)

        sorting(liquid_list)

        for i in liquid_list:
            print(i)
