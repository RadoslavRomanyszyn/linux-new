#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} NUMBER", file=sys.stderr)
        sys.exit(2)

    number = int(sys.argv[1])
    if number % 2 == 0:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
