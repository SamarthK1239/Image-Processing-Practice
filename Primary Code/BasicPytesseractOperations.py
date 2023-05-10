from PIL import Image
from pytesseract import pytesseract
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="Environment Variables/.env")

path_to_tesseract = r"" + os.getenv('path_to_tesseract')

images_path = os.getenv('images_path')

current_image_index = 1

current_image_path = images_path + str(current_image_index) + ".jpg"

pytesseract.tesseract_cmd = path_to_tesseract

img = Image.open(current_image_path)

text = pytesseract.image_to_string(img)

print(text)