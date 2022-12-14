class Liquid:
    id: int  # номер жижи, реализовать автоинкремент
    title: str  # название
    density: float  # плотность

    def __init__(self, title, density):
        self.title = title
        self.density = density

    def __str__(self):
        return f'{self.id}. Жижа "{self.title}" с плотностью {self.density}'


if __name__ == '__main__':
    liquid_list = list()
    while True:
        print('Предлагаю вам ввести параметры жидкости')
        title = input('Введите название: ')
        density = input('Введите плотность: ')
        type_of_liquid = input('Это можно пить? [Y/n]: ')
        new_item = Liquid(title, density)
        liquid_list.append(new_item)

        for i in liquid_list:
            print(i)
