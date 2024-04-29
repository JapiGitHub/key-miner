#!/bin/bash
# diggging raw material

# Base key parameters
KEY_BASE_NAME="id_rsa_MINED_"

#COMMENT="your_email@example.com"

DATESTAMP=$(date +"%Y%m%d_%H%M%S")

mkdir -p ./ssh-keys-${DATESTAMP}/

# Generate 100 SSH keys
for i in $(seq 1 500); do
    # Define the full path with iteration
    FULL_KEY_PATH="ssh-keys-${DATESTAMP}/${KEY_BASE_NAME}_$i"


    START_TIME=$(date +%s%N)

    # Create the SSH key
    ssh-keygen -t rsa -b 4096 -f "$FULL_KEY_PATH" -N "" | grep -A 12 "\[RSA 4096\]----+"


    # Create the SSH key
    #ssh-keygen -t rsa -b 4096 -f "$FULL_KEY_PATH" -N "" >/dev/null 2>&1
    END_TIME=$(date +%s%N)
    TIME_DIFF=$(echo "scale=3; ($END_TIME - $START_TIME)/1000000000" | bc)
    TIMES+=($TIME_DIFF)

    # Calculate stats
    TOTAL_TIME=$(echo "${TIMES[@]}" | tr ' ' '+' | bc -l)
    AVG_TIME=$(echo "scale=3; $TOTAL_TIME / $i" | bc -l)

    # Clear the line before printing
    #echo -ne "\033[2K\r"
    echo ""

    echo  "Keys generated: $i, Average Speed: $AVG_TIME s/key, Latest Speed: $TIME_DIFF s/key"


done