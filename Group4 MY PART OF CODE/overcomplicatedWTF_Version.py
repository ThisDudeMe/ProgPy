'''


import os
from PIL import Image, ImageEnhance
import json
import numpy as np
import random

# CHANGE THIS LATER TO GUI
catTrainingFolder = "C:/Users/PC/Downloads/cat_dog_images/test/cats"
dogTrainingFolder = "C:/Users/PC/Downloads/cat_dog_images/test/dogs"

# Specify the output file path
outputFilePath = "C:/Users/PC/Downloads/trainingData.json"

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
        total_images = sum(len(data[category]["trainingData"]) + len(data[category]["testingData"]) for category in data)
        images_saved = 0

        with open(outputFileName, 'w') as jsonFile:
            for category in data:
                for data_item in data[category]["trainingData"]:
                    json.dump(data_item, jsonFile)
                    jsonFile.write('\n')
                    images_saved += 1
                    print(f"Progress: {images_saved}/{total_images} images saved")

                for data_item in data[category]["testingData"]:
                    json.dump(data_item, jsonFile)
                    jsonFile.write('\n')
                    images_saved += 1
                    print(f"Progress: {images_saved}/{total_images} images saved")

        print(f"Data saved to {outputFileName}")
        print("Progress: 100% completed")
    except Exception as e:
        print(f"Error saving data to JSON: {e}")

# Process and split images for a given category
def ProcessImageCategory(category, trainingFolder):
    for idx, imageFile in enumerate(os.listdir(trainingFolder)):
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
        # Print progress after analyzing each image
        print(f"Progress: {idx + 1} out of {len(os.listdir(trainingFolder))} images analyzed)")

# Process the cat images
ProcessImageCategory("Cat", catTrainingFolder)

# Process the dog images
ProcessImageCategory("Dog", dogTrainingFolder)

# Save data to a JSON file
SaveDataToJSON(data, outputFilePath)
print("Data saving completed.")

'''