""" 
Loading 3 batches of datasets from Roboflow for darkent.
Run this in datasets/logos_yolo_darknet 
"""

# !pip install roboflow

# from roboflow import Roboflow

# rf = Roboflow(api_key="70km9PLbgHy58nZXL4s8")

# # batch 1
# project = rf.workspace().project("logo-detection-c9uz0")
# dataset = project.version(2).download("darknet")
curl -L https://app.roboflow.com/ds/CzzqtiN5C0?key=avNDDUhYaf > batch1.zip

# # batch 2
# rf = Roboflow(api_key="vL2pF4wwm0sPdNpP35Zd")
# project = rf.workspace().project("logo-detection-2-dlely")
# dataset = project.version(1).download("darknet")
curl -L https://app.roboflow.com/ds/lavhrylwrW?key=9se8DiMnGn > batch2.zip

# # batch 3
# project = rf.workspace().project("logo-detection-3")
# dataset = project.version(2).download("darknet")
curl -L https://app.roboflow.com/ds/OLS8P15j7i?key=PxG8by7Uia > batch3.zip


## ----------------- DATA AUGMENTATION STEPS ----------------- ## 

# Outputs per training example: 3
# Flip: Horizontal, Vertical
# Rotation: Between -25° and +25°
# Bounding Box: Crop: 20% Minimum Zoom, 50% Maximum Zoom
# Bounding Box: Shear: ±15° Horizontal, ±15° Vertical
# Bounding Box: Brightness: Between -40% and +40%
# Bounding Box: Blur: Up to 10px
# Bounding Box: Noise: Up to 12% of pixels