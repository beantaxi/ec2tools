#!/bin/bash

git commit -am "$1" && git push; python3 setup.py clean sdist upload -r sparktools
