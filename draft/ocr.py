import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
from splinter import *
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
out = text.split("*")
browser = Browser('chrome')
url = "http://worksfromhome.in/Customer/Default.aspx"
browser.visit(url)
time.sleep(5)
browser.find_by_id("__tab_ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail").click()   #PROVIDERS DETAIL
browser.find_by_id("").fill(out[0])                                                               #
browser.find_by_id("").fill(out[1])                                                               #
browser.find_by_id("").fill(out[2])                                                               #
browser.find_by_id("").fill(out[3])                                                               #
browser.find_by_id("").fill(out[4])                                                               #
browser.find_by_id("").fill(out[5])                                                               #
browser.find_by_id("__tab_ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail").click()   #TRANSACTION DETAILS
browser.find_by_id("").fill(out[6])                                                               #
browser.find_by_id("").fill(out[7])                                                               #
browser.find_by_id("").fill(out[8])                                                               #
browser.find_by_id("").fill(out[9])                                                               #
browser.find_by_id("").fill(out[10])                                                               #
browser.find_by_id("").fill(out[11])                                                               #
browser.find_by_id("").fill(out[12])                                                               #
browser.find_by_id("ctl00_ContentPlaceHolder1_btnsubmit").click()  # SUBMIT
browser.find_by_id("").fill(out[13])                                                               #
browser.find_by_id("").fill(out[14])                                                               #
browser.find_by_id("").fill(out[15])                                                               #
browser.find_by_id("").fill(out[16])                                                               #
browser.find_by_id("").fill(out[17])                                                               #
browser.find_by_id("").fill(out[18])                                                                #
browser.find_by_id("").fill(out[19])
browser.find_by_id("ctl00_lnklogout").click()  # LOGOUT
toc = time.clock()
a = tic-toc
print (a)