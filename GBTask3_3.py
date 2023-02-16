# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 10.01] => 0.19

import os
clear = lambda: os.system('cls')
clear()

numList1 = [1.1, 1.2, 3.1, 10.01]

def decimalMax(lst:list):
    max = 0
    min = lst[0]
    for element in lst:
        fractValue = round(element % 1, 2)
        if(fractValue > max): max = fractValue
        if(fractValue < min): min = fractValue
        
    print(f'max = {max}; min = {min}')
    return max - min


print(decimalMax(numList1))