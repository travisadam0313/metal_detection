 #Script to build dataframe that ALL Frames will be compared against in search of metal.
import pandas as pd
import numpy as np
import matplotlib as plt
import os
import cv2
from PIL import Image
from collections import Counter

os.chdir('/home/tlabarre/Desktop/DroneFootage/python/staging3')

#Next, find common colors in 0_metal3.csv, 0_metal1.csv, and 0_metal2.csv 

df1 = pd.read_csv('0_metal1.csv')
df2 = pd.read_csv('0_metal2.csv')
df3 = pd.read_csv('0_metal3.csv')
df4 = pd.read_csv('0_metal4.csv')
df5 = pd.read_csv('0_metal5.csv')
df6 = pd.read_csv('0_metal6.csv')
df7 = pd.read_csv('0_metal7.csv')
df8 = pd.read_csv('0_metal8.csv')
df9 = pd.read_csv('0_metal9.csv')

#os.chdir('/home/tlabarre/Desktop/DroneFootage/python/staging2')

#Next, find common colors in 0_metal3.csv, 0_metal1.csv, and 0_metal2.csv 

#df10 = pd.read_csv('0_metal1.csv')
#df11 = pd.read_csv('0_metal2.csv')
#df12 = pd.read_csv('0_metal3.csv')
#df13 = pd.read_csv('0_metal4.csv')
#df14 = pd.read_csv('0_metal5.csv')
#df15 = pd.read_csv('0_metal6.csv')
#df16 = pd.read_csv('0_metal7.csv')
#df17 = pd.read_csv('0_metal8.csv')
#df18 = pd.read_csv('0_metal9.csv')
#
df_alt = pd.merge(df1,df2,on=['R','G','B'],how='inner')
df_alt = pd.merge(df_alt,df3,on=['R','G','B'],how='inner')
df_alt = pd.merge(df_alt,df4,on=['R','G','B'],how='inner')
df_alt = pd.merge(df_alt,df5,on=['R','G','B'],how='inner')
df_alt = pd.merge(df_alt,df6,on=['R','G','B'],how='inner')
df_alt = pd.merge(df_alt,df7,on=['R','G','B'],how='inner')
df_alt = pd.merge(df_alt,df8,on=['R','G','B'],how='inner')
df_alt = pd.merge(df_alt,df9,on=['R','G','B'],how='inner')
#df_alt = pd.merge(df_alt,df10,on=['R','G','B'],how='inner')
#df_alt = pd.merge(df_alt,df11,on=['R','G','B'],how='inner')
#df_alt = pd.merge(df_alt,df12,on=['R','G','B'],how='inner')
#df_alt = pd.merge(df_alt,df13,on=['R','G','B'],how='inner')
#df_alt = pd.merge(df_alt,df14,on=['R','G','B'],how='inner')
#df_alt = pd.merge(df_alt,df15,on=['R','G','B'],how='inner')
#df_alt = pd.merge(df_alt,df16,on=['R','G','B'],how='inner')
#df_alt.to_csv('rgb.csv')
print(df_alt)
df_alt = df_alt[['R','G','B']]


#create blank dataframe for logging
os.chdir('/home/tlabarre/Desktop/DroneFootage/python/staging3')
clip_log = pd.DataFrame(columns=['Frame','X','Clr_Match'])

for x in range(0,4700,5):
    frame='frame'+str(x)+'.jpg'
    print(frame + ' ' + str(x))
    
    img = Image.open(frame)

    colors = Counter(img.getdata())

    colors = pd.DataFrame({"colors":colors})
    colors.reset_index(inplace=True)
    colors = colors.rename(columns = {'level_0':'R'})
    colors = colors.rename(columns = {'level_1':'G'})
    colors = colors.rename(columns = {'level_2':'B'})

    temp = pd.merge(colors,df_alt,on=['R','G','B'],how='inner')
    
    p = x/4700
    
    clr_match = len(temp.index)

    clip_log = clip_log.append({
        'Frame':frame,
        'X':p,
        'Clr_Match':clr_match
        },ignore_index=True).fillna(0)
    img.close()
    
clip_log.to_csv('clip_log_1x.csv')
