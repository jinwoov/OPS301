#!/usr/bin/python
from requests import get, post, put, delete, head, patch, options
import getpass
import os
import time

# Script Name: Ops Challenge: Class 13
# Author: Jin Kim
# Date of last revision: 09/16/2020
# Description of purpose: To perform HTTP protocols through user's input. Every input from user will determine the final outcome.

# Declaring variable


# Declaring function
## Main interface with error handling
def mainMenu():
    try:
        userChoice = input(f"""
        Hi {getpass.getuser()}! What do you want to perform?
        1. GET
        2. POST
        3. PUT
        4. DELETE
        5. HEAD
        6. PATCH
        7. OPTIONS
        8. Exit
        Choice --> """)

        if(userChoice == "1"):
            requestMethod("GET")
        elif(userChoice == "2"):
            requestMethod("POST")
        elif(userChoice == "3"):
            requestMethod("PUT")
        elif(userChoice == "4"):
            requestMethod("DELETE")
        elif(userChoice == "5"):
            requestMethod("HEAD")
        elif(userChoice == "6"):
            requestMethod("Patch")
        elif(userChoice == "7"):
            requestMethod("OPTIONS")
        else:
            exit(0)
    except:
        print("Application didn't work like how it intended to be !!!")

## request method (refactored)
def requestMethod(method):
    if(validateChoice(method)):
        response = eval(str.lower(method))(url)
        statCode = int(response.status_code)
        statusCodes(statCode)

# Final out put after running the query to the given URL
def statusCodes(statCode):
    timeOut()
    if (statCode >= 100 and statCode < 200):
        print(colors.fg.orange,f"{getpass.getuser()}, you got informational response from {url}")
    elif (statCode >= 200 and statCode < 300):
        print(colors.fg.green,f"{getpass.getuser()}, your response came back successful from {url}")
    elif (statCode >= 300 and statCode < 400):
        print(colors.fg.orange,f"{getpass.getuser()}, you were redirected from {url}")
    elif (statCode >= 400 and statCode < 500):
        print(colors.fg.red,f"{getpass.getuser()}, you done mess up from {url}")
    else:
        print(colors.fg.red,f"{getpass.getuser()}, Server had error to your request from {url}")
    print(colors.reset)

## Validating if the choice was yes
def validateChoice(choice):
    userOption = input(f"You chose to perform {choice} method to {url}. Do you want to proceed (y)es/(n)o? ")
    if(userOption == "y" or userOption == "yes" or userOption == "Y" or userOption == "Yes"):
        return True
    else:
        return False

## what site does user want to query
def whatSite():
    url = input("which site do you want to request? ")
    while (len(url) < 3):
        print(colors.fg.red,"You entered wrong url", colors.reset)
        url = input("which site do you want to request? ")
    if(url.__contains__("https") == False):
        url = f"https://{url}"
    return url


### HELPER FUNCTION
## class that contains default color that can be used for console
class colors:
    reset='\033[0m'
    class fg:
        green='\033[32m'
        red='\033[0;31m'
        orange = '\033[33m'

## timeout to give user a realistic experience
def timeOut():
    print("Querying.....")
    time.sleep(2)

### STRETCH GOAL
## Calling authentication to the GitHub api
def authentication():
    username = input("Type your username: ")
    password= input("Type your password: ")
    response = requests.get(f"https://api.github.com/user, ",
                auth = requests.auth.HTTPBasicAuth(username, password))
    print(response.status_code)


# MAIN
url = whatSite()
mainMenu()
authentication()
exit(0)

# END