#!/usr/bin/python
import random

# Script Name: Ops Challenge: Class 10
# Author: Jin Kim
# Date of last revision: 09/10/2020
# Description of purpose: Use if/elif/else logics to create a interactive game.


# Declare Function
## First interface when user enters the application
def guessNumber():
    print("""
    #======================#
    #     Guess Number     #
    #    by Jinfluenza     #
    #======================#
    """)
    Answer = int(input("what Number am I thinking? (between 1~10) "))
    if(Answer > 10 or Answer < 0):
        guessNumber()
    else:
        return Answer
## Creating random number
def generateRandomNum():
    return random.randrange(1,10)
## Checking user's answer
def checkAnswer(user, me):
    if (user == me):
        print(colors.fg.green,"CORRECT!! You chose right! ")
        return
    elif (user > me):
        print(colors.fg.red, "Your chose high number")
        print(colors.reset)
    else:
        print(colors.fg.red, "Your choice was too little")
        print(colors.reset)
    ## Taking user's input again and depending on the input, game will determine if its going to continue to play or quit the application
    choice = input("Choose AGAIN to guess right OR type 'quit/q' to quit ")
    if(choice == "quit" or choice == "q"):
        return
    else:
        choice = int(choice)
        checkAnswer(choice, me)

## HELPER METHOD
## Color class to add colors to the console application
class colors:
    reset='\033[0m'
    class fg:
        green='\033[32m'
        red='\033[0;31m'

# Declare Variables (due to the call stack variables has to reside under the functions)
userChoice = guessNumber()
myChoice = generateRandomNum()

# Main
checkAnswer(userChoice, myChoice)
print("Thanks for playing!")

# END