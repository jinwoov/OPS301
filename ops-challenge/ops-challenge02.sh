#!/usr/bin/env bash

# Script Name: Code Challenge 2
# Author: Jin Kim
# Date of last revision: 09/1/2020
# Description of purpose: To create a bash script that copies /var/log/syslog to the current working directory and appends the current date and time to the filename.

# Declaration of variables
dateShort=`date -I`
timeNowLocal=`date +%R`
timestamp="$dateShort $timeNowLocal"

# Declaration of functions
## Main function that creates the file
CreatingFile() {
    cp "/var/log/syslog" "./"
    echo "$timestamp copying file into current directory" >> "syslog"
}

## Appending the date to the file
Output() {
    echo "$timestamp Appending"
    EmptySpace
    echo "$timestamp Appending" >> "syslog"
}

## HELPER METHODS ##
## Created a mock statusbar 
ProgressBar() {
    echo "$timestamp Creating a file with Date and time"
    echo -ne '#####                   (33%)\r'
    sleep 1
    echo -ne '#############           (66%)\r'
    sleep 1
    echo -ne '####################### (100%)\r'
    echo -ne '\n'
}

## funciton that creates empty space
EmptySpace() {
    echo
}

# Main (Invoking everything)
ProgressBar
EmptySpace
CreatingFile
Output

# End