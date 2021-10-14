"""
This is just to fix the dataset folder structure for darknet. Run in Logo_project/datasets/logos_darknet/
"""

import os
import shutil

for f in ['train', 'test', 'valid']:
    pics = os.listdir(os.path.join(os.getcwd(), f+'/images'))
    labels = os.listdir(os.path.join(os.getcwd(), f+'/labels'))
    for pic in pics:
        shutil.move(os.path.join(os.getcwd(), f+'/images/'+pic), os.path.join(os.getcwd(), f))
    for label in labels:
        shutil.move(os.path.join(os.getcwd(), f+'/labels/'+label), os.path.join(os.getcwd(), f))
