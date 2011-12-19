#!/usr/bin/env python
"""Project Euler - project 1 - Hadoop version (mapper)

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""

import sys

def read_input(file):
    for line in file.readlines():
        yield line.strip()

def main():
    # input comes from STDIN (standard input)
    # we expect a file containing a number on each line for the desired range of calculation
    data = read_input(sys.stdin)
    
    for number in data:
        if not int(number) % 3 or not int(number) % 5:
            print number
    
if __name__ == "__main__":
    main()