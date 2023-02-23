# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять 
# первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import os
os.system('cls') # Clear Terminal

TOTAL_SWEETS = 100
MAX_SWEETS_INPUT = 28

def inputPlayer(player_num:int, ply_cur_num:int , max_input:int, cur_balance:int):
    input_error = True # for do one cycle
    in_num = None
    while input_error:
        in_num = input(f'Ход игрока № {player_num}, (Ваших конфет: {ply_cur_num}) введите число: ')
        if(not in_num.isdigit()):
            print(f'Неверный ввод, введите число!!!')
            input_error = True
        elif(int(in_num)  > max_input):
            print(f'Неверный ввод, максимальное число {max_input} !!!')
            input_error = True
        else:    
            in_num = int(in_num)      
            input_error = False

    cur_balance = (cur_balance - (ply_cur_num + in_num))
    
    if(cur_balance < 0): 
        cur_balance = 0   
        print(f'Конфет больше нету!!! ({cur_balance})')  
       
    return cur_balance

def play_game(mum_of_players:int):
    move_number = 0
    player_winner_num = 0
    sweets_balance = TOTAL_SWEETS
    player_list = [0 for i in range(mum_of_players)]
    print(player_list)
    
    while (player_winner_num == 0):
        os.system('cls')
        print('=========================================================')
        print(f'Количество конфет на столе: {sweets_balance}')
        print('---------------------------------------------------------')
        for player in range(mum_of_players):
            move_number += 1
            sweets_balance = inputPlayer(player + 1, player_list[player], MAX_SWEETS_INPUT, sweets_balance)
            if sweets_balance == 0:
                player_winner_num = player + 1
                print('***************************************************')
                print(f'Игра закончена, ход: {move_number}. \nИгрок № {player_winner_num} победитель!')
                print('***************************************************')
                break
        print('=========================================================\n')
        
    return player_winner_num
 
# ========== Запуск Игры  ================= 
play_game(2) # 2 игрока