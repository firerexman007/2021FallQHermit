################################################################
#Group: Hermit 
#Names: Matthew Tucker, Siva Karuturi, Colby Boyd, Cori Allbritton, Varat Chaichamnarn, Thien Vu
#Desc: FTP storage gathering permistions and converting the covert message to regualr text
#Date: 9-29-2021
################################################################
#Division of labor:
#Matthew: 
#Siva: 
#Colby: 
#Cori:
#Varat:
#Thien: 
# All members worked together and help when others strugled

## Need: 
# 7-bit function  
# 10-bit function 
# convert - and letters to 0 and 1 
# get file permissions 

# imports
from ftplib import FTP

# variable to determine whether to use a 7-bit or 10-bit method
METHOD = 10

# FTP server details
IP = "138.47.157.5"
PORT = 21
USER = "anonymous"
PASSWORD = ""
FOLDER = "/10/"
USE_PASSIVE = True # set to False if the connection times out

# connect and login to the FTP server
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

# navigate to the specified directory and list files
ftp.cwd(FOLDER)
files = []
ftp.dir(files.append)

# exit the FTP server
ftp.quit()


# functions 
#from binary numbers to ASCII to characters
def covertMessage(binary):
    text = ""
    i = 0
    while (i < len(binary)):
        #slices binary from 0 to 7
        bits = binary[i:i+7]
        bits = int(bits, 2)
        #remove last character of string if backspace
        if(bits == 7):
            text = text[:-1]
            i+=n
        else:
            #character for given ASCII value
            text += chr(bits)
            i += 7
    return text


# new list made up of just the permissions from the files to be used if needed
permissions = []
for f in files:
    permissions.append(f[:10])


# code for extracting the message using the 7 bit method
if METHOD == 7:
    #empty binary 7
    binary7 = ""
    value = []
    # remove 3 spaces at begining turning 10 to 7 bits
    for rows in permissions: 
        if(rows[0:3] == "---"):
            value.append(rows[3:10])
    # convert to binary     
    i = 0 
    while(i<len(value)):
        j=0
        while(j<len(value[i])):
            if(value[i][j]=="-"):
                binary7 += "0"
            else:
                binary7 += "1"
            j+=1
        i+=1
    
    textF7 = covertMessage(binary7)
    print(textF7)
    

# code for extracting the message using the 10 bit method
if METHOD == 10:
    #empty binary 10
    binary10 = ""
    value = []
    for rows in permissions: 
        value.append(rows[0:10])
    # convert to binary     
    i = 0 
    
    while(i<len(value)):
        j=0
        while(j<len(value[i])):
            if(value[i][j]=="-"):
                binary10 += "0"
            else:
                binary10 += "1"
            j+=1
        i+=1

    textF10 = covertMessage(binary10)
    print(textF10)
