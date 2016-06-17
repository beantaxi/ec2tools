#!/bin/bash
    
cmd="python3 -c 'import ec2tools; ec2tools.listThe.Instances()'"
eval $cmd | awk -F',' 'NR>1 { printf "%10s %-32s %-12s %15s %-20s\n", $1, $2, $3, $4, $5 }'

