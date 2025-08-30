#!/usr/bin/env python3

import sys

def run_with_file(input_file):
    total = 0
    for line in input_file:
        line = line.strip()
        if (not line) or line.startswith('#'):
            continue
        parts = line.split()
        if parts[0] == 'echo':
            print(total)
        elif parts[0] == 'add':
            total += int(parts[1])
        else:
            print("Unknown command ('{}')!".format(parts[0]))

def main():
    if len(sys.argv) != 2:
        print("Run with exactly one argument - filename with commands.")
        return
    with open(sys.argv[1]) as inp:
        run_with_file(inp)

if __name__ == '__main__':
    main()
