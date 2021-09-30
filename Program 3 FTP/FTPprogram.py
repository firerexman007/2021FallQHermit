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
METHOD = 7

# FTP server details
IP = "138.47.157.5"
PORT = 21
USER = "anonymous"
PASSWORD = ""
FOLDER = "/7/"
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

# new list made up of just the permissions from the files to be used if needed
permissions = []
for f in files:
    permissions.append(f[:10])

# code for extracting the message using the 7 bit method
if METHOD == 7:
    print("This is the 7 bit method")


# code for extracting the message using the 10 bit method
if METHOD == "10-bit":
    print("This is the 10 bit method")
