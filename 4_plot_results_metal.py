 #Script to build dataframe that ALL Frames will be compared against in search of metal.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from PIL import Image
from collections import Counter

os.chdir('/home/tlabarre/Desktop/DroneFootage/python/staging2')


    
clr_results = pd.read_csv('clip_log_1x.csv')

print(clr_results)
plt.plot(clr_results['X'],clr_results['Clr_Match'])
plt.suptitle('Metal Frames',fontsize=16)
plt.show()
