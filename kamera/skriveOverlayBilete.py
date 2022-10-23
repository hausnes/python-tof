from PIL import Image, ImageDraw
from datetime import datetime

filnavn = "test.jpg"
img = Image.open(filnavn)
d1 = ImageDraw.Draw(img)
d1.text((28, 36), "Bildetekst", fill=(255, 0, 0))
img.show()
img.save("test_med_tekst.jpg")

# Les meir om korleis du kan endre skriftstørrelse: https://www.tutorialspoint.com/python_pillow/python_pillow_writing_text_on_image.htm