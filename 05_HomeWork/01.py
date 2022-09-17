# Задача 021:
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
def file_reading(x):
    with open(f'D:/EducationalProjects/03_Python/HomeWork/05_HomeWork/{x}', 'r', encoding="utf-8") as file:
        y = file.read()
    return y


my_string = file_reading('file.txt').split()
search_value = 'абв'
print(my_string)
result_list2 = [item for item in my_string if search_value not in item]
print(result_list2)

