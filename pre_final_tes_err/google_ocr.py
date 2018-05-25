# API KEY IS : AIzaSyCZaj9q2B5hmRemboPZPg-qwDeTCOO1WpU

# https://www.youtube.com/watch?v=bHkQb3gnSRA

import io
import os

# Imports the Google Cloud credentials library
from google.cloud import vision
from google.cloud.vision import *
from google.cloud import vision


from google.oauth2 import service_account








credentials = service_account.Credentials.from_service_account_file('My Project-6748fa243896.json')


path = "locol1.png"
"""Detects text in the file."""
# credentials1 = vision.ImageAnnotatorcredentials('My Project-6748fa243896.json')

with io.open(path, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

response = credentials.text_detection(image=image)
texts = response.text_annotations
print('Texts:')

for text in texts:
    print('\n"{}"'.format(text.description))

    vertices = (['({},{})'.format(vertex.x, vertex.y)
                 for vertex in text.bounding_poly.vertices])

    print('bounds: {}'.format(','.join(vertices)))