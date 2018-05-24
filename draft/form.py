
import pyautogui
import imutils
import cv2
import os
import argparse
import pytesseract
from PIL import Image
import time

tic = time.clock()



# pyautogui.screenshot("straightodisk.png")
# img = Image.open('7332.png')
# img.show()
# im = pyautogui.screenshot(region=(0,0, 300, 400))

image = cv2.imread(r"C:\Users\servadmin\Desktop\test.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# gray = cv2.medianBlur(gray, 3)
filename = "temp.png"
cv2.imwrite(filename, gray)
gray = gray.convert('1')
gray.save("temp2.png")


text = pytesseract.image_to_string(Image.open("temp2.png"))
os.remove(filename)
print(text)



toc = time.clock()
a = tic-toc
print (a)
