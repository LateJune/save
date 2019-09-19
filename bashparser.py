#!/usr/bin/env python3

import sys

def main():
    
    file = open(sys.argv[1], 'r')
    dump = file.read().split('\n')

    cmdarr = []
    for line in dump:
        if '$' in line:
            cmdarr.append([line])
        else: cmdarr[-1].append(line)

    for line in cmdarr:
        print(line)

if __name__ == "__main__":
    main()