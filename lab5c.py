#!/usr/bin/env python3
# Author ID: 123860231

def add(number1, number2):
    """Adds two numbers. If an error occurs, returns a string indicating the error."""
    try:
        # Ensure both arguments are numbers
        number1 = float(number1)
        number2 = float(number2)
        return number1 + number2
    except (ValueError, TypeError):
        return 'error: could not add numbers'

def read_file(filename):
    """Reads the contents of a file. If an error occurs, returns a string indicating the error."""
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return 'error: could not read file'
    except PermissionError:
        return 'error: no permission to read file'
    except IsADirectoryError:
        return 'error: provided path is a directory, not a file'

if __name__ == '__main__':
    # Test cases for add() function
    print(add(10, 5))  # works: returns 15
    print(add('10', 5))  # works: returns 15
    print(add('abc', 5))  # error: returns 'error: could not add numbers'
    print(add('10', '5'))  # works: returns 15
    print(add('hello', 5))  # error: returns 'error: could not add numbers'

    # Test cases for read_file() function
    print(read_file('seneca2.txt'))  # error: file does not exist, returns error message
    print(read_file('file10000.txt'))  # error: file does not exist, returns error message
