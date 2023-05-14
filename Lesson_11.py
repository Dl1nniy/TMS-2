# Задача №1 Напишите генератор, который будет генерировать числа от 0 до бесконечности и вызовите его несколько раз
def get_infinity(i):
    while True:
        yield i
        i+=1
numbers = get_infinity(1)
print(next(numbers))
print(next(numbers))
print(next(numbers))




# Задача №2 Напишите итератор, который будет генерировать числа от О до заданного
# (по сути реализовать функцию range только в виде итератора)

class Numbers:
    def __init__(self, num):
        self.num = num
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.num:
            self.counter += 1
            return self.counter
        raise StopIteration


for item in Numbers(10):
    print(item)




# Задача №3 Допишите класс Family таким образом чтобы он влялся итератором
# и мы могли при помощи цикла for вывести всех ченов семьи
class Family:

    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def __len__(self):
        return len(self.members)

    def add_family_member(self, member):
        self.members.append(member)

    def __str__(self):
        return f"Family: last_name - {self.last_name}, count - {len(self.members)}"


family_member_1 = Family('Paulouski', "husband")
family_member_2 = Family("Klopotok", "wife")
family_member_3 = Family('Paulouskay', 'mother')
family_member_4 = Family('Paulouski', 'father')

family = [family_member_1,family_member_2,family_member_3,family_member_4]
number_iterator = family.__iter__()
print(number_iterator.__next__())
print(number_iterator.__next__())
print(number_iterator.__next__())
print(number_iterator.__next__())




# Задача №5 Реализовать генератор чисел Фибоначчи

def fib(n):
    a, b = 1, 1
    for __ in range(n):
        yield a
        a, b = b, a + b

gen = fib(10)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))



