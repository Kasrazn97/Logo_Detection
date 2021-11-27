# Logo Detection
A logo detection system using YOLOv5.

## Intro
Brands want to understand who uses their products and how. One way to do so is to use Computer Vision algorithms to detect relevant pictures on social media. Object Detection is the method of detecting objects in images or videos. 
Our goal here was to train a model able to detect brand logos.

## Detection Results
 -- put here some pictures with the bounding boxes --

## Table of contents
1. [ Environment ](#env)
2. [ Description ](#usage)
    1. [ Dataset ](#dataset)
    2. [ Training ](#train)
    3. [ Evaluation ](#eval)
3. [ Usage Tips ](#desc)
4. [ Usage Example ](#ex)

<a name="env"></a>
## 1. Environment

We developed our codes using Google Colab, and then we trained the largest ones on an Azure Virtual Machine. 
--- IMMAGINE DI NICO DELLA VM ---

<div align="center">
    <a href="https://colab.research.google.com/github/ultralytics/yolov5/blob/master/tutorial.ipynb">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-colab-small.png" width="10%"/>
    </a>
    <a href="https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwiS0f6Bt7j0AhWRzXcKHXXkA0gYABAAGgJlZg&ae=2&ohost=www.google.com&cid=CAESQOD2WXDDC3bcaN6__E7gY08J137qyTW6nOQb8DRsJPfVaCbKW_MnwwecmS8dCR7oZPQSLYd6V8LfB32ZLnpJUqA&sig=AOD64_2JGNrArPWvbnOJLMOXwqSsXl1gSw&q&adurl&ved=2ahUKEwjrovWBt7j0AhW3gv0HHXPGCYYQ0Qx6BAgCEAE&dct=1">
        <img src="https://aspiracloud.com/wp-content/uploads/2019/07/azure.png" width="10%"/>
    </a>
</div>

<a name="desc"></a>
## 2. Description

We used two model architectures from the **YOLOv5** family : **YOLOv5s**, **YOLOv5l**. Experimenting with dataset preprocessing steps and fine-tuning procedures, we produced 5 different models and compared their performance. 

We chose [YoloV5](https://github.com/ultralytics/yolov5/blob/master/README.md) since it is state-of-the-art model and is considered to be one of the best in terms of speed and accuracy trade-off. Here the details of the two models we chose to train (you can find the details of all the YOLOv5 models [here](https://github.com/ultralytics/yolov5/blob/master/README.md)):
 
|Model |size<br><sup>(pixels) |mAP<sup>val<br>0.5:0.95 |mAP<sup>val<br>0.5 |Speed<br><sup>CPU b1<br>(ms) |Speed<br><sup>V100 b1<br>(ms) |Speed<br><sup>V100 b32<br>(ms) |params<br><sup>(M) |FLOPs<br><sup>@640 (B)
|---                    |---  |---    |---    |---    |---    |---    |---    |---
|YOLOv5s      |640  |37.2   |56.0   |98     |6.4    |0.9    |7.2    |16.5
|YOLOv5l      |640  |48.8   |67.2   |430    |10.1   |2.7    |46.5   |109.1
<br>
   
   
<a name="dataset"></a>
### 1. Dataset

The raw dataset we deployed consists of images representing the following logos: Nike, Adidas, Under Armour, Puma, The North Face, Starbucks, Apple Inc., Mercedes-Benz, NFL, Emirates, Coca-Cola, Chanel, Toyota, Pepsi, Hard Rock Cafè. We used [Roboflow](https://roboflow.com/?ref=ultralytics) to convert dataset to a COCO format and apply preprocessing steps which include image resize and data augmentation. In particular we applied the following augmentations: rotation, blur, flip, shear, exposure, mosaic, crop (both at image and bounding box levels). 
 
 <div align="center">
    <a href="https://roboflow.com/?ref=ultralytics">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-roboflow-long.png" width="35%"/>
    </a>
</div>

<a name="train"></a>
### 2. Training

Our final models differ both in the input data used and the training steps applied.
 
1. Yolov5s (version 1): trained on initial dataset with augmentations. We kept frozen 10 layers of the model (the backbone) and fine-tuned the rest. Since the model results were unsatisfatory, we manually cleaned the data by removing images with multiple logos and poorly annotated ones. 
2. Yolov5s (version 2): cleaned dataset with augmentations (about 20k images). Again, we trained all layers except for the backbone.
3. Yolov5s (version 3): Fine-tuning the second model with extra augmentation steps adding up to 60k images. Only 6 last layers were trained with 18 others frozen.
4. Yolov5s (version 4): combined dataset from step 2 and step 3, training all the layers except for the backbone.
5. Yolov5l: combined dataset from step 2 and step 3 adding more augmentation steps, training all the layers except for the backbone.

<a name="eval"></a>
### 3. Evaluation
We used xx different metrics to evaluate our model:
  - **IoU**
  - **mAP**

**IoU**, Intersection over Union, is an evaluation metric used to evaluate the goodness of an object detector by measuring the overlap between two bounding boxes.
**mAP**, mean Average Precision, of the model measures the Average Precision (computed by calculating the AuC for a particular class) averaged over all the classes .
**INSERT TABLES WITH THE RESULTS FOR EVERY LOGO**
 
 <center>
  
| Model| Size<br><sup>(pixels) | Params<br><sup>(M) |
| :-----: | :-: | :-: |
| Yolov5s | 640 | 7.4 |
| Yolov5l | 640 | 46.5 |
 
 </center>
 
<a name="usage"></a>
## 3. Usage Tips
 Instructions to follow - this file is needed for this; to test our algo run this
 
 <a name="ex"></a>
## 4. Usage Example
put the commands to run on the terminal to use our algo
