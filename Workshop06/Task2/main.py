"""
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

Пример:
Ввод: [-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
"""

import random

b1 = bool(True)
while b1:
    text = input('Введите размер массива: ')
    if text == '' and text.isdigit() == False:
        print('Введено не число! Повторите ввод!')
    else:
        b1 = False
list = [random.randint(-10, 20) for _ in range(int(text))]
print(f'Ввод: {list}')

b2 = bool(True)
while b2: 
    try:
        min_number = int(input('Введите минимум: '))
        b2 = False
    except:
        print('Введено не число! Повторите ввод!')

b3 = bool(True)
while b3:
    max_number = input('Введите максимум: ')
    if max_number == '' and max_number.isdigit() == False:
        print('Введено не число! Повторите ввод!')
    else:
        b3 = False
        
print('Вывод индексов массива: ')
for i in range(len(list)):
    if min_number <= list[i] <= int(max_number):
          print(i, end=' ')
