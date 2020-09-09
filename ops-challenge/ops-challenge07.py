# Script Name: Ops-Challenge 07
# Author: Jin Kim
# Date of last revision: 09/08/2020
# Description of purpose: This script file is to show what kind of files are in the directory 

# bringing os library
import os

# Declaration of variables
## putting user's input into the variable
userInput = input("what directory do you want to see? ")

# Declaration of functions
## taking the input from the user and displaying all of the files within user's input directory.
def directory(inputs):
    for (root,dirs,files) in os.walk(inputs):
        print(root)
        intoText(root)
        print(dirs)
        intoText(dirs)
        print(files)
        intoText(files)


## stretch goals
## putting all the out put to the text files
def intoText(texts):
    fileWrite = open("./output.txt", 'a')
    fileWrite.writelines(texts)
    fileWrite.write("")
    fileWrite.close()
## creating a user input directory and subdirectory of string
def createDir():
    userInput2 = input("What directory do you want to make? ")
    os.makedirs(userInput2)
    for i in range(1,4):
        os.makedirs(f"{userInput2}/string_0{i}")


## Main 
directory(userInput)
os.system("libreoffice --writer ./output.txt")
createDir()
# END