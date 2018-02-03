
import os  
import shutil  
i = 0000

#path0 is for annotations
path0 = '/home/ypang/darknet/VOCdevkit/VOC2018/Annotations/'
path0_output = '/home/ypang/darknet/VOCdevkit/VOC2018/Annotations_Rename/'
path0_backup = '/home/ypang/darknet/VOCdevkit/VOC2018/Annotations_BackUp/'
os.mkdir(path0_output)

#path1 is for images
path1 = '/home/ypang/darknet/VOCdevkit/VOC2018/JPEGImages/'
path1_output = '/home/ypang/darknet/VOCdevkit/VOC2018/JPEGImages_Rename/'
path1_backup = '/home/ypang/darknet/VOCdevkit/VOC2018/JPEGImages_BackUp/'
os.mkdir(path1_output)

shutil.copytree(path0,path0_backup)
shutil.copytree(path1,path1_backup)

for file in os.listdir(path0):
    if os.path.isfile(os.path.join(path0,file))==True:
       file1 = os.path.splitext(file)[0] + '.JPEG'
       print file1
       if i < 10:
          newname='000'+str(i)+'.xml'
          newname1='000'+str(i)+'.jpg'
       elif 10 <= i < 100:
          newname='00'+str(i)+'.xml'
          newname1='00'+str(i)+'.jpg'
       elif 100 <= i < 1000:
          newname='0'+str(i)+'.xml'
          newname1='0'+str(i)+'.jpg'
       else:
          newname=str(i)+'.xml'
          newname1=str(i)+'.jpg'
       os.rename(os.path.join(path0,file),os.path.join(path0_output,newname))
       os.rename(os.path.join(path1,file1),os.path.join(path1_output,newname1))
       i = i + 1
       print file,'ok'

shutil.rmtree(path0)
shutil.move(path0_output, path0)
shutil.rmtree(path1)
shutil.move(path1_output, path1)
