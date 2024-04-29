#!/bin/bash

# Base key parameters
KEY_BASE_NAME="id_rsa_MINED_"

#COMMENT="your_email@example.com"

rm ./ssh-keys/id_rsa_MINED_*

# Generate 100 SSH keys
for i in $(seq 1 5); do
    # Define the full path with iteration
    FULL_KEY_PATH="ssh-keys/${KEY_BASE_NAME}_$i"

    # Create the SSH key
    ssh-keygen -t rsa -b 4096 -f "$FULL_KEY_PATH" -N ""

done

for file in $(ls ./ssh-keys); do
    grep "BB" ./ssh-keys/$file
done