#!/bin/bash
    
PYPATH=${PYPATH:-python3}
cmd="$PYPATH -c 'import ec2tools; ec2tools.listThe.SecurityGroups()'"
eval $cmd | awk -F',' 'NR>1 { printf "%12s %-32s %6s %-12s %s\n", $1, $2, $3, $4, $5 }'
