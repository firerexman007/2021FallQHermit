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
# get file permistion 

from ftplib import FTP

##### Functions 


##### FTP HANDELER 
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

# display the folder contents
for f in files:
    print(f[0:10]) 

#Decode and print 
