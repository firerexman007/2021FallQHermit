################################################################
#Group: Hermit 
#Names: Matthew Tucker,Thien 
#Desc: This code takes a time stamp and current time to make a time key based on the amount of seconds the original time stamp is from current time
#Date: 10/11/2021
################################################################
#Division of labor:
#Matthew: Input/output system, elapsed time, structure, MD5 
#Thien: Troubleshooting seconds elapsed
# All members worked together and help when others struggled



#imports 
import sys
import re
from datetime import datetime, date 
import calendar 
import hashlib 

#import pytz

# sets 
INTERVAL = 60
#current time
#MANUAL_DATETIME = "2017 03 23 18 02 06" # example 
MANUAL_DATETIME = ""
netcat host 13847134178


###########Start of Program
if((not(sys.stdin.isatty()))): # if there is input from start of run
    # get input from .txt or echo
    epoch = sys.stdin.readline().rstrip()
    epoch = datetime.strptime(epoch, "%Y %m %d %H %M %S")
    #print(epoch)
    #print("{}".format(year)) # test print
    
    # get current time 
    if(MANUAL_DATETIME == ""):
        now = datetime.utcnow()
        currentTime = now.strftime("%Y %m %d %H %M %S") # get time stamp from computer
    else:
        currentTime = MANUAL_DATETIME
        currentTime = datetime.strptime(MANUAL_DATETIME, "%Y %m %d %H %M %S")
    #print(currentTime) # print test 
    
    #get total elapsed seconds
    cT = currentTime.timestamp()
    cE = epoch.timestamp()

    # get time diff
    timeD = int(cT - cE)       ##### CHECK THIS                  ## FIXED
    #print(timeD)
    #subtract by INTERTVAL
    if (INTERVAL != 0):
        timeD -= timeD % INTERVAL
    timeD = str(timeD)
      
    #timeD = str(421137839)  # HARD TEST CODE 
    # convert to encoded md5
    string = (hashlib.md5((timeD).encode('utf-8')).hexdigest())      ## FIXED
    #print("MD5 #1: " + string) # test code 
    string2 = (hashlib.md5((string).encode('utf-8')).hexdigest())
    #print("MD5 #2: " + string2) # test code 
    
    # get output
    only_alpha ="" # For all letters 
    only_number = ""  # for all numbers 
    all_things =""
    for char in string2: # go charater by charater
        # get the ACII num to determin what it is 
        if(ord(char) >= 65 and ord(char) <= 90):  # lower case 
            only_alpha += char
            all_things += char
        elif(ord(char) >= 97 and ord(char) <= 122): # upper case 
            only_alpha += char
            all_things += char
        elif(ord(char) >= 48 and ord(char) <= 57): # numbers 
            only_number += char
            all_things += char
    key ="" # set up final key 
    # get first two alphabetical and last to numbers 
    key += only_alpha[0:2]
    key += only_number[-1]
    key += only_number[-2]
    key += all_things[len(all_things)//2]
    print(key) # output key END OF CODE

else: # else print error for in correct use 
    print("Incorrect input. Please use: ")
    print('echo "YYYY MM DD HH mm SS" | python3 ' + sys.argv[0])
    print("or")
    print('python3 ' + sys.argv[0] + ' < input.txt')

    

