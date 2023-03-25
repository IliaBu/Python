"""
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

Пример:
2 2
4
"""

def sum(a: int, b: int) -> int:
    if b == 0:
        return a
    if b != 0:
        a += 1
        return sum(a, b - 1)
    
b1 = bool(True)
while b1:
    a = input('Введите первое число: ')
    if a.isdigit() == False:
        print('Введено не число! Повторите ввод!')
    else:
        b1 = False

b2 = bool(True)
while b2:
    b = input('Введите второе число: ')
    if b.isdigit() == False:
        print('Введено не число! Введите целое число. Повторите ввод!')
    else:
        b2 = False
        
print(f'a = {a}; b = {b} -> {sum(int(a),int(b))}')