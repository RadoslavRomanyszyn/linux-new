#!/bin/bash

# Print matrix slice containing rows 10-19 and cols 3-7.
# Expects matrix with a fixed format (matrix.txt) on stdin.

set -ueo pipefail

tr -d '|' | tr -s ' ' | cut -d ' ' -f 4-8 | head -n 19 | tail -n +10 | column -t -o ' ' -R 1,2,3,4,5
