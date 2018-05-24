from PIL import Image
import pytesseract
import splinter
from splinter import Browser
import cv2
import time

import urllib

a = "http://worksfromhome.in/Symetrix_AdminCode414/ClientImage/9500.jpg"
print "a"

urllib.urlretrieve(a, "locol.png")
print "b"
im = Image.open("locol.png")
print "c"

im.show()

print "d"