# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.
import random
from functools import reduce


N = int(input('Введите N: '))

list_N = [random.randint(-N, N) for x in range(N)]
print(list_N)

multiplication_list = input('Введите порядковый номер чисел, через пробел, которые нужно перемножить: ').split(sep=' ')
multiplication_list = [int(x) for x in multiplication_list]


list_my = [list_N[multiplication_list[x]] for x in range(len(multiplication_list))]

mult = reduce(lambda x, y: x * y, list_my, 1)
print(mult)