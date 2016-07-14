#!/bin/bash

if [ $# -lt 1 ]; then
	>&2 echo Usage: python3 ${BASH_SOURCE} idInstance
	exit -1
fi

idInstance=$1
python3 -c "import ec2tools; ec2tools.getA.Instance(id='$idInstance').stop()"

