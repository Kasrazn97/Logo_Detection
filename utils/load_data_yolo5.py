""" Run this in datasets/logos_yolo5 """

# !pip install roboflow

# from roboflow import Roboflow

# rf = Roboflow(api_key="70km9PLbgHy58nZXL4s8")
# project = rf.workspace().project("logo-detection-c9uz0") # batch 1
# batch_1 = project.version(1).download("yolov5")
!curl -L "https://app.roboflow.com/ds/aMpyqaLzwC?key=Xh3aIpe2Jw" > batch_1.zip

# project = rf.workspace().project("logo-detection-3") # batch 3
# batch_3 = project.version(1).download("yolov5")
!curl -L "https://app.roboflow.com/ds/0CJcFhdysb?key=oF5qvyJcMN" > batch_3.zip
# rf = Roboflow(api_key="vL2pF4wwm0sPdNpP35Zd")  # batch 2
# project = rf.workspace().project("logo-detection-2-dlely")
# batch_2 = project.version(2).download("yolov5")
!curl -L "https://app.roboflow.com/ds/Y1Qh90EYw1?key=nCLvnfSd8L" > batch_2.zip