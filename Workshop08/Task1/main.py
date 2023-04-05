"""
Задача №49. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи (Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной

Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

"""

filename = 'file.txt'

def read_file(filename):
    with open(filename, 'r') as data:
        data_array = []
        for line in data:
            item = line.replace('\n', '').split(sep=',')
            data_array.append(item)
    return data_array


def write_file(filename, data_array):
    with open(filename, 'w') as data:
        for i in data_array:
            write_element = ', '.join(i)
            data.write(f'{write_element}\n')


def add_item(filename):
    data_array = read_file(filename)
    max_id = 0
    for i in range(1, len(data_array)):
        if max_id < int(data_array[i][0]):
            max_id = int(data_array[i][0])
    next_id = max_id + 1
    # print(next_id)
    new_item = []
    new_item.append(str(next_id))
    new_item.append(input('Фамилия: '))
    new_item.append(input('Имя: '))
    new_item.append(input('Отчество: '))
    new_item.append(input('Телефон: '))
    data_array.append(new_item)
    write_file(filename, data_array)
    print('Запись добавлена!')
    return str(data_array)


def show_all_items(filename):
    data_array = read_file(filename)
    for i in range(1, len(data_array)):
        print("ID: ", data_array[i][0], "Фамилия: ", data_array[i][1], "Имя: ",
              data_array[i][2], "Отчество: ", data_array[i][3], "Телефон: ", data_array[i][4])


def search_contact(filename):
    data_array = read_file(filename)
    temp = []
    find = str(input('Введите из любых предложенных вариантов: Фамилию, Имя, Отчество, Телефон: '))
    for i in range(1, len(data_array)):
        if find.lower() in str(data_array[i]).lower():
            print(str(data_array[i]))
            temp.append(data_array[i])
    if len(temp) == 0:
        print('Нет такого контакта!')


def edit_contact(filename):
    data_array = read_file(filename)
    temp = []
    find = str(input('Введите данные контакта который хотите изменить: '))
    for i in range(1, len(data_array)):
        if find.lower() in str(data_array[i]).lower():
            print(str(data_array[i]))
            print(f'Введите "{str(data_array[i][0])}" чтобы изменить контакт "{data_array[i]}"')
            temp.append(data_array[i])
    if bool(temp):
        remake_index = int(input(""))
        data_array.pop(remake_index)  
        write_file(filename, data_array)      
        new_item = []
        new_item.append(str(remake_index))
        new_item.append(input('Фамилия: '))
        new_item.append(input('Имя: '))
        new_item.append(input('Отчество: '))
        new_item.append(input('Телефон: '))
        data_array.append(new_item)
        write_file(filename, data_array)
        print(f'Запись с id: {str(remake_index)} изменена!')
    else:
        print('Нет такого контакта!')


def del_contact(filename):
    data_array = read_file(filename)
    temp = []
    find = str(input('Введите данные контакта который хотите удалить: '))
    for i in range(1, len(data_array)):
        if find.lower() in str(data_array[i]).lower():
            print(str(data_array[i]))
            print(f'Введите "{str(data_array[i][0])}" чтобы удалить контакт "{data_array[i]}"')
            temp.append(data_array[i])         
        if bool(temp):
            del_index = int(input(""))
            data_array.pop(del_index) 
            write_file(filename, data_array)
            print(f'Запись с id: {str(data_array[i][0])} удалена!')
        else:
            print('Нет такого контакта!')

def menu():
    b1 = bool(True)
    while b1:
        print()
        print('Добро пожаловать в телефонный справочник!')
        print('1 - Показать все записи')
        print('2 - Добавить запись')
        print('3 - Найти запись')
        print('4 - Изменить запись')
        print('5 - Удалить запись')
        print('0 - Выйти')
        print()
        user_operation = int(input())
        if user_operation == 1 or user_operation == 2 or user_operation == 3 or user_operation == 4 or user_operation == 5 or user_operation == 0:
            if user_operation == 1:
                show_all_items(filename)
            if user_operation == 2:
                add_item(filename)
            if user_operation == 3:
                search_contact(filename)
            if user_operation == 4:
                edit_contact(filename)
            if user_operation == 5:    
                del_contact(filename)
            if user_operation == 0:
                b1 = False
        else:
            print("Некорректный ввод! Повторите ввод")

menu()