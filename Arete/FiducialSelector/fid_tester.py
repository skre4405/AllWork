# -*- coding: utf-8 -*-
"""
Created on Wed May  1 13:51:16 2019

@author: wevonosky
"""

import numpy as np
import glob2 as glob
import os
import matplotlib.pyplot as plt

#Where to find the data
base = 'C:/Users/sreynolds/Desktop/D2T4S4_clean_v2/'
filePath = "C:\\Users\\sreynolds\\Desktop\\shiftFiles\\"
#Load in the file paths
files = glob.glob(base + '*.npy')

#**********initializing all variables to be used***********
#variable for plt.figure
fig = plt.figure()
#first image variable
ax1 = fig.add_subplot(122)
#second image variable
ax2 = fig.add_subplot(121)
#list to hold first image coordinates of fiducials
coordsIm1 = []
#list to hold second imag fiducial coordinates
coordsIm2 = []
#count of how many fiducials are on first image
fidCountIm1 = 0
#count of how many fiducials are on the second image
fidCountIm2 = 0
#list to hold the shifts between x positions in the imagey organized by selected fiducials
shiftx = []
#list to hold the shifts between y positions in the images organized by selected fiducials
shifty = []
#value to hold the sum of the x shifts between the points
shiftxTot = 0
#value to hold the sum of the y shifts between the points
shiftyTot = 0
#value of the x shift. is the average of all refence points
shiftAvgx = 0.0
#value of the y shift. is the average of all refence points
shiftAvgy = 0.0
#list to keep track of last fiducial point put in for undo
undoTrack = []
#temporary list to hold coords from image 2 and put on image one in next
#Create figure
def openImage(imNum):
    global fig
    global files
    global ax1
    global ax2
    global coordsIm1
    global coordsIm2
    global fidCountIm1
    global fidCountIm2
    global shiftx
    global shifty
    global shiftxTot
    global shiftyTot
    global shiftAvgx
    global shiftAvgy
    #empty all variables for a new image
    coordsIm1 = []
    coordsIm2 = []
    fidCountIm1 = 0
    fidCountIm2 = 0
    shiftx = []
    shifty = []
    shiftxTot = 0
    shiftyTot = 0
    shiftAvgx = 0.0
    shiftAvgy = 0.0
    im1 = np.load(files[imNum])
    im2 = np.load(files[imNum+1])
    
    
    ax1.clear()
    ax1.set_title('image ' + str(imNum + 1) )
    ax1.imshow(im1)
    
    ax2.clear()
    ax2.set_title('image ' + str(imNum + 2))
    ax2.imshow(im2)
    plt.draw()


def add_fid(axTemp, xLoc, yLoc,fidCount):
    axTemp.scatter(xLoc, yLoc, color = 'red')
    axTemp.text(xLoc, yLoc-20,'Fid' + fidCount, color = 'red')
#Start clicking event
def on_key(event):
    global fidCountIm1
    global fidCountIm2
    global ix, iy
    global coordsIm1
    global coordsIm2
    global ax1
    global ax2
    global shiftx 
    global shifty 
    global shiftxTot
    global shiftyTot
    global shiftAvgx
    global shiftAvgy
    global imNum
    global temp
    global fileName
    print('you pressed', event.key)
    if event.key == 'a':
        ix, iy = event.xdata, event.ydata 
        print ('x = {0}, y = {1}'.format(ix, iy))
        if event.inaxes == ax1:
            fidCountIm1 += 1
            print ("event in ax1")
            add_fid(ax1, ix, iy, str(fidCountIm1))
            coordsIm1.append((ix, iy))
            
        elif event.inaxes == ax2:
            fidCountIm2 += 1
            print ("event in ax2")
            add_fid(ax2, ix, iy, str(fidCountIm2))
            coordsIm2.append((ix, iy))
            
        plt.draw()
        return 0
    if event.key == 'u':
         print('undo fiducial select')
         if event.inaxes == ax1:
             if fidCountIm1 > 0:
                 fidCountIm1 -= 1
                 coordsIm1.remove(coordsIm1[fidCountIm1])
                 ax1.clear()
                 im1 = np.load(files[imNum])
                 ax1.set_title('image ' + str(imNum + 1) )
                 ax1.imshow(im1)
                 for i in range(len(coordsIm1)): 
                     add_fid(ax1,coordsIm1[i][0], coordsIm1[i][1],str(i+1))
         elif event.inaxes == ax2:
             if fidCountIm2 > 0:
                 fidCountIm2 -= 1
                 coordsIm2.remove(coordsIm2[fidCountIm2])
                 ax2.clear()
                 
                 im2 = np.load(files[imNum+1])
                 
                 ax2.set_title('image ' + str(imNum + 2) )
                 ax2.imshow(im2)
                 for i in range(len(coordsIm2)):
                     add_fid(ax2, coordsIm2[i][0], coordsIm2[i][1], str(i+1))
                 
             plt.draw()
         plt.draw()
             
    if event.key == 'n':
        if fidCountIm1 == fidCountIm2 and fidCountIm1 > 0:
            fileName = filePath + "%04d.txt"%(imNum+1)
            temp = coordsIm2
            tempCount = fidCountIm2
            if not os.path.exists(os.path.dirname(fileName)):
                os.makedirs(os.path.dirname(fileName))
            for i in range(fidCountIm1):
                shiftAvgx += (coordsIm2[i][0] - coordsIm1[i][0])/fidCountIm1
                shiftAvgy += (coordsIm2[i][1] - coordsIm1[i][1])/fidCountIm2
            
            file = open(fileName,"w")
            file.write(str(shiftAvgx) +"\n" + str(shiftAvgy))
            file.close()
            imNum += 1
            openImage(imNum)
            fidCountIm1 = tempCount
            coordsIm1 = temp
            im1 = np.load(files[imNum])
            ax1.set_title('image ' + str(imNum + 1) )
            ax1.imshow(im1)
            for i in range(len(coordsIm1)):
                print(i)
                add_fid(ax1, coordsIm1[i][0], coordsIm1[i][1], str(i+1))
        else:
            print('Error: Fiducials uneven or no fiducials')
    if event.key == 'r':
        openImage(imNum)
userBegin = input('Enter number: ')
imNum = int(userBegin) - 1
openImage(imNum)      
cid = fig.canvas.mpl_connect('key_press_event', on_key)

