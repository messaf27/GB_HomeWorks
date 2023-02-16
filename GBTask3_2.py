# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import os
clear = lambda: os.system('cls')
clear()

numList1 = [2, 3, 4, 5, 6]
numList2 = [2, 3, 5, 6] 

def MultList(lst:list):
    result = []
    rangeNum =  int(len(lst) / 2)   
    
    for i in range(rangeNum):
        mult = lst[i] * lst[len(lst) - i - 1]
        result.append(mult)
        
    if(len(lst) % 2 != 0):
        mult = lst[rangeNum]
        mult *= lst[rangeNum]
        result.append(mult)   
        
    return result    
        
print(MultList(numList1))        
print(MultList(numList2))