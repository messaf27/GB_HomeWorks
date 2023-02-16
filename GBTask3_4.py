# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

import os
clear = lambda: os.system('cls')
clear()

inValue = int(input('Input num: '))
print(bin(inValue).replace('0b', ''))