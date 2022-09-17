# Задача 024:
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных файлах


def file_reading(x):
    with open(f'D:/EducationalProjects/03_Python/HomeWork/05_HomeWork/{x}', 'r', encoding="utf-8") as file:
        y = file.read()
    return y


def data_entry_to_file(x, y):
    with open(f'D:/EducationalProjects/03_Python/HomeWork/05_HomeWork/{x}', 'a', encoding="utf-8") as file:
        file.writelines(f'{y}\n')


def dictionary(x: str):
    y = ''
    count = 1
    for i in range(1, len(x)):
        if x[i-1] == x[i]:
            count += 1
        else:
            y += str(count) + x[i-1] + ' '
            count = 1
        if i == len(x) - 1:
            y += str(count) + x[i]
    return y


my_string = file_reading('file_input.txt')
result_string = dictionary(my_string)
dictionary(result_string)
