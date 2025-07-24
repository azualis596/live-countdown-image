from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

# יעד הספירה לאחור
target_date = datetime(2025, 8, 10, 22, 0, 0)  # שנה, חודש, יום, שעה, דקה, שנייה

# חישוב הזמן שנותר
now = datetime.utcnow()
remaining = target_date - now
days = remaining.days
hours, remainder = divmod(remaining.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

# יצירת תמונה שקופה בגודל 800x200
width, height = 800, 200
image = Image.new("RGBA", (width, height), (255, 255, 255, 0))  # רקע שקוף
draw = ImageDraw.Draw(image)

# טקסט להצגה
text = f"{days:02d} Days  {hours:02d} Hours  {minutes:02d} Min"

# חישוב מיקום מרכזי
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]
x = (width - text_width) // 2
y = (height - text_height) // 2

# כתיבת טקסט בצבע שחור
draw.text((x, y), text, font=font, fill=(0, 0, 0, 255))

# שמירת הקובץ
image.save("countdown.png")
