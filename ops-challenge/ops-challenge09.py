#!/usr/bin/python

# Script Name: Ops Challenge: Class 09
# Author: Jin Kim
# Date of last revision: 09/10/2020
# Description of purpose: Working with list to print out element that is in and also mutate element in the array.

# Declaration of variables
fruit = ["Pikachu", "Charmander ", "Bulbasaur", "Onyx", "Eevee", "Gangar", "Grimer", "Rattat", "Pidgey", "Mew"]

# Declaration of functions

def getElement(num, numTwo):
    print(fruit[num:numTwo])

def changeElement(num, string):
    fruit[num] = string


# Main
## Print the fourth element of the list.
getElement(3,4)

## Print the sixth through tenth element of the list.
getElement(5,9)

## Change the value of the seventh element to "onion".
changeElement(6, "onion")
getElement(6,7)