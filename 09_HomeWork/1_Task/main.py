# 1. Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP
import random


def condition_of_victory(x: bool, y: list[list]):
    z = list(zip(y[0], y[1], y[2]))
    if y[0].count('0') == 3 or y[1].count('0') == 3 or y[2].count('0') == 3 or \
            z[0].count('0') == 3 or z[1].count('0') == 3 or z[2].count('0') == 3 or \
            y[0][0].count('0') == 1 and y[1][1].count('0') == 1 and y[2][2].count('0') == 1 or \
            y[0][2].count('0') == 1 and y[1][1].count('0') == 1 and y[2][0].count('0') == 1:
        return True
    return False


def check_input(x: int, y: str):
    while not (0 < x < 4):
        x = int(input(f'Введен неверный номер {y} введите заново (от 1 до 3): '))
    return x


pole = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

print('Вас приветствует игра в крестики нолики')
user1 = input('Введите имя первого игрока: ').capitalize()
user2 = input('Введите имя второго игрока: ').capitalize()
print(pole[0])
print(pole[1])
print(pole[2])
counter = random.randint(0, 1)
sum: bool = True
while sum:
    counter = not counter
    row = int(input(f'{user1 if counter else user2} ваш ход. Введите номер строки где нарисовать крестик: '))
    if not 0 < row < 4:
        row = check_input(row, 'строки')
    col = int(input(f'{user1 if counter else user2} ваш ход. Введите номер столбца где нарисовать крестик: '))

    if not 0 < col < 4:
        col = check_input(col, 'столбца')
    pole[row - 1][col - 1] = 'x' if counter else '0'
    for i in range(3):
        for j in range(3):
            sum += pole[i][j].count('x')
    print(pole[0])
    print(pole[1])
    print(pole[2])
    if condition_of_victory(counter, pole):
        print(f'{user1 if counter else user2} вы выйграли')
        print(pole[0])
        print(pole[1])
        print(pole[2])
        sum = not sum

        print(pole[0])
        print(pole[1])
        print(pole[2])
