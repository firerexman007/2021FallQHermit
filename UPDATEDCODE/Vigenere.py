################################################################
#Group: Hermit sub-team B
#Names: Matthew Tucker, Siva, Colby 
#Desc: to encode or decode strings and output it
#Date: 9-24-2021
################################################################
#Division of labor:
#Matthew: Input/output system
#Siva: Decryption and Encryption
#Colby: Logic/orginization 
# All members worked together and help when others strugled
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
def change(inputs, formattedKey): # This function changes to what key is 
    returnL = []
    for word in inputs:
        count2 = 0
        alphaKey = ""
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
    return returnL # Returns list of each input 

def decryp(inputs, formattedKey): # does decryptions 
    doutput = [] # output list for this group
    word = "" 
    transition= change(inputs, formattedKey) # change to key
    for w in range(len(inputs)): # loop through inputs
        word = inputs[w] # each input is word
        currentTransition=transition[w] # each transition is currentTransition
        cipherText =""
        for j in range(len(word)): # loop through letters in word and decryp
            if word[j].isalpha():
                #CURRENT ERROR IS HERE FIX PLEASE 
                ciphercharindex = (26 + (alphaList.index(word[j].upper()) - alphaList.index(currentTransition[j].upper()))) % 26
                cipherText += alphaList[ciphercharindex].upper() if word[j].isupper() else alphaList[ciphercharindex].lower()
            else:
                cipherText += word[j] 
        doutput.append(cipherText)
    return doutput
    
    
        

def encryp(L:list, key):
    eoutput = [] # output list for this group
    word = "" 
    transition= change(inputs, formattedKey) # change to key
    for w in range(len(inputs)): # loop through inputs
        word = inputs[w] # each input is word
        currentTransition=transition[w] # each transition is currentTransition
        cipherText =""
        for j in range(len(word)): # loop through letters in word and decryp
            if word[j].isalpha():
                ciphercharindex = (alphaList.index(word[j].upper()) + alphaList.index(currentTransition[j].upper())) % 26
                cipherText += alphaList[ciphercharindex].upper() if word[j].isupper() else alphaList[ciphercharindex].lower()
            else:
                cipherText += word[j] 
        eoutput.append(cipherText)
    return eoutput 

###########Start of Program

if len(sys.argv)>1:
    if(sys.argv[1] == "h" or sys.argv[1] == "help"):
        print("python3 " + sys.argv[0] + " -(ed) KEY < [INPUT FILE] > [OUTPUT FILE]")
        print("OR")
        print("python3 " + sys.argv[0] + " -(ed) (input).txt > [OUTPUT File]")
        print("-e for Encrypting and - d for Decryption")        
        exit(0)
if len(sys.argv)>2: # for user input handling
    if(sys.argv[1] != "-e" and sys.argv[1] != "-d"):
        print(sys.argv[1])
        print("Please -e for Encryption and -d for Decryption mode")
        exit(0)
    if(sys.argv[2][-4:] != ".txt"):
        #get system variables 
        mode = sys.argv[1] # this is the type
        Key = sys.argv[2] # this is the key
        formattedKey = "".join(re.split("[^a-zA-Z]*", sys.argv[2]))
        
        
        #get user input (LOOP TILL Ctrl+D)
        for line in sys.stdin: 
            inputs.append(line)

        # determin if out or input from file if so no ^D
        if sys.stdout.isatty():
            if sys.stdin.isatty():
                print("^D") #ctrl+D print out 
          
        # call functions 
        if(mode == "-e"):
            output = encryp(inputs,formattedKey)
        elif(mode == "-d"):
            output = decryp(inputs,formattedKey)
        
        # print output
        for x in output:
            print(x)
    else:
        with open(sys.argv[2]) as f: # if input 2 is a .txt get first and second line
            lines = f.read()
            key = lines.split('\n', 1)[0]
            inputs.append((lines.split('\n', 1)[1]))
        #get system variables 
        mode = sys.argv[1] # this is the type
        formattedKey = "".join(re.split("[^a-zA-Z]*", key))
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
