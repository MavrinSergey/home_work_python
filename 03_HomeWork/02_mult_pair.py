# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from math import ceil

def creation_list(n):
    import random
    list_N = [0] * n
    for i in range(n):
        list_N[i] = random.randint(-n, n)
    return list_N

def mult_pair(list_N):
    res_list = []
    for i in range(ceil(len(list_N) / 2)):
        res_list.append(list_N[i] * list_N[-i-1])
    return res_list

N = int(input('Введите N: '))
my_list = creation_list(N)
print(my_list)
result = mult_pair(my_list)
print(result)