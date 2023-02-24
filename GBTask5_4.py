# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
import os
clear_terminal = lambda: os.system('cls') # Clear Terminal

data_str = 'AAAAAAFDDCCCCCCCAEEEEBBBEEEEEEFFFEEEEEEE'


def rle_encode(in_data):
    result = '' 
    prev_sym = '' 
    count = 1 
    
    if not in_data: return '' 
    
    for sym in in_data: 
        if sym != prev_sym: 
            if prev_sym: 
                result += str(count) + prev_sym 
            count = 1 
            prev_sym = sym 
        else: 
            count += 1 
    else:
        result += str(count) + prev_sym 
        return result


def rle_decode(in_data):
    result = '' 
    count = '' 
    for sym in in_data: 
        if sym.isdigit():
            count += sym 
        else: 
            result += sym * int(count) 
            count = '' 
    return result


clear_terminal()
print(f'Исходные данные (размер: {len(data_str)}): "{data_str}"')
encode_str = rle_encode(data_str)
print(f'Сжатые данные (размер: {len(encode_str)}): "{encode_str}"')
decode_str = rle_decode(encode_str)
print(f'Восстановленные данные (размер: {len(decode_str)}): "{decode_str}"')

if(decode_str == data_str):
    print('Исходные и восстановленные данные идентичны!')
else:
    print('Ошибка кодирования, данные отличаются!!!')