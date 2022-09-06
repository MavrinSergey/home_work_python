# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

k = int((input('Программа показывает фракталы от 1 до указанного вами числа: ')))
counter = 1
sum = float()
while counter <= k:
        res = (1 + 1 / counter) ** counter
        counter += 1
        sum += res
print(sum)