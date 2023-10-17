import os
from PIL import Image, ImageEnhance
import json
import numpy as np
import random

# CHANGE THIS LATER TO GUI
catTrainingFolder = "C:/Users/PC/Downloads/cat_dog_images/test/ncats"
dogTrainingFolder = "C:/Users/PC/Downloads/cat_dog_images/test/ndogs"

data = {
    "Cat": {
        "trainingData": [],
        "testingData": [],
        "imageMetadata": [],
        "augmentation": {
            "rotation": 15,  # Maximum rotation angle in degrees
            "brightness": 0.5,  # Maximum brightness enhancement factor
        },
    },
    "Dog": {
        "trainingData": [],
        "testingData": [],
        "imageMetadata": [],
        "augmentation": {
            "rotation": 15,
            "brightness": 0.5,
        },
    },
}

# ANALYZES IMAGES AND APPLIES DATA AUGMENTATION
def AugmentImageData(image, imageMetadata, augmentationParams):
    try:
        # Apply rotation
        rotationAngle = random.uniform(-augmentationParams["rotation"], augmentationParams["rotation"])
        img = image.rotate(rotationAngle, resample=Image.BILINEAR)

        # Apply brightness adjustment
        brightnessFactor = random.uniform(1.0 - augmentationParams["brightness"], 1.0 + augmentationParams["brightness"])
        img = ImageEnhance.Brightness(img).enhance(brightnessFactor)

        imgArr = np.array(img) / 255.0

        return imgArr, imageMetadata

    except Exception as e:
        print(f"Error augmenting image: {e}")
        return None, None  # Return None for both image and metadata in case of an error

# Data Split Ratio (e.g., 80% training, 20% testing)
splitRatio = 0.8

# ANALYZES IMAGES AND SPLITS DATA
def AnalyzeAndResizeImage(imageLocation, newImageSize=(64, 64)):
    try:
        img = Image.open(imageLocation)
        img = img.resize(newImageSize)
        imgArr = np.array(img) / 255.0

        # Determine the color space
        colorSpace = DetectImageColorSpace(img)

        # Extract image metadata
        imageMetadata = {
            "Dimensions": img.size,
            "ColorSpace": colorSpace,
        }

        return imgArr, imageMetadata

    except Exception as e:
        print(f"Error analyzing image: {e}")
        return None, None  # Return None for both image and metadata in case of an error

# Function to detect color space
def DetectImageColorSpace(img):
    if img.mode == "RGB":
        return "RGB"
    elif img.mode == "L":
        return "Grayscale"
    elif img.mode == "CMYK":
        return "CMYK"
    # Add more color space detection as needed
    else:
        return "Unknown"  # If the color space is not recognized

# Function to save data to a JSON file
def SaveDataToJSON(data, outputFileName):
    try:
        with open(outputFileName, 'w') as jsonFile:
            json.dump(data, jsonFile)
        print(f"Data saved to {outputFileName}")
    except Exception as e:
        print(f"Error saving data to JSON: {e}")

# Process and split images for a given category
def ProcessImageCategory(category, trainingFolder):
    for imageFile in os.listdir(trainingFolder):
        imageLocation = os.path.join(trainingFolder, imageFile)
        imageData, imageMetadata = AnalyzeAndResizeImage(imageLocation)
        if imageData is not None:
            # Check if there is any testing data; if not, add all data to training
            if len(data[category]["testingData"]) == 0:
                data[category]["trainingData"].append({"Data": imageData.tolist(), "Label": category})
                data[category]["imageMetadata"].append(imageMetadata)
            else:
                # Split data for training and testing based on the ratio
                if len(data[category]["trainingData"]) / len(data[category]["testingData"]) < splitRatio:
                    augmentedImage, augmentedMetadata = AugmentImageData(
                        Image.fromarray((imageData * 255).astype(np.uint8)),
                        imageMetadata,
                        data[category]["augmentation"]
                    )
                    if augmentedImage is not None and augmentedMetadata is not None:
                        data[category]["trainingData"].append({"Data": augmentedImage.tolist(), "Label": category})
                        data[category]["imageMetadata"].append(augmentedMetadata)
                    else:
                        print(f"Error augmenting image: {imageLocation}")
                else:
                    data[category]["testingData"].append({"Data": imageData.tolist(), "Label": category})
                    data[category]["imageMetadata"].append(imageMetadata)


# Process the cat images
ProcessImageCategory("Cat", catTrainingFolder)

# Process the dog images
ProcessImageCategory("Dog", dogTrainingFolder)

# Specify the output file name
outputFileName = "data.json"

# Save data to a JSON file
SaveDataToJSON(data, outputFileName)





#SIMPLIFIED VERSION vvvv
'''
# CHANGE THIS LATER TO GUI
catTrainingFolder = "TODO: IMPLEMENT CAT FOLDER LOCATION"
dogTrainingFolder = "TODO: IMPLEMENT DOG FOLDER LOCATION"

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

    
