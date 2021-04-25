#!/bin/bash
TIME_FILE=`dirname $BASH_SOURCE`/Time.txt
echo -n `date +%Y-%m-%d`$'\t'`date +%H:%M`$'\t' | tee -a $TIME_FILE
python3 -c 'import getch; getch.getch()' &> /dev/null
date +%H:%M | tee -a $TIME_FILE

