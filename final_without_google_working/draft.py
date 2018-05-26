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
print "#----------------------START HERE -----------------------------------#"

tic = time.clock()
print "#------------------ INFORMATION ON THE PAGE ARE : -----------------#"
print "THE LENGTH OF THE TOTAL PAGES ARE: "
print len(no_box)
id = 1073
while id < 2150 and id > 700:
    no_box = browser.find_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_drp_pagejump"]/option')

    no_box[id].click()
    time.sleep(1)

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
    print "THE LENGTH OF OUT IS AFTER SEP OF * : "
    print len(out)
    final = []
    for items in out:
        final.append(re.sub('\n', '', items))
    print"THE LENGTH OF THE FINAL LIST WITH TAKING OUT NEWLINE IS :"
    print len(final)
    flist1 = []
    for i in range(0, len(final)):
        flist1.extend(final[i].split("\""))
    print "THE LENGTH OF THE LIST THAT IS SPLIT INTO CORRECT ARE (\") : "
    print len(flist1)
    time.sleep(0.5)
    print "THE CURRENT PAGE IS"
    print id +1
    toc = time.clock()
    c = tic - toc
    print("THE TIME TAKEN TO COLLECT ALL THE INFORMATION IS : ")
    print c
    print "#----------------------------------THE FORM FILLING STARET FROM HERE--------------------------------#"
    tic = time.clock()

    # id = id + 1
    # -------------------------------------------# SECTION ONE (7) -------------------------------------------#
    try:
        browser.find_by_id("__tab_ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail").click() # tab detail
        time.sleep(0.5)
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_tbc").fill(flist1[0].strip())
        time.sleep(0.5)# first name
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_name").fill(flist1[1].strip())
        time.sleep(0.5)# last name
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_email").fill(flist1[2].strip())
        time.sleep(0.5)# email
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_mobno").fill(flist1[3].strip())
        time.sleep(0.5)# mobile number
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_gender").fill(flist1[4].strip())
        time.sleep(0.5)# gender
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_licenceno").fill(flist1[5].split('\\')[0].strip())
        time.sleep(0.5)# licence number
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_girno").fill(flist1[6].strip())  # grid number
        time.sleep(0.5)

        # ------------------------------------------- SECTION ONE END -------------------------------------------#

        # ------------------------------------------- SECTION TWO START (7) -------------------------------------#

        browser.find_by_id("__tab_ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail").click()  # provider tab click
        time.sleep(0.5)
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_panno").fill(flist1[7].strip())
        time.sleep(0.5)# pan number
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_HState").fill(flist1[8].strip())
        time.sleep(0.5)# state
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_Hcity").fill(flist1[9].strip())
        time.sleep(0.5)# city
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_Hpin").fill(flist1[10].strip())
        time.sleep(0.5)# pin
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_Hadd").fill(flist1[11].strip())
        time.sleep(0.5)# address
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_Oadd").fill(flist1[12].strip())
        time.sleep(0.5)# address
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_Ocity").fill(flist1[13].strip())# city
        time.sleep(0.5)
        # ------------------------------------------- SECTION TWO END ----------------------------------------------#

        # -------------------------------------------##### SECTION THREE START (6) ----------------------------------#

        browser.find_by_id("__tab_ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail").click()
        time.sleep(0.5)
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_Opincode").fill(flist1[14].strip())
        time.sleep(0.5)# pincode
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_loanapproval").fill(flist1[15].strip())
        time.sleep(0.5)# loan approval
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_menno").fill(flist1[16].strip())
        time.sleep(0.5)# men number
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_af").fill(flist1[17].strip())
        time.sleep(0.5)# af
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_nri").fill(flist1[18].strip())
        time.sleep(0.5)# nri
        browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_cp").fill(flist1[19].strip())
        time.sleep(0.5)# cpi
        time.sleep(1)
        # ------------------------------------------------- SECTION THREE END -------------------------------------------#

        # ------------------------------------------------ SUBMISION ON END -------------------------------------------#

        browser.find_by_id("ctl00_ContentPlaceHolder1_btnsubmit").click()  # submit
        toc = time.clock()
        a = tic - toc
        print
        print ("THE TIME TAKEN TO COMPLETE THE FORM IS : ")
        print(a)
        print "#------------------------ PAGE COMPLETED SUCESSFULL--------------------------#"
        time.sleep(0.5)
    except:
        print "#---------------------------- THE ERROR SECTION --------------------------#"
        f = open("error_log.txt", 'w')
        f.write("#---------------------------- THE ERROR SECTION --------------------------#")
        tic = time.clock()
        print "Error has occurred"
        f.write("Error has occurred")
        print "THE ERREOR OCCURED PAGE NUMBER IS ALWYS (n-1):"
        f.write("THE ERREOR OCCURED PAGE NUMBER IS ALWYS (n-1):")
        print id
        f.write(str(id))
        print"THE ERROR PAGE WITH THIS LIST SO PLEASE CHECK THIS : "
        f.write("THE ERROR PAGE WITH THIS LIST SO PLEASE CHECK THIS : ")
        print flist1
        # f.write(str(flist1))
        toc = time.clock()
        b = tic- toc
        print "THE TIME TAKEN TO GET THE ERROR OUT IS : "
        f.write("THE TIME FOR THE ERROR TO LOG :")
        print b
        f.write(str(b))
        f.write("#-----------------------------THE ERROR SECTION ENDS--------------------------#")
        print "#------------------------------ THE EROOR SECTION ENDS HERE --------------------#"

        id = id + 1
        continue
    id = id + 1
    #------------------------------------------- SUBMIT END -------------------------------------------#


#---------------------------------------- FORM FILLING END -------------------------------------------#



#------------------------------------------ LOGOUT -----------------------------#

browser.find_by_id("ctl00_lnklogout").click()

#----------------------------------------- DONE ---------------------------------#

