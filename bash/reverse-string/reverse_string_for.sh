#!/bin/bash

line="$1"
line_length=${#line}
echo $line

for (( i=$line_length; i>=0; i-- ))
do
    echo -n ${line:i:1}
done
