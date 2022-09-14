# Задача 016: Вычислить число pi c заданной точностью d 
# Пример: при d = 0.001, π = 3.141
# 0.1 ≤ d ≤ 0.0000000001
import math
print(math.pi)
# print()
# # Вычисление Пи с помощью ряда Нилаканта.
def PI(d):
    pi = 3
    counter = 2
    raznica = d + 1
    const = 4
    while d < raznica:     
        pi += const / (counter * (counter+1) * (counter+2))
        const = -const
        pi_next = pi + const / ((counter+2) * (counter+3) * (counter+4))
        raznica = abs(pi - pi_next)
        print(raznica)
        counter += 2
    print(f'кол-во итераций - {(counter - 2) / 2}')
    return pi

d = float(input('Введите точность числа Пи от 0.1 до 0.0000000001: '))
res = PI(d)
print(res) # не при всех точностях выдает нужный результат


# to_round = 0.001
# pip = 3
# i = 2
# curr_round = to_round + 1
# sign = 4
# while curr_round > to_round:
#     pip += sign / (i * (i + 1) * (i + 2))
#     sign = -sign
#     pip_next = pip + sign / ((i + 2) * (i + 3) * (i +4))
#     curr_round = abs(pip - pip_next)
#     i += 2
# print(pip, (i/2))

# Вычисление Пи с помощью бесконечного числового ряда Лейбниц
pi = 0
counter = 3
for i in range(1, 99999999999, 4):
    a = 4 / i - 4 / counter
    counter += 4
    pi += a
    # print(sum)
print(pi)

# Вычисление Пи с формулы Валлиса
# pi = 2
# divisible = 2
# divider = 1
# a, b, c = 1, 1, 1
# for i in range(1500):
#     pi *= (divisible / divider) * (divisible / (divider + 2))
#     divisible += 2
#     divider += 2
#     # print(sum)
# print(pi)

# Вычисление Пи с помощью формулы Эйлера
# pi = 12
# divisible = 1
# divider = 1
# res = 0
# for i in range(50):
#     res += (divisible / divider**2) - (divisible / (divider + 1)**2)
#     divider += 2
#     # print(sum)
# pi *= res
# pi = pi**0.5
# print(pi)