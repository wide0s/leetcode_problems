#!/bin/bash

CC='\033[0;35m'
OC='\033[0;33m'
GC='\033[0;32m'
BC='\033[0;34m'
NC='\033[0m'

SECONDS=0
drafts=0
count=0
others=0

make -C C run_and_clean

for file in $(find . -name "[0-9]*_*.py");
do
	if grep -q '#DRAFT' ${file}; then
		drafts=$(expr $drafts + 1)
		continue
	fi
	echo -e "${GC}RUNNING ${file}${NC}"
	python3 $file
	if [[ "$file" =~ "youtube/"* ]]; then
		others=$(expr $others + 1)
	else
		count=$(expr $count + 1)
	fi
done
echo -e "${OC}LEETCODE SOLUTIONS IN PYTHON: ${count}${NC} ${CC}DRAFTS: ${drafts}${NC} ${BC}OTHER SOLUTIONS: ${others}${NC} TIME ELAPSED: ${SECONDS}s"
