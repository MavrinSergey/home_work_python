# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# ОПИСАНИЕ ФУНКЦИИ: функция первым аргументом принимает порядковый номер фибоначи 
# до которого нужно вывести последовательность. 
# вторым аргументом принимает (1) если нужно вывести положительную последовательность
# или (-1) если нужно построить отрицательную последовательность

def fibonachi_sequence(n, x): # ненашел как сделать чтобы при вводе числа отличного от 1 или -1 в аргумент функции она ругалась
    fib1 = 0
    fib2 = 1
    fibo_sequence = [fib1, fib2]
    for i in range(n-1):
        fib1, fib2 = fib2, fib1 + (fib2 * x)
        fibo_sequence.append(fib2)
    if x == -1:
        fibo_sequence.reverse()
    return fibo_sequence

n = int(input('Введите число: '))
list_neg = fibonachi_sequence(n, -1)
list_neg.remove(0)
list_pos = fibonachi_sequence(n, 1)
res = list_neg + list_pos
print(res)