import pandas as pd
import os
import shutil
import re

os.chdir(os.path.normpath(os.getcwd() + os.sep + os.pardir))
asset_path = os.path.join(os.getcwd(),'Assets')
data_path = os.path.join(asset_path,'DLCV_logo_project')
os.chdir(data_path)

annotations = pd.read_csv("annot_train.csv")
annotations['class'] = annotations['class'].apply(lambda x: re.sub(' ', '_', x))
annotations['class'] = annotations['class'].apply(lambda x: re.sub('-', '_', x))
# annotations.head()

# annotations['class'].unique()

annotations.to_csv('annotations.csv', index=False)

# mandatory_classes = 'Nike, Adidas, Under_Armour, Puma, The_North_Face'.split(", ")
# annotations_mandatory = annotations[annotations['class'].apply(lambda x: x in mandatory_classes)]
# annotations_optional = annotations[annotations['class'].apply(lambda x: x not in mandatory_classes)]
# annotations_mandatory.to_csv('annotations_mandatory.csv',index=False)
# annotations_optional.to_csv('annotations_optional.csv',index=False)
# print(f'Mandatory annotations: {len(annotations_mandatory)}\nOptional annotations: {len(annotations_optional)}')

train_data_dir = os.path.join(data_path, 'train')
train_pics = os.listdir(train_data_dir)
image_dir = os.path.join(data_path,'images_by_logo')
try:
    os.mkdir(image_dir)
except:
    print('image dir exists')
logos = annotations['class'].unique()

for i in logos:
    try:
        os.mkdir(os.path.join(image_dir,i))
        os.mkdir(os.path.join(image_dir, i,'images'))
    except:
        print('{0} alredy exits'.format(i))

pics = [pic for pic in train_pics if pic in annotations['photo_filename'].tolist()]
for img in train_pics:
     class_name = annotations[annotations['photo_filename'] == img]['class']
     shutil.copy(os.path.join(train_data_dir, img), os.path.join(image_dir,class_name.unique()[0],'images'))

# moving optional 12 logos to train/mandatory_logos folder
# optional_logos_dir = os.path.join(data_path, 'train','images')
# optional_pics = [pic for pic in train_pics if pic not in annotations_mandatory['photo_filename'].tolist()]
# for pic in optional_pics:
#      shutil.move(os.path.join(train_data_dir, pic), optional_logos_dir)


# print(f'Number of mandatory 5 classes train pics: {len(os.listdir(mandatory_logos_dir))}\nNumber of optional 12 classes train pics: {len(os.listdir(optional_logos_dir))}')
# To use in Roboflow you may uncomment the followings to devide into three batches due to it's limitation
# batch1_dir = os.path.join(data_path,'train/mandatory_logos/batch1')
# batch2_dir = os.path.join(data_path, 'train/mandatory_logos/batch2')
# batch3_dir = os.path.join(data_path,'train/mandatory_logos/batch3')
# os.mkdir(batch1_dir)
# os.mkdir(batch2_dir)
# os.mkdir(batch3_dir)
#
# for pic in [pic for pic in os.listdir(mandatory_logos_dir) if pic.endswith('jpg')][:7000]: # first 7000 pics
#     shutil.move(os.path.join(mandatory_logos_dir, pic), batch1_dir)
# for pic in [pic for pic in os.listdir(mandatory_logos_dir) if pic.endswith('jpg')][:7000]: # second 7000 pics
#     shutil.move(os.path.join(mandatory_logos_dir, pic), batch2_dir)
# for pic in [pic for pic in os.listdir(mandatory_logos_dir) if pic.endswith('jpg')]: # the rest
#     shutil.move(os.path.join(mandatory_logos_dir, pic), batch3_dir, pic)

# print(f'Batch 1 size: {len(os.listdir(batch1_dir))}\nBatch 2 size: {len(os.listdir(batch2_dir))}\nBatch 3 size: {len(os.listdir(batch3_dir))}')

# renaming all noise classes to NULL
annotations_noise = pd.read_csv("annot_noise.csv")
annotations_noise['class'] = ['NULL']*len(annotations_noise)
annotations_noise.to_csv('annotations_noise.csv', index=False)
