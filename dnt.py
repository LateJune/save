# Save command -> saves line by line into a text file


#!/bin/usr/env python3

import sys
import os

path = "/home/crushedblind/test-dir"

def main():
    walk_dir()

    return None


def walk_dir():
    contents = ''
    for subdir, dir, files in os.walk(path):
        for file in files:
            #print(type(file))
            #print(file)
            file_path = os.path.join(subdir,file)
            open_file = open(file_path,'r')
            contents = open_file.readlines()
            print(contents)

    return



main()