#Pixel Parser
import pandas as pd
import numpy as np
import matplotlib as plt
import os
import cv2
from PIL import Image
from collections import Counter

#os.chdir('/home/tlabarre/Desktop/DroneFootage/python/staging2')
os.chdir('/home/tlabarre/Desktop/DroneFootage/python/staging3')

#One Time Use Script to acquire metal RGB's

#First Metal Array
#Select an image that contains metal has metal
metal_frames=['3028','2998','3030']
non_metal_frames=['3123','3124','3125']
print('Metal Frames Used:')
print(non_metal_frames)
print('Non-Metal Frames Used:')
print(metal_frames)

i=0
for y in metal_frames:

    frame_y = 'frame'+ str(y) + '.jpg'
    
    for x in non_metal_frames:
        
        i=i+1
        frame_x = 'frame'+ str(x) + '.jpg'

        img = Image.open(frame_y)

        colors = Counter(img.getdata())
        
        
        colors = pd.DataFrame({"colors":colors})
        colors.reset_index(inplace=True)
        colors = colors.rename(columns = {'level_0':'R'})
        colors = colors.rename(columns = {'level_1':'G'})
        colors = colors.rename(columns = {'level_2':'B'})

        colors.to_csv('0_frame1.csv')

        img.close()

    #Step2
    #Select an image with no metal
        img = Image.open(frame_x)

        colors2 = Counter(img.getdata())

        colors2 = pd.DataFrame({"colors2":colors2})
        colors2.reset_index(inplace=True)
        colors2 = colors2.rename(columns = {'level_0':'R'})
        colors2 = colors2.rename(columns = {'level_1':'G'})
        colors2 = colors2.rename(columns = {'level_2':'B'})

        colors2.to_csv('0_frame2.csv')

    #This process is Metal Image - Non Metal Image = Metal Only Pixels. This way, ONLY RGB color codes associated with metal-containing images can be isolated.

        colors3 = pd.merge(colors,colors2,how='outer')

        colors3 = colors3[~colors3['colors2'].notnull()]

        colors3 = colors3[colors3['colors']>2]
    #Create a few 0_metal#.csv files to merge for common metal RGBs
        output_file = '0_metal' + str(i) + '.csv'
        colors3.to_csv(output_file)

#Next, find common colors in 0_metal3.csv, 0_metal1.csv, and 0_metal2.csv 
