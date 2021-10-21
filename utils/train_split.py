import os
import shutil
import random

random.seed(10)
# Defines the path where the assets are going to be located
os.chdir(os.path.normpath(os.getcwd() + os.sep + os.pardir))
asset_path = os.path.join(os.getcwd(), 'Assets')
data_path = os.path.join(asset_path, 'DLCV_logo_project')

train_path = os.path.join(data_path, 'train')
train_image_path = os.path.join(train_path, 'images')
train_label_path = os.path.join(train_path, 'labels')

val_path = os.path.join(data_path, 'val')
val_image_path = os.path.join(val_path, 'images')
val_label_path = os.path.join(val_path, 'labels')

test_path = os.path.join(data_path, 'test')
test_image_path = os.path.join(test_path, 'images')
test_label_path = os.path.join(test_path, 'labels')

def train_test_dev_split():
    try:
        os.mkdir(val_path)
        os.mkdir(val_image_path)
        os.mkdir(val_label_path)
    except:
        print('val folders already there')
        pass

    try:
        os.mkdir(test_path)
        os.mkdir(test_image_path)
        os.mkdir(test_label_path)
    except:
        print('test folders already there')
        pass

    #Accesses the current data to be handled for the lab_01 task
    images = os.listdir(train_image_path)
    labels = os.listdir(train_label_path)
    val_size = int(len(images)*0.2)
    test_size = int(len(images)*0.1)

    val_images = random.sample(images,k=val_size)
    images = list(set(images) - set(val_images))

    test_images = random.sample(images,k=test_size)
    images = list(set(images) - set(test_images))

    def move_files(images,image_dest_dir,label_dest_dir, image_dir=train_image_path, label_dir=train_label_path):
        for img in images:
            label = img + '.txt'
            shutil.move(os.path.join(image_dir,img), image_dest_dir)
            shutil.move(os.path.join(label_dir, label), label_dest_dir)

    print('moving val')
    move_files(val_images,val_image_path,val_label_path)
    print('moving test')
    move_files(test_images,test_image_path,test_label_path)
    print('done')
train_test_dev_split()
