#!/bin/bash

# ==============================================================================
# Created by: laercio.serra@gmail.com
# Created at: 27/10/2020
# ==============================================================================
clear

echo "WELCOME TO BOA CHALLENGE FOR DATA ENGINEER!"
echo "NAME: LAERCIO SERRA"
echo "----------------------------------------------"
echo "=> CHECKING APPLICATION . . ."
echo "----------------------------------------------"

# Check for file existence
file="./scripts/eda.py"
if [ -e $file ]; then
	echo "=> [OK] - EXPLORATORY DATA ANALYSIS"
else
	echo "=> [NOK] - File 'eda.py' does not exists!"
fi

# Check if file is readable
file="./scripts/eda.py"
if [ -r $file ]; then
  python3 ./scripts/eda.py
else
  echo "=> [NOK] - File 'eda.py' is not readable!"
fi