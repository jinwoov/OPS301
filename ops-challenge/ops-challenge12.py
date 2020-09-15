#!/usr/bin/python

import psutil
import math

# Script Name: Ops Challenge: Class 11
# Author: Jin Kim
# Date of last revision: 09/14/2020
# Description of purpose: Able to perform file manipulation 


def printCPU(param):
    result = str(psutil.cpu_times())
    finalOutput = result.split(",")
    print(finalOutput)
    if(param == "user"):
        output = finalOutput[0].split("(")[1]
    elif(param == "system"):
        output = finalOutput[1]
    elif(param == "idle"):
        output = finalOutput[2]
    #elif(param == "")
    
    print(f"{output} seconds")


## HELPER 

def heading(headings):
    print(colors.fg.green, headings)
    print(colors.reset)

class colors:
    reset='\033[0m'
    class fg:
        green='\033[32m'
        red='\033[0;31m'

heading("Time spent by normal processes")
printCPU("user")

heading("Time spent by processes executing in kernel mode")
printCPU("system")

heading("Time when system was idle")
# printCPU()

