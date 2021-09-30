#filters out files with a 1 on the first 3 bits
def covertCheck(permBits):
    #checks the first 3 bits for a 1
    for i in range(3):
        #the checking part
        if permBits[i] == "1":
            #not covert
           return False
    #covert
    return True

#testing
#permissions go here
permBits = "1111100000"

#make it true or false or something idk man
covertFile = covertCheck(permBits)
if (covertFile):
    print("File is covert")
else:
    print("File is not covert")
