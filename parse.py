#!/usr/bin/env python3

# Know when a comment is made

import os
import time

def main():
    
    open_file = open("notes.md", 'r')
    file_contents = open_file.readlines()

    parse_notes(file_contents)

    print(file_contents)
    return

def parse_notes(file_contents):
    # two dictionaries????

    date_list = []
    comment_list = []
    command_list = []
    output_list = []

    for entry in file_contents:
        if '####' in entry:
            date_list.append(entry)
        elif '- ' in entry:
            # if there is no comment
            comment_list.append(entry)
        elif '```' in entry:
            command_list.append(entry)
        elif '`' in entry:
            output_list.append(entry)

    return 



if __name__ == "__main__":
    main()