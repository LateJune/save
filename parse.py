#!/usr/bin/env python3

import os
import time

def main():
    dir_dict = walk_dir()
    for entry in dir_dict:
        print(entry)
        print(dir_dict[entry])
        break

    open_file = open("notes.txt", 'r')
    file_contents = open_file.read()
    

    parse_single_save_file(file_contents)
    return

def parse_single_save_file(file_contents):
    entry_list = []
    buffer = []
    clean_list = []
    
    for ch in file_contents:
        if ch == '`':
            entry_list.append(''.join(buffer))
            buffer = []
        else:
            buffer.append(ch)

    for entry in entry_list:
        if not entry == '' and not entry == '\n':
            clean_list.append(entry)
        print(clean_list)

    return clean_list

def walk_dir():
    cwd = os.getcwd()
    file_path_dic = {}

    subdir_list = []
    file_list = []
    
    for subdir, dir, files in os.walk(cwd):
        subdir_list.append(subdir)
        for file in files:
            file_path = os.path.join(subdir,file)
            #print(file_path)
            open_file = open(file_path,'r')
            file_list.append(file)

            if subdir not in file_path_dic:
                file_path_dic[subdir] = []
            
            file_path_dic[subdir].append(file)

    return file_path_dic

if __name__ == "__main__":
    main()