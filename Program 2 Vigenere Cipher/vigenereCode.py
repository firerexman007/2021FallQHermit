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
import re

########### global Variables 
inputs = [] # all input list
transition = []
output = [] # all output list 
# two alpabet for lower and upper case 
alphaList = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

########### functions
def change(inputs, formattedKey):
    count2 = 0
    alphaKey = ""
    returnL = []
    for word in inputs:
        temp = [] 
        transition2 = ""
        for char in word:
            if char.isalpha():
                alphaKey = formattedKey[count2 % len(formattedKey)]
                temp.append(alphaKey)
                count2 +=1
            else:
                temp.append(char)
        transition2 += (''.join(temp))
        returnL.append(transition2)
    return returnL

def decryp(inputs, formattedKey):
    empty = [] 
    word = ""
    transition= change(inputs, formattedKey)
    for w in range(len(inputs)):
        word = inputs[w]
        cipherText =""
        for j in range(len(word)):
            currentletter = word[j]
            if currentletter.isalpha():
                ciphercharindex = (26 + (alphaList.index(word[j].upper()) - alphaList.index(transition[j].upper()))) % 26
                cipherText += alphaList[ciphercharindex].upper() if word[j].isupper() else alphaList[ciphercharindex].lower()
            else:
                cipherText += word[j] 
        empty.append(cipherText)
    return empty
    
    
        

def encryp(L:list, key):
    pass 

###########Start of Program
if len(sys.argv)>3: # for fill handling
    pass
elif len(sys.argv)>2: # for user input handling
    if(sys.argv[1] != "-e" and sys.argv[1] != "-d"):
        print(sys.argv[1])
        print("Please -e for Encryption and -d for Decryption mode")
        exit(0)
    #get system variables 
    mode = sys.argv[1] # this is the type
    Key = sys.argv[2] # this is the key
    formattedKey = "".join(re.split("[^a-zA-Z]*", sys.argv[2]))
    
    #get user input (LOOP TILL Ctrl+D)
    for line in sys.stdin: 
        inputs.append(line)
    
    print("^D") #ctrl+D print out 

    # call functions 
    if(mode == "-e"):
        output = encryp(inputs,formattedKey)
    elif(mode == "-d"):
        output = decryp(inputs,formattedKey)
    
    # print output
    for x in output:
        print(x)
else: # invalid system
    print("INVALID CALL")
    print("python3 " + sys.argv[0] + "-e KEY")
