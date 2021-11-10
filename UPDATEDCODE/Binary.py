################################################################
#Group: Hermit sub-team A
#Names: Cori Allbritton, Varat Chaichamnarn, Thien Vu
#Desc: Decodes binary into 7-bit or 8-bit ASCII and prints it
#Date: 9-21-2021
################################################################
#Division of labor:
#Cori: File merging
#Varat: Decoding ASCII and writeup
#Thien: Differentiation of 7-bit and 8-bit ASCII
#Wheel of names when done: Writeup

import fileinput
import sys

#detects whether its the ASCII is in 7bit or 8bit
def detectorASCII(binaryASCII):
    finalStr = ""
    if(len(binaryASCII) % 7 == 0):
        print("7-Bit Conversion")

        # slicing the input and converting it
        # in decimal and then converting it in string
        for i in range(0, len(binaryASCII), 7):

            # slicing the bin_data from index range [0, 6]
            # and storing it as integer in temp_data
            temp_data = int(binaryASCII[i:i + 7])

            if (temp_data == 1000):
                finalStr = finalStr.rstrip(finalStr[-1])

            else:
                # passing temp_data in BinarytoDecimal() function
                # to get decimal value of corresponding temp_data
                decimal_data = BinaryToDecimal(temp_data)

                # Deccoding the decimal value returned by
                # BinarytoDecimal() function, using chr()
                # function which return the string corresponding
                # character for given ASCII value, and store it
                # in str_data
                finalStr = finalStr + chr(decimal_data)
        print(finalStr)

    if(len(binaryASCII) % 8 == 0):
        print("8-Bit Conversion")

        # slicing the input and converting it
        # in decimal and then converting it in string
        for i in range(0, len(binaryASCII), 8):

            # slicing the binaryASCII from index range [0, 7]
            # and storing it as integer in temp_data
            temp_data = int(binaryASCII[i:i + 8])

            if (temp_data == 1000):
                finalStr = finalStr.rstrip(finalStr[-1])

            else:
                # passing temp_data in BinarytoDecimal() function
                # to get decimal value of corresponding temp_data
                decimal_data = BinaryToDecimal(temp_data)

                # Deccoding the decimal value returned by
                # BinarytoDecimal() function, using chr()
                # function which return the string corresponding
                # character for given ASCII value, and store it
                # in str_data
                finalStr = finalStr + chr(decimal_data)
        print(finalStr)

# Defining BinarytoDecimal() function
def BinaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return (decimal)
#testing part
binaryASCII = ""

#HELP FUNCTION
if(len(sys.argv)>1):
    if(sys.argv[1] == "h" or sys.argv[1] == "help"):
        print("Python3 "+ sys.argv[0] + " < [INPUT FILE] > [OUTPUT FILE]")
        exit(0)

#file will be input like "CSC442BinaryDecoder.py < [some file]"
for line in fileinput.input():
    binaryASCII += line.rstrip()
detectorASCII(binaryASCII)
