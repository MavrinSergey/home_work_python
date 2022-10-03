from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
from bs4 import BeautifulSoup as BS
from aiogram import *
from config import *
from pytube import YouTube


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'start {update.effective_user.first_name}! Я могу предсказывать погоду и скачивать видео с Youtube. Для того, что бы узнать как это сделать напиши команду /help')
   

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/help\n'
                                f'/start - приветствует вас\n'
                                f'/help - показывает возможные команды\n'
                                f'/get - принимает аргумент - название города на русском, и возвращает текукщую погоду\n'
                                f'/download (ссылка) - скачивает видео из Ютуб.\n')
    

async def get_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    city = msg.split()[1]  # вычленяет из команды название города
    r = requests.get('https://sinoptik.ua/погода-' + city)
    html = BS(r.content, 'html.parser')

    s = ''
    for day in range(3):
        for el in html.select('#content'):
            t_min = el.select('.temperature .min')[day].text
            t_max = el.select('.temperature .max')[day].text
            s += ("Сегодня: ", "Завтра: ", "Послезавтра: ")[day]
            s += str('\t' + t_min + ', ' + t_max + '\n')
    print(s)
    await update.message.reply_text(s)



async def download_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat.id
    url = update.message.text
    yt = YouTube(url)
    if update.message.text.startswith == 'http://youtu.be/' or 'http://www.youtube.com/':
        await Bot(TOKEN).send_message(chat_id, f'*Начинаю загрузку видео* : *{yt.title}*\n'
                                        f'*С канала *: [{yt.author}]({yt.channel_url})', parse_mode='Markdown')
        await download_youtube_video(url, update.message, TOKEN)

 

