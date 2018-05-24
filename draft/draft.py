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

    time.sleep(2)

    # id = id + 1
    # -------------------------------------------# SECTION ONE (7) -------------------------------------------#

    browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_tbc").fill(out[0].strip())  # first name
    browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_name").fill(out[1].strip())  # last name
    browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_email").fill(out[2].strip())  # email
    browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_mobno").fill(out[3].strip())  # mobile number
    browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_gender").fill(out[4].strip())  # gender
    browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_licenceno").fill(out[5].split('\\')[0].strip()) # licence number
    browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_girno").fill(out[6].strip())  # grid number
    time.sleep(2)

    id = id + 1
#     # ------------------------------------------- SECTION ONE END -------------------------------------------#
#
#     # ------------------------------------------- SECTION TWO START (7) -------------------------------------#
#
#     browser.find_by_id("__tab_ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail").click()  # provider tab click
#
#     browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_panno").fill(out[7].strip())  # pan number
#     browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_HState").fill(out[8].strip())  # state
#     browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_Hcity").fill(out[9].strip())  # city
#     browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_Hpin").fill(out[10].strip())  # pin
#     browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_Hadd").fill(out[11].strip())  # address
#     browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_Oadd").fill(out[12].strip())  # address
#     browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_Ocity").fill(out[13].strip())  # city
#     time.sleep(2)
#     # ------------------------------------------- SECTION TWO END ----------------------------------------------#
#
#     # -------------------------------------------##### SECTION THREE START (6) ----------------------------------#
#
#     browser.find_by_id("__tab_ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail").click()
#     browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_Opincode").fill(out[14].strip())  # pincode
#     browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_loanapproval").fill(out[15].strip())  # loan approval
#     browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_menno").fill(out[16].strip())  # men number
#     browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_af").fill(out[17].strip())  # af
#     browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_nri").fill(out[18].strip())  # nri
#     browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_cp").fill(out[19].strip())  # cpi
#     time.sleep(5)
#     # ------------------------------------------------- SECTION THREE END -------------------------------------------#
#
#     # ------------------------------------------------ SUBMISION ON END -------------------------------------------#
#
#     browser.find_by_id("ctl00_ContentPlaceHolder1_btnsubmit").click()  # submit
#
#     time.sleep(3)
#     id = id + 1
#     time.sleep(2)
#     #------------------------------------------- SUBMIT END -------------------------------------------#
#
#
# #---------------------------------------- FORM FILLING END -------------------------------------------#
#
#
#
# #------------------------------------------ LOGOUT -----------------------------#
#
# browser.find_by_id("ctl00_lnklogout").click()
#
# #----------------------------------------- DONE ---------------------------------#
