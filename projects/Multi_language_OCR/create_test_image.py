from PIL import Image, ImageDraw, ImageFont

# Create an image with white background
img = Image.new('RGB', (400, 100), color=(255, 255, 255))
d = ImageDraw.Draw(img)

# Try to use a standard font, fallback to default
try:
    font = ImageFont.truetype("arial.ttf", 36)
except:
    font = ImageFont.load_default()

d.text((20, 30), "Hello Python OCR!", fill=(0, 0, 0), font=font)

img.save('test_ocr.png')
print("Created test_ocr.png")
