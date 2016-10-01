#!/bin/bash

if [[ -z SSH_AUTH_SOCK || -z SSH_AGENT_PID ]]; then
	>&2 echo "Please run ssh-agent and then rerun this script"
	exit 1
fi

git commit -am "$1" && git push; python3 setup.py clean sdist upload -r sparktools
