# استفاده از تصویر رسمی پایتون 3.10
FROM python:3.10-slim

# نصب وابستگی‌های لازم برای Pillow و Requests
RUN apt-get update && apt-get install -y \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# تعیین دایرکتوری کاری
WORKDIR /app

# کپی کردن فایل requirements.txt و نصب پکیج‌ها
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# کپی کردن باقی فایل‌های پروژه
COPY . .

# اجرای فایل اصلی
CMD ["python", "main.py"]