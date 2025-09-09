#!/usr/bin/env python3

import sys

def main():
    arg_num = len(sys.argv) - 1
    if arg_num == 0 or arg_num > 3:
        print('Wrong argument count.', file=sys.stderr)
        sys.exit(2) 


if __name__ == '__main__':
    main()
