################################################################
#Group: Hermit 
#Names: Matthew Tucker, 
#Desc: 
#Date: 10/11/2021
################################################################
#Division of labor:
#Matthew: Input/output system
#ADD YOUR NAME 
# All members worked together and help when others strugled


## HAVE NOT TESTED YET JUST DID QUICKLY IN CLASS

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
MANUAL_DATETIME = "2013 05 06 07 43 25"
#MANUAL_DATETIME = ""

#functions 
    # convert YYYY, MM, DD, HH, mm, S to seconds 
def getTime(Y,M,D,H,m,S):
    seconds = 0
    seconds += (Y*31556926)
    seconds += (M*2629743)
    seconds += (D*86400)
    seconds += (H*3600)
    seconds += (m*60)
    seconds += S
    print(seconds)
    return seconds 
     
    



###########Start of Program
if((not(sys.stdin.isatty()))): # if there is input from start of run
    # get input from .txt or echo
    year = sys.stdin.readline().rstrip()
    #print("{}".format(year)) # test print
    
    # get current time 
    if(MANUAL_DATETIME == ""):
        now = datetime.utcnow()
        currentTime = now.strftime("%Y %m %d %H %M %S") # get time stamp from computer 
    else:
        currentTime = MANUAL_DATETIME
    #print(currentTime) # print test 
    
    # break up the current time and given time 
    cT = currentTime.split( )
    cE = year.split( )

    # convert to seconds 
    print(cT)
    print(cE)
    timeN = getTime(int(cT[0]),int(cT[1]),int(cT[2]),int(cT[3]),int(cT[4]),int(cT[5]))
    timeE = getTime(int(cE[0]),int(cE[1]),int(cE[2]),int(cE[3]),int(cE[4]),int(cE[5]))
    
    print(timeN) # test seconds 
    print(timeE)
    print("Time diff " + str((timeE%INTERVAL)))

    # get time diff with only chaning every interval sec
    timeD = int(timeN-timeE)       ##### CHECK THIS                  ## SOMTHING WRONG HERE
    if(not(int(cE[5])%INTERVAL == 0)):
        timeF =str(timeD-int(cE[5])%INTERVAL)
    
    print(timeF)
      
    #timeD = str(421137839)  # HARD TEST CODE 
    # convert to encoded md5
    string = (hashlib.md5((timeF).encode('utf-8')).hexdigest())      ## SOMTHING WRONG HERE
    print("MD5 #1: " + string) # test code 
    string2 = (hashlib.md5((string).encode('utf-8')).hexdigest())
    print("MD5 #2: " + string2) # test code 
    
    # get output
    only_alpha ="" # For all letters 
    only_number = ""  # for all numbers 
    for char in string2: # go charater by charater
        # get the ACII num to determin what it is 
        if(ord(char) >= 65 and ord(char) <= 90):  # lower case 
            only_alpha += char
        elif(ord(char) >= 97 and ord(char) <= 122): # upper case 
            only_alpha += char
        elif(ord(char) >= 48 and ord(char) <= 57): # numbers 
            only_number += char
    key ="" # set up final key 
    # get first two alphabetical and last to numbers 
    key += only_alpha[0:2]
    key += only_number[-1]
    key += only_number[-2]
    print(key) # output key END OF CODE

else: # else print error for in correct use 
    print("Incorrect input. Please use: ")
    print('echo "YYYY MM DD HH mm SS" | python3 ' + sys.argv[0])
    print("or")
    print('python3 ' + sys.argv[0] + ' < input.txt')

    

