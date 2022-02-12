#!/usr/bin/env bash

if [ $# -ne 1 ] || [[ ! "$1" =~ ^[0-9]+$ ]]; then
    echo "Usage: leap.sh <year>"
    exit 1
fi

[[ $1/4*4 -eq $1 ]] && ([[ $1/100*100 -ne $1 ]] || [[ $1/400*400 -eq $1 ]]) && echo "true" || echo "false"
