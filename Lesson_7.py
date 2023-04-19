 # Задачи на Декоратор!

#Задача 5: Написать декоратор, который добавляет в kwargs время старта выполнения функции
from datetime import datetime

def timer(func):
    def wrapper():
        start_time = datetime.now()
        print(f'Время старта выполнения функции: {start_time}')
        func()

    return wrapper

@timer
def func(**kwargs):
    print(kwargs)  # в эти kwargs хотим добавить время старта выполнения функции

func()




#Задача 8: Написать декоратор, который удалит из args повторяющиеся элементы

def add_one_to_order(func):
    def get_result(*args):
        result = func(*args)
        final = set(result)
        return final
    return get_result

@add_one_to_order
def func(*args):
    return args


print(func("string", 1, 2, 3, 2, "string"))



                                                # Задачи на функции!

#Задание 1: Даны списки:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#Нужно вернуть список, который состоит из элементов, общих для этих двух списков

def get_overlap():
    return [x for x in b if x in a]
print(get_overlap())




#Задача 8: написать функцию, которая принимает в себя время в виде "HH:mm:ss" и считает, сколько всего секунд
def get_time_to_seconds(time):
    return (int(time[0:2]) * 3600) + (int(time[3:5]) * 60) +(int(time[6:8]))

print(get_time_to_seconds("12:12:12")) # всего 43932 секнуд







