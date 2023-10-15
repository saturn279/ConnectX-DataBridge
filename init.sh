#!/bin/bash

# Run the first command

airflow db init

# Run the second command in a subshell
( airflow users create -u airflow -p airflow -r Admin -e admin@example.com -f Admin -l User)

# Run the third command in another subshell
( exec airflow webserver & airflow scheduler)
