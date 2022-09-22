# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from math import ceil
import random


N = int(input('Введите N: '))
my_list = [random.randint(-N, N) for x in range(N)]
print(my_list)

result = [my_list[i] * my_list[-i-1] for i in range(ceil(len(my_list) / 2))]
print(result)