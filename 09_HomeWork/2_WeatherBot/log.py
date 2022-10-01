import json
import telebot
import requests as req
from geopy import geocoders
from os import environ
from main import *


token = environ['token_bot']
token_accu = environ['token_accu']
token_yandex = environ['token_yandex']

def geo_pos(city: str):
    geolocator = geocoders.Nominatim(user_agent="telebot")
    latitude = str(geolocator.geocode(city).latitude)
    longitude = str(geolocator.geocode(city).longitude)
    return latitude, longitude

def code_location(latitude: str, longitude: str, token_accu: str):
    url_location_key = f'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey={token_accu}&q={latitude},{longitude}&language=ru'
    resp_loc = req.get(url_location_key, headers={"APIKey": token_accu})
    json_data = json.loads(resp_loc.text)
    code = json_data['Key']
    return code

def yandex_weather(latitude, longitude, token_yandex: str):
    url_yandex = f'https://api.weather.yandex.ru/v2/informers/?lat={latitude}&lon={longitude}&[lang=ru_RU]'
    yandex_req = req.get(url_yandex, headers={'X-Yandex-API-Key': token_yandex}, verify=False)
    conditions = {'clear': 'ясно', 'partly-cloudy': 'малооблачно', 'cloudy': 'облачно с прояснениями',
                  'overcast': 'пасмурно', 'drizzle': 'морось', 'light-rain': 'небольшой дождь',
                  'rain': 'дождь', 'moderate-rain': 'умеренно сильный', 'heavy-rain': 'сильный дождь',
                  'continuous-heavy-rain': 'длительный сильный дождь', 'showers': 'ливень',
                  'wet-snow': 'дождь со снегом', 'light-snow': 'небольшой снег', 'snow': 'снег',
                  'snow-showers': 'снегопад', 'hail': 'град', 'thunderstorm': 'гроза',
                  'thunderstorm-with-rain': 'дождь с грозой', 'thunderstorm-with-hail': 'гроза с градом'
                  }
    wind_dir = {'nw': 'северо-западное', 'n': 'северное', 'ne': 'северо-восточное', 'e': 'восточное',
                'se': 'юго-восточное', 's': 'южное', 'sw': 'юго-западное', 'w': 'западное', 'с': 'штиль'}

    yandex_json = json.loads(yandex_req.text)
    yandex_json['fact']['condition'] = conditions[yandex_json['fact']['condition']]
    yandex_json['fact']['wind_dir'] = wind_dir[yandex_json['fact']['wind_dir']]
    for parts in yandex_json['forecast']['parts']:
        parts['condition'] = conditions[parts['condition']]
        parts['wind_dir'] = wind_dir[parts['wind_dir']]

    pogoda = dict()
    params = ['condition', 'wind_dir', 'pressure_mm', 'humidity']
    for parts in yandex_json['forecast']['parts']:
        pogoda[parts['part_name']] = dict()
        pogoda[parts['part_name']]['temp'] = parts['temp_avg']
        for param in params:
            pogoda[parts['part_name']][param] = parts[param]

    pogoda['fact'] = dict()
    pogoda['fact']['temp'] = yandex_json['fact']['temp']
    for param in params:
        pogoda['fact'][param] = yandex_json['fact'][param]

    pogoda['link'] = yandex_json['info']['url']
    return pogoda

def print_yandex_weather(dict_weather_yandex, message):
    day = {'night': 'ночью', 'morning': 'утром', 'day': 'днем', 'evening': 'вечером', 'fact': 'сейчас'}
    bot.send_message(message.from_user.id, f'А яндекс говорит:')
    for i in dict_weather_yandex.keys():
        if i != 'link':
            time_day = day[i]
            bot.send_message(message.from_user.id, f'Температура {time_day} {dict_weather_yandex[i]["temp"]}'
                                                   f', на небе {dict_weather_yandex[i]["condition"]}')

    bot.send_message(message.from_user.id, f' А здесь ссылка на подробности '
                                           f'{dict_weather_yandex["link"]}')

def big_weather(message, city):
    latitude, longitude = geo_pos(city)
    cod_loc = code_location(latitude, longitude, token_accu)
    # you_weather = weather(cod_loc, token_accu)
    # print_weather(you_weather, message)
    yandex_weather_x = yandex_weather(latitude, longitude, token_yandex)
    print_yandex_weather(yandex_weather_x, message)

def add_city(message):
    try:
        latitude, longitude = geo_pos(message.text.lower().split('город ')[1])
        global cities
        cities[message.from_user.id] = message.text.lower().split('город ')[1]
        with open('cities.json', 'w') as f:
            f.write(json.dumps(cities))
        return cities, 0
    except Exception as err:
        return cities, 1