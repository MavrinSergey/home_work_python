# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# Пример: k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# u00B2
# a = '2\u00B2'
# print(a)

def creation_list(n):
    import random
    list_N = [0] * n
    for i in range(n):
        list_N[i] = round(random.randint(0, 3), 2)
    return list_N

def creation_list_member(k):
    l_m = []
    for i in range(k):
        l_m.insert(0, i)
    return l_m

def res(l_m, d_l):
    res_list = str()
    for i in range(len(l_m)):
        if int(l_m[i]) == 0:
            continue
        elif i == len(l_m)-1:
            res_list += f'{l_m[i]} = 0'
        # elif i == len(l_m)-2:
        #     res_list += f'{l_m[i]}x + ' # так как файл который получается в конце кода участвует в след задаче, решил степень 1 выводить
        else:
            res_list += f'{l_m[i]}x**{d_l[i]} + '
    return res_list


k = int(input('Введите число: '))
polynomial = creation_list(k)
print(polynomial)
degree_list = creation_list_member(k)
print(degree_list)
polynomial = [str(x) for x in polynomial]
degree_list = [str(x) for x in degree_list]
result_list = res(polynomial, degree_list)
print(result_list)

data = open('D:/EducationalProjects/03_Python/HomeWork/04_HomeWork/file.txt', 'w') # a - (добавляет) r - чтение w - (перезаписывает) 
data.writelines(result_list) # разделителей не будет

data.close()
