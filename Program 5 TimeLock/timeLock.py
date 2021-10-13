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
from hashlib import md5

#import pytz

# sets 
INTERVAL = 60
#MANUAL_DATETIME = "2021 2 23 0 0 0"
MANUAL_DATETIME = ""

#functions 
    # convert YYYY, MM, DD, HH, mm, S to seconds 
def getTime(Y,M,D,H,m,S):
    seconds = 0
    #print(Y)
    M += (Y*12)
    #print(M)
    D += (M*30)
    H += (D*24)
    m += (H*60)
    S += (m*60)
    seconds = S
    return seconds 
    
    # convert everything to final string 
def getCode(time1):
    # if not manual datetime then get current date time 
    if(MANUAL_DATETIME == ""):
        currentTime = "" # get time stamp from computer 
    else:
        currentTime = MANUAL_DATETIME
    # print out for test 
    print("Current(UTC) ") # test code 
    print("Epoch (UTC ) " + MANUAL_DATETIME) # test code 
    
    # get time diff
    time2 = getTime(currentTime)
    timediff = time1-(time2%60)
    #print test 
    print("Seconds: " + time1) # test code 
    print("Seconds: " + time2) # test code 
    
    # get md5 and print test 
    string = md5(timediff)
    print("MD5 #1: " + string) # test code 
    string2 = md5(string)
    print("MD5 #2: " + string2) # test code 
    
    #get the final bit
    
    



###########Start of Program
if(not(sys.stdin.isatty())): # if there is input from start of run
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
    timeN = getTime(int(cT[0]),int(cT[1]),int(cT[2]),int(cT[3]),int(cT[4]),int(cT[5]))
    timeE = getTime(int(cE[0]),int(cE[1]),int(cE[2]),int(cE[3]),int(cE[4]),int(cE[5]))
    #print(timeN) # test seconds 
    #print(timeE)

    # get time diff with only chaning every 60 sec
    timeD = timeN-timeE - ((timeN-timeE)%60)       ##### CHECK THIS 
    #print(timeD)
    
    # convert to encoded md5
    string = md5.new((timeD))
    print("MD5 #1: " + string) # test code 
    string2 = md5.new((string))
    print("MD5 #2: " + string2) # test code 
    

else: # else print error
    print("Incorrect input. Please use: ")
    print('echo "YYYY MM DD HH mm SS" | python3 ' + sys.argv[0])
    print("or")
    print('python3 ' + sys.argv[0] + ' < input.txt')

    
"""
if len(sys.argv)>=6: # for user input handling 
    # convert to UTC TIME 
    

    # change input time to seconds 
    time1 = getTime(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
    print(time1) # test seconds
    stringF = getCode(time1)
    print(stringF)
else:
    print("Incorrect input")
    print("python3 " + sys.argv[0] + "YYYY MM DD HH mm SS")
"""
