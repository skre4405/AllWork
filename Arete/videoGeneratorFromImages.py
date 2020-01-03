# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 13:12:44 2019

@author: sreynolds
"""

# importing libraries 
import os 
import cv2  
from PIL import Image  
import matplotlib.pyplot as plt

# Checking the current directory path   
  
# Folder which contains all the images 
# from which video is to be generated 
   
# =============================================================================
# path = "C:\\Python\\Geekfolder2"
#   
# mean_height = 0
# mean_width = 0
#   
# num_of_images = len(os.listdir('\\coam01\coam01\slow01\CSVData\Results\HeatMapImages\RXRot_1E-7_P2\OccSize5')) 
# # print(num_of_images) 
#   
# for file in os.listdir('\\coam01\coam01\slow01\CSVData\Results\HeatMapImages\RXRot_1E-7_P2\OccSize5'): 
#     im = Image.open(os.path.join(path, file)) 
#     width, height = im.size 
#     mean_width += width 
#     mean_height += height 
#     # im.show()   # uncomment this for displaying the image 
#   
# # Finding the mean height and width of all images. 
# # This is required because the video frame needs 
# # to be set with same width and height. Otherwise 
# # images not equal to that width height will not get  
# # embedded into the video 
# mean_width = int(mean_width / num_of_images) 
# mean_height = int(mean_height / num_of_images) 
#   
# # print(mean_height) 
# # print(mean_width) 
#   
# # Resizing of the images to give 
# # them same width and height  
# for file in os.listdir('.'): 
#     if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"): 
#         # opening image using PIL Image 
#         im = Image.open(os.path.join(path, file))  
#    
#         # im.size includes the height and width of image 
#         width, height = im.size    
#         print(width, height) 
#   
#         # resizing  
#         imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)  
#         imResize.save( file, 'JPEG', quality = 95) # setting quality 
#         # printing each resized image name 
#         print(im.filename.split('\\')[-1], " is resized")  
# =============================================================================


#Function to create frames with explicit info in image.  
def genDeatiledImgFromNPY():
    plt.figure().canvas.set_window_title(chip_name)
    plt.rcParams["axes.grid"] = False
    plt.imshow(chip, cmap = "YlGnBu")
    
    title = "Epoch_"+str(10000+epoch)[1:5]+"_Chip_"+str(1000000+chip_num)[1:7]+"(" + cat + ")"+"_Heat Map"
    plt.figure().canvas.set_window_title(title)
    manager = plt.get_current_fig_manager()
    manager.window.showMaximized()
    plt.subplot(121)
    plt.title("Epoch: "+str(10000+epoch)[1:5] + " Chip: " + str(chip_num))
    plt.imshow(temp, cmap = 'jet', clim=(0,1))
    plt.subplot(122)
    temp2 = np.expand_dims(temp2,0)
    plt.imshow(temp2, cmap = 'jet', clim=(0,1))
    if saveHM == True:
        plt.savefig(r'\\coam01\coam01\slow01\CSVData\Results\HeatMapImages\MirroredLR5e-5_WD1e-4Epoch3/'+title)
        plt.close('all')
    
# Video Generating function 
def generate_video(): 
    image_folder = r'\\coam01\coam01\slow01\CSVData\Results\HeatMapImages\MirroredLR5e-5_WD1e-4Epoch3' # make sure to use your folder 
    video_name = r'\Desktop\SMDCFrames.avi' 
     
    images = sorted(os.listdir(image_folder))    
              
     
    # Array images should only consider 
    # the image files ignoring others if any 
    #print(images)  
  
    frame = cv2.imread(os.path.join(image_folder, images[0])) 
  
    # setting the frame width, height width 
    # the width, height of first image 
    height, width, layers = frame.shape   
  
    video = cv2.VideoWriter(video_name, 0, 2, (width, height))  
  
    # Appending the images to the video one by one 
    for image in images:  
        video.write(cv2.imread(os.path.join(image_folder, image)))  
      
    # Deallocating memories taken for window creation 
    cv2.destroyAllWindows()  
    video.release()  # releasing the video generated 
  
  
# Calling the generate_video function 
generate_video()
print("Done!")