from PIL import Image
import pytesseract
import splinter
from splinter import Browser
import cv2
import time

img =  Image.open("abre.png")
img2 = img.crop((49,39,899,71))
one = img2.save("1_line.png")
img2 = img.crop((24,78,921,109))
two = img2.save("2_line.png")
img2 = img.crop((103,116,845,142))
tree = img2.save("3_line.png")

im1 = Image.open("1_line.png")
im2 = Image.open("2_line.png")
im3 = Image.open("3_line.png")
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
text = pytesseract.image_to_string(Image.open('1_line.png'))
out = text.split("*")
print out
print len(out)

for i in range(0,len(out)):
    print out[i]

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
text = pytesseract.image_to_string(Image.open('2_line.png'))
out = text.split("*")
print out
print len(out)
for i in range(0,len(out)):
    print out[i]

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
text = pytesseract.image_to_string(Image.open('3_line.png'))
out = text.split("*")
print out
print len(out)

for i in range(0,len(out)):
    print out[i]