## create contrusted images of 2d patches 
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os 
import shutil
from dcm2 import dicom2png
from skimage import data, img_as_float
from skimage import exposure
import cv2

root_dir = "/home/pkpc/Medical_image/CT"

"""
##create 2d patches 
for f in os.listdir(root_dir):
    source_folder = os.path.join(root_dir,f,"DICOM_anon")
    #os.mkdir(os.path.join(root_dir,f,"patches"))                         #run just once to create subfolder 
    output_folder = os.path.join(root_dir,f,"patches")
    dicom2png(source_folder, output_folder)
    #shutil.rmtree(os.path.join(root_dir,f,"patches"))

##create folder to save contrusted patches 
for f in os.listdir(root_dir):
    os.mkdir(os.path.join(root_dir,f,"contrust_patches"))
    
""" 
##create contrusted patches 
for f in os.listdir(root_dir):
    contrust_patches  = os.path.join(root_dir,f,"contrust_patches")
    patches = os.path.join(root_dir,f,"patches")

    for i in os.listdir(patches):
        img  = cv2.imread(os.path.join(patches,i))
        img  = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        # Contrast stretching
        p2 = np.percentile(img, 2)
        p98 = np.percentile(img, 98)
        img_rescale = exposure.rescale_intensity(img, in_range=(p2, p98))
        cv2.imwrite(os.path.join(contrust_patches,i),img_rescale)
        #plt.imshow(img_rescale)
        #plt.show()

        