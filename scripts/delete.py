# !/usr/bin/env python
# encoding: utf-8

import os
import glob
from PIL import Image

New_Image_Location = '/home/ypang/Downloads/JPEGImages'
Old_Image_Location = '/home/ypang/Downloads/JPEGImages_Old'
Annotations_Location = '/home/ypang/Downloads/Annotations'

os.mkdir(New_Image_Location) 
outDir = os.path.abspath(New_Image_Location) 
imageDir1 = os.path.abspath(Old_Image_Location)

image1 = [] #The full name of image will be saved
imgname1 = [] #The name without the suffix of image will be saved

#Glob all the JPEG images in the JPEGImages folder.
imageList1 = glob.glob(os.path.join(imageDir1, '*.JPEG'))

#Search all the image files to get the full name of images
for item in imageList1:
    image1.append(os.path.basename(item))

#Search all the image files to get the name without suffix of images
for item in image1:
    (temp1, temp2) = os.path.splitext(item)
    imgname1.append(temp1)
print 'Please wait for several seconds'
#Do the similar thing for the annotations 
imageDir2 = os.path.abspath(Annotations_Location)
image2 = []
imgname2 = []
imageList2 = glob.glob(os.path.join(imageDir2, '*.xml'))

for item in imageList2:
    image2.append(os.path.basename(item))

for item in image2:
    (temp1, temp2) = os.path.splitext(item)
    imgname2.append(temp1)

count = 0
#Search all the images files, save those images with annotations to outDIR
for item1 in imgname1:
    for item2 in imgname2:
        if item1 == item2:
            dir = imageList1[imgname1.index(item1)]
            img = Image.open(dir)
            name = os.path.basename(dir)
            img.save(os.path.join(outDir, name))
            count = count + 1
print 'The total number of images with annnotation is ' + str(count) + '.'