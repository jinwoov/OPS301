#!/usr/bin/python

import psutil

# Script Name: Ops Challenge: Class 12
# Author: Jin Kim
# Date of last revision: 09/15/2020
# Description of purpose: To show different aspects of CPU information

## This is to check what the function call is going to be using to output cpu info
def printCPU(param):
    result = str(psutil.cpu_times())
    finalOutput = result.split(",")
    if(param == "user"):
        output = finalOutput[0].split("(")[1]
        output = output.split("=")[1]
    elif(param == "system"):
        output = finalOutput[2]
        output = output.split("=")[1]
    elif(param == "idle"):
        output = finalOutput[3]
        output = output.split("=")[1]
    elif(param == "iowait"):
        output = finalOutput[4]
        output = output.split("=")[1]
    elif(param == "irq"):
        output = finalOutput[5]
        output = output.split("=")[1]
    elif(param == "softirq"):
        output = finalOutput[6]
        output = output.split("=")[1]
    elif(param == "steal"):
        output = finalOutput[7]
        output = output.split("=")[1]
    elif(param == "guest"):
        output = finalOutput[8]
        output = output.split("=")[1]
    print(f" {output} seconds")

## To make it clean, call stack carries all of the function call
def callStack():
    heading("Time spent by normal processes")
    printCPU("user")

    heading("Time spent by processes executing in kernel mode")
    printCPU("system")

    heading("Time when system was idle")
    printCPU("idle")

    heading("Time spent waiting for I/O to complete.")
    printCPU("iowait")

    heading("Time spent for servicing hardware interrupts")
    printCPU("irq")

    heading("Time spent for servicing software interrupts")
    printCPU("softirq")

    heading("Time spent by other operating systems running in a virtualized environment")
    printCPU("steal")

    heading("Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel")
    printCPU("guest")

## HELPER 
## For putting head for function call
def heading(headings):
    print(colors.fg.green, headings)
    print(colors.reset)

## class that contains default color that can be used for console
class colors:
    reset='\033[0m'
    class fg:
        green='\033[32m'
        red='\033[0;31m'

# MAIN
callStack()

# END