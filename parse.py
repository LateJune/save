#!/usr/bin/env python3

import os
import time

def main():
    
    open_file = open("notes.md", 'r')
    
    file_contents = open_file.readlines()

    date, cmnt, cmd, out  = parse_notes(file_contents)
    open_file.close()
    format_output(date, cmnt, cmd, out)
    return

def get_comments(file_contents):
    comments_list = []
    for entry in file_contents:
        if '- ' in entry:
            comments_list.append(entry.strip('- '))
        
    return comments_list


def get_output(file_contents):
    indicies = []
    for i in range(len(file_contents)):
        if not '```\n' in file_contents:
            return None
        elif file_contents[i] ==  "```\n":
            indicies.append(i)
    
    output_list = []
    # print(file_contents)
    i = 0
    j = 1
    while True:
        output_list.append(file_contents[indicies[i]+1:indicies[j]])
        i += 2
        j += 2       
        if i >= len(indicies):
            break

    return output_list

def parse_notes(file_contents):
    # two dictionaries????

    date_list = []
    command_list = []
    comment_list = get_comments(file_contents)
    output_list = get_output(file_contents)

    for entry in file_contents:
        if '####' in entry:
            date_list.append(entry.strip('#### '))
        #elif '- ' in entry:
        #    comment_list.append(entry.strip('- '))
        
        elif '` ' in entry:
            command_list.append(entry[:-1].strip('` '))

    return date_list, comment_list, command_list, output_list

def format_output(date,cmnt,cmd,out):
    for i in range(len(date)):
        print('\n')
        print(date[i].strip('\n'))
        print("Comment: " + cmnt[i].strip('\n'))
        print("Command: " + cmd[i])
        for entry in out[i]:
            print("### " + entry.strip('\n'))
        

    return


if __name__ == "__main__":
    main()