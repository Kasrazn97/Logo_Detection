import os
import pandas as pd
import numpy as np


#Gets the list of all preds labels
preds_labels_txts = os.listdir(os.path.join(os.getcwd(), 'labels_hat_l', 'labels'))


#Gets the list of all true labels
true_labels_txts = os.listdir(os.path.join(os.getcwd(), 'labels_true', 'true_labels'))


#Creates empty dataframe
complete_preds = pd.DataFrame(columns=['label', 'x', 'y','w','h', 'fname'])
complete_true = pd.DataFrame(columns=['label', 'x_t', 'y_t','w_t','h_t', 'fname'])


#Stacks in a pd dataframe all the annots true
for file in true_labels_txts:
    true_instance = pd.read_csv(f'labels_true/true_labels/{file}', names=['label', 'x_t', 'y_t','w_t','h_t'], delim_whitespace=True, index_col=False)
    true_instance['fname'] = file
    complete_true = pd.concat((complete_true, true_instance))


#Stacks in a dataframe all the annotations predictions
for file in preds_labels_txts:
    pred_instance = pd.read_csv(f'labels_hat_l/labels/{file}', names=['label', 'x', 'y','w','h'], delim_whitespace=True, index_col=False)
    pred_instance['fname'] = file
    complete_preds = pd.concat((complete_preds, pred_instance))


#Merges the files on file name
merged_df = pd.merge(complete_preds,complete_true, on='fname', how='right')

#KEEP THIS COMMENTED
#Takes where the predicted class is the same as the true class
#filtered_merged_df = merged_df[merged_df['label_x']==merged_df['label_y']]


#Just resetting the index
merged_df.reset_index(drop=True,inplace=True)

np.isnan(merged_df.loc[1]['x'])


def calc_iou(boxA, boxB):
    #Maps [0,1] into [0,640], back to the original dimension of the images and
    #applies a change of coordinates to the dataframe to obtain x1, y1, x2, y2 from x, y, w, h
    xa, ya, wa, ha = boxA
    x1a, y1a, x2a, y2a = xa - wa/2 * 640, ya - ha/2 * 640, xa + wa/2 * 640, ya + ha/2 * 640
    
    if np.isnan(xa):
        return 0
    
    xb, yb, wb, hb = boxB
    x1b, y1b, x2b, y2b = xb - wb/2 * 640, yb - hb/2 * 640, xb + wb/2 * 640, yb + hb/2 * 640
    
    boxA = (x1a, y1a, x2a, y2a)
    boxB = (x1b, y1b, x2b, y2b)
    
    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])
    
    # compute the area of intersection rectangle, if they don't intersect return 0
    interArea = max(0, xB - xA) * max(0, yB - yA)
    
    # compute the area of both the prediction and ground-truth
    boxAArea = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    boxBArea = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])
    
    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    iou = interArea / float(boxAArea + boxBArea - interArea)
    
    # return the intersection over union value
    return iou


#Amongst those for each computes the IoU and takes the one which is between 0 and 1
#Meaning the best among the existing ones, if they're all shit it's going to take shit
for row in merged_df.iterrows():
    true_box = row[1][['x', 'y', 'w', 'h']]
    pred_box = row[1][['x_t', 'y_t', 'w_t', 'h_t']]
    merged_df.loc[row[0], 'IoU'] = calc_iou(true_box, pred_box)


classes = ['Adidas', 'Apple_Inc-', 'Chanel', 'Coca_Cola', 'Emirates', 'Hard_Rock_Cafe', 'Mercedes_Benz', 'NFL', 'Nike', 'Pepsi', 'Puma', 'Starbucks', 'The_North_Face', 'Toyota', 'Under_Armour']
classes_dict = {
    idx:val for idx, val in enumerate(classes)
}


#merged_df.groupby('fname').count().sort_values('x')
merged_df.reset_index(drop = False, inplace = True)
#merged_df

new = merged_df.sort_values('IoU', ascending = False).groupby('fname').first()
new.reset_index(inplace=True)

new[['label_y','IoU']].groupby('label_y').mean('IoU')

