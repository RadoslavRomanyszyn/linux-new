#!/bin/bash

# Expects file /etc/passwd from stdin.
# Print sum of five highest user IDs.

set -ueo pipefail

cut -d : -f 3 | sort -n | tail -n 5 | paste -s -d + | bc
