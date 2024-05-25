#!/bin/bash

is_prime() {
    if [ $1 -eq 2 ]; then
        return 0
    fi
    for ((i=2; i<=$1/2; i++)); do
        if [ $(($1 % $i)) -eq 0 ]; then
            return 1
        fi
    done
    return 0
}

print_pyramid() {
    num_rows=$1
    count=2
    for ((i=1; i<=num_rows; i++)); do
        for ((j=1; j<=i; j++)); do
            while true; do
                if is_prime $count; then
                    echo -n "$count "
                    ((count++))
                    break
                fi
                ((count++))
            done
        done
        echo ""
    done
}

if [ $# -eq 0 ]; then
    echo "Usage: $0 "
else
    print_pyramid $1
fi
