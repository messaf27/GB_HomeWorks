# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

import os
os.system('cls') # Clear Terminal

finde_str = 'абв'
str1 = 'Здравствуйте, как дела у вас? Что нового произошло за вчерашний день?'
print(str1)

list_words = str1.split(' ') # Преобразуем в список по словам
list_finde_sym = finde_str.split(' ')
print(list_words)

# new_list_words = []
for word in list_words:
    
    for i in range(len(list_finde_sym)):
        if list_finde_sym[i] in word:
            list_words.remove(i)
        
print(list_words)        

str1 = " ".join(list_words)
print(str1)