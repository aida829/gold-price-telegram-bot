# gold-price-telegram-bot
import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import aiohttp
import json
from datetime import datetime
import pytz

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

# لیست جملات انگیزشی
with open("motivations.json", "r", encoding="utf-8") as f:
    motivations = json.load(f)

# تابع برای گرفتن قیمت‌ها از sarafiyaran.com (نمونه ساده)
async def fetch_prices():
    url = "https://sarafiyaran.com"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            html = await resp.text()
            # اینجا باید ساختار HTML رو بررسی و قیمت‌ها استخراج بشه
            # برای نمونه فرض می‌کنیم قیمت‌ها به شکل زیر استخراج شده:
            prices = {
                "gold24": 1580000,
                "gold18": 1180000,
                "coin_emam_86": 14500000,
                "half_coin_86": 7600000
                # بقیه قیمت‌ها ...
            }
            return prices

# تابع ارسال پیام قیمت‌ها
async def send_price_message():
    prices = await fetch_prices()
    now = datetime.now(pytz.timezone("Asia/Tehran"))
    date_shamsi = now.strftime("%Y/%m/%d")
    date_miladi = now.strftime("%Y-%m-%d")

    message = (
        f"📅 تاریخ: {date_shamsi} | {date_miladi}\n"
        "⏰ پایان معاملات: ساعت ۲۰:۰۰\n\n"
        "💰 قیمت‌ها (تومان):\n"
        f"▫ طلا ۲۴ عیار: {prices['gold24']:,}\n"
        f"▫ طلا ۱۸ عیار: {prices['gold18']:,}\n"
        f"▫ سکه امام ۸۶: {prices['coin_emam_86']:,}\n"
        f"▫ نیم سکه ۸۶: {prices['half_coin_86']:,}\n"
        # بقیه موارد رو اضافه کن
    )
    await bot.send_message(chat_id="@YourChannelName", text=message)

# تابع ارسال پیام پایان معاملات
async def send_end_message():
    msg = "✅ پایان معاملات امروز\n"
    msg += "✨ " + motivations[datetime.now().day % len(motivations)]
    await bot.send_message(chat_id="@YourChannelName", text=msg)

async def scheduler():
    while True:
        now = datetime.now(pytz.timezone("Asia/Tehran"))
        if now.hour == 9 and now.minute == 0:
            await send_price_message()
        if now.hour == 20 and now.minute == 0:
            await send_end_message()
        await asyncio.sleep(60)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(scheduler())
    executor.start_polling(dp)
    [
  "هر روز یک شروع تازه است، با قدرت ادامه بده!",
  "موفقیت از قدم‌های کوچک آغاز می‌شود.",
  "با تلاش امروز، فردای بهتری بساز.",
  "هیچ وقت از شکست نترس، از تلاش دست نکش!",
  "با امید به جلو حرکت کن.",
  "هر لحظه فرصت تازه‌ای است برای پیشرفت.",
  "به خودت ایمان داشته باش.",
  "نگذار مشکلات، تو را متوقف کنند.",
  "پشتکار، کلید موفقیت است.",
  "امروز بهترین روز برای شروع است.",
  "هدف‌هایت را فراموش نکن.",
  "با انگیزه قوی به دنبال رؤیاهایت برو.",
  "موفقیت در انتظار توست.",
  "قدم‌های کوچک، تغییرات بزرگ می‌آفرینند.",
  "از فرصت‌ها بهترین استفاده را بکن.",
  "اعتماد به نفس رمز پیروزی است.",
  "هر روزت را با لبخند شروع کن.",
  "با اراده قوی می‌توانی هر کاری انجام دهی.",
  "مسیر سخت، به مقصد شیرین می‌انجامد.",
  "رویاهات را به واقعیت تبدیل کن."
]aiogram
aiohttp
pytz
# Gold Price Telegram Bot

## راه اندازی

1. این ریپازیتوری رو کلون یا دانلود کن.
2. فایل `.env` بساز و توکن ربات تلگرام رو داخلش قرار بده:
3. # استفاده از Python 3.10
FROM python:3.10-slim

# تنظیم پوشه کاری
WORKDIR /app

# کپی کردن فایل‌ها به کانتینر
COPY . .

# نصب کتابخانه‌ها
RUN pip install --no-cache-dir -r requirements.txt

# اجرای ربات
CMD ["python", "main.py"]
from PIL import Image, ImageDraw, ImageFont
import datetime
import jdatetime

def create_daily_gif():
    # اندازه تصویر
    width, height = 600, 300
    img = Image.new('RGB', (width, height), color=(0, 0, 0))

    # فونت (باید فونت مناسب آپلود کنی)
    font = ImageFont.truetype("arial.ttf", 40)

    # تاریخ میلادی و شمسی
    miladi = datetime.datetime.now().strftime("%Y-%m-%d")
    shamsi = jdatetime.date.today().strftime("%Y/%m/%d")

    draw = ImageDraw.Draw(img)
    draw.text((50, 100), f"📅 {shamsi} | {miladi}", font=font, fill=(255, 215, 0))

    # ذخیره به عنوان GIF
    img.save("daily.gif", save_all=True, append_images=[img], duration=500, loop=0)

if __name__ == "__main__":
    create_daily_gif()
    aiogram==2.25.1
aiohttp==3.8.6
pytz==2023.3
Pillow==10.0.0
jdatetime==4.1.0
