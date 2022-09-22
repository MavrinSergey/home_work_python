# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# u00B2
# a = '2\u00B2'
# print(a)
import random


k = int(input('Введите число: '))
polynomial = [str(random.randint(0, 100)) + (f'x**{x}') for x in range(k, -1, -1)]
print(polynomial)
resul_list = list(map(lambda x: x.translate({ord(i): None for i in 'x**0'}) + ' = 0' if 'x**0' in x else x + ' + ', polynomial))
print(resul_list)

data = open('D:/EducationalProjects/03_Python/HomeWork/04_HomeWork/file.txt', 'w') # a - (добавляет) r - чтение w - (перезаписывает)
data.writelines(resul_list) # разделителей не будет

data.close()