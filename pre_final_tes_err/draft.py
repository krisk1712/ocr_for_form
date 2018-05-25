from PIL import Image
import pytesseract
import splinter
from splinter import Browser
import cv2
import time
import urllib
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
id = 622
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

    print len(out)
    final = []
    for items in out:
        final.append(re.sub('\n', '', items))


    time.sleep(1)

    # id = id + 1
    # -------------------------------------------# SECTION ONE (7) -------------------------------------------#
    try:
        browser.find_by_id("__tab_ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail").click() # tab detail
        time.sleep(1)
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_tbc").fill(final[0].strip())
        time.sleep(1)# first name
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_name").fill(final[1].strip())
        time.sleep(1)# last name
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_email").fill(final[2].strip())
        time.sleep(1)# email
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_mobno").fill(final[3].strip())
        time.sleep(1)# mobile number
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_gender").fill(final[4].strip())
        time.sleep(1)# gender
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_licenceno").fill(final[5].split('\\')[0].strip())
        time.sleep(1)# licence number
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_girno").fill(final[6].strip())  # grid number
        time.sleep(1)

        # ------------------------------------------- SECTION ONE END -------------------------------------------#

        # ------------------------------------------- SECTION TWO START (7) -------------------------------------#

        browser.find_by_id("__tab_ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail").click()  # provider tab click
        time.sleep(1)
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_panno").fill(final[7].strip())
        time.sleep(1)# pan number
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_HState").fill(final[8].strip())
        time.sleep(1)# state
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_Hcity").fill(final[9].strip())
        time.sleep(1)# city
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_Hpin").fill(final[10].strip())
        time.sleep(1)# pin
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_Hadd").fill(final[11].strip())
        time.sleep(1)# address
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_Oadd").fill(final[12].strip())
        time.sleep(1)# address
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_Ocity").fill(final[13].strip())# city
        time.sleep(1)
        # ------------------------------------------- SECTION TWO END ----------------------------------------------#

        # -------------------------------------------##### SECTION THREE START (6) ----------------------------------#

        browser.find_by_id("__tab_ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail").click()
        time.sleep(1)
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_Opincode").fill(final[14].strip())
        time.sleep(1)# pincode
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_loanapproval").fill(final[15].strip())
        time.sleep(1)# loan approval
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_menno").fill(final[16].strip())
        time.sleep(1)# men number
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_af").fill(final[17].strip())
        time.sleep(1)# af
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_nri").fill(final[18].strip())
        time.sleep(1)# nri
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_cp").fill(final[19].strip())
        time.sleep(1)# cpi
        time.sleep(3)
        # ------------------------------------------------- SECTION THREE END -------------------------------------------#

        # ------------------------------------------------ SUBMISION ON END -------------------------------------------#

        browser.find_by_id("ctl00_ContentPlaceHolder1_btnsubmit").click()  # submit

        time.sleep(1)
    except:
        print "Error has occurred"
        print final
        id = id + 1
        continue
    id = id + 1
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
