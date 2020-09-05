#!bin/bash

# Script Name: Ops301- Challenge 05 
# Author: Jin Kim
# Date of last revision: 09/04/2020
# Description of purpose: To clear the content inside of files

# variables
MESSAGELOGS="/var/log/syslog"
WTMP="/var/log/wtmp"

# functions
## This function use argument to find the filepath and erase the content
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

## linux log files
echo "Following commands can be detrimental to your Linux system. YOU BEEN WARNED!"
read

## auth.log - authentication log
AuthLog="/var/log/auth.log"
read -p "Do you want to delete authentication log? (y|n)" Answer
if [ $Answer -eq "y" ]
then
ClearContent $AuthLog
fi

## kern.log - information about kernel
KernelLog="/var/log/kern.log"
read -p "Do you want to delete kernel log? (y|n)" Answer
if [ $Answer -eq "y" ]
then
ClearContent $KernelLog
fi

## boot.log - booting information
BootLog="/var/log/boot.log"
read -p "Do you want to booting log? (y|n)" Answer
if [ $Answer -eq "y" ]
then
ClearContent $BootLog
fi
## http.log - information about web server apache
HTTPLog="/var/log/HTTPLog"
read -p "Do you want to web service log? (y|n)" Answer
if [ $Answer -eq "y" ]
then
ClearContent HTTPLog
fi

## bash history: is a file that kept separate by user. 
# cd /home/username/.bash_history
HostName="hostname"
BashHistory="/home/$HostName/.bash_history"
read -p "Do you want to bash history? (y|n)" Answer
if [ $Answer -eq "y" ]
then
ClearContent $BashHistory
fi


## Forensic tools
## shred is delete the file permenantly
## shred prevents recovery


### Clearing the log is important as to prevent any detection from forensic team. For the forensic team, they can use this data to analyze who and what kind of attack was done during the session. Attack leave malware for persistent connection, but that can lead a breadcrumbs for defensive to find where the attack is coming from.

#END