from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, timedelta

# הגדרת יעד (למשל בעוד 1 יום)
target_time = datetime.utcnow() + timedelta(days=1)

# חישוב הזמן שנותר
now = datetime.utcnow()
delta = target_time - now
days = delta.days
hours, remainder = divmod(delta.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

# יצירת תמונה עם רקע שקוף
width, height = 800, 200
image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)

# פונט ברירת מחדל
font = ImageFont.load_default()

# טקסט להצגה
text = f"Meeting in: {days:02} Days {hours:02} Hours {minutes:02} Min"

# מיקום מרכזי
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]
position = ((width - text_width) // 2, (height - text_height) // 2)

# ציור הטקסט
draw.text(position, text, fill="black", font=font)

# שמירה
image.save("countdown.png")
