# Задача №1 Задача 1. Создать родительский класс машина, у которого есть атрибуты model
# age, color и weigth, из них обязательный только model. Также у класса должны
# быть методы moive, stop, birthday, методы move и stop выводят сообщение на
# экран "move", "stop", а birthday увеличивает атрибут age на 1. Если атрибут age = None,
# то выбрасывает исключение с сообщением "атрибут age не задан".

class car:
    def __init__(self, model, age=None, color=None, weight=None):
        self.model = model
        self.age = age
        self.color = color
        self.weight = weight

    def get_move(self):
        print('Move')

    def get_stop(self):
        print('Stop')


    def get_age_up(self):
        try:
            print(self.age+1)
        except TypeError:
            print('атрибут age не задан')


car_1 = car(model='s80')
car_1.get_move()
car_1.get_stop()
car_1.get_age_up()





# Задача №2 Есть csv файл со списком людей, нужно прочитать его и преобразовать
# в список датаклассов. То есть нужно создать датакласс с атрибутами name, age,
# при этом тип age : Optional[int]. У датакласса должно быть property birth_year,
# которое считает возраст
from dataclasses import dataclass
from typing import Optional

@dataclass
class Person:
    name: str
    age: Optional[int] = None

    @property
    def birth_year(self):
        try:
            return 2023 - self.age
        except:
            return None

person_1=Person(name = 'Lena', age = 24)
person_2=Person(name = 'Dima')
person_3=Person(name = 'Vova', age = 35)

print(person_1.name, person_1.age,person_1.birth_year)
print(person_2.name, person_2.age,person_2.birth_year)
print(person_3.name, person_3.age,person_3.birth_year)