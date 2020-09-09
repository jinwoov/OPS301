# Script Name: Ops-Challenge 08
# Author: Jin Kim
# Date of last revision: 09/09/2020
# Description of purpose: Creating a new user, group and organization unit to the Active Directory


# Declaring the functions
function CreateUser()
{
    New-ADUser `
        -Name "Franz Ferdinand" `
        -GivenName "Franz" `
        -Surname "Ferdinand" `
        -Company "Globex Nuclear USA" `
        -Title "TPS Reporting Lead" `
        -State "Oregon" `
        -City "Springfield" `
        -Department "TPS Department" `
        -DisplayName "Franz Ferdinand" `
        -EmailAddress "ferdi@globexnuclear.com" `
        -Country "USA"
}

function CreateGroup()
{
    New-ADGroup `
        -Name "TPS Reporting" `
        -GroupCategory "Security" `
        -GroupScope "Global" `
        -DisplayName "TPS Department"
}

function CreateOU()
{
    New-ADOrganizationalUnit `
        -Name "UserAccount" `
        -City "Springfield" `
        -State "Oregon" `
        -Country "USA" `
}

# MAIN
CreateUser
CreateGroup
CreateOU

# END