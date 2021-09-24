# Matthew T  9/23/2021
# This code gets input from user in multiple ways 
#



#imports 
import sys

#global 
inputs = []
output = [] 
alp1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
alp2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#functions
def decryp(L:list, key):
    for word in inputs:
        for char in word:
            print(char)
            # will need to finish

def encryp(L:list, key):
    pass 

#code
if len(sys.argv)>3: # for fill handling
    pass
elif len(sys.argv)>2: # for user input 
    
    #get system
    Etype = sys.argv[1]
    Key = sys.argv[2]
    
    #get user input 
    for line in sys.stdin:
        inputs.append(line)
    
    print("^D") #ctrl+D

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
