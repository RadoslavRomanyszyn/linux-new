#!/usr/bin/env python3

# Convert dates at the beginning of lines to days of week.
#
# Input:  2023-02-20 Rest of the line
#         Some other line
#         2023-02-21 Line  contents
#
# Output: Monday Rest of the line
#         Some other line
#         Tuesday Line  contents

import sys
from datetime import date

def date_to_day(iso_date):
    d = date.fromisoformat(iso_date)
    return d.strftime('%A')

def process_inp(inp):
    for line in inp:
        split_line = line.split()
        try:
            first_part = split_line[0]
            day = date_to_day(first_part)
            print(day + line.lstrip(first_part), end='')
        except ValueError:
            print(line, end='')

def main():
    if len(sys.argv) == 1:
        process_inp(sys.stdin)
    elif len(sys.argv) == 2:
        try:
            with open(sys.argv[1], 'r') as inp:
                process_inp(inp)
        except FileNotFoundError:
            print(f'{sys.argv[1]}: No such file', file=sys.stderr)
            sys.exit(1)
    else:
        print('Provide either one or no argument.')

if __name__ == '__main__':
    main()
