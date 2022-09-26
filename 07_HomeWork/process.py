import gui


def creat_contact():
    my_list = []
    my_list.append(gui.input_user('Введите фамилию: '))
    my_list.append(gui.input_user('Введите имя: '))
    my_list.append(gui.input_user('Введите телефонами: '))
    my_list.append(gui.input_user('Введите комментарий: '))
    return my_list


def delete_contact(data, x):
    for i in range(1, len(data)):
        if 0 == data[i][0].find(x):
            del data[i]
            break
    return data


def search_next_Id(data):
    try:
        num = data[-1][0].split(';')
        next_id = int(num[0]) + 1
        return next_id
    except Exception:
        return 1


def contact_editing(data, x):
    for i in range(1, len(data)):
        if 0 == data[i][0].find(x):
            num = data[i][0].split(';')
            print(num)
            a = input('Введите новую фамилию, если не хотите менять введите NO ')
            if a != 'NO':
                num[1] = a
            b = input('Введите новое имя, если не хотите менять введите NO ')
            if b != 'NO':
                num[2] = b
            c = input('Введите новый номер, если не хотите менять введите NO ')
            if c != 'NO':
                num[3] = c
            d = input('Введите новый коментарий, если не хотите менять введите NO ')
            if d != 'NO':
                num[4] = d
            num = [';'.join(num)] # СОЕД ВСЕ ЕЛЕМЕНТЫ СПИСКА С НУЖНЫМ РАЗДЕЛИТЕЛЕМ
            data[i] = num
            print(data[i])
            break
    return data


def search_surname(data, last_name):
    res_list = []
    for i in range(1, len(data)):
        if last_name in data[i][0]:
            res_list.append(data[i])
    return print(res_list)
