#!/bin/bash
# Help:
# the output will be saved on Assets/outputs/output{number}
# the pretraind models folder should be downloded and put and Assets
# Put Insert all the images you want to run prediction on on Assets/testnow



DIR="${PWD}/yolov5"
# Models list to choose from:
# yolov5l_extra_cleanData : big yolo traind on 90K images
# yolov5s_extra_cleanData : small yolo traind on 90K images
# yolov5s_cleanData_fintuning :small yolo finetuned on with extra 50K images on yolov5s_cleanData
# yolov5s_cleanData       : small yolo traind on 20K images
# yolov5s_DirtyData	  : small yolo trained on 40K images witout removing inccorect annotations

Modelname="yolov5s_extra_cleanData" #replace the name of the model you want get inference from here

FOTODIR="${PWD}/Assets/testnow"

WEIGHTS="${PWD}/Assets/Models/$Modelname/weights/best.pt"

if [ $# -ne 3 ]; then
	SOURCE=$FOTODIR
	CONF=0.40
	IOU=0.4999
else
	SOURCE=$1
	CONF=$2
	IOU=$3
fi

CDIR="${PWD}/Assets/outputs"
(cd $DIR; python detect.py --weights $WEIGHTS --source $SOURCE --conf-thres $CONF --iou-thres $IOU --agnostic-nms --augment --project $CDIR --name output --save-txt --save-conf)
