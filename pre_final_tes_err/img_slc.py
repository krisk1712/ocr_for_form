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
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
text = pytesseract.image_to_string(Image.open('2_line.png'))
out = text.split("*")
print out
print len(out)
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
text = pytesseract.image_to_string(Image.open('3_line.png'))
out = text.split("*")
print out
print len(out)
browser = Browser('chrome')
url = "http://worksfromhome.in/Customer/Default.aspx"
browser.visit(url)
################################################## LOGIN #######################################

browser.find_by_id("txt_Uname").fill("C070520182826")     # Enter the Users name
browser.find_by_id("txt_pass").fill("tvsm123#")             # entering the password
browser.find_by_id("btnsubmit").click()                     # submit to login

################################################## LOGED IN ####################################
time.sleep(5)
############################################# FORM FILLING ######################################



############################################ SECTION ONE (7) ######################################

browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_tbc").fill(out[0])   # first name
browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_name").fill(out[1])     #last name
browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_email").fill(out[2])    #email
browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_mobno").fill(out[3])    #mobile number
browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_gender").fill(out[4])   #gender
browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_licenceno").fill(out[5])    #licence number
browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_girno").fill(out[6])    #grid number

########################################## SECTION ONE END ########################################


######################################### SECTION TWO START (7) ####################################

browser.find_by_id("__tab_ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail").click()              #provider tab click

browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_panno").fill(out[7])     #pan number
browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_HState").fill(out[8])   # state
browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_Hcity").fill(out[9])    #city
browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_Hpin").fill(out[10])    #pin
browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_Hadd").fill(out[11])    #address
browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_Oadd").fill(out[12])    #address
browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_Ocity").fill(out[13])   # city

########################################### SECTION TWO END #########################################

########################################## SECTION THREE START (6) ##################################

browser.find_by_id("__tab_ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail").click()
browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_Opincode").fill(out[14])     #pincode
browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_loanapproval").fill(out[15])     #loan approval
browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_menno").fill(out[16])    #men number
browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_af").fill(out[17])       #af
browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_nri").fill(out[18])      #nri
browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_cp").fill(out[19])       #cpi

############################################## SECTION THREE END ######################################

############################################# SUBMISION ON END #######################################

browser.find_by_id("ctl00_ContentPlaceHolder1_btnsubmit").click()    # submit

####################################### SUBMIT END #####################################################


############################## FORM FILLING END ##########################################################



############################### LOGOUT ###############################

browser.find_by_id("ctl00_lnklogout").click()

############################## DONE ##################################
