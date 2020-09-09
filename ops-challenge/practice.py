

import os

## storing the user's input here 
userInput = input("what directory do you want to go into ? ")

def printUsersInput(userinput):
    for (root, dirs, files) in os.walk(userInput):
        print(root)
        print(dirs)
        print(files)

printUsersInput(userInput)