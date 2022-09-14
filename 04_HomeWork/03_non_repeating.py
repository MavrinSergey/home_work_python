# Задача 018:
# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

def creation_list(n):
    import random
    list_N = [0] * n
    for i in range(n):
        list_N[i] = round(random.randint(-n, n), 2)
    return list_N

def non_repeating(list_N):
    result_list = []
    for i in range(len(list_N)-1):
        if list_N[i] != list_N[i+1]:
            if list_N[i-1] != list_N[i]:
                result_list.append(list_N[i])
                if i + 1 == len(list_N)-1:
                    result_list.append(list_N[i+1])
    return result_list

k = int(input('Введите число: '))
sequence = creation_list(k)
sequence = [int(x) for x in sequence]
sequence.sort()
print(sequence)
result_list = non_repeating(sequence)
print(result_list)