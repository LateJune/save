#!/usr/bin/env python3

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
        time.sleep(1) # slow down execution of program
        
    return 

def count_dir_files():
    cwd = os.getcwd()
    num_of_files = 0
    num_of_folders = 0
        
    for subdirs, dir, files in os.walk(cwd):
        for file in files:
            num_of_files += 1    
        num_of_folders += 1

    return num_of_folders, num_of_files
    
def walk_dir():
    cwd = os.getcwd()
    file_path_dic = {}

    subdir_list = []
    file_list = []
    
    for subdir, dir, files in os.walk(path):
        subdir_list.append(subdir)
        for file in files:
            file_path = os.path.join(subdir,file)
            #print(file_path)
            open_file = open(file_path,'r')
            file_list.append(file)

            
            # read the contents of each file
            # Do something later
            # file_contents = open_file.readlines()

            if subdir not in file_path_dic:
                file_path_dic[subdir] = []
            
            file_path_dic[subdir].append(file)

    return file_path_dic

def display_dirs(subdir_list):

    return


def display_files(file_list):

    return 

if __name__ == '__main__':
    main()