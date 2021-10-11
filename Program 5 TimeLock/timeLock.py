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
from datetime import datetime 
from hashlib import md5
import pytz

# sets 
INTERVAL = 60
MANUAL_DATETIME =""


#functions 
    # convert YYYY, MM, DD, HH, mm, S to seconds 
def getTime(Y,M,D,H,m,S):
    seconds = 0
    M += (Y*12)
    D += (M*30)
    H += (D*24)
    m += (H*60)
    s += (m*60)
    seconds = s
    return seconds 
    
    # convert everything to final string 
def getCode(time1):
    # if not manual datetime then get current date time 
    if(MANUAL_DATETIME == ""):
        currentTime = ""
    else:
        currentTime = MANUAL_DATETIME
    # print out for test 
    print("Current(UTC) " +sys.argv[1] +" "+ sys.argv[2] +" "+ sys.argv[3] +" "+ sys.argv[4] +" "+ sys.argv[5] +" "+ sys.argv[6] # test code 
    print("Epoch (UTC )" + MANUAL_DATETIME) # test code 
    
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

if len(sys.argv)>=6: # for user input handling 
    # change input time to seconds 
    time1 = getTime(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
    print(time1) # test seconds
    stringF = getCode(time1)
    print(stringF)
else:
    print("Incorrect input")
    print("python3 " + sys.argv[0] + "YYYY MM DD HH mm SS")