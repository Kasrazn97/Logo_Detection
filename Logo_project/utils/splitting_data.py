""" 
Run in DLCV_logo_project folder. 
Splits the data (images and labels) into mandatory and optional part. Mandatory part is split further into 3 batches for Roboflow (due to limits).
Roboflow only allows to process 10k pics per one project, and 50k pics per account for free. 
"""

import pandas as pd
import os
import shutil
import re

ROW_DATA_DIR = os.getcwd()

annotations = pd.read_csv("annot_train.csv")
annotations['class'] = annotations['class'].apply(lambda x: re.sub(' ', '_', x))
annotations['class'] = annotations['class'].apply(lambda x: re.sub('-', '_', x))
# annotations.head()

# annotations['class'].unique()

annotations.to_csv('annotations.csv', index=False)

mandatory_classes = 'Nike, Adidas, Under_Armour, Puma, The_North_Face'.split(", ")
annotations_mandatory = annotations[annotations['class'].apply(lambda x: x in mandatory_classes)]
annotations_optional = annotations[annotations['class'].apply(lambda x: x not in mandatory_classes)]
print(f'Mandatory annotations: {len(annotations_mandatory)}\nOptional annotations: {len(annotations_optional)}')

train_data_dir = os.path.join(ROW_DATA_DIR, 'train')
train_pics = os.listdir(train_data_dir)

# moving mandatory 5 logos to train/mandatory_logos folder
mandatory_pics = [pic for pic in train_pics if pic in annotations_mandatory['photo_filename'].tolist()]
os.mkdir(os.path.join(ROW_DATA_DIR, 'train/mandatory_logos'))
mandatory_logos_dir = os.path.join(ROW_DATA_DIR, 'train/mandatory_logos')           
for pic in mandatory_pics:
     shutil.move(os.path.join(train_data_dir, pic), mandatory_logos_dir)

# moving optional 12 logos to train/mandatory_logos folder
optional_logos_dir = os.path.join(ROW_DATA_DIR, 'train/optional_logos')   
os.mkdir(optional_logos_dir)
optional_pics = [pic for pic in train_pics if pic not in annotations_mandatory['photo_filename'].tolist()]
for pic in optional_pics:
     shutil.move(os.path.join(train_data_dir, pic), optional_logos_dir)

print(f'Number of mandatory 5 classes train pics: {len(os.listdir(mandatory_logos_dir))}\nNumber of optional 12 classes train pics: {len(os.listdir(optional_logos_dir))}')

batch1_dir = os.path.join(ROW_DATA_DIR,'train/mandatory_logos/batch1')
batch2_dir = os.path.join(ROW_DATA_DIR, 'train/mandatory_logos/batch2')
batch3_dir = os.path.join(ROW_DATA_DIR,'train/mandatory_logos/batch3')
os.mkdir(batch1_dir)
os.mkdir(batch2_dir)
os.mkdir(batch3_dir)

for pic in [pic for pic in os.listdir(mandatory_logos_dir) if pic.endswith('jpg')][:7000]: # first 7000 pics
    shutil.move(os.path.join(mandatory_logos_dir, pic), batch1_dir)
for pic in [pic for pic in os.listdir(mandatory_logos_dir) if pic.endswith('jpg')][:7000]: # second 7000 pics
    shutil.move(os.path.join(mandatory_logos_dir, pic), batch2_dir)
for pic in [pic for pic in os.listdir(mandatory_logos_dir) if pic.endswith('jpg')]: # the rest
    shutil.move(os.path.join(mandatory_logos_dir, pic), batch3_dir, pic)

print(f'Batch 1 size: {len(os.listdir(batch1_dir))}\nBatch 2 size: {len(os.listdir(batch2_dir))}\nBatch 3 size: {len(os.listdir(batch3_dir))}')

# renaming all noise classes to NULL
annotations_noise = pd.read_csv("annot_noise.csv")
annotations_noise['class'] = ['NULL']*len(annotations_noise)
annotations_noise.to_csv('annotations_noise.csv', index=False)
