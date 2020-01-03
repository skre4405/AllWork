# -*- coding: utf-8 -*-
"""
Created on Thu May 30 13:46:51 2019

@author: sreynolds
"""

import numpy as np
import glob2 as glob
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

fig = plt.figure()
# image variable
ax = fig.add_subplot(111)

fidCount = 0

coords = []

filePath = r"\\Arete\Shared\Longmont\_EVONOSKY\SBIR\SMDC\camera_calibration\\"
files = glob.glob(filePath + '*.png')

def openImage(imNum):
    
    global fidCount
    
    global ax
    
    global files
    
    global fig
    global coords
    
    fidCount = 0
    coords = []
    img=mpimg.imread( files[imNum])
    
    
    ax.clear()
    ax.set_title('image ' + str(imNum + 1) )
    ax.imshow(img)
    
        
    
def add_fid(axTemp, xLoc, yLoc,fidCount):
    axTemp.scatter(xLoc, yLoc, color = 'red')
    axTemp.text(xLoc, yLoc-20,'Fid' + fidCount, color = 'red')
def on_key(event):
    global filePath
    global coords
    global fileName
    global fidCount
    global imNum
    
    print('you pressed', event.key)
    if event.key == 'a':
        ix, iy = event.xdata, event.ydata 
        print ('x = {0}, y = {1}'.format(ix, iy))
        fidCount += 1
        add_fid(ax, ix, iy, str(fidCount))
        coords.append((ix, iy))
# =============================================================================
#         if event.inaxes == ax1:
#             fidCountIm1 += 1
#             print ("event in ax1")
#             add_fid(ax1, ix, iy, str(fidCountIm1))
#             coordsIm1.append((ix, iy))
#             
#         elif event.inaxes == ax2:
#             fidCountIm2 += 1
#             print ("event in ax2")
#             add_fid(ax2, ix, iy, str(fidCountIm2))
#             coordsIm2.append((ix, iy))
#             
# =============================================================================
        plt.draw()
        return 0
    if event.key == 'u':
         print('undo fiducial select')
         if fidCount > 0:
             fidCount -= 1
             coords.remove(coords[fidCount])
             ax.clear()
             img = mpimg.imread( files[imNum])
             ax.set_title('image ' + str(imNum + 1) )
             ax.imshow(img)
             for i in range(len(coords)): 
                 add_fid(ax,coords[i][0], coords[i][1],str(i+1))
         plt.draw()
# =============================================================================
#          if event.inaxes == ax1:
#              if fidCountIm1 > 0:
#                  fidCountIm1 -= 1
#                  coordsIm1.remove(coordsIm1[fidCountIm1])
#                  ax1.clear()
#                  im1 = np.load(files[imNum])
#                  ax1.set_title('image ' + str(imNum + 1) )
#                  ax1.imshow(im1, interpolation = None)
#                  for i in range(len(coordsIm1)): 
#                      add_fid(ax1,coordsIm1[i][0], coordsIm1[i][1],str(i+1))
#          elif event.inaxes == ax2:
#              if fidCountIm2 > 0:
#                  fidCountIm2 -= 1
#                  coordsIm2.remove(coordsIm2[fidCountIm2])
#                  ax2.clear()
#                  
#                  im2 = np.load(files[imNum+1])
#                  
#                  ax2.set_title('image ' + str(imNum + 2) )
#                  ax2.imshow(im2, interpolation = None)
#                  for i in range(len(coordsIm2)):
#                      add_fid(ax2, coordsIm2[i][0], coordsIm2[i][1], str(i+1))
#                  
#              plt.draw()
# =============================================================================
         plt.draw()
             
    if event.key == 'n':
        if not fidCount == 28:
            print('Too Small bucky')
            print( fidCount)
        else:
            imNum+=1
            coordsArr = np.asarray(coords)
            np.save(filePath+'FidCoords\\image0001{0}'.format(imNum+10), coordsArr)
            openImage(imNum)
        print('next')
        plt.draw()
        
# =============================================================================
#         if fidCountIm1 == fidCountIm2 and fidCountIm1 > 0:
#             fileName = filePath + "%04d.txt"%(imNum+1)
#             temp = coordsIm2
#             tempCount = fidCountIm2
#             if not os.path.exists(os.path.dirname(fileName)):
#                 os.makedirs(os.path.dirname(fileName))
#             for i in range(fidCountIm1):
#                 shiftAvgx += (coordsIm2[i][0] - coordsIm1[i][0])/fidCountIm1
#                 shiftAvgy += (coordsIm2[i][1] - coordsIm1[i][1])/fidCountIm2
#             
#             file = open(fileName,"w")
#             file.write(str(shiftAvgx) +"\n" + str(shiftAvgy))
#             file.close()
#             imNum += 1
#             openImage(imNum)
#             fidCountIm1 = tempCount
#             coordsIm1 = temp
#             im1 = np.load(files[imNum])
#             ax1.set_title('image ' + str(imNum + 1) )
#             ax1.imshow(im1, interpolation = None)
#             for i in range(len(coordsIm1)):
#                 print(i)
#                 add_fid(ax1, coordsIm1[i][0], coordsIm1[i][1], str(i+1))
#         else:
#             print('Error: Fiducials uneven or no fiducials')
# =============================================================================
    if event.key == 'r':
        openImage(imNum)
        plt.draw()

    
userBegin = input('Enter number: ')
imNum = int(userBegin) - 1
openImage(imNum)      
cid = fig.canvas.mpl_connect('key_press_event', on_key)