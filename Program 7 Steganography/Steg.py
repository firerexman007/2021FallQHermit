################################################################
#Group: Hermit 
#Names: Matthew Tucker,Thien 
#Desc: 
#Date: 10/25/2021
################################################################
#Division of labor:
#Matthew: input/output system 
#Thien: 
# All members worked together and help when others struggled

#import 
import sys
import re


# Start of Code 
# help mode
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

#Check if input is valid 
if len(sys.argv)>6:
    #check each set of input in correc order and there 
    if(sys.argv[1] != "-s" and sys.argv[1] != "-r"):
        print("Please -s for Store and -r for Retrieve mode")
        exit(0)
    if(sys.argv[2] != "-b" and sys.argv[2] != "-B"):
        print("Please -b for bit and -B for byte mode")
        exit(0)
    if(sys.argv[3][0:2] != "-o"):
        print("Please -o<val> set offset to <val> (defualt is 0)")
        exit(0)
    if(sys.argv[4][0:2] != "-i"):
        print("Please -i<val> set interval to <val> (defualt is 1)")
        exit(0)
    if(sys.argv[5][0:2] != "-w"):
        print("Please -w<val> set wrapper file to <val>")
        exit(0)
    if(sys.argv[6][0:2] != "-h"):
        print("Please -h<val> set hiddent file to <val>")
        exit(0)
    Pmode = sys.argv[1][1:]
    Ptype = sys.argv[2][1:]
    PoffS = sys.argv[3][2:]
    Pinte = sys.argv[4][2:]    
    Pwrap = sys.argv[5][2:]
    Phidd = sys.argv[6][2:]
        
    #test input system
    print(f"Mode = {Pmode}")
    print(f"Type = {Ptype}") 
    print(f"OffS = {PoffS}") 
    print(f"Inte = {Pinte}") 
    print(f"Wrap = {Pwrap}") 
    print(f"Hidd = {Phidd}") 

else: # invalid system
    print("INVALID Input:")
    print("Python3 "+ sys.argv[0] + " -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]")
    print("Need help run:")
    print("Python3 "+ sys.argv[0] + " h")
