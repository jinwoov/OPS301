#!/usr/bin/env bash

# Script Name: Code Challenge 3
# Author: Jin Kim
# Date of last revision: 09/2/2020
# Description of purpose: To change user's authorization over files and configure permission everything in a directory


# VARIABLES
DIRECTORYPATH=""
PERMISSIONNUM=""
dateShort=`date -I`
timeNowLocal=`date +%R`
timestamp="$dateShort $timeNowLocal"
LOGFILE="./log.txt"

# FUNCTION
function DirectoryPath()
{
    read -p "Please enter directory path way (default will be current directory) " DIRECTORYPATH

    if [ -z "$DIRECTORYPATH" ]
    then
        DIRECTORYPATH="./"
    fi
    echo "User chose $DIRECTORYPATH as a file path" | tee -a $LOGFILE

}

function AskPermission()
{
    read -p "Please enter permission number to change (ie. 755) " PERMISSIONNUM
    if [ -z "$PERMISSIONNUM" ] || [ ${#PERMISSIONNUM} -lt 3 ]
    then
        echo "Please enter correct number"
        AskPermission
    fi
    echo "User chose permission to be $PERMISSIONNUM" | tee -a $LOGFILE
}

function FinalWork()
{
    sudo chmod -R $PERMISSIONNUM $DIRECTORYPATH
    StatusBar
    ls -la $DIRECTORYPATH | tee -a $LOGFILE
}


### HELPER METHOD
function StatusBar()
{
    echo "Changing permission in progress"
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
echo $timestamp >> $LOGFILE
DirectoryPath 
AskPermission
FinalWork
echo >> $LOGFILE

# END 