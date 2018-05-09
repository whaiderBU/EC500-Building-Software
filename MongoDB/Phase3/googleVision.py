import tweet as tw
import mov as movie
import mongoDatabase as db
import cleanup
import os
import wget
import io
from google.cloud import vision
from google.cloud.vision import types
from os import listdir

def lable_images():

    client = vision.ImageAnnotatorClient()

    labelData = []

    pictures = [pic for pic in listdir("./output") if pic.endswith('jpg')]
    for picture in pictures:
        file_name = os.path.join(os.path.dirname(__file__), "output", picture)

        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        # label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations

        print('Lables:' + picture)

        for label in labels:
            data = {}
            data["description"] = str(label.description)
            data ["score"] = str(label.score)
            labelData.append(data)

            print(label.description)

    return labelData
