# Logo Detection
A logo detection system using YOLOv5.

## Intro
Brands want to understand who uses their products and how. One way to do so is to use Computer Vision algorithms to detect relevant pictures on social media. Object Detection is the method of detecting objects in images or videos. 
Our goal here was to train a model able to detect brand logos.

## Detection Results


## Table of contents
1. [ Environment & Requirements ](#env)
2. [ Description ](#desc)
    1. [ Dataset ](#dataset)
    2. [ Training ](#train)
    3. [ Evaluation ](#eval)
3. [ Usage Tips ](#usage)
    1. [ Data preparation ](#dataprep)
    2. [ Inference ](#inf)
    3. [ Detection ](#det)
4. [ Usage Example ](#ex)

<a name="env"></a>
## 1. Environment
<div align="center">
    <a href="https://colab.research.google.com/github/ultralytics/yolov5/blob/master/tutorial.ipynb">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-colab-small.png" width="10%"/>
    </a>
    <a href="https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwiS0f6Bt7j0AhWRzXcKHXXkA0gYABAAGgJlZg&ae=2&ohost=www.google.com&cid=CAESQOD2WXDDC3bcaN6__E7gY08J137qyTW6nOQb8DRsJPfVaCbKW_MnwwecmS8dCR7oZPQSLYd6V8LfB32ZLnpJUqA&sig=AOD64_2JGNrArPWvbnOJLMOXwqSsXl1gSw&q&adurl&ved=2ahUKEwjrovWBt7j0AhW3gv0HHXPGCYYQ0Qx6BAgCEAE&dct=1">
        <img src="https://aspiracloud.com/wp-content/uploads/2019/07/azure.png" width="10%"/>
    </a>
</div>

We developed our codes using *Google Colab*, and then we trained the largest ones on an *Azure Virtual Machine*:   

<p align="center">
<img src="https://github.com/Kasrazn97/Logo_Detection/blob/main/images/VM.jpeg" width="800" height="200">
<p>
 
 

To use the package, follow the guidline bellow:

1. Install python version 3.8
2. Install the latest version of PyTorch with Cuda 11.3 enabled from the official website
3. Install the required packages:
  ``` 
      $ git clone https://github.com/Kasrazn97/Logo_Detection
      $ cd Logo_Detection
      $ pip install -r requirments.txt 
 ```
 
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

<div align="center">
 <img src="https://github.com/Kasrazn97/Logo_Detection/blob/main/images/NO_augmentation.png" width ="200" /> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Purple_arrow_right.svg/1200px-Purple_arrow_right.svg.png" width ="70" />  <img src="https://github.com/Kasrazn97/Logo_Detection/blob/main/images/augmentation.png" width ="200" />
</div>

<a name="train"></a>
### 2. Training

Our final models differ both in the input data used and the training steps applied.
 
1. **Yolov5s (version 1)**: trained on the raw dataset to which we added augmentations. We kept the 10 backbone layers frozen and fine-tuned the rest. Since the model results were unsatisfatory, we manually cleaned the data by removing the poorly annotated images. **TO DO: ADD TOT NUMBER OF IMAGES**
2. **Yolov5s (version 2)**: cleaned dataset with augmentations (about 20k images in total). Again, we trained all layers except for the backbone. **TODO: ADD NUMBER OF IMAGES PER LOGO AFTER THE CLEANING, BUT BEFORE AUGMENTATION**
3. **Yolov5s (version 3)**: cleaned dataset with extra augmentation steps, for a total of around 60k images (4549 per logo). Only 6 last layers were trained, thus keeping 18 frozen.
4. **Yolov5s (version 4)**: combined dataset from step 2 and step 3, with arounf 8994 images for each logo. Tuning all the layers except for the backbone.
5. **Yolov5l**: combined dataset from step 2 and step 3, adding more augmentation steps. We ended up having 7479 images for each logo. Again, we trained all the layers except for the backbone.

<a name="eval"></a>
### 3. Evaluation
We used 2 different metrics to evaluate our model:
  - **IoU**
  - **mAP**

**IoU**, Intersection over Union, is an evaluation metric used to evaluate the goodness of an object detector by measuring the overlap between two bounding boxes.
**mAP**, mean Average Precision, of the model measures the Average Precision (computed by calculating the AuC for a particular class) averaged over all the classes .

 Here the average results for each model: 
 
 <center>
  
| Model| mAP<sup>val<br>0.5 |mAP<sup>val<br>0.5:0.95  
| :-----: | :-: | :-: 
| YOLOv5s - v1 | 0.598 | 0.364 
| YOLOv5s - v2 | 0.851 | 0.662 
| YOLOv5s - v3 | 0.846 | 0.563 
| YOLOv5s - v4 | 0.881 | 0.664 
| YOLOv5l | 0.943 | 0.713 
<br>
 </center>

Model 1             |  Model 3             | Final model
:-------------------------:|:-------------------------:|:-------------------------:
![](https://github.com/Kasrazn97/Logo_Detection/blob/main/images/YOLOv5s_v1.jpg)  |  ![](https://github.com/Kasrazn97/Logo_Detection/blob/main/images/YOLOv5s_v3.jpg)  |  ![](https://github.com/Kasrazn97/Logo_Detection/blob/main/images/YOLOv5l.jpg)

  
   Here the results for **YOLOv5l** for each logo: 
 
 <center>
  
| Logo| mAP<sup>val<br>0.5 |mAP<sup>val<br>0.5:0.95 | IoU
| :-----: | :-: | :-: | :-:
| Adidas | 0.98 | 0.753 | 0.873
| Apple Inc. | 0.981 | 0.761 | 0.896
| Chanel | 0.981 | 0.678 | 0.797
| Coca Cola | 0.886 | 0.619 | 0.786
| Emirates | 0.779 | 0.569 | 0.158
| Hard Rock Cafè | 0.957 | 0.743 | 0.859
| Mercedes Benz | 0.984 | 0.789 | 0.915
| NFL | 0.965 | 0.731 | 0.876
| Nike | 0.959 | 0.706 | 0.868
| Pepsi | 0.942 | 0.676 | 0.843
| Puma | 0.925 | 0.667 | 0.793
| Starbucks | 0.975 | 0.823 | 0.916
| The North Face | 0.975 | 0.741 | 0.887
| Toyota | 0.961 | 0.737 | 0.883
| Under Armour | 0.977 | 0.71 | 0.867
<br>
 </center>
 
<a name="usage"></a>
## 3. Usage Tips
  
<a name="dataprep"></a>
### Data preparation:
  **Train and Inference:**
  
  1. Clone the repository on your local machine.
  2. Cd Logo_Detection
  3. Create a folder name **Assets**
  4. Cd Assets
  5. Create a folder name **dataset**
  6. Put your Yolo formated data based on the following structure:
  ```
  --Assets|
          |--dataset|
                    |--train|
                    |        |--images
                    |        |--labels
                    |--valid
                    |        |--images
                    |        |--labels
                    |--test
                    |        |--images
                    |        |--labels
  ```
  
  **Detect:**
  
  1. Clone the repository on your local machine.
  2. Cd Logo_Detection
  3. Create a folder name **Assets**
  4. Cd Assets
  5. Create a folder name **testnow**
  6. Put all your images you want to do inference on under **testnow** folder
- **Training**: 
  1. Put the related data.yaml file on yolov5/data
  2. Run the following command (you can change the model name or any other settings you want):
  ```
  python train.py --batch-size 32 --weights yolov5s.pt --data data.yaml --epochs 50 --hyp hyp.finetune.yaml --freeze 10
  ```
  
  For more information regarding the data prepration refer to:
  https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data
  
# TO DO
<a name="inf"></a>

  
<a name="det"></a>
### Inference and detection: 
  Once our algorithm has finished training, we can evaluate its performance on a test set. Follow the instructions provided in the points below to run the algorithm and retrieve the results of both image.jpg with a bounding box around the precition, and its respective image.txt label describing the detected classes and their respective bounding box in a format (class_id, x_mid, y_mid, width, height).
  1. Open your terminal
  2. Activate your specific environment you installed the [requirments.txt](https://github.com/Kasrazn97/Logo_Detection/blob/main/requirements.txt) on
  3. Open [detect_batch.sh] (https://github.com/Kasrazn97/Logo_Detection/blob/main/detect_batch.sh) with a text editor, and change the variable Modelname according to the specific model you're evaluating (exact names are specified inside detect_batch.sh).
  4. See the results under Assets/outputs/\<Modelname\> . There you're going to be provided with a folder containing all the images, and in that same folder there is going to be another folder called "labels" containing all the predicted labels.
