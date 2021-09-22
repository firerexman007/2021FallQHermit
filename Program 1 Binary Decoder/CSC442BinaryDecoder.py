#Group: Hermit sub-team A
#Names: Cori Allbritton, Varat Chaichamnarn, Thien Vu 
#Desc: Decodes binary into 7-bit or 8-bit ASCII and prints it
#Date: 9-21-2021
import fileinput

#detects whether its the ASCII is in 7bit or 8bit
def detectorASCII(binaryASCII):
    if (len(binaryASCII) % 7 == 0 and len(binaryASCII) % 8 == 0):
        #put Varat's code here
        print("7and8")
    elif(len(binaryASCII) % 7 == 0):
        #put Varat's code here
        print("7")
    elif(len(binaryASCII) % 8 == 0):
        #put Varat's code here
        print("8")
    else:
        print("Does not match 7-bit or 8-bit ASCII values, aborting.")

#testing part
binaryASCII = ""
#file will be input like "CSC442BinaryDecoder.py < [some file]"
for line in fileinput.input():
    binaryASCII += line.rstrip()
print(binaryASCII)
print(len(binaryASCII))
detectorASCII(binaryASCII)
