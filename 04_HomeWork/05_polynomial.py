# Задача 020: Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# ________________________________________

def data_preparation(x):
    x = str(x)
    x = x.split(sep=' = 0')
    x = x[0].split(sep=' + ')
    for i in range(len(x)):
        x[i] = list(map(int, (x[i].split(sep='x**'))))
    return x

def sum_of_zero_polynomial_indices(x, y):
    res = []
    if x[0][1] > y[0][1]:
        length = x[0][1] + 1
    else:
        length = y[0][1] + 1
    for i in range(length):
        if len(x[i]) != 1:
            if x[i][1] == y[i][1]:
                res.append(x[i][0] + y[i][0])
            elif x[i][1] > y[i][1]:
                res.append(x[i][0])
                y.insert(i, x[i][0])
            elif x[i][1] < y[i][1]:
                res.append(y[i][0])
                x.insert(i, y[i][0])
        else:
            res.append(x[i][0] + y[i][0])
    return res

def amount_of_polynomials(l_m):
    res_list = str()
    count = len(l_m) - 1
    for i in range(len(l_m)):
        if count > 1:
            res_list += f'{l_m[i]}x**{count} + '
        elif count == 1:
            res_list += f'{l_m[i]}x + '
        else:
            res_list += f'{l_m[i]} = 0'
        count -= 1    
    return res_list

def file_reading(x):
    with open(f'HomeWork/04_HomeWork/{x}', 'r') as file:
        y = file.read()
    return y

def data_entry_to_file(x):
    with open('HomeWork/04_HomeWork/file_result.txt', 'a') as file:
        file.writelines(f'{x}\n')

many_member_1 = file_reading('file.txt')
many_member_2 = file_reading('file2.txt')
many_member_1 = data_preparation(many_member_1)
many_member_2 = data_preparation(many_member_2)
many_member_3 = sum_of_zero_polynomial_indices(many_member_1, many_member_2)
result = amount_of_polynomials(many_member_3)
data_entry_to_file(result)

