import pandas as pd
import os
import shutil
import re
import random
import argparse

random.seed(10)





def sampler(logo,sample_number,data_path,dataset_path):
    logo_path = os.path.join(data_path,'images_by_logo',logo)
    logo_image_path = os.path.join(logo_path,'images')
    images = os.listdir(logo_image_path)
    if len(images) > 2000:
        images = random.sample(images, k=min(sample_number,len(images)))
    for img in images:
        shutil.move(os.path.join(logo_image_path, img), dataset_path)


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--logos', nargs='+', help='logos list to choose from')
    parser.add_argument('--samples', type=int, default=1000, help='number of samples in case of more than 2000 images')

    opt = parser.parse_args()
    return opt

def main(opt):
    os.chdir(os.path.normpath(os.getcwd() + os.sep + os.pardir))
    asset_path = os.path.join(os.getcwd(), 'Assets')
    data_path = os.path.join(asset_path, 'DLCV_logo_project')
    dataset_path = os.path.join(data_path, 'datasets')
    os.chdir(data_path)
    try:
        os.mkdir(dataset_path)
    except:
        print('folder exits')
        pass

    logos_path = os.path.join(data_path, 'images_by_logo')
    os.chdir(logos_path)

    for logo in opt.logos:
        sampler(logo, opt.samples,data_path,dataset_path)
        print('{0} finished'.format(logo))
if __name__ == "__main__":
    opt = parse_opt()
    main(opt)