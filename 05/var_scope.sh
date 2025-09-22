#!/bin/bash

global_var="one"

change_global() {
    echo "change_global():"
    echo "  global_var=$global_var"
    global_var="two"
    echo "  global_var=$global_var"
}

change_local() {
    echo "change_local():"
    echo "  global_var=$global_var"
    local global_var="three"
    echo "  global_var=$global_var"
}

echo "global_var=$global_var"
change_global
echo "global_var=$global_var"
change_local
echo "global_var=$global_var"

(
    global_var="four"
    echo "global_var=$global_var"
)

echo "global_var=$global_var"

echo "loop:"
(
    echo "five"
    echo "six"
) | while read value; do
    global_var="$value"
    echo "  global_var=$global_var"
done
echo "global_var=$global_var"
