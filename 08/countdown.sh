#!/bin/bash

set -ueo pipefail

abort() {
    echo Aborted
    exit 17
}

trap abort INT TERM

counter="$1"
while [ "$counter" -gt 0 ]; do
    echo "$counter"
    sleep 1
    counter=$(( counter - 1 ))
done
