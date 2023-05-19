import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import cv2

#-------------------------------------Data Load ----------------------------------------------#

data = pd.read_csv('./data(05_18).csv')

temp = '3403580.jpg'
path = "E:/reusable-trash-images/selectstar-reusable-trash-image"
image_path = path + "/" + temp

image = cv2.imread(image_path,cv2.IMREAD_COLOR)


print(data[data['imagePath']=='343580'])

#-------------------------------------Image Load ----------------------------------------------#
image = cv2.resize(image, (1280, 960))








