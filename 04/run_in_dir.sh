#!/bin/bash

# Switch to 01 directory and count words in file input.txt.
# If 01 directory does not exist or the file input.txt is not in that directory,
# print 0 to stdout.

set -ueo pipefail

cd ../01 2>/dev/null && 2>/dev/null wc -w <input.txt || echo 0
