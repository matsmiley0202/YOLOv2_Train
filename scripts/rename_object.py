
import os  
import shutil  
  
path0 = '/home/ypang/darknet/VOCdevkit/VOC2018/Annotations/'
path1 = '/home/ypang/darknet/VOCdevkit/VOC2018/Annotations_NewObject/'
os.mkdir(path1)

for file in os.listdir(path0):
    if os.path.isfile(os.path.join(path0,file))==True:
       temp_Digits = os.path.splitext(file)[0].split('_')[0]
	   print temp_Digits
       if temp_Digits == 'n02068974':
          temp_English = 'dolphin'
       elif temp_Digits == 'n01482330':
          temp_English = 'shark'
       elif temp_Digits == 'n02062744':
          temp_English = 'whale'       
       Oldone = '<name>' + temp_Digits + '</name>'
       Newone = '<name>' + temp_English + '</name>'
       file_location0 = path0 + file
       file_location1 = path1 + file
       fp0 = open(file_location0, 'r')
       fp1 = open(file_location1, 'w')
       lines = fp0.readlines()
       for s in lines:
           fp1.write(s.replace(Oldone, Newone))
       fp0.close()
       fp1.close()
shutil.rmtree(path0)
shutil.move(path1, path0)
