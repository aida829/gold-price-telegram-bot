import logging
import asyncio
import jdatetime
from datetime import datetime
from aiogram import Bot, Dispatcher
from aiogram.types import InputFile

import os
TOKEN = os.getenv("7917634871:AAEfARByraLax2uiHclWMyz40fe-76Em8Kc")
CHANNEL_ID = os.getenv("https://t.me/talahatam")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def send_daily_gif():
    today_shamsi = jdatetime.datetime.now().strftime("1404/04/26")
    today_miladi = datetime.now().strftime("2025/07/17")
    text = f"📅17\n🇮🇷 26: {26}\n🌍 میلادی: {17}"

    gif_path = "daily.gif animated_logo.gif
    if os.path.exists(gif_path):
        gif = InputFile(gif_path)
        await bot.send_animation(chat_id=CHANNEL_ID, animation=gif, caption=text)
    else:
        await bot.send_message(chat_id=CHANNEL_ID, text=text)

async def main():
    # ارسال تستی GIF هنگام اجرای ربات
    await send_daily_gif()
    await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())