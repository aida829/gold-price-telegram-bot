import asyncio
import datetime
import json
import random
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import jdatetime
from gif_generator import generate_gif_with_date

TELEGRAM_TOKEN =7917634871:AAEfARByraLax2uiHclWMyz40fe-76Em8Kc

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async def fetch_gold_prices():
    url = "https://sarafiyaran.com/"
    response = requests.get(url)
    # اینجا کد استخراج قیمت‌ها از HTML سایت رو اضافه کن
    # به عنوان نمونه فرضی:
    prices = {
        "gold_24": "1400000",
        "gold_18": "1050000",
        "coin_emam": "15000000",
        "coin_nim": "8000000",
        "coin_rob": "4000000",
        "coin_bahar": "14000000"
    }
    return prices

async def send_price_update():
    prices = await fetch_gold_prices()
    now = datetime.datetime.now()
    persian_date = jdatetime.datetime.now().strftime("%Y/%m/%d")
    gregorian_date = now.strftime("%Y-%m-%d")
    
    # تولید گیف با تاریخ
    gif_path = generate_gif_with_date(persian_date, gregorian_date)
    
    text = (
        f"قیمت‌های امروز ({persian_date} | {gregorian_date}):\n\n"
        f"طلای 24 عیار: {prices['gold_24']} تومان\n"
        f"طلای 18 عیار: {prices['gold_18']} تومان\n"
        f"سکه امامی: {prices['coin_emam']} تومان\n"
        f"نیم سکه: {prices['coin_nim']} تومان\n"
        f"ربع سکه: {prices['coin_rob']} تومان\n"
        f"سکه بهار آزادی: {prices['coin_bahar']} تومان\n\n"
        f"{random.choice(load_motivations())}"
    )
    
    await bot.send_animation(chat_id='@https://t.me/talahatam animation=open(gif_path, 'rb'), caption=text)

def load_motivations():
    with open('motivations.json', 'r', encoding='utf-8') as f:
        return json.load(f)

async def scheduler():
    while True:
        now = datetime.datetime.now()
        # ساعت 9 صبح برای ارسال قیمت
        if now.hour == 9 and now.minute == 0:
            await send_price_update()
        # ساعت 20 پایان معاملات
        if now.hour == 20 and now.minute == 0:
            await bot.send_message(chat_id='@your_channel_or_chat_id', text="ساعت ۸ شب است. معاملات امروز به پایان رسید. برای فردا انرژی مثبت داشته باشید!")
        await asyncio.sleep(60)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(scheduler())
    executor.start_polling(dp)