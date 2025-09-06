#!/bin/bash

# Print real names of users containing 'system' anywhere in their record.
# The list of users comes from stdin.

grep -F "system" - | cut -d : -f 5
