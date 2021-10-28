################################################################
#Group: Hermit 
#Names: Matthew Tucker,Thien, Colby
#Desc: 
#Date: 10/25/2021
################################################################
#Division of labor:
#Matthew: input/output system, help system
#Thien: 
#Colby: Byte retrieval
# All members worked together and help when others struggled

#import 
import sys
import re
sentinel = bytearray(b'\x00\xff\x00\x00\xff\x00')

## functions 
def bitRetrieve(Pwrap, sentinel, PoffS, Pinte):
    #read file as byte array
    wrapFile = open(Pwrap, "rb")
    wrapBytes = bytearray(wrapFile.read())
    wrapFile.close()
    #make empty bytearray to put hidden bytes in
    hiddenBytes = bytearray()

    while PoffS < len(wrapBytes):
        #hidden byte to be constructed
        b = 0
        for i in range(8):
            #get least significan bit of current byte
            b |= (wrapBytes[PoffS] & 0o0000001)
            if i < 7:
                # bitshift byte by one and prevent overflow
                b = (b << 1) & (2 ** 8 - 1)
                #move to next byte
                PoffS += Pinte
        #turn into an actual byte
        b = b.to_bytes(1, 'big')
        #add to byte array
        hiddenBytes += b
        #if sentinel is detected, stop
        if hiddenBytes[len(hiddenBytes) - len(sentinel):] == sentinel:
            break
        PoffS += Pinte
    #output
    sys.stdout.buffer.write(hiddenBytes)
    
 #function for byte retrieval
def byteRetrieve(Pwrap, sentinel, PoffS, Pinte):
    #read wrapper bytees
    wrapFile = open(Pwrap, "rb")
    wrapBytes = bytearray(wrapFile.read())
    wrapFile.close()
    #empty byte array
    hiddenBytes = bytearray()

    #while loop for hidden byte
    while PoffS < len(wrapBytes):
        b = wrapBytes[PoffS]
        #turn into an actual byte
        b = b.to_bytes(1, 'big')
        #add to byte array 
        hiddenBytes += b
        #if sentinel is detected, stop
        if hiddenBytes[len(hiddenBytes) - len(sentinel):] == sentinel:
            break
        #offset += interval
        PoffS += Pinte 
    #output
    sys.stdout.buffer.write(hiddenBytes)

def byteStorage(Pwrap, Phidd, sentinel, Poffs, Pinte):
    # read files as byte arrays
    wrapFile = open(Pwrap, "rb")
    wrapBytes = bytearray(wrapFile.read())
    wrapFile.close()
    hiddenFile = open(Phidd, "rb")
    hiddenBytes = bytearray(hiddenFile.read())
    hiddenFile.close()
    i = 0
    n = 0
    # store hidden bytes in wrap file
    while(i < len(hiddenBytes)):
        wrapBytes[Poffs] = hiddenBytes[Pinte]
        Poffs += Pinte
        i += 1
    # add sentinel bytes
    while n < len(sentinel):
        wrapBytes[Poffs] = sentinel[n]
        Poffs += Pinte
        n += 1
    # output
    sys.stdout.buffer.write(wrapBytes)

###### Start of Code 
## help mode
if(len(sys.argv)>1):
    if(sys.argv[1] == "h" or sys.argv[1] == "help"):
        print("Python3 "+ sys.argv[0] + " -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]")
        print("-s       store")
        print("-r       retrieve")
        print("-b       bit mode")
        print("-B       byte mode")
        print("-o<val>  set offset to <val> (defualt is 0)")
        print("-i<val>  set interval to <val> (defualt is 1)")
        print("-w<vak>  set wrapper file to <val>")
        print("-h<val>  set hiddent file to <val>")
        exit(0)

## main mode (get/org inputs) 
if len(sys.argv)>4: # see if have min inputs needed
    Pwrap ="" # is here for future needs   
    if(sys.argv[1] == "-s" or sys.argv[1] == "-r"): # if there
        Pmode = sys.argv[1][1:]
    else: # else error control 
        print("Please use -s for Store and -r for Retrieve mode")
        exit(0)
    if(sys.argv[2] == "-b" or sys.argv[2] == "-B"): # if there
        Ptype = sys.argv[2][1:]
    else: # else error control
        print("Please use -b for bit and -B for byte mode")
        exit(0)
    if(sys.argv[3][0:2] == "-o"): # if there 
        PoffS = sys.argv[3][2:]
        if(PoffS ==""): # if there but no val
            PoffS = "0"
    else: # else error control
        print("Please use -o<val> set offset to <val> (defualt is 0)")
        exit(0)
    if(sys.argv[4][0:2] == "-i"): # if there 
        Pinte = sys.argv[4][2:] 
        if(Pinte == ""): # if there but no val
           Pinte = "1"
    elif(sys.argv[4][0:2] == "-w"): # if not there 1 , if there 2
           Pwrap = sys.argv[4][2:]
           Pinte ="1"
    else: # else error control
        print("Please use -i<val> set interval to <val> (defualt is 1)")
        print("OR -w<val> set wrapper file to <val>")
        exit(0)
    if(len(sys.argv)>5): # if there are more inputs
        if(Pwrap == sys.argv[4][2:]): # if Pwrap has been made
            if(sys.argv[5][0:2] == "-h"): # if there 
                Phidd = sys.argv[5][2:]
            else: # default
                Phidd = ""
        else: # if not done
            if(sys.argv[5][0:2] == "-w"): # if there 
                Pwrap = sys.argv[5][2:] 
            else: # else error control
                print("Please use -w<val> set wrapper file to <val>")
                exit(0)
            if(len(sys.argv)>6): # if more inputs 
                if(sys.argv[6][0:2] == "-h"): # if there 
                    Phidd = sys.argv[6][2:]
                else: # default
                    Phidd = ""
            else: # else if no more inputs 
                Phidd = ""   
    else:
         Phidd =""   
    #change strings into int as needed 
    PoffS = int(PoffS)
    Pinte = int(Pinte)
    #test input system
    """
    print(f"Mode = {Pmode}")
    print(f"Type = {Ptype}") 
    print(f"OffS = {PoffS}") 
    print(f"Inte = {Pinte}") 
    print(f"Wrap = {Pwrap}") 
    print(f"Hidd = {Phidd}") 
    """
else: # invalid system not enough inputs 
    print("INVALID Input:")
    print("Python3 "+ sys.argv[0] + " -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]")
    print("Need help run:")
    print("Python3 "+ sys.argv[0] + " h")
    exit(0)

#The rest of the code with inputs
#all combinations of modes
if (sys.argv[1] == "-s" and sys.argv[2] == "-b"):
    #put bit storage here
    pass
if (sys.argv[1] == "-r" and sys.argv[2] == "-b"):
    print("ruh")
    bitRetrieve(Pwrap, sentinel, PoffS, Pinte)
if (sys.argv[1] == "-s" and sys.argv[2] == "-B"):
    #put byte storage here
    print("bruh")
    byteStorage(Pwrap, Phidd, sentinel, PoffS, Pinte)
if (sys.argv[1] == "-r" and sys.argv[2] == "-B"):
    #put byte retrieval here
    pass
