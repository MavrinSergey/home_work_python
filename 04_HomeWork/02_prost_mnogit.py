# Задача 017:
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


n = int(input('Введите число: '))
my_list = []
for i in range(2, n):
    while n % i == 0:
        n /= i
        my_list.append(i)
print(my_list)


