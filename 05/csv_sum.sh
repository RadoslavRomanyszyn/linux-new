#!/bin/bash

set -ueo pipefail

if [ $# -ne 1 ]; then
	echo "Provide column name as the first and only argument." >&2
	exit 1
fi

column_to_sum="$1"
read -r header
header=$( echo "$header" | tr ',' ' ' )
column_no=0

for column in $header; do
	column_no=$(( column_no + 1 ))
	if [ "$column" = "$column_to_sum" ]; then
		break
	fi
done

cut -d , -f "$column_no" | paste -s -d + | bc
