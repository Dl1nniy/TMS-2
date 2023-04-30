# Задача № 1.
#Дописать функцию так, чтобы она возвращала None в случае если ключа нет,
# а не генерировала исключение (для реализации используем исключения)
dict_ = {'фрукт': 'яблоко', 'машина': 'легковая', 'день': 'ясный'}
key = ['мяч']
def func(dict_, key):
    try:
        return dict_['мяч']
    except KeyError:
        return None
print(func(dict_, key))




# Задача №2.
# Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные. Создать
#файл и записать в него первые 2 строки и закрыть файл. Затем открыть файл на
#редактирование и дозаписать оставшиеся 2 строки. В итогом файле должны быть 4
#строки, каждая из которых должна начинаться с новой строки.


first_str = input('Введите первую строку: ')
second_str = input('Введите вторую строку: ')
third_str = input('Введите третью строку: ')
fourth_str = input('Введите четвертую строку: ')
with open("new_txt_example.txt", 'w+') as write_file:
    write_file.write(str(first_str + '\n'))
    write_file.write(str(second_str + '\n'))
with open("new_txt_example.txt", 'a') as write_file:
    write_file.write(str(third_str + '\n'))
    write_file.write(str(fourth_str + '\n'))



# Задача №3
#3. Создать словарь в качестве ключа которого будет 6-ти значное число (id), а в
#качестве значений кортеж состоящий из 2-х элементов - имя(name), возраст(age).
#Сделать около 5-6 элементов словаря. Записать данный словарь на диск в json-файл.


dict_ = {
    '111111': 'Oleg, 25',
    '222222': 'kostya, 25',
    '333333': 'vlad, 26',
    '444444': 'Philip, 27',
    '555555': 'sergey, 30',
    '666666': 'Egor, 23',
}

with open("data_file.json", "w") as write_file:
    for key, value in dict_.items():
        write_file.write(f'{key}, {value}\n')



