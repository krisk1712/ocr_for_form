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


line =[u'AUDRA ', u' CLEMENS ', u' 1003062738 ', u' Guriella Cabels privated limited company ', u' Single ', u' BH456211\n', u' KD74516871 ', u' 260001 ', u' ST JOHNS REGIONAL MEDICAL CENTER ', u' 2817 ST JOHNS BLVD ', u' JOPLIN\n', u' MO ', u' 64801 ', u' Cardiology ', u' MO - loplin ', u' 13 ', u' 16028.38 ', u' 5110.84 ', u' 4421.61 ', u' Employeed']
temp =0
for i in line:
    line1 = i.strip()
    print str(temp) +"     " + str(line1)
    temp = temp + 1
print len(line)