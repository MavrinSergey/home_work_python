# Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций).
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def decimal_to_binary(n):
    preliminary_result = 0
    result = 0
    while n > 0:
        preliminary_result *= 10
        b = n % 2        #
        preliminary_result = preliminary_result + b
        n = n // 2
    while preliminary_result > 0:
        result *= 10
        b = preliminary_result % 2  #
        result = result + b
        preliminary_result = preliminary_result // 10
    return result

N = int(input('Введите N: '))
my_binary = decimal_to_binary(N)
print(my_binary)