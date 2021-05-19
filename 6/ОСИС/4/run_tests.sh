#!/bin/bash

in_list=(tests/in*.txt)

for i in "${!in_list[@]}"; do
  echo "Running test №$((i + 1))"
  ./build/program <"${in_list[$i]}" >"tests/out$((i + 1)).txt"
  if diff -Z "tests/output$((i + 1)).txt" "tests/out$((i + 1)).txt" > /dev/null; then
    echo "Passed"
  else
    echo "Fail"
    echo "tests/output$((i + 1)).txt"
    echo "tests/out$((i + 1)).txt"
    break
  fi
done
