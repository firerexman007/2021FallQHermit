################################################################
#Group: Hermit 
#Names: Matthew Tucker, Siva Karuturi, Colby Boyd, Cori Allbritton, Varat Chaichamnarn, Thien Vu
#Desc: 
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


from ftplib import FTP

# FTP server details
IP = "138.47.102.120"
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
	print(f)