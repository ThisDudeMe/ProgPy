'''




import os
from PIL import Image
import numpy as np




# CHANGE THIS LATER TO GUI
catTrainingFolder = "C:/Users/PC/Downloads/cat_dog_images/test/ncats"
dogTrainingFolder = "C:/Users/PC/Downloads/cat_dog_images/test/ndogs"

data = {"Cat": [], "Dog": []}


# ANALYZES IMAGES
def AnalyzeAndResizeImage(imageLocation, newImageSize = (64, 64)):

    try:

        img = Image.open(imageLocation)
        img = img.resize(newImageSize)

        imgArr = np.array(img) / 255.0

        return imgArr
    
    except Exception as e:

        print(f"Error analyzing image {imageLocation}: {e}")

        return None


#Opening the cat folder triggers analyze imnage and labels them as cat from the cat folder
for catImage in os.listdir(catTrainingFolder):

    catImageLocation = os.path.join(catTrainingFolder, catImage)

    catImageData = AnalyzeAndResizeImage(catImageLocation, catImage)

    if catImageData is not None:

        label = "Cat"

        data["Cat"].append({"Data": catImageData.tolist(), "Label": "Cat"})


#Opening the dog folder triggers analyze imnage and labels them as dog from the dog folder
for dogImage in os.listdir(dogTrainingFolder):

    dogImageLocation = os.path.join(dogTrainingFolder, dogImage)

    dogImageData = AnalyzeAndResizeImage(dogImageLocation, dogImage)

    if dogImageData is not None:

        label = "Dog"

        data["Dog"].append({"Data": dogImageData.tolist(), "Label": "Dog"})


#TODO: IMPLEMET SAVE TO JASON

'''