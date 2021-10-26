import cv2
import sys
import os
import pandas as pd

os.chdir(os.path.normpath(os.getcwd() + os.sep + os.pardir))
asset_path = os.path.join(os.getcwd(),'Assets')
data_path = os.path.join(asset_path,'DLCV_logo_project')
os.chdir(data_path)
annotations = pd.read_csv('annotations.csv')
logos_path = os.path.join(data_path,'images_by_logo')
os.chdir(logos_path)
logos = os.listdir(logos_path)

def drawBoundingBoxes(imgName,imageData, imageOutputPath, box):
    """Draw bounding boxes on an image.
    imageData: image data in numpy array format
    imageOutputPath: output image file path
    inferenceResults: inference results array off object (l,t,w,h)
    colorMap: Bounding box color candidates, list of RGB tuples.
    """
    left = int(box.iloc[0]['xmin'])
    top = int(box.iloc[0]['ymin'])
    right = int(box.iloc[0]['xmax'])
    bottom = int(box.iloc[0]['ymax'])
    label = box.iloc[0]['class']
    imgHeight, imgWidth, _ = imageData.shape
    thick = int((imgHeight + imgWidth) // 900)
    cv2.rectangle(imageData,(left, top), (right, bottom), (0,225,0), thick)
    cv2.putText(imageData, label, (left, top - 12), 0, 1e-3 * imgHeight, (0,225,20), thick//3)
    cv2.imwrite(os.path.join(imageOutputPath,imgName), imageData)

for logo in logos:
        image_path = os.path.join(os.path.abspath(logo),'images')
        image_list = os.listdir(image_path)
        image_anotate_path = os.path.join(os.path.abspath(logo),'image_annotated')
        try:
            os.mkdir(image_anotate_path)
        except:
            print('folder exists')

        for img in image_list:
            imgcv = cv2.imread(os.path.join(image_path,img))
            box = annotations[annotations['photo_filename']==img]
            drawBoundingBoxes(img, imgcv, image_anotate_path, box)

