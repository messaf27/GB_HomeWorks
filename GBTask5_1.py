# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

import os
os.system('cls') # Clear Terminal

srch = 'пр'
srch_obj = 'Абв бав к прпод абв кз преабв'

def str_romover(in_str:str, srch_str:str):
    wrd_list = in_str.split()
    print(wrd_list)
    for i in wrd_list:
        low_word = i.lower()
        if srch_str in low_word:
            wrd_list.remove(i)
            
    return   " ".join(wrd_list)      

print(str_romover(srch_obj, srch))