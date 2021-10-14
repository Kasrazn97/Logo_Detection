""" 
Run in Logo_project folder
Clones yolo5, moves data.yaml to yolo5/data/
"""

!git clone https://github.com/ultralytics/yolov5  # clone repo
%cd yolov5
%pip install -qr requirements.txt # install dependencies
%pip install -q roboflow
