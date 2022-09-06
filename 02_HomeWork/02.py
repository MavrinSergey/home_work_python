# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: -пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int((input('Программа показывает фракталы от 1 до указанного вами числа: ')))
counter = 1
frac = 1
while counter <= N:
    if counter == 1:
        frac = frac * counter
        counter += 1
        print(f"[ {frac}", end=", ")
    elif counter == N:
        frac = frac * counter
        counter += 1
        print(f"{frac}", end=" ]")
    else:
        frac = frac * counter
        counter += 1
        print(f"{frac}", end=", ")
