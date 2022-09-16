import pandas as pd
import numpy as np
import matplotlib as plt
import os
import cv2


print('Beginning...')

os.chdir('/home/tlabarre/Desktop/DroneFootage/python/staging3')
print(os.getcwd())


vidcap = cv2.VideoCapture('NORM0015.MP4')
print(vidcap)
success,image = vidcap.read()
count = 0

while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1

print('Done, stepping out to main directory...')
os.chdir('/home/tlabarre/Desktop/DroneFootage/python')
print(os.getcwd())
print('Finished.')


