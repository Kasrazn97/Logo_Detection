import pandas as pd
import os

os.chdir(os.path.normpath(os.getcwd() + os.sep + os.pardir))
asset_path = os.path.join(os.getcwd(), 'Assets')
data_path = os.path.join(asset_path, 'DLCV_logo_project')
train_path = os.path.join(data_path, 'train')
<<<<<<< HEAD
=======
train_image_path = os.path.join(train_path, 'images')
mandatory_logos_path = os.path.join(train_path, 'mandatory_logos')
optional_logos_path = os.path.join(train_path, 'optional_logos')
>>>>>>> b0128298f8341723592ba6e7b23fe8567a8e8b77
noise_path = os.path.join(data_path, 'noise')


def make_dir(path):
    try:
        os.mkdir(path)
    except:
        print('folder already exists')
        pass
    return

def BndBox2YoloLine(box, noise=False,classList = []):

    xmin = box['xmin']
    xmax = box['xmax']
    ymin = box['ymin']
    ymax = box['ymax']

    xcen = float((xmin + xmax)) / 2 / float(box['width'])
    ycen = float((ymin + ymax)) / 2 / float(box['height'])

    w = float((xmax - xmin)) / float(box['width'])
    h = float((ymax - ymin)) / float(box['height'])

    boxName = box['class']

    try:
        if noise:
            classList.append('Null')
            classIndex = -1
        else:
            if boxName not in classList:
                classList.append(boxName)
            classIndex = classList.index(boxName)
    except:
        print(box)

    return classIndex, xcen, ycen, w, h, classList


def label_writer(file, list, path):
    os.chdir(path)
    with open(file, 'w') as f:
        for i in list:
            f.write(str(i))
            f.write(' ')
        f.close()

def make_label(create_path,data_path,noise=False):
    df = pd.read_csv(data_path)
    for index, row in df.iterrows():
        file_name = '{0}.txt'.format(row['photo_filename'])
        if noise:
            classIndex, xcen, ycen, w, h, trashClass = BndBox2YoloLine(row,noise=True)
        else:
            classIndex, xcen, ycen, w, h, classList = BndBox2YoloLine(row)
        param_list = [classIndex, xcen, ycen, w, h]
        label_writer(file_name, param_list,create_path)
    if not noise:
        return classList

if __name__ == '__main__':
<<<<<<< HEAD
    make_dir(os.path.join(train_path, 'labels'))

    make_dir(os.path.join(noise_path, 'labels'))

    print('making labels for train logos')
    make_label(os.path.join(train_path,'labels'),os.path.join(data_path,'annotations.csv'))
=======
    make_dir(os.path.join(train_path, 'images'))
    make_dir(os.path.join(train_path, 'labels'))

    # make_dir(os.path.join(optional_logos_path, 'images'))
    # make_dir(os.path.join(optional_logos_path, 'labels'))

    make_dir(os.path.join(noise_path, 'images'))
    make_dir(os.path.join(noise_path, 'labels'))

    print('making labels for mandatory and optional logos')
    make_label(os.path.join(train_path,'labels'),os.path.join(data_path,'annotations.csv'))
    # print('making labels for optional logos')
    # classList = make_label(os.path.join(optional_logos_path,'labels'),os.path.join(data_path,'annotations_optional.csv'))
>>>>>>> b0128298f8341723592ba6e7b23fe8567a8e8b77
    print('making labels for noise images')
    make_label(os.path.join(noise_path,'labels'),os.path.join(data_path,'annotations_noise.csv'),noise=True)
