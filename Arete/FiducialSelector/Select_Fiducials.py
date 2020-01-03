# -*- coding: utf-8 -*-
"""
Created on Wed May  1 13:51:16 2019

@author: wevonosky
"""

import numpy as np
import glob2 as glob
from skimage.feature import register_translation
from imageio import imread
import pandas as pd
import matplotlib.pyplot as plt
from scipy import ndimage

#Where to find the data
base = 'C:/Users/sreynolds/Desktop/D2T4S4_clean_v2/'

#Load in the file paths
files = glob.glob(base + '*.npy')

#Load in two images for example
im1 = np.load(files[1500])
im2 = np.load(files[1501])

#Defines the bhavior of matplotlib after a click event
#Disconnects from click event if (0,0) appears in the cords array
#This likely isn't the best wya to exit a session, just a result
#of me playing for a few minutes
def onclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata
    global ax
    
    ax.scatter(ix, iy, color = 'black')
    print ('x = %d, y = %d',ix, iy)

    global coords
    coords.append((ix, iy))

    if (0,0) in coords:
        fig.canvas.mpl_disconnect(cid)

    return coords

#Create figure
fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow(im1)

coords = []

#Start clicking event
cid = fig.canvas.mpl_connect('button_press_event', onclick)
