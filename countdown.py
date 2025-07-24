from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

# תאריך האירוע שלך (שנה, חודש, יום, שעה, דקה, שנייה)
event_time = datetime(2025, 8, 5, 22, 30, 0)

# צור תמונה בגודל 600x200 עם רקע לבן
img = Image.new('RGB', (600, 200), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

# חישוב זמן נותר
now = datetime.utcnow()
remaining = event_time - now

if remaining.total_seconds() <= 0:
    text = "🎉 האירוע התחיל!"
else:
    days = remaining.days
    hours, rem = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    text = f"⏳ נותרו {days} ימים {hours:02}:{minutes:02}:{seconds:02}"

# נסה להשתמש בפונט arial אם קיים, אחרת ברירת מחדל
try:
    font = ImageFont.truetype("arial.ttf", 32)
except:
    font = ImageFont.load_default()

# כתוב את הטקסט על התמונה
draw.text((30, 80), text, font=font, fill=(0, 0, 0))

# שמור את התמונה בשם קבוע
img.save("countdown.png")
