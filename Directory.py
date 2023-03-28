
telephone_book = r'data.txt'

def show_data(telephone_book):
    '''Эта функция показывает содержимое справочника'''
    with open(telephone_book, 'r', encoding='utf-8') as file:
        return file.read().split('\n')

def new_data(telephone_book):
    '''добавляет новую информацию в справочник'''
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    phone_number = input("Введите номер контакта: ")
    with open(telephone_book, 'a', encoding='utf-8') as file:
        file.write(last_name + ' '+ first_name + ' ' + middle_name + ' | ' + phone_number + '\n')

def find_data(telephone_book):
    '''Эта функция ищет информацию в справочнике'''
    search_by = input("Введите информацию для поиска (фамилия, имя или отчество): ")
    with open(telephone_book, 'r', encoding="utf-8") as f:
        for line in f:
            if search_by in line:
                print(line)
                return str(line)


def change_data(telephone_book):
    '''Эта функция меняет информацию в справочнике'''
    print('Для изменения контакта: ')
    contact = find_data(telephone_book)
    old_contact = (input(f'Вы хотите изменить контакт {contact} \n 1 - Да \n 2 - Нет\n')) 
    if old_contact == '1':
        with open(telephone_book, 'r', encoding="utf-8") as f: 
                all = f.readlines()
        for i in range(len(all)): 
            if  contact == all[i]: 
                last_name = input("Введите фамилию: ")
                first_name = input("Введите имя: ")
                middle_name = input("Введите отчество: ")
                phone_number = input("Введите номер контакта: ")
                new_contact = (str(last_name + ' '+ first_name + ' ' + middle_name + ' | ' + phone_number +'\n')) 
                all[i] = new_contact
        new_contact = ''.join(all) 
        with open(telephone_book, 'w', encoding="utf-8") as f:
            f.write(f'{new_contact}')
            print ('Контакт изменён')
    if old_contact == '2':
        print("Введите, пожалуйста, более точные данные ")
        change_data(telephone_book)



def delet_data(telephone_book):
    '''Эта функция удаляет в справочнике'''
    with open(telephone_book, 'r', encoding="utf-8") as f:
        x = input('Введите Имя или Фамилию для удаления: ')
        lines = f.readlines()
        with open(telephone_book, 'w', encoding="utf-8") as f:
            for line in lines:
                if x in line:
                    print("Строка удалена")
                else:
                    print(line)    
                    f.write(line)

while True:
    mode = input('Выберите режим работы справочника:\
    \n 1. Показать содержимое справочника \
    \n 2. Создать новый контакт\
    \n 3. Найти контакт\
    \n 4. Изменить контакт\
    \n 5. Удалить контакт\
    \n 0. Закончить работу со справочником\
    \n Ввод  ')
    if mode == '1':
        print(show_data(telephone_book))
    elif mode == '2':
        new_data(telephone_book)
    elif mode == '3':
        find_data(telephone_book)
    elif mode == '4':
        change_data(telephone_book)
    elif mode == '5':
        delet_data(telephone_book)
    elif mode == '0':
        break
    else:
        print('No mode')