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

def append_file_string(file_name, string_of_lines):
    """Appends a string to the given file."""
    with open(file_name, 'a') as file:
        file.write(string_of_lines)

def write_file_list(file_name, list_of_lines):
    """Writes a list of lines to the given file, each item in the list on a new line."""
    with open(file_name, 'w') as file:
        for line in list_of_lines:
            file.write(line + '\n')

def copy_file_add_line_numbers(file_name_read, file_name_write):
    """Reads a file and copies its contents to another file, adding line numbers to each line."""
    with open(file_name_read, 'r') as file_read, open(file_name_write, 'w') as file_write:
        for i, line in enumerate(file_read, start=1):
            file_write.write(f"{i}:{line}")

if __name__ == '__main__':
    # Example usage
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    
    append_file_string(file1, string1)
    print(read_file_string(file1))  # This will now work because we defined it here
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
