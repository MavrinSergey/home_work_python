# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12

def creation_list(n):
    import random
    list_N = [0] * n
    for i in range(n):
        list_N[i] = random.randint(-n, n)
    return list_N

def sum_negative(list_N):
    res = 0
    for i in range(1, len(list_N), 2):
        res += list_N[i]
    return res

N = int(input('Введите N: '))
my_list = creation_list(N)
print(my_list)
result = sum_negative(my_list)
print(result)