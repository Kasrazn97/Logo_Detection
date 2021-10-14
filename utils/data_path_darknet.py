"""
Run in /Logo_project/datasets/logos_darknet
"""

import os
import pandas as pd 

train_pics = [f for f in os.listdir("train") if f.endswith(".jpg")]
test_pics = [f for f in os.listdir("test") if f.endswith(".jpg")]

train_df = pd.DataFrame(train_pics)
test_df = pd.DataFrame(test_pics)

train_df.to_csv("../../darknet/data/train.txt", index=False, header=False)
test_df.to_csv("../../darknet/data/test.txt", index=False, header=False)