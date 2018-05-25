import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from google.cloud.vision_v1 import *
print "PLEASE DONT WORK"
print "a"
# Instantiates a client
client = vision.ImageAnnotatorClient(credentials='important.json')  #credentials='important.json'
print "b"
# The name of the image file to annotate
file_name = os.path.join(os.path.dirname(__file__),'fale1.jpg')
print "c"
# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
print type(content)
print "d"
image = types.Image(content=content)
print("e")
print(type(image))
# Performs label detection on the image file
response = client.label_detection(image=image)
print response
labels = response.label_annotations
print("f")
print('Labels:')
for label in labels:
    print(label.description)
    print "g"
print "h"