import os  
from os import listdir, getcwd  
from os.path import join

if __name__ == '__main__':  
    source_folder='JPEGImages/'
    dest='ImageSets/Main/train.txt'  
    file_list=os.listdir(source_folder)
    if os.path.isfile(dest) == True:
       os.remove(dest)
    train_file=open(dest,'w')

    for file_obj in file_list:  
        file_path=os.path.join(source_folder,file_obj)   
        file_name,file_extend=os.path.splitext(file_obj)  
        file_num=int(file_name)  
        train_file.write(file_name+'\n')  
 
    train_file.close()  
