# !/usr/bin/env python
# encoding: utf-8

import os
import glob
import shutil

New_Annotations_Location = '/home/ypang/darknet/VOCdevkit/VOC2018/Annotations_new'
Old_Annotations_Location = '/home/ypang/darknet/VOCdevkit/VOC2018/Annotations/'
Images_Location = '/home/ypang/darknet/VOCdevkit/VOC2018/JPEGImages'

os.mkdir(New_Annotations_Location) 
outDir = os.path.abspath(New_Annotations_Location) 
imageDir1 = os.path.abspath(Old_Annotations_Location)

image1 = [] #The full name of Annotations will be saved
imgname1 = [] #The name without the suffix of Annotations will be saved

#Glob all the xml files in the Annotations folder.
imageList1 = glob.glob(os.path.join(imageDir1, '*.xml'))

#Search all the xml files to get the full name of Annotations
for item in imageList1:
    image1.append(os.path.basename(item))

#Search all the xml files to get the name without suffix of Annotations
for item in image1:
    (temp1, temp2) = os.path.splitext(item)
    imgname1.append(temp1)
print 'Please wait for several seconds'
#Do the similar thing for the Images 
imageDir2 = os.path.abspath(Images_Location)
image2 = []
imgname2 = []
imageList2 = glob.glob(os.path.join(imageDir2, '*.JPEG'))

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
            sourceDir = imageList1[imgname1.index(item1)]
            name = os.path.basename(sourceDir)
            targetDir = New_Annotations_Location + '/' + name
            shutil.copy(sourceDir,  targetDir)
            count = count + 1
print 'The total number of annotations with image is ' + str(count) + '.'
shutil.rmtree(Old_Annotations_Location)
shutil.move(New_Annotations_Location, Old_Annotations_Location)

