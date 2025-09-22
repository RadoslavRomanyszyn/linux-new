#!/bin/bash

echo "$#"
echo "${0}"
echo "${1:-parameter one not set}"
echo "${2:-parameter two not set}"
echo "${3:-parameter three not set}"
echo "${4:-parameter four not set}"
echo "${5:-parameter five not set}"
echo "$@"
