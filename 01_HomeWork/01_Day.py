# 01. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

number = int(input('Программа принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.\nВведите число: '))
while (number <= 0) or (7 < number):
    number = int(input('Такого дня недели не существует. Введите число от 1 до 7: '))

weekends = [True for n in range(6, 8) if number == n]
x = 'выходным днем'
y = 'рабочим днем'

print(f'День {number} является {x if weekends else y} {}')
