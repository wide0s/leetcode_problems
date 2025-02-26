#!/bin/bash

OC='\033[0;33m'
GC='\033[0;32m'
NC='\033[0m'

count=0
for file in $(find . -name "[0-9]*_*.py");
do
	echo -e "${GC}RUNNING ${file}${NC}"
	python3 $file
	count=$(expr $count + 1)
done
echo -e "${OC}SOLUTIONS: ${count}${NC}"
