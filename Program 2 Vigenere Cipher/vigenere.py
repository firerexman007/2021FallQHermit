import sys
import re
if(len(sys.argv) <3):
    print("Please provide encryption/decryption mode and key")
    exit(0)
elif(sys.argv[1] != "-e" and sys.argv[1] != "-d"):
    print(sys.argv[1])
    print("Please -e for Encryption and -d for Decryption mode")
    exit(0)
alphaList = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mode = sys.argv[1]
key = sys.argv[2]
formattedKey = "".join(re.split("[^a-zA-Z]*", sys.argv[2]))
plainText = input("Enter your message:")
alphaKey = ""
count1=0
count2=0

while(count1 < len(plainText)):
    if plainText[count1].isalpha():
        alphaKey += formattedKey[count2 % len(formattedKey)]
        count2 += 1
    else:
        alphaKey += plainText[count1]
    count1+=1

def todocipher(mode):
    cipherText = ""
    for j in range(len(plainText)):
        currentletter = plainText[j]
        if currentletter.isalpha():
            if mode == '-e':
                ciphercharindex = (alphaList.index(plainText[j].upper()) + alphaList.index(alphaKey[j].upper())) % 26
                cipherText += alphaList[ciphercharindex].upper() if plainText[j].isupper() else alphaList[
                    ciphercharindex].lower()
            else:
                ciphercharindex = (26 + (
                        alphaList.index(plainText[j].upper()) - alphaList.index(alphaKey[j].upper()))) % 26
                cipherText += alphaList[ciphercharindex].upper() if plainText[j].isupper() else alphaList[
                    ciphercharindex].lower()
        else:
            cipherText += plainText[j]
    print(cipherText)
    
todocipher(mode)
