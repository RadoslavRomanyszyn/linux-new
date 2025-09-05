#!/usr/bin/env python3

import sys

def print_day(day_num):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    print(days[day_num % 7])

def main():
    try:
        print_day(int(sys.argv[1]))
    except (IndexError, ValueError):
        print("Invalid invocation, specify day number as the only argument.")

if __name__ == "__main__":
    main()

