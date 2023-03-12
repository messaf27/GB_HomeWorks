import os
clear_term = lambda: os.system('cls') # Clear Terminal

VERSION = '1.0'
TABLE_LEN = 105

MENU_ITEMS = (
    "Прочитать справочник",
    "Добавить запись",
    "Удалить запись",
    "Выйти из программы"
)

format_dict = {"last_name": "Пупкин", "name":"Василий", "surname":"Степаныч", "tel_num":"+79143701845"}

line_list = list()


def write_data():
    pass


def read_data():
    phone_book = [format_dict for i in range(10)]
    return phone_book


def screen(data:list):
    itm_num = 0
    print('-' * TABLE_LEN)
    print('|\t Фамилия \t|\t Имя \t\t|\t Отчество \t|\t Номер телефона \t|')
    print('-' * TABLE_LEN)

    for idx in data:
        itm_num +=1 
        print(f'({itm_num})\t {idx["last_name"]}\t\t\t{idx["name"]}\t\t\t{idx["surname"]}\t\t{idx["tel_num"]}')

def menu():
    item_num = 0
    # need_exit  = False
    clear_term()

    # while not need_exit:
    while True:
        print()
        print(f"{'='*25} Справочник v. {VERSION} {'='*26}")
        print(f"{'-'*32} МЕНЮ {'-'*32}")
        for m_itm in range(len(MENU_ITEMS)):
            print(f'[{m_itm + 1}] {MENU_ITEMS[m_itm]}')
        print('-'*70)
        
        item_num = int(input('Введите пункт меню: '))
        if item_num > len(MENU_ITEMS):
            print("Неверный ввод, повторите попытку!")
        else:
            if item_num == 1:
                phone_book_list = read_data()
                screen(phone_book_list)
                print('-' * TABLE_LEN)

            elif item_num == 2:
                pass

            elif item_num == 3:
                pass

            elif item_num == 4:
                exit()
                
        print('='*70)        





def main():
    # print(format_dict.keys())
    menu()


if __name__ == '__main__':
    main()

