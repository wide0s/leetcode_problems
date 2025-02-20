#!/bin/bash

GC='\033[0;32m'
NC='\033[0m'

for file in $(find . -name "[0-9]*_*.py");
do
	echo -e "${GC}RUNNING ${file}${NC}"
	python3 $file
done
