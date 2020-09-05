#!bin/bash

# Script Name: Ops301- Challenge 05 
# Author: Jin Kim
# Date of last revision: 09/04/2020
# Description of purpose: To clear the content inside of files

# variables
MESSAGELOGS="/var/log/syslog"
WTMP="/var/log/wtmp"

# functions

function ClearContent()
{
    > $1
    StatusBar
    echo "Here is the output after clearing footprint"
    cat $1
}

### HELPER METHOD
## Status bar using interation
function StatusBar()
{
    echo "Clearing contents in progress"
    status=""
    for((i=0;i<=100;i++)); do
        sleep 0.02
        if [ $((i%5)) -eq 0 ]
        then
            status+="*"
            echo -ne "($i%) $status\r"
        fi
    done
    echo " DONE "
}

# MAIN
ClearContent $MESSAGELOGS
ClearContent $WTMP


### Stretch Goals



### Clearing the log is important as to prevent any detection from forensic team. For the forensic team, they can use this data to analyze who and what kind of attack was done during the session. Attack leave malware for persistent connection, but that can lead a breadcrumbs for defensive to find where the attack is coming from.

#END