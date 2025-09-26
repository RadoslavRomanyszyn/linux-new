#!/bin/bash

set -ueo pipefail

format_normal() {
    cut '-d:' -f 2,3 | column -t -s:
}

format_passwd() {
    cut '-d:' -f 1,3
}

format_shell() {
    cut '-d:' -f 1,3 | sed 's#:\(.*\)#="\1"#'
}

format_json() {
    local varname
    local varvalue
    echo "{"
    cut '-d:' -f 1,3 | sed 's#:# #' | while read -r varname varvalue; do
        echo -n "$varname" | tr 'A-Z' 'a-z' | sed 's#.*#  "&": #'
        echo "\"$varvalue\"",
    done | sed '$s#,$##'
    echo "}"
}

if [ -r "$HOME/.nswi177/sysinfo.rc" ]; then
    . "$HOME/.nswi177/sysinfo.rc"
fi

if [ -z "${FORMATTER:-}" ]; then
    FORMATTER="${DEFAULT_FORMATTER:-normal}"
fi

FORMATTER="format_${FORMATTER}"

(
    echo "PLATFORM:Hardware platform:$( uname -m )"
    echo "KERNEL_VERSION:Kernel version:$( uname -r )"
    echo "CPU_COUNT:CPU count:$( nproc )"
    echo "RAM_TOTAL:RAM size:$( sed -n 's#^MemTotal:[ ]*\([0-9]*\) kB#\1#p' </proc/meminfo )"
) | $FORMATTER
