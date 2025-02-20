#!/bin/bash

GC='\033[0;32m'
NC='\033[0m'

for file in $(egrep -irl --include=*.py "linkedlist" .);
do
	echo -e "${GC}RUNNING ${file}${NC}"
	python3 $file
done
