import asyncio
import requests
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from datetime import datetime
import jdatetime
import random

API_TOKEN = "7917634871:AAEfARByraLax2uiHclWMyz40fe-76Em8Kc"
CHANNEL_ID = "@talahatam"  # آیدی کانال یا گروه تلگرام
GIF_PATH = "animated_logo.gif"  # نام فایل گیف لوگو (باید کنار main.py باشه)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

motivational_texts = [
    "امروز را با امید شروع کن و با موفقیت به پایان برسان!",
    "هر روز فرصتی است برای بهتر شدن، استفاده کن!",
    "با تلاش و صبر، پیروزی نزدیک است.",
    "موفقیت نتیجه استمرار است، تو قادری!",
    "امروز یک قدم به هدف نزدیک‌تر شدی.",
    "ذهن مثبت، زندگی مثبت می‌آفریند.",
    "هر شکست، پلی به سوی موفقیت است.",
    "قدرت درونت را باور کن و حرکت کن.",
    "لحظه‌های امروزت را به بهترین شکل بساز.",
    "تو بهترین نسخه خودت هستی، بدرخش!",
    "چالش‌ها فقط موانع نیستند، فرصت‌اند.",
    "هر روز را با انرژی شروع کن و ادامه بده.",
    "موفقیت در انتظار توست، پیش برو!",
    "با خودت مهربان باش، شایسته‌اش هستی.",
    "امروز، روز تغییر توست.",
    "آینده روشن‌تر از آن است که فکرش را می‌کنی.",
    "با امید و تلاش، ناممکن‌ها ممکن می‌شوند.",
    "هر صبح یک شروع تازه است، قدرش را بدان.",
    "تو قدرت ایجاد هر چیزی را داری.",
    "زندگی را با عشق و تلاش بساز."
]

def get_dates():
    now = datetime.now()
    persian_date = jdatetime.datetime.now().strftime("%Y/%m/%d")
    gregorian_date = now.strftime("%Y-%m-%d")
    return persian_date, gregorian_date

def get_prices():
    url = "https://sarafiyaran.com"
    try:
        r = requests.get(url)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        
        # --- اینها شناسه‌ها فرضی هستن، ممکنه لازم باشه اصلاح کنی ---
        gold_24 = soup.find("span", {"id": "gold_24_price"}).text.strip()  
        gold_18 = soup.find("span", {"id": "gold_18_price"}).text.strip()  
        seke_emami = soup.find("span", {"id": "seke_emami_price"}).text.strip()  
        
        return f"طلا 24 عیار: {gold_24} تومان\nطلا 18 عیار: {gold_18} تومان\nسکه امامی: {seke_emami} تومان"
    except Exception as e:
        return "قیمت‌ها فعلا در دسترس نیست."

async def send_daily_update(chat_id):
    persian_date, gregorian_date = get_dates()
    prices_text = get_prices()
    text = f"قیمت‌های امروز ({persian_date} - {gregorian_date}):\n\n{prices_text}"
    with open(GIF_PATH, 'rb') as gif_file:
        await bot.send_animation(chat_id=chat_id, animation=gif_file, caption=text)

async def send_market_close(chat_id):
    text = random.choice(motivational_texts)
    await bot.send_message(chat_id=chat_id, text=f"پایان معاملات امروز!\n\n{text}")

async def scheduler(chat_id):
    sent_update_today = False
    sent_close_today = False
    while True:
        now = datetime.now()
        if now.hour == 9 and now.minute == 0 and not sent_update_today:
            await send_daily_update(chat_id)
            sent_update_today = True
        if now.hour == 20 and now.minute == 0 and not sent_close_today:
            await send_market_close(chat_id)
            sent_close_today = True
        if now.hour == 21:
            sent_update_today = False
            sent_close_today = False
        await asyncio.sleep(30)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.reply("ربات شروع به کار کرد و قیمت‌ها را هر روز ساعت ۹ صبح و پایان معاملات ساعت ۸ شب ارسال خواهد کرد.")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(scheduler(CHANNEL_ID))
    executor.start_polling(dp, skip_updates=True)