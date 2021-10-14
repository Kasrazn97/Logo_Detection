# WHAT IS HAPPENNING HERE?

### If you want to have data locally

1. Prepare the dataset: Run ```splitting_data.py``` in DLCV_logo_project folder, upload batches of data to Roboflow, resize to 720x720 for Yolo5 and 608x608 for Darknet, download batches in zips
2. Run ```merge_batches.py``` in the folder with zips
3. OR download data for Yolo5 from [here](https://www.amazon.it/clouddrive/share/5KRAWjhyoVmYMK4MQcfBcGGA256UrAiZ0h7bDYrgugh).

### Upload data to VM (done)

1. Connect to VM
2. Run commands from ```load_data_yolo5.py``` in home/labuser/Logo_project/datasets/logos_yolo5 (just running the script doesnt work, idk why)
3. Run ```merge_batches.py```

### Set up Yolo5 (done)

1. Run ```yolo5_main.py``` in home/labuser/Logo_project
2. Upload ```logos_yolo5.yaml``` to home/labuser/Logo_project/yolo5/data
3. Configure yolo5 [TBD]
4. Run ```pip3 install wandb``` for visualization and cloud logging of training runs