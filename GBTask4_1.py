
# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141   

#       Ввод: 0.01
#       Вывод: 3.14

#       Ввод: 0.001
#       Вывод: 3.141
import os

os.system('cls')

my_list = [2,4,1,6,6,9,3,5,55,8,4,1]
print(my_list)
# my_set = set(my_list)
# print(my_set)

def normalize_list(inList:list):
    return list(set(inList))

print(normalize_list(my_list))