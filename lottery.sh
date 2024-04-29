#!/bin/bash
# Generate a random number between 1 and 2
if [ $((RANDOM % 2 + 1)) -eq 1 ]; then
    echo "COMMIT + PUSH :  "
    #else
        #echo $RANDOM
fi

if [ $((RANDOM % 4 + 1)) -eq 1 ]; then
    echo "week break"
    #else
        #echo $RANDOM
fi