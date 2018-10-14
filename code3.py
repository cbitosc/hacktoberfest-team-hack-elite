from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

import os
datadir =r'C:/xampp/htdocs/'
javascripts=["uploads"]
for javascript in javascripts:
	path1=os.path.join(datadir,javascript)
	for img in os.listdir(path1):
		img=os.path.join(path1,img)

im = Image.open(os.path.join(path1,img))
text = pytesseract.image_to_string(im, lang='eng')
print(text)
from gtts import gTTS 
speech=gTTS(text)
speech.save("one.mp3") 
