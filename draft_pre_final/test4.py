from PIL import Image
import pytesseract
import splinter
from splinter import Browser
import cv2
import time
import urllib
#------------------------------------ GLOBAL -----------------------------------------------------#
browser = Browser('chrome')
url = "http://worksfromhome.in/Customer/Default.aspx"
browser.visit(url)


#------------------------------------------------------- LOGIN -----------------------------------------#

browser.find_by_id("txt_Uname").fill("C070520182826")     # Enter the Users name
browser.find_by_id("txt_pass").fill("tvsm123#")             # entering the password
browser.find_by_id("btnsubmit").click()                     # submit to login

#------------------------------------------------ LOGED IN ----------------------------------------------#
time.sleep(10)

# state = browser.find_by_id('id of drop down box')
# for option_state in state.find_by_tag('option'):
#     print "the number is = " + (option_state.value)
#     st = option_state.value
#     option_state.click()
#     temp = 1
#
#     for option_city in city.find_by_tag('option'):
#
#         if temp <= 620:
#             temp = temp + 1
#         else:
