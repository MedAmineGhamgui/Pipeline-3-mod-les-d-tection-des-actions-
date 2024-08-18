from track_with_x3d import tracking1
import time
import torch
import cv2
import colorsys
import numpy as np
import psutil
import imageio
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f'***************************************************************************************\n device : {device}')


from ocsort import ocsort
from ultralytics import YOLO
from super_gradients.training import models
from super_gradients.training.models.detection_models.customizable_detector import CustomizableDetector
from super_gradients.training.pipelines.pipelines import DetectionPipeline
if __name__ == "__main__":
    
 
        
    video_path = r"/kaggle/input/test-model-yowo-et-x3d/1.mp4"

    tracking1(video_path)
