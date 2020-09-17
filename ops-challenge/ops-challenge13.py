#!/usr/bin/python
from requests import get, post, put, delete, head, patch, options
## library utilized to get current user's username 
import getpass
import os
import time

# Script Name: Ops Challenge: Class 13
# Author: Jin Kim
# Date of last revision: 09/16/2020
# Description of purpose: To perform HTTP protocols through user's input. Every input from user will determine the final outcome.

# Declaring variable

requestArr = ["GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS"]
# Declaring function
## Main interface with error handling
def mainMenu():
    try:
        count = 1
        print(f"Hi {getpass.getuser()}! What do you want to perform?")
        for r in requestArr:
            print(f"{str(count)}. {r}")
            count += 1
        userChoice = input("Choice --> ")
        if(int(userChoice) > 6):
            raise ValueError
        userChoice = int(userChoice) - 1
        requestMethod(requestArr[userChoice])

    except ValueError:
        print("You entered wrong choice!!")
        exit(0)



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
        print(colors.fg.orange,f"{getpass.getuser()}, you got informational querying response from {url}")
    elif (statCode >= 200 and statCode < 300):
        print(colors.fg.green,f"{getpass.getuser()}, your response came back querying successful from {url}")
    elif (statCode >= 300 and statCode < 400):
        print(colors.fg.orange,f"{getpass.getuser()}, you were redirected querying from {url}")
    elif (statCode >= 400 and statCode < 500):
        print(colors.fg.red,f"{getpass.getuser()}, you done mess up querying from {url}")
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

#checking if its int parsable
def checkParsable(num):
    try: 
        int(s)
        return True
    except ValueError:
        return False

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