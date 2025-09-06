#!/bin/bash

# Assuming a matrix of the following format (max 3 digits, m rows, n cols)
#    | 106 179 |
#    | 188  50 |
#    |   5 125 |
# print the sum of each row.

tr -d '|' | tr -s ' ' | cut -d ' ' -f 2- | rev | cut -d ' ' -f 2- | rev | tr ' ' '+' | bc
