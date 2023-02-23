# Создайте программу для игры в ""Крестики-нолики"".

import os
clear_terminal = lambda: os.system('cls') # Clear Terminal

game_field = [i+1 for i in range(10)]
win_combinations = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

print(game_field)

def print_game_field(fld_list:list): 
    clear_terminal()
    print() 
    print('\t     |     |') 
    print(f'\t  {fld_list[0]}  |  {fld_list[1]}  |  {fld_list[2]}') 
    print('\t_____|_____|_____') 
  
    print("\t     |     |") 
    print(f'\t  {fld_list[3]}  |  {fld_list[4]}  |  {fld_list[5]}') 
    print('\t_____|_____|_____') 
  
    print("\t     |     |") 
  
    print(f'\t  {fld_list[6]}  |  {fld_list[7]}  |  {fld_list[8]}') 
    print('\t     |     |') 
    print() 

# Сделать ход в ячейку
def set_cell_field(fld_list:list, cell, xo):
    ind = fld_list.index(cell)
    fld_list[ind] = xo

# Получить текущий результат игры
def get_current_result(fld_list:list, win_comb):
    result = ''
    print(fld_list)
    for i in win_comb:
        if fld_list[i[0]] == 'X' and fld_list[i[1]] == 'X' and fld_list[i[2]] == 'X':
            result = 'X'
        elif fld_list[i[0]] == 'O' and fld_list[i[1]] == 'O' and fld_list[i[2]] == 'O':
            result = 'O'   
    return result

def game_run(fld_list:list):
    game_finish = False
    player_num = 1
    xo = ''
    
    while not game_finish:
        # 1. Показываем карту
        print_game_field(fld_list)
    
        # 2. Спросим у играющего куда делать ход
        if player_num == 1:
            xo = "X"
        else:
            xo = "O"
            
        cell = int(input(f'Игрок №{player_num}({xo}), ваш ход: '))
        
        set_cell_field(fld_list, cell, xo) # делаем ход в указанную ячейку
        winner = get_current_result(fld_list, win_combinations) # определим победителя
        if winner != "":
            game_finish = True
        else:
            game_finish = False
    
        player_num += 1   
        if(player_num >2 ): player_num = 1    
        
    print_game_field(fld_list)
    return winner    

print('-----=====*** Start Game XO *** =====-----')
player_winner = game_run(game_field)
print(f'Победитель игрок: "{player_winner}"')