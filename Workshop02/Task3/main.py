"""
## Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
Пример:
10 -> 1 2 4 8
"""
b = bool(True)
while b:
    text = input('Введите число: ')
    if text.isdigit() == False:
        print('Введено не число! Повторите ввод!')
    else:
        b = False
temp = 1
print(text + ' ->', end=' ')
while temp <= int(text):
    print(temp, end=' ')
    temp *= 2