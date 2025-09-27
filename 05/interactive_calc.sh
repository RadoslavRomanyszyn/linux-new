#!/bin/bash

set -ueo pipefail

input=/dev/stdin

if [ $# -eq 1 ]; then
	if [ "$1" = "-" ]; then
		input=/dev/stdin
	elif [ -f "$1" ]; then
		input="$1"
	else
		echo ""$0": "$1": No such file" >&2
		exit 1
	fi
fi

result=0

while read -r op num; do
	case "$op" in
		+)
			result=$(( $result + $num ))
			;;
		-)
			result=$(( $result - $num ))
			;;
		\*)
			result=$(( $result * $num ))
			;;
		/)
			result=$(( $result / $num ))
			;;
	esac
done <"$input"

echo "= $result"
