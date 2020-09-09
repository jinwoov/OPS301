# Script Name: Ops-Challenge 06
# Author: Jin Kim
# Date of last revision: 09/07/2020
# Description of purpose: This is to utitlize commands that's avaible in bash using python script file

# bringing os library
import os
from subprocess import Popen, PIPE


# Declaration of variables
currentUser = os.popen("whoami").read()
myIP = os.popen("ip a | grep inet").read()
hardwareInfo = os.popen("sudo lshw -short").read()

currentUserSG = Popen(["whoami"], stdout=PIPE, shell=True, encoding='utf-8').communicate()[0]
myIPSG = Popen(["ip a | grep inet"], stdout=PIPE, shell=True, encoding='utf-8').communicate()[0]
hardwareInfoSG = Popen(["sudo lshw -short"], stdout=PIPE, shell=True, encoding='utf-8').communicate()[0]

# Declaration of functions
# modularizing all of the ops challenge into one invocation 
def firstPart():
    Heading("whoami command")
    print(currentUser)
    promptUser()
    Heading("ip a command")
    print(myIP)
    promptUser()
    Heading("lshw -short command")
    print(hardwareInfo)

def stretchGoal():
    Heading("whoami command")
    print(currentUserSG)
    Heading("ip a command")
    print(myIPSG)
    Heading("lshw -short command")
    print(hardwareInfoSG)


## HELPER
# creating a color class to be used for heading
class colors:
    reset='\033[0m'
    class fg:
        green='\033[32m'

# Prompting user if they want to continue with the rest of execution.
def promptUser():
    input("Press enter to continue")
    print()

# Heading to show what the user is going to expect on next execution
def Heading(name):
    print(colors.fg.green + f"This is {name} output")
    print(colors.reset)

# MAIN (Invoking all of the commands)
firstPart()
input("Ready for stretch goal?")
stretchGoal()