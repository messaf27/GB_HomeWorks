
import os
clear_terminal = lambda: os.system('cls') # Clear Terminal

rhythm_ok = "парам-пам-пам"
rhythm_bad = "пам-парам"

# Constants
VOWELS_LIST = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
NUM_OF_VOWEL = 4


def is_vowel(char):
    for elem in VOWELS_LIST:
        if(elem == char):
            return True
    return False

def rhythm_str_is_ok(rtm_str, num_vowel):
    counter = 0 
    sym_list = list(rtm_str)
    for sym in sym_list:
        if(is_vowel(sym)):
            counter +=1
    if(counter == num_vowel):
        return True
    
    return False        

def input_rhythm_process(in_str_list:list):
    result = False
    for curr_str in in_str_list:
      if not rhythm_str_is_ok(curr_str, NUM_OF_VOWEL):
          return False
    
    return True  

# ======== Main Program ==================== #
clear_terminal()
input_list = input("Введите рифму: ").split()
if(input_rhythm_process(input_list)):   
    print(rhythm_ok)
else:
    print(rhythm_bad)

# пум-пурум-пам