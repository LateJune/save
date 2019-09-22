#!/usr/bin/env python3

import sys

def main():

    file = open(sys.argv[1], 'r')
    dump = file.read().split('\n')

    cmdlist = []
    for line in dump:
        if '$' in line:
            cmdlist.append([line])
        else: cmdlist[-1].append(line)

    
    for cmd in cmdlist:
        if sys.argv[2] in cmd[0]:
            for output in cmd:
                print(output)

if __name__ == "__main__":
    main()
