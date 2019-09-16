# Save command -> saves line by line into a text file
# proof of concept
# mvp 
# 


#!/bin/usr/env python3

import sys
import os

path = "/home/crushedblind/test-dir"

def main():
    #sys.argv[1]
    subdir_list, file_list = walk_dir()
    print(subdir_list)
    print(file_list)
    num_of_folders, num_of_files = count_dir_files()

    scan_directories(num_of_folders, num_of_files)


    return None

# update continously
# when save is called --> the commands file is updated 
# When we run a command and it puts its output to a file 
# we need to see that new file in the directory and update interfac

def scan_directories(num_of_folders, num_of_files):

    print(num_of_folders)
    print(num_of_files)
    while True:
        pass


    return 

def count_dir_files():
    num_of_files = 0
    num_of_folders = 0
        
    for subdirs, dir, files in os.walk(path):
        for file in files:
            num_of_files += 1    
        num_of_folders += 1

    return num_of_folders, num_of_files
    

def walk_dir():
    subdir_list = []
    file_list = []
    
    for subdir, dir, files in os.walk(path):
        for file in files:
            #print(subdir)
            #print(file)
            file_path = os.path.join(subdir,file)
            #print(file_path)
            open_file = open(file_path,'r')
            contents = open_file.readlines()
            #print(contents)
            file_list.append(file)
        subdir_list.append(subdir)


    return subdir_list, file_list



if __name__ == '__main__':
    main()