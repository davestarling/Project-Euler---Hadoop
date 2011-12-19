#!/usr/bin/env python
"""Project Euler - project 1 - Hadoop version (reducer)

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""

import sys

def read_mapper_output(file):
    for line in file.readlines():
        yield line.strip()

def main():
    # input comes from STDIN (standard input)
    # expects a set of data to sum
    data = read_mapper_output(sys.stdin)

    total = 0
    for x in data:
        total += int(x)
    
    print total

if __name__ == "__main__":
    main()