#!/bin/bash
    
if [ $# -lt 2 ]; then
	>&2 echo Usage: python3 ${FUNCNAME[0]} idInstance
	sys.exit(-1)

$idInstance=$1
python3 -c "import ec2tools; ec2tools.waitFor.InstanceRunning('$idInstance')"
