# Save command -> saves line by line into a text file
# proof of concept
# mvp 
# 


#!/bin/usr/env python3

import sys
import os
import time

path = "/home/crushedblind/test-dir"

def main():
    #sys.argv[1]
    subdir_list, file_list = walk_dir()
    #print(subdir_list)
    #print(file_list)
    num_of_folders, num_of_files = count_dir_files()
    while True:
        scan_directories()

    return None


def scan_directories():
    init_num_of_folders, init_num_of_files = count_dir_files()

    while True:
        print(walk_dir())
        time.sleep(2)
        
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
            file_path = os.path.join(subdir,file)
            #print(file_path)
            open_file = open(file_path,'r')
            file_list.append(file)
            
            # read the contents of each file
            # Do something later
            file_contents = open_file.readlines()
        subdir_list.append(subdir)


    return subdir_list, file_list, 



if __name__ == '__main__':
    main()