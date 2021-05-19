#!/bin/bash

./build/program tests out.txt
sort -o out.txt out.txt
sort -o output.txt output.txt




if cmp -s "output.txt" "out.txt"; then
    echo "PASS"
else
    echo "FAIL"
fi
