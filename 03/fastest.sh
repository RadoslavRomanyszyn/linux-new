#!/bin/bash

# Assuming input of the following format
#
#    name1,duration_in_secs_1
#    name2,duration_in_secs_2
#
# print the name with the smallest duration.

sort -t , -k 2 | head -n 1 | cut -d , -f 1
