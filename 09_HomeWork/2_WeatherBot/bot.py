from main import *
from log import *

@bot.message_handler(command=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я погодабот, приятно познакомитсья, {message.from_user.first_name}')

bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global cities
    if message.text.lower() == 'привет' or message.text.lower() == 'здорова':
        bot.send_message(message.from_user.id,
                         f'О великий и могучий {message.from_user.first_name}! Позвольте Я доложу '
                         f' Вам о погоде! Напишите  слово "погода" и я напишу погоду в Вашем'
                         f' "стандартном" городе или напишите название города в котором Вы сейчас')
    elif message.text.lower() == 'погода':
        if message.from_user.id in cities.keys():
            city = cities[message.from_user.id]
            bot.send_message(message.from_user.id, f'О великий и могучий {message.from_user.first_name}!'
                                                   f' Твой город {city}')
            big_weather(message, city)

        else:
            bot.send_message(message.from_user.id, f'О великий и могучий {message.from_user.first_name}!'
                                                   f' Я не знаю Ваш город! Просто напиши:'
                                                   f'"Мой город *****" и я запомню твой стандартный город!')
    elif message.text.lower()[:9] == 'мой город':
        cities, flag = add_city(message)
        if flag == 0:
            bot.send_message(message.from_user.id, f'О великий и могучий {message.from_user.first_name}!'
                                                   f' Теперь я знаю Ваш город! это'
                                                   f' {cities[str(message.from_user.id)]}')
        else:
            bot.send_message(message.from_user.id, f'О великий и могучий {message.from_user.first_name}!'
                                                   f' Что то пошло не так :(')
    else:
        try:
            city = message.text
            bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}! Твой город {city}')
            big_weather(message, city)
        except AttributeError as err:
            bot.send_message(message.from_user.id, f'{message.from_user.first_name}! Не вели казнить,'
                                                   f' вели слово молвить! Я не нашел такого города!'
                                                   f'И получил ошибку {err}, попробуй другой город')
