from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

# 🎯 תאריך יעד לאירוע
event_time = datetime(2025, 8, 5, 22, 30, 0)

# 🖼️ צור תמונה 800x200 עם רקע שקוף
img = Image.new("RGBA", (800, 200), (255, 255, 255, 0))
draw = ImageDraw.Draw(img)

# 🧠 חישוב הזמן הנותר
now = datetime.utcnow()
remaining = event_time - now

if remaining.total_seconds() <= 0:
    text = "🎉 האירוע התחיל!"
else:
    days = remaining.days
    hours, rem = divmod(remaining.seconds, 3600)
    minutes, _ = divmod(rem, 60)
    text = f"נפגשים בעוד: {days} ימים {hours} שעות {minutes} דקות"

# 🅰️ הגדרת פונט ברירת מחדל (אפשר לשדרג אחר כך)
font = ImageFont.load_default()

# 📏 חישוב גודל הטקסט עם textbbox במקום textsize
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# 🧭 מיקום מרכזי
x = (800 - text_width) // 2
y = (200 - text_height) // 2

# 🖋️ ציור הטקסט
draw.text((x, y), text, font=font, fill=(0, 0, 0))

# 💾 שמירה עם רקע שקוף
img.save("countdown.png")
