################################################################
#Group: Hermit 
#Names: Siva Karuturi, Varat Chaichamnarn, Colby Boyd
#Desc: Take the contents of one file and encncrypt it with the contents of another file and store it in a file
#Date: 10/27/2021
################################################################
#Division of labor:
#Siva: Handling all the code
#Varat: Testing 
#Colby: Testing and upload
# All members worked together and help when others strugled

#import stdin and stdout
from sys import stdin, stdout
import sys


#HELP FUNCTION
if(len(sys.argv)>1):
    if(sys.argv[1] == "h" or sys.argv[1] == "help"):
        print("Python3 "+ sys.argv[0] + " < [INPUT FILE] > [OUTPUT FILE]")
        exit(0)

#read key file as byte arrays
key = bytearray(open("key","rb").read())

#print(key)

#read message file as byte arrays
message=bytearray(stdin.buffer.read())



#Xor betwwen two files
for i in range(0,len(message)):

    temp=bytes([message[i]^key[i%len(key)]])
    
    #output the result in a file
    stdout.buffer.write(temp)
