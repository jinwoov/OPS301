#!/usr/bin/python

from os import remove

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
    print(file1.readlines()[0])
    file1.close()

## Erase the File
def removeFile(file):
    remove(file)
    print("file is gone")

# Main
writeFile(filePath)
readFile(filePath)
removeFile(filePath)
# END