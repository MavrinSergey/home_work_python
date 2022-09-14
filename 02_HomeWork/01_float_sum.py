# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример: - 0,56 -> 11

input_data  = float(input('напишите дробное число и программа покажет сумму его цифр: '))
sum = int()
while input_data > 1:
    input_data /= 10

my_list = (str(input_data)).split(sep='.')

result = int(my_list[1])

while result > 0:
    sum += result % 10
    result //= 10
print(sum) 

