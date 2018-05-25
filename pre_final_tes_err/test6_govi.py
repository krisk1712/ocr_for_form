import io
from google.cloud import vision


vision_client = vision.ImageAnnotatorClient()
file_name = "locol1.png"


with io.open(file_name, 'rb') as image_file:
    content =  image_file.read()
    image = vision_client.image(content=content)



lab = image.detect_text()

for text in lab:
    print(text)