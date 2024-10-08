# Пункты задачи:
# Создайте класс House.
# Вунтри класса House определите метод __init__, в который передадите название и кол-во этажей.
# Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors, присвойте им переданные значения.
# Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
# Создайте объект класса House с произвольным названием и количеством этажей.
# Вызовите метод go_to у этого объекта с произвольным числом.
class House:
    def __init__(self, name: str, numberOfFloors: int):

        self.name: str = name
        self.numberOfFloors: int = numberOfFloors

    def goto(self, floor: int):
        if floor < 1 or floor > self.numberOfFloors:
            print('Такого этажа не существует')
        else:
            [print(x) for x in range(1, floor + 1)]


sweatyHome = House('sweatyHome', 19)
sweatyHome.goto(6)
