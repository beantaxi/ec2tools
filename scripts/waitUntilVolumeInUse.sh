#!/bin/bash
    
if [ $# -lt 2 ]; then
	>&2 echo Usage: python3 ${FUNCNAME[0]} idVolume
	exit -1
fi

$idVolume=$1
python3 -c "import ec2tools; ec2tools.waitFor.VolumeInUse('$idVolume')"
