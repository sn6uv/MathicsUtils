#!/bin/bash

for f in $(find . -name "*.py")
do
    scores=$(pylint $f | grep 'Your code has been rated at' | grep -oP '\-?[0-9.]+/10')
    old=$(echo $scores | cut -d' ' -f2)
    new=$(echo $scores | cut -d' ' -f1)
    echo $f $old "->" $new
done
