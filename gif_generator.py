from PIL import Image, ImageDraw, ImageFont
import datetime

def generate_gif_with_date(persian_date, gregorian_date):
    # ابعاد تصویر
    width, height = 400, 100

    # ایجاد تصویر سفید
    img = Image.new('RGBA', (width, height), (255, 255, 255, 0))

    draw = ImageDraw.Draw(img)

    # فونت (برای ویندوز یا لینوکس مسیر مناسب فونت را بگذارید)
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    font = ImageFont.truetype(font_path, 24)

    # نوشتن تاریخ‌ها
    draw.text((10, 20), f"تاریخ شمسی: {persian_date}", fill="black", font=font)
    draw.text((10, 60), f"Gregorian: {gregorian_date}", fill="black", font=font)

    # ذخیره موقت گیف
    gif_path = "date.gif"
    img.save(gif_path, "GIF")

    return gif_path