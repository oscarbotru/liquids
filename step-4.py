class Liquid:
    id: int  # номер жижи, реализовать автоинкремент
    title: str  # название
    density: float  # плотность

    def __init__(self, title, density):
        """ Должно быть реализовано на прошлом шаге """

    def __str__(self):
        """ Должно быть реализовано на прошлом шаге """


class Eatable(Liquid):
    __taste: str  # вкус, для которого нужно реализовать getter/setter

    def __str__(self):
        """ Добавить уточнение, можно пить или нет и вывести признак вкуса """
        pass


class Technical(Liquid):
    __usage: str  # применение, для которого нужно реализовать getter/setter

    def __str__(self):
        """ Добавить уточнение, можно пить или нет и вывести признак применимости """
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
        ...  # в зависимости от введенного типа, запросит ввод вкуса или применения и записать в объект
        liquid_list.append(new_item)

        sorting(liquid_list)

        for i in liquid_list:
            print(i)
