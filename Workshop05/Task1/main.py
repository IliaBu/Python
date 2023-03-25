"""
Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
Пример:
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
"""

def ExponentiationFunction(A:int, B:int) -> int:
    if (B == 0):
        return 1
    if (B == 1):
        return (A)
    if (B != 1):
        return (A * ExponentiationFunction(A, B - 1))
        
b1 = bool(True)
while b1:
    A = input('Введите первое число: ')
    if A.isdigit() == False:
        print('Введено не число! Повторите ввод!')
    else:
        b1 = False

b2 = bool(True)
while b2:
    B = input('Введите второе число: ')
    if B.isdigit() == False:
        print('Введено не число! Введите целое число. Повторите ввод!')
    else:
        b2 = False
        
print(f'A = {A}; B = {B} -> {ExponentiationFunction(int(A),int(B))} ({A}^{B})')