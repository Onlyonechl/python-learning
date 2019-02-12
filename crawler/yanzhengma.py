
import pytesseract
from PIL import Image
from urllib3 import request
import time

pytesseract.pytesseract.tesseract_cmd = '/usr/local/Cellar/tesseract/3.05.02/bin/tesseract'

image = Image.open('3.jpg')
text = pytesseract.image_to_string(image)
print(text)

