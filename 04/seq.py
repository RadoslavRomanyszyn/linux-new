#!/usr/bin/env python3

# Python alternative to Shell seq program

import sys

def print_seq(nums):
    if len(nums) == 1:
        for i in range(1, nums[0]+1):
            print(i, end=' ')
        print()
    elif len(nums) == 2:
        for i in range(nums[0], nums[1]+1):
            print(i, end=' ')
        print()
    else:
        if nums[1] == 0:
            print('Step cannot be zero.', file=sys.stderr)
            sys.exit(3)
        for i in range(nums[0], nums[2]+1, nums[1]):
            print(i, end=' ')
        print()

def main():
    arg_num = len(sys.argv) - 1
    if arg_num == 0 or arg_num > 3:
        print('Wrong argument count.', file=sys.stderr)
        sys.exit(2)
    try:
        nums = []
        for i in range(arg_num):
            arg = int(sys.argv[i+1])
            nums.append(arg)
        print_seq(nums)
    except ValueError:
        print('Wrong argument (integer expected).', file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
