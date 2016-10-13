#!/bin/bash
    
if [ $# -lt 2 ]; then
	>&2 echo Usage: python3 ${FUNCNAME[0]} idInstance
	exit -1
fi

idInstance=$1
PYPATH=${PYPATH:-python3}
$PYPATH -c "import ec2tools; ec2tools.waitFor.InstanceRunning('$idInstance')"
