# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

import os
clear = lambda: os.system('cls')
clear()

numList1= [2, 3, 5, 9, 3] 
numList2= [2, 3, 5, 9, 6, 8] 

def SearchSum(lst:list):
    sum = 0
    for i in range(len(lst)):  
        if(i % 2 != 0):
            sum += lst[i]
            print(f'lst[{i}] = {lst[i]}')          
    return sum   


print(SearchSum(numList1)) 
print(SearchSum(numList2)) 