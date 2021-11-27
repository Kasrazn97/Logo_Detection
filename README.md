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
We mainly worked on Azure Virtual Machine 
 
<a name="desc"></a>
## 2. Description
We compared different models.
YoloV5 is considered to be one of the best models in terms of speed and accuracy trade-off.


<a name="dataset"></a>
### 1. Dataset
The dataset we deployed consists of xx images. We used Roboflow to do augmentation. We did rotation, mosaic bla bla
We trained our model to recognize the following logos: Nike, Adidas, Under Armour, Puma, The North Face, Starbucks, Apple Inc., Mercedes-Benz, NFL, Emirates, Coca-Cola, Chanel, Toyota, Pepsi, Hard Rock Cafè.

<a name="train"></a>
### 2. Training
...

<a name="eval"></a>
### 3. Evaluation
We used xx different metrics to evaluate our model:
  - **IoU**
  - **mAP**

**IoU**, Intersection over Union, is an evaluation metric used to evaluate the goodness of an object detector by measuring the overlap between two bounding boxes.
**mAP**, mean Average Precision, of the model measures the Average Precision (computed by calculating the AuC for a particular class) averaged over all the classes .
**INSERT TABLES WITH THE RESULTS FOR EVERY LOGO**

| Model| Size<br><sup>(pixels) | Params<br><sup>(M) |
| :-----: | :-: | :-: |
| Yolov5s | 640 | 7.4 |
| Yolov5l | 640 | 46.5 |

<a name="usage"></a>
## 3. Usage Tips
 Instructions to follow - this file is needed for this; to test our algo run this
 
 <a name="ex"></a>
## 4. Usage Example
put the commands to run on the terminal to use our algo
