# -*- coding: \xc2 -*-

from splinter import Browser
import time
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
from splinter import *
import time
tic = time.clock()
browser = Browser('chrome')
url = "file:///C:/Users/servadmin/Documents/Atom%20Projects/formfill/index.html"
browser.visit(url)
im = Image.open("abre.png")  # the second one
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('temp2.png')
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
text = pytesseract.image_to_string(Image.open('temp2.png'))
out = text.split("*")

browser.find_by_id("1").fill(out[0])                                                               #
browser.find_by_id("2").fill(out[1])                                                               #
browser.find_by_id("3").fill(out[2])                                                               #
browser.find_by_id("4").fill(out[3])                                                               #
browser.find_by_id("5").fill(out[4])                                                               #
browser.find_by_id("6").fill(out[5])                                                               #
# browser.find_by_id("__tab_ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail").click()   #TRANSACTION DETAILS
browser.find_by_id("7").fill(out[6])                                                               #
browser.find_by_id("8").fill(out[7])                                                               #
browser.find_by_id("9").fill(out[8])                                                               #
browser.find_by_id("10").fill(out[9])                                                               #
browser.find_by_id("11").fill(out[10])                                                               #
browser.find_by_id("12").fill(out[11])                                                               #
browser.find_by_id("13").fill(out[12])                                                               #
# browser.find_by_id("ctl00_ContentPlaceHolder1_btnsubmit").click()  # SUBMIT
browser.find_by_id("14").fill(out[13])                                                               #
browser.find_by_id("15").fill(out[14])                                                               #
browser.find_by_id("16").fill(out[15])                                                               #
browser.find_by_id("17").fill(out[16])                                                               #
browser.find_by_id("18").fill(out[17])                                                               #
browser.find_by_id("19").fill(out[18])                                                                #
browser.find_by_id("20").fill(out[19])

