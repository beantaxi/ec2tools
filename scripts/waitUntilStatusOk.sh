#!/bin/bash
    
if [ $# -lt 1 ]; then
	>&2 echo Usage: python3 ${FUNCNAME[0]} idInstance
	exit -1
fi

idInstance=$1
python3 -c "import ec2tools; ec2tools.waitFor.InstanceStatusOk('$idInstance')"
