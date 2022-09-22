import gui


def creat_contact():
    my_list = []
    my_list.append(gui.input_user('Введите фамилию: '))
    my_list.append(gui.input_user('Введите имя: '))
    my_list.append(gui.input_user('Введите телефонами: '))
    my_list.append(gui.input_user('Введите комментарий: '))

    return my_list