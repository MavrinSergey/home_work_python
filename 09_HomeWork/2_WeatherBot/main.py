import json
import telebot
import requests as req
from geopy import geocoders
from os import environ

token = environ['5759772520:AAEVHcs8e7Jd4lA-pjZ8GoZRcZR382rCnWs']
# token_accu = environ['token_accu']
token_yandex = environ['4ac044f7-1951-44d8-a889-2b764f9911d9']

bot = telebot.TeleBot(token_yandex)

with open('cities.json', encoding='utf-8') as f:
    cities = json.load(f)

bot.polling(none_stop=True)