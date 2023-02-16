# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

import math 

print('Введите номер четверти (1-4)')
numQuart = int(input('X: '))

if numQuart > 4 or numQuart <=0:
    print('Введен не допустимый номер четверти!!!')
else:
    if numQuart == 1:
        print('X = 1 : +∞; Y = 1 :+ ∞')
    elif numQuart == 2:
        print('X = 1 : +∞; Y = -1 : -∞')
    elif numQuart == 3:
        print('X = -1 : -∞; Y = -1 : -∞')
    elif numQuart == 4:
        print('X = -1 : -∞; Y = 1 : +∞')