import io
import os
# Imports the Google Cloud client library
from google.cloud import vision
print "a"
# Instantiates a client (Change the line below******)
vision_client = vision.ImageAnnotatorClient(credentials='My Project-6748fa243896.json')
print "b"
# The name of the image file to annotate (Change the line below 'image_path.jpg' ******)
file_name = os.path.join(os.path.dirname(__file__), 'locol1.png') # Your image path from current directory
print "c"
# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    print "d"
    content = image_file.read()
    print content
    image = vision_client.

        annotate_image(content=content)

print  "e"
# Performs label detection on the image file
labels = image.detect_labels()
print "f"
print('Labels:')
for label in labels:
    print(label.description)
    print("g")
print("i")
