from PIL import Image
import pytesseract
import splinter
from numpy.polynomial.tests.test_hermite import trim
from splinter import Browser
import cv2
import time
import urllib
import string
import re
#------------------------------------ GLOBAL -----------------------------------------------------#
browser = Browser('chrome')
url = "http://worksfromhome.in/Customer/Default.aspx"
browser.visit(url)


#------------------------------------------------------- LOGIN -----------------------------------------#

browser.find_by_id("txt_Uname").fill("C070520182826")     # Enter the Users name
browser.find_by_id("txt_pass").fill("tvsm123#")             # entering the password
browser.find_by_id("btnsubmit").click()                     # submit to login

#------------------------------------------------ LOGED IN ----------------------------------------------#


#------------------------------------------------- FORM FILLING ------------------------------------------#
no_box = browser.find_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_drp_pagejump"]/option')
print len(no_box)
id = 620
while id < len(no_box) and id > 619:
    no_box = browser.find_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_drp_pagejump"]/option')

    no_box[id].click()
    time.sleep(3)

    # ------------------------------------------------ PRINTING THE IMAGE URL FOR DOWNLOAD ----------------------------------------------#
    image_url = browser.find_by_id('ctl00_ContentPlaceHolder1_MainImg')['src']

    # ----------------------------------------- SAVING IMAGE VIA URLLIB --------------------------------#
    urllib.urlretrieve(image_url, "locol1.png")
    # -------------------------------------------- IMAGE SAVED AS (loco.png) -----------------------------#

    # ----------------------------------------- PYTESSRACT OCR -------------------------------------------#
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
    text = pytesseract.image_to_string(Image.open('locol1.png'))

    # -------------------------------------- TEXT COVERTERD BY THE OCR --------------------------------------#
    out = text.split("*")
    print out
    print len(out)
    for i in range(0,len(out)):
        print out[i]