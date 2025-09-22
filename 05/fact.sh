#!/bin/bash

set -ueo pipefail

fact_stdin() {
	read -r n
	result=1
	while [ $n -gt 1 ]; do
		result=$(( result * n ))
		n=$(( n - 1 ))
	done
	echo $result
}

fact_arg() {
	n=$1
	if [ $n -eq 0 ]; then
		echo 1
	else
		echo $(( $( fact_arg $(( n - 1 )) ) * n ))
	fi
}

fact_stdin
fact_arg "${1:-0}"
