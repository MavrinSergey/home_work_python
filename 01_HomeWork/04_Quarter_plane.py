# 04. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

x = int(input('Программа по заданному номеру четверти, показывает диапазон возможных координат точек.\nВведите четверть: '))
while (x < 1) or (4 < x):
    x  = int(input('При выборе четверти пользуйтесь цифрами от 1 до 4. Введите четверть повторно: '))

if (x == 1):
    print('X > 0 и Y > 0')
    
elif (x == 2):
    print('X < 0 и Y > 0')
    
elif (x == 3):
    print('X < 0 и Y < 0')
    
else:
    print('X > 0 и Y < 0')