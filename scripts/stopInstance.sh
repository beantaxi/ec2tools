#!/bin/bash

if [ $# -lt 1 ]; then
	>&2 echo Usage: python3 ${BASH_SOURCE} idInstance
	exit -1
fi

idInstance=$1
PYPATH=${PYPATH:-python3}
$PYPATH -c "import ec2tools; ec2tools.getA.Instance(id='$idInstance').stop()"

