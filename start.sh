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

dir="./data"
if [ -d $dir ]; then
  echo "=> [OK] - CSV FILES"
else
	echo "=> [NOK] - Directory '/data' does not exists!"
	exit
fi

dir="./db"
if [ -d $dir ]; then
  echo "=> [OK] - SQLITE DATABASE"
else
	echo "=> [NOK] - Directory '/db' does not exists!"
	exit
fi

dir="./scripts"
if [ -d $dir ]; then
  echo "=> [OK] - PYTHON SCRIPTS"
else
	echo "=> [NOK] - Directory '/scripts' does not exists!"
	exit
fi

dir="./secret"
if [ -d $dir ]; then
  echo "=> [OK] - GOOGLE CREDENTIALS"
else
	echo "=> [NOK] - Directory '/secret' does not exists!"
	exit
fi

dir="./venv"
if [ -d $dir ]; then
  echo "=> [OK] - VIRTUAL ENVIRONMENT"
  export GOOGLE_APPLICATION_CREDENTIALS=../challenge_boa/secret/gcs.json
  source venv/bin/activate
else
	echo "=> [NOK] - Directory '/venv' does not exists!"
	exit
fi

# Check for file existence
file="./scripts/csv_to_sqlite.py"
if [ -e $file ]; then
	echo "=> [OK] - SCRIPT: CSV TO SQLITE"
else
	echo "=> [NOK] - Script 'csv_to_sqlite.py' does not exists!"
	exit
fi

file="./scripts/sqlite_to_gcs.py"
if [ -e $file ]; then
	echo "=> [OK] - SCRIPT: SQLITE TO GCS"
else
	echo "=> [NOK] - Script 'sqlite_to_gcs.py' does not exists!"
	exit
fi

echo
echo "=> EXECUTING CSV TO SQLITE . . ."
echo

# Check if file is readable
file="./scripts/csv_to_sqlite.py"
if [ -r $file ]; then
  python3 $file
else
  echo "=> [NOK] - File 'csv_to_sqlite.py' is not readable!"
  exit
fi

echo
echo "=> EXECUTING SQLITE TO GCS . . ."
echo

file="./scripts/sqlite_to_gcs.py"
if [ -r $file ]; then
  python3 $file
else
  echo "=> [NOK] - File 'sqlite_to_gcs.py' is not readable!"
  exit
fi

echo
echo "----------------------------------------------"
echo "=> JOB FINISHED!"
echo "----------------------------------------------"
echo
