# {"last_name": "Пупкин", "name": "Василий", "surname": "Степаныч", "tel_num": "+79143701845"}
# {"last_name": "Орленок", "name": "Егор", "surname": "Юрьевич", "tel_num": "+79243138022"}
# {"last_name": "Иванов", "name": "Иван", "surname": "Иванович", "tel_num": "8885557676"}
# {"last_name": "Петров", "name": "Иннокентий", "surname": "Витальевич", "tel_num": "2465265465462"}

import os
import json
from prettytable import PrettyTable
clear_term = lambda: os.system('cls') # Clear Terminal

# App constant settings
PHONE_BOOK_VERSION = '1.0'
PHONE_BOOK_FILE_NAME = "phone_book.txt"
PHONE_BOOK_FILE_PATH = "" + PHONE_BOOK_FILE_NAME
PHONE_BOOK_TABLE_LEN = 60

# Titles
TITLE_NAME_PHONE_BOOK = "Справочник v."
TITLE_MENU = "МЕНЮ"

# Phone book table rows
LIST_TABLE_COLUMNS = (
    "#",
    "Фамилия",
    "Имя",
    "Отчество",
    "Номер телефона"
)

# Menu items
MENU_ITEMS = (
    "Прочитать справочник",
    "Добавить запись",
    "Удалить запись",
    "Выйти из программы"
)

def file_check_ok():
    if(os.path.exists(PHONE_BOOK_FILE_PATH) and os.path.isfile(PHONE_BOOK_FILE_PATH)):
        return True
    
    return False

def write_data(data:list):
    try:
        with open(PHONE_BOOK_FILE_PATH, "w", encoding="UTF-8") as file:
            for line_dict in data:
                line = json.dumps(line_dict, ensure_ascii=False) + '\n'
                file.write(line)
    except: 
        print(f'Возникли ошибки при чтении файла {PHONE_BOOK_FILE_PATH}')    

# Read phone book file
def read_data(data:list):
    data.clear()
    if(file_check_ok()):
        try:
            with open(PHONE_BOOK_FILE_PATH, "r", encoding="UTF-8") as file:
                for line in file:
                    jstring = line.strip()
                    dict_line = json.loads(jstring)
                    data.append(dict_line)
        except: 
            print(f'Возникли ошибки при чтении файла {PHONE_BOOK_FILE_PATH}')    
            return False
    else:
         print(f"Файл справочника (\"{PHONE_BOOK_FILE_PATH}\") не найден в дирректории!!!")    
         return False
            
    return True        

# Phone book output to terminal         
def screen(data:list):
    itm_num = 0
    phone_book_table = PrettyTable(LIST_TABLE_COLUMNS)

    if(read_data(data)):
        for idx in data:
            itm_num +=1 
            phone_book_table.add_row([itm_num, idx["last_name"], idx["name"], idx["surname"], idx["tel_num"]])
    else:
        pass        
    
    print(phone_book_table)   

# Delete entry in phone book
def delete_entry(data:list):
    list_len = len(data)
       
    while file_check_ok():
        entry_num = int(input("Введите номер записи для удаления: "))
        if(entry_num > list_len or entry_num < 1):
            print("Неверный ввод, повторите попытку!") 
        else:    
            user_answer = input(f'Вы действительно хотите удалить: \n'
                f'({entry_num}) '
                f'{data[entry_num - 1]["last_name"]} '
                f'{data[entry_num - 1]["name"]} '
                f'{data[entry_num - 1]["surname"]} '
                f'{data[entry_num - 1]["tel_num"]}'
                '\n'
                'Да(Д) / Нет(Н) ?: ')    
            if(user_answer.lower() == 'д'):
                data.pop(entry_num - 1)
                write_data(data)
                break
            elif(user_answer.lower() == 'н'):
                print("Удаление отменено, выходим в меню.")
                break
            else:
                print("Ответ не определён, выходим в меню.")
                break
    else:
        print("Ошибка удаления записи (Файл отсутствует либо пуст)")        

#Add new entry to phoe book
def add_entry():
    entry = dict()
    
    # format_dict = {"last_name": "Пупкин", "name":"Василий", "surname":"Степаныч", "tel_num":"+79143701845"}
    last_name = input("Ведите Фамилию: ")
    name = input("Ведите Имя: ")
    surname = input("Ведите Отчество: ")
    tel_num = input("Ведите Номер телефона: ")
    
    entry["last_name"] = last_name
    entry["name"] = name
    entry["surname"] = surname
    entry["tel_num"] = tel_num
      
    try:
        with open(PHONE_BOOK_FILE_PATH, "a", encoding="UTF-8") as file:
            line = json.dumps(entry, ensure_ascii=False) + '\n'
            file.write(line)
    except: 
        print(f'Возникли ошибки при чтении файла {PHONE_BOOK_FILE_PATH}')
        return
    
    print("Запись успешно добавлена")       

# Output menu to terminal
def menu():
    item_num = 0
    phone_book_list = list()
    # need_exit  = False
    clear_term()

    # while not need_exit:
    while True:
        print()
        print(f"{'=' * int((PHONE_BOOK_TABLE_LEN / 2) - (len(TITLE_NAME_PHONE_BOOK) + 2))} {TITLE_NAME_PHONE_BOOK} {PHONE_BOOK_VERSION} {'=' * int((PHONE_BOOK_TABLE_LEN / 2) - 3)}")
        print(f"{'-' * int((PHONE_BOOK_TABLE_LEN / 2) - (len(TITLE_MENU) + 3))} {TITLE_MENU} {'-' * (int(PHONE_BOOK_TABLE_LEN / 2) + 2)}")
        
        for m_itm in range(len(MENU_ITEMS)):
            print(f'[{m_itm + 1}] {MENU_ITEMS[m_itm]}')
            
        print('-' * PHONE_BOOK_TABLE_LEN)
        
        item_num = int(input('Введите пункт меню: '))
        if item_num > len(MENU_ITEMS):
            print("Неверный ввод, повторите попытку!")
        else:
            if item_num == 1:
                if(read_data(phone_book_list)):
                    screen(phone_book_list)
                # print('-' * PHONE_BOOK_TABLE_LEN)

            elif item_num == 2:
                add_entry()
                read_data(phone_book_list)
                screen(phone_book_list)
                
            elif item_num == 3:
                delete_entry(phone_book_list)
                screen(phone_book_list)

            elif item_num == 4:
                exit()
 
        print('=' * PHONE_BOOK_TABLE_LEN)        
# Main app
def main():
    menu()


if __name__ == '__main__':
    main()
    # print(file_check())

