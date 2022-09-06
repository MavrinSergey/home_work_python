# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.
import random
N = int(input('Введите N: '))
list_N = [0] * N

for i in range(N):
    list_N[i] = random.randint(-N, N)

multiplication_list = input('Введите порядковый номер чисел, через пробел, которые нужно перемножить: ').split(sep=' ')

multiplication_list = [int(x) for x in multiplication_list]
print(type(multiplication_list[0]))

mult = 1
for i in range(len(multiplication_list)):
    mult = mult * multiplication_list[i]

print(mult)

