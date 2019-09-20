#!/usr/bin/env python3

import os
import time
def main():

    open_file = open("masterfile", 'r')

    note_file_str = open_file.read()
    note_file_list = change_color(note_file_str)

    parsed_notes = parse_note_file(note_file_list)
    find_cmd(parsed_notes)

    return

def change_color(note_file_str):
    new_colored_string = ''
    
    index = 0
    leng_of_str = len(note_file_str)
    while '[01;32m' in note_file_str:
        new_colored_string = note_file_str.replace('[01;32m', '[01;35m')
        index += 1
        if index == leng_of_str:
            break

    return new_colored_string.split('\n')


def find_cmd(parsed_notes):
    user_cmd = input("Enter command to scan for 'Enter' to get everything: ")

    for line in parsed_notes:
        for entry in line: 
            if user_cmd in entry:
                for index in range(len(line)):
                    print(line[index].strip('\n'))

    return

def parse_note_file(note_file):
    command_list = []
    output_list = []


    for line in note_file:
        if 'bash -i' in line:
            continue
        elif '$' in line or '#' in line:
            command_list.append([line])
        else:
            command_list[-1].append(line)

    return command_list


if __name__ == "__main__":
    main()
