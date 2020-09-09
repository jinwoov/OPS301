# Script Name: Ops-Challenge 06
# Author: Jin Kim
# Date of last revision: 09/07/2020
# Description of purpose: This is to utitlize commands that's avaible in bash using python script file

# bringing os library
import os


# Declaration of variables



# Declaration of functions

def directory(inputs):
    for (root,dirs,files) in os.walk(inputs):
        print(root)
        intoText(root)
        print(dirs)
        intoText(dirs)
        print(files)
        intoText(files)

def intoText(texts):
    fileWrite = open("./output.txt", 'a')
    fileWrite.writelines(texts)
    fileWrite.write("")
    fileWrite.close()


userInput = input("what directory do you want to see? ")
directory(userInput)