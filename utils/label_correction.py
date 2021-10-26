import os

# Defines the path where the assets are going to be located
os.chdir(os.path.normpath(os.getcwd() + os.sep + os.pardir))
asset_path = os.path.join(os.getcwd(), 'Assets')
data_path = os.path.join(asset_path, 'DLCV_logo_project')

train_path = os.path.join(data_path, 'train')
train_image_path = os.path.join(train_path, 'images')
train_label_path = os.path.join(train_path, 'labels')

labels = os.listdir(train_label_path)
for i in labels:
    os.rename(i,i.replace('.jpg.txt','.txt'))