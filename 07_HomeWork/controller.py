import gui
from process import creat_contact, delete_contact, search_next_Id, contact_editing, search_surname
from bd import data_entry_to_file, print_contact, read_data, data_rewrite_to_file, creat_file


while True:
    action = int(gui.input_user(
        'Что будем делать?(1 - добавление контакта, 2 - удаление контакта, 3 - редактирование контакта, 4 - поиск контакта, 5 - выйти из приложения: '))
    print(action)
    if action == 1:
        creat_file()
        data = read_data()
        row = creat_contact()
        row.insert(0, search_next_Id(data))
        print(row)
        data_entry_to_file(row)
    elif action == 2:
        print("Вот список контактов")
        print_contact()
        del_id = gui.input_user('Введите id контакта который хотите удалить: ')
        data = read_data()
        data = delete_contact(data, del_id)
        data_rewrite_to_file(data)
    elif action == 3:
        print_contact()
        edit_id = gui.input_user('Введите id контакта который хотите изменить: ')
        data = read_data()
        data = contact_editing(data, edit_id)
        data_rewrite_to_file(data)
    elif action == 4:
        print_contact()
        last_name = gui.input_user('Введите фамилию или номер контакта который хотите найти: ')
        data = read_data()
        data = search_surname(data, last_name)
    elif action == 5:
        break
    else:
        print('Ошибка ввода')



