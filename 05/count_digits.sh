#!/bin/bash

for i in *.txt; do
	echo -n "$i: "
	tr -c -d '0-9' <"$i" | wc -c
done
