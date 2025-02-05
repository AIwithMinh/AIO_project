# -*- coding: utf-8 -*-
"""untitled34.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/gist/AIwithMinh/67881751cf6c151a28ec83c735d9cecb/untitled34.ipynb
"""

!git clone https://github.com/THU-MIG/yolov10.git

!pwd

# Commented out IPython magic to ensure Python compatibility.
# %cd yolov10

!pip install -q -r requirements.txt
!pip install -e .

# Nano version: yolov10n.pt
!wget https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10n.pt

from google.colab import drive

drive.mount('/content/drive')

!cp '/content/drive/MyDrive/DATA.MINH/Safety_Helmet_Dataset.zip' .

from ultralytics import YOLOv10

MODEL_PATH = 'yolov10n.pt'
model = YOLOv10(MODEL_PATH)

model.info()

!gdown '1twdtZEfcw4ghSZIiPDypJurZnNXzMO7R'

!mkdir safety_helmet_dataset

!unzip -q '/content/yolov10/Safety_Helmet_Dataset.zip' -d '/content/safety_helmet_dataset'

YAML_PATH = '/content/safety_helmet_dataset/data.yaml'
EPOCHS = 1
IMG_SIZE = 640
BATCH_SIZE = 256

model.train(data=YAML_PATH,
            epochs=EPOCHS,
            batch=BATCH_SIZE,
            imgsz=IMG_SIZE)