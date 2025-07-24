from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

# זמן האירוע שלך
event_time = datetime(2025, 8, 5, 22, 30, 0)

# צור תמונה שקופה בגודל 800x200
img = Image.new("RGBA", (800, 200), (255, 255, 255, 0))
draw = ImageDraw.Draw(img)

# חישוב זמן נותר
now = datetime.utcnow()
remaining = event_time - now

if remaining.total_seconds() <= 0:
    text = "🎉 האירוע התחיל!"
else:
    days = remaining.days
    hours, rem = divmod(remaining.seconds, 3600)
    minutes, _ = divmod(rem, 60)
    text = f"נפגשים בעוד: {days} ימים {hours} שעות {minutes} דקות"

# פונט בסיסי, טקסט שחור
font = ImageFont.load_default()

# מיקום הטקסט – מרכז אופקי
text_width, text_height = draw.textsize(text, font=font)
x = (800 - text_width) // 2
y = (200 - text_height) // 2

draw.text((x, y), text, fill=(0, 0, 0), font=font)

# שמור את התמונה עם רקע שקוף
img.save("countdown.png")
