################################################################
#Group: Hermit sub-team B
#Names: Matthew Tucker, Siva, Colby 
#Desc: to encode or decode strings and output it
#Date: 9-24-2021
################################################################
#Division of labor:
#Matthew: Input system and logic
#Siva: 
#Colby: 
#Each member adds to Program 2 Info.txt about there part(how it works)


#imports 
import sys

########### global Variables 
inputs = [] # all input list
output = [] # all output list 
# two alpabet for lower and upper case 
alp1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
alp2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

########### functions
def decryp(L:list, key):
    for word in inputs:
        for char in word:
            print(char)
            # will need to finish

def encryp(L:list, key):
    pass 

###########Start of Program
if len(sys.argv)>3: # for fill handling
    pass
elif len(sys.argv)>2: # for user input handling
    
    #get system variables 
    Etype = sys.argv[1] # this is the type
    Key = sys.argv[2] # this is the key
    
    #get user input (LOOP TILL Ctrl+D)
    for line in sys.stdin: 
        inputs.append(line)
    
    print("^D") #ctrl+D print out 

    # call functions 
    if(Etype == "-e"):
        encryp(inputs,Key)
    elif(Etype == "-d"):
        decryp(inputs,Key)
    
    # print output
    for x in output:
        print(x)
else: # invalid system
    print("INVALID CALL")
    print("python3 " + sys.argv[0] + "-e KEY")
