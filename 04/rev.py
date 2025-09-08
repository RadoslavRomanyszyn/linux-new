#!/usr/bin/env python3

import sys

def reverse(inp):
    for line in inp:
        print(line.rstrip('\n')[::-1])

def main():
    if len(sys.argv) == 1:
        reverse(sys.stdin)
    elif len(sys.argv) == 2:
        try:
            with open(sys.argv[1], "r") as inp:
                reverse(inp)
        except FileNotFoundError as e:
            print(f"{sys.argv[1]}: No such file", file=sys.stderr)
    else:
        print("Provide either one or no argument.")

if __name__ == '__main__':
    main()
