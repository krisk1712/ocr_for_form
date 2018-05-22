import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import pyautogui

import time

tic = time.clock()

im = Image.open("abre.png")  # the second one
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('temp2.png')
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
text = pytesseract.image_to_string(Image.open('temp2.png'))
print text

pyautogui.keyDown()

toc = time.clock()
a = tic-toc
print (a)