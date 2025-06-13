#!/usr/bin/env python3
# Author ID: 123860231

def read_file_string(file_name):
    """Reads a file and returns its entire contents as a string."""
    with open(file_name, 'r') as file:
        return file.read()

def read_file_list(file_name):
    """Reads a file and returns its contents as a list of lines, without new-line characters."""
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
