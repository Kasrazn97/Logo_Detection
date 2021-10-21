"""
Merges batches of preprocessed data from Roboflow into one folder for each of train, test and valid.
Run this in the folder with zipped files.
"""

import os
import shutil

# get rid of .DS_Store file if it's there
# try:
#     for file in [z for z in os.listdir(path_to_foolder_with_zips) if not z.endswith('zip')]:
#         os.remove(os.path.join(path_to_foolder_with_zips, file))
# except FileNotFoundError:
#     pass

zipped_batches = os.listdir(os.getcwd())

# unzipping
for zip_batch in zipped_batches:
    shutil.unpack_archive(zip_batch)
    os.remove(zip_batch)    

# merging batches into combined train, test and valid folder of the first batch
# unzipped_batches = [f for f in os.listdir(path_to_foolder_with_zips) if not f.endswith('zip')]

# for b in unzipped_batches[1:]:
#     test_images = os.listdir(os.path.join(os.path.join(path_to_foolder_with_zips, b), 'test/images'))
#     test_labels = os.listdir(os.path.join(os.path.join(path_to_foolder_with_zips, b), 'test/labels'))
#     train_images = os.listdir(os.path.join(os.path.join(path_to_foolder_with_zips, b), 'train/images'))
#     train_labels = os.listdir(os.path.join(os.path.join(path_to_foolder_with_zips, b), 'train/labels'))
#     valid_images = os.listdir(os.path.join(os.path.join(path_to_foolder_with_zips, b), 'valid/images'))
#     valid_labels = os.listdir(os.path.join(os.path.join(path_to_foolder_with_zips, b), 'valid/labels'))
    
#     splits_from = [test_images, train_images, valid_images, test_labels, train_labels, valid_labels]
#     splits_to = ['test/images', 'train/images', 'valid/images', 'test/labels', 'train/labels', 'valid/labels']
    
#     # from each train, test and valid move all images and labels to the first batch folder
#     for k1, k2 in zip(splits_from, splits_to):
#         for file in k1:
#             shutil.move(os.path.abspath(file), os.path.join(unzipped_batches[0], k2))
    
#     # remove all empty batch folders
#     os.remove(os.path.abspath(b))

# # move train, test and valid folder one level upper
# final_splits_of_data = os.listdir(os.path.abspath(unzipped_batches[0]))
# for f in final_splits_of_data:
#     shutil.move(os.path.abspath(f), path_to_foolder_with_zips)

# os.mkdir(os.path.join(os.getcwd(), 'train/images'))
# os.mkdir(os.path.join(os.getcwd(), 'train/labels'))
# os.mkdir(os.path.join(os.getcwd(), 'test/images'))
# os.mkdir(os.path.join(os.getcwd(), 'test/labels'))
# os.mkdir(os.path.join(os.getcwd(), 'valid/images'))
# os.mkdir(os.path.join(os.getcwd(), 'valid/labels'))

# splits = ['train','test', 'valid']

# def allocate_files(spt):
        
#     for file in os.listdir(os.path.join(os.getcwd(), spt)):
#         if file.endswith('jpg'):
#             shutil.move(os.path.join(os.path.join(os.getcwd(), spt), file), os.path.join(os.getcwd(), f'{spt}/images'))
#         elif file.endswith('txt'):
#             shutil.move(os.path.join(os.path.join(os.getcwd(), spt), file), os.path.join(os.getcwd(), f'{spt}/labels'))

# for spt in splits:
#     allocate_files(spt)

