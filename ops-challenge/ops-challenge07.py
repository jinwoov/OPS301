# Script Name: Ops-Challenge 07
# Author: Jin Kim
# Date of last revision: 09/08/2020
# Description of purpose: This is to utitlize commands that's avaible in bash using python script file

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

## putting all the out put to the text files
def intoText(texts):
    fileWrite = open("./output.txt", 'a')
    fileWrite.writelines(texts)
    fileWrite.write("")
    fileWrite.close()

## main 
directory(userInput)

# END