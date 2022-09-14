# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

def creation_list(n):
    import random
    list_N = [0] * n
    for i in range(n):
        list_N[i] = round(random.uniform(-n, n), 2)
    return list_N

def remote_whole(list_N):
    for i in range(len(list_N)):
        list_N[i] -= int(list_N[i])
    return list_N

def min_max_diff(list_N):
    min = list_N[0]
    max = list_N[0]
    for i in range(1, len(list_N)):
        if list_N[i] > max:
            max = list_N[i]
        if list_N[i] < min:
            min = list_N[i]
    return (max - min)


N = int(input('Введите N: '))
my_list = creation_list(N)
print(my_list)
result = remote_whole(my_list)
print(result)
diff = min_max_diff(result)
print(diff)