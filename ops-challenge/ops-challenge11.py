#!/usr/bin/python

# Script Name: Ops Challenge: Class 11
# Author: Jin Kim
# Date of last revision: 09/14/2020
# Description of purpose: Able to perform file manipulation 

# Declare the variables
## File path to the text file
filePath = "./jedi.txt"

# Declare the functions
## Writing into the file
def writeFile(file):
    file1 = open(file, "w")
    file1.writelines("May\n")
    file1.writelines("the\n")
    file1.writelines("force be with you")
    file1.close()

## reading the file
def readFile(file):
    file1 = open(file, "r")
    lines = file1.readlines()
    for line in lines:
        print(line)
    file1.close()


# Main
writeFile(filePath)
readFile(filePath)

# END