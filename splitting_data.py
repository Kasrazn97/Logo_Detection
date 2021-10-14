import pandas as pd
import os
import re

annotations = pd.read_csv("DLCV_logo_project/annot_train.csv")
annotations['class'] = annotations['class'].apply(lambda x: re.sub(' ', '_', x))
annotations['class'] = annotations['class'].apply(lambda x: re.sub('-', '_', x))
annotations.head()

# annotations['class'].unique()
annotations.to_csv('DLCV_logo_project/annotations.csv', index=False)

mandatory_classes = 'Nike, Adidas, Under_Armour, Puma, The_North_Face'.split(", ")
annotations_mandatory = annotations[annotations['class'].apply(lambda x: x in mandatory_classes)]
annotations_optional = annotations[annotations['class'].apply(lambda x: x not in mandatory_classes)]
print(f'Mandatory annotations: {len(annotations_mandatory)}\nOptional annotations: {len(annotations_optional)}')

annotations_mandatory.to_csv('annotations_mandatory.csv')
annotations_optional.to_csv('annotations_optional.csv')

train_data_dir = os.path.join(os.getcwd(), 'DLCV_logo_project/train')
train_pics = os.listdir(train_data_dir)

# moving mandatory 5 logos to train/mandatory_logos folder
mandatory_pics = [pic for pic in train_pics if pic in annotations_mandatory['photo_filename'].tolist()]
os.mkdir(os.path.join(os.getcwd(), 'DLCV_logo_project/train/mandatory_logos'))
mandatory_logos_dir = os.path.join(os.getcwd(), 'DLCV_logo_project/train/mandatory_logos')           
for pic in mandatory_pics:
    os.rename(os.path.join(train_data_dir, pic), os.path.join(mandatory_logos_dir, pic))

# moving optional 12 logos to train/mandatory_logos folder
optional_logos_dir = os.path.join(os.getcwd(), 'DLCV_logo_project/train/optional_logos')   
os.mkdir(optional_logos_dir)
optional_pics = [pic for pic in train_pics if pic not in annotations_mandatory['photo_filename'].tolist()]
for pic in optional_pics:
    os.rename(os.path.join(train_data_dir, pic), os.path.join(optional_logos_dir, pic))

print(f'Number of mandatory 5 classes train pics: {len(os.listdir(mandatory_logos_dir))}      \nNumber of optional 12 classes train pics: {len(os.listdir(optional_logos_dir))}')

batch1_dir = os.path.join(os.getcwd(),'DLCV_logo_project/train/mandatory_logos/batch1')
batch2_dir = os.path.join(os.getcwd(), 'DLCV_logo_project/train/mandatory_logos/batch2')
batch3_dir = os.path.join(os.getcwd(),'DLCV_logo_project/train/mandatory_logos/batch3')
os.mkdir(batch1_dir)
os.mkdir(batch2_dir)
os.mkdir(batch3_dir)

for pic in [pic for pic in os.listdir(mandatory_logos_dir) if pic.endswith('jpg')][:7000]: # first 7000 pics
    os.rename(os.path.join(mandatory_logos_dir, pic), os.path.join(batch1_dir, pic))
for pic in [pic for pic in os.listdir(mandatory_logos_dir) if pic.endswith('jpg')][:7000]: # second 7000 pics
    os.rename(os.path.join(mandatory_logos_dir, pic), os.path.join(batch2_dir, pic))
for pic in [pic for pic in os.listdir(mandatory_logos_dir) if pic.endswith('jpg')]: # the rest
    os.rename(os.path.join(mandatory_logos_dir, pic), os.path.join(batch3_dir, pic))

print(f'Batch 1 size: {len(os.listdir(batch1_dir))}      \nBatch 2 size: {len(os.listdir(batch2_dir))}      \nBatch 3 size: {len(os.listdir(batch3_dir))}')