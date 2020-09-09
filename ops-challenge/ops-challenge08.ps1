# Script Name: Ops-Challenge 08
# Author: Jin Kim
# Date of last revision: 09/09/2020
# Description of purpose: Creating a new user, group and organization unit to the Active Directory


# Declaring the functions
<#
.Description
To Create a Franz in to the users using powershell commands
#>
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

## STRETCH GOALS

<#
.Description
To Create a group using powershell commands
#>
function CreateGroup()
{
    New-ADGroup `
        -Name "TPS Reporting" `
        -GroupCategory "Security" `
        -GroupScope "Global" `
        -DisplayName "TPS Department"
}

<#
.Description
To Create an organization unit using powershell commands
#>
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