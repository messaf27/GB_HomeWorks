# Реализуйте алгоритм перемешивания списка.

import os
clear = lambda: os.system('cls')
clear()

import random

n = int(input('Введите число элементов для генерации списка: '))
numList = []

for i in range(n):
    numList.append(random.randint(0, 200))
    
print(f'Исходный список: {numList}')
random.shuffle(numList)
print(f'Перемешанный список: {numList}')