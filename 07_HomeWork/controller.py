import gui
from process import creat_contact

count = 1
action = int(gui.input_user('Что будем делать?(1 - добавление контакта, 2 - удаление контакта, 3 - редактирование контактаб поиск контакта: '))
print(action)
if action == 1:
    row = creat_contact()
print(row)