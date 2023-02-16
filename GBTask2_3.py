# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

import os
clear = lambda: os.system('cls')
clear()

number = int(input('Введите число: '))

mStrResults = []
rStr = ''
summ = 0.0

for i in range(1, number + 1):
    rNum = float((1 + 1/i)**i)
    summ += rNum
    rStr = str(i) + ': ' + str(round(rNum, 2))
    mStrResults.append(rStr)

print(f'Для N = {number} {mStrResults} Сумма: {round(summ, 2)}') 