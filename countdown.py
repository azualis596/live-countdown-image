from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

# יצירת רקע שקוף
width, height = 800, 200
image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)

# יעד הספירה לאחור
target_date = datetime(2025, 8, 1, 18, 0, 0)  # שנה לפי תאריך היעד שלך
now = datetime.now()
delta = target_date - now

days = delta.days
hours = delta.seconds // 3600
minutes = (delta.seconds % 3600) // 60

# טקסט לספירה לאחור
text = f"נפגשים בעוד: {days} ימים {hours:02} שעות {minutes:02} דקות"

# טען פונט בגודל מתאים (אם אין TTF – ישמש ברירת מחדל)
try:
    font = ImageFont.truetype("arial.ttf", 48)  # אפשר גם DejaVuSans.ttf
except:
    font = ImageFont.load_default()

# חישוב מיקום מרכזי
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
x = (width - text_width) // 2
y = (height - text_height) // 2

# ציור הטקסט
draw.text((x, y), text, font=font, fill="black")

# שמירת התמונה
image.save("countdown.png")
