TOKEN = '5759772520:AAEVHcs8e7Jd4lA-pjZ8GoZRcZR382rCnWs'
import os
from pytube import YouTube


async def download_youtube_video(url, message, bot):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4')
    stream.get_highest_resolution().download(f'{message.chat.id}', f'{message.chat.id}_{yt.title}')
    with open(f'{message.chat.id}/{message.chat.id}_{yt.title}', 'rb') as video:
        await bot.send_video(message.chat.id, video, caption='*Вот ваше видео *', parse_mode='Markdown')
        os.remove(f'{message.chat.id}/{message.chat.id}_{yt.title}')







