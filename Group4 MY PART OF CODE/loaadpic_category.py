import os
from PIL import Image
import json
import numpy as np


# CHANGE THIS LATER TO GUI
catTrainingFolder = "TODO: IMPLEMENT CAT FOLDER LOCATION"
dogTrainingFolder = "TODO: IMPLEMENT DOG FOLDER LOCATION"

data = {}


# ANALYZES IMAGES
def AnalyzeImage(imageLocation, newImageSize = (64, 64)):

    try:

        img = Image.open(imageLocation)
        img = img.resize(newImageSize)

        imgArr = np.array(img)
        imgArr = imgArr / 255.0

        return imgArr
    
    except Exception as e:

        print(f"Error analyzing image {imageLocation}: {e}")

        return None


#Opening the cat folder triggers analyze imnage and labels them as cat from the cat folder
for catImage in os.listdir(catTrainingFolder):

    catImageLocation = os.path.join(catTrainingFolder, catImage)

    catImageData = AnalyzeImage(catImageLocation, catImage)

    if catImageData is not None:

        label = "Cat"

        data[catImageLocation] = {"Data": catImageData.tolist(), "Label": label}


#Opening the dog folder triggers analyze imnage and labels them as dog from the dog folder
for dogImage in os.listdir(dogTrainingFolder):

    dogImageLocation = os.path.join(dogTrainingFolder, dogImage)

    dogImageData = AnalyzeImage(dogImageLocation, dogImage)

    if dogImageData is not None:

        label = "Dog"

        data[dogImageLocation] = {"Data": dogImageData.tolist(), "Label": label}


#TODO: IMPLEMET SAVE TO JASON
    

    
