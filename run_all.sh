#!/bin/bash

CC='\033[0;35m'
OC='\033[0;33m'
GC='\033[0;32m'
NC='\033[0m'

drafts=0
count=0
for file in $(find . -name "[0-9]*_*.py");
do
	if grep -q '#DRAFT' ${file}; then
		drafts=$(expr $drafts + 1)
		continue
	fi
	echo -e "${GC}RUNNING ${file}${NC}"
	python3 $file
	count=$(expr $count + 1)
done
echo -e "${OC}SOLUTIONS: ${count}${NC} ${CC}DRAFTS: ${drafts}${NC}"
