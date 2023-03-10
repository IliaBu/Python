# Задача 1: Найдите сумму цифр трёхзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

b = bool(True)
while b:
    text = input('Введите трёхзначное число: ')
    if text.isdigit() == False or len(text) > 3:
        print('Введено не число! Повторите ввод!')
    else:
        b = False
sum = int(text[0]) + int(text[1]) + int(text[2])
print(text + ' -> ' + str(sum) + ' (' + text[0] + ' + ' + text[1] + ' + ' + text[2] + ')')
