#!/bin/usr/env python3

import sys
import os

path = "/home/crushedblind/final-project"

def main():
    walk_dir()


    return None


def walk_dir():
    contents = ''
    for subdir, dir, files in os.walk(path):
        for file in files:
            #print(type(file))
            #print(file)
            print(os.path.join(subdir,file))
            #contents = open(file,'r')
            #print(contents)
    return



main()