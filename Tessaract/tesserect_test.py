from PIL import Image
from email.mime import image
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\ADAWAS\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

img = Image.open('wow.jpg')
txt = tess.image_to_string(img)

print(txt)
