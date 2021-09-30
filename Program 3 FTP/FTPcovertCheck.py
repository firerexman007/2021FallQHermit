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

#from binary numbers to ASCII to characters
def covertMessage(binary, n):
    text = ""
    i = 0
    while (i < len(binary)):
        #slicing the  binary numbers from index range [0-n]
        bits = binary[i:i+n]
        bits = int(bits, 2)
        #remove last character of string if backspace
        if(bits == 7):
            text = text[:-1]
            i+=n
        else:
            #character for given ASCII value
            text += chr(bits)
            i += n
    return text

#testing
#permissions go here
permBits = "1111100000"

#make it true or false or something idk man
covertFile = covertCheck(permBits)
if (covertFile):
    print("File is covert")
else:
    print("File is not covert")
