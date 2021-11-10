#import stuff
from pynput.keyboard import Controller
from time import sleep
from random import uniform
from termios import tcflush, TCIFLUSH
from sys import stdout
import sys 


if(len(sys.argv)>1):
    if(sys.argv[1] == "h" or sys.argv[1] == "help"):
        print("Python3 "+ sys.argv[0] + " > [OUTPUT FILE]")
        print("Will need to change fetures and timings")
        exit(0)
sleep(6)
#reads timing, in this case input is a file
password = ['A', 'r', 'e', ' ', 'y', 'o', 'u', ' ', 'f', 'r', 'u', 's', 't', 'r', 'a', 't', 'e', 'd', ' ', 'o', 'r', ' ', 'e', 'x', 'c', 'i', 't', 'e', 'd', '?', 'Ar', 're', 'e ', ' y', 'yo', 'ou', 'u ', ' f', 'fr', 'ru', 'us', 'st', 'tr', 'ra', 'at', 'te', 'ed', 'd ', ' o', 'or', 'r ', ' e', 'ex', 'xc', 'ci', 'it', 'te', 'ed', 'd?']







timings = ['0.19', '0.97', '0.51', '0.81', '0.78', '0.78', '0.17', '0.11', '0.75', '0.36', '0.60', '0.21', '0.49', '0.62', '0.34', '0.35', '0.52', '0.92', '0.55', '0.40', '0.92', '0.31', '0.85', '0.13', '0.12', '0.21', '0.99', '0.41', '0.98', '0.56', '0.24', '0.26', '0.31', '0.63', '0.18', '0.10', '0.11', '0.64', '1.00', '0.69', '0.68', '0.75', '0.28', '0.91', '0.71', '0.59', '0.82', '0.68', '0.91', '0.42', '0.49', '0.60', '0.55', '0.13', '0.81', '0.12', '0.95', '0.60', '1.00']



print(f"Features = {password}")
print(f"Timings = {timings}")
#splits the password into a list
#first half of passwordlist + 1 is the actuall password
#the rest can be discarded
password = password[:len(password)// 2 + 1]
#put the password back together
password = "".join(password)
print(f"Sample = \"{password}\"")
#split timings into a list

timings = [ float(a) for a in timings ]
#first half of timings is the timings for holding each key that is preessed down
keypress = timings[:len(timings) // 2 + 1]
#the rest is the timings for intervals
keyinterval = timings[len(timings) // 2 + 1:]
print(f"KHTS = {keypress}")
print(f"KITs = {keyinterval}")
#setup input
keyboard = Controller()

#presses each char in password 
#for its corresponding key hold timing
#then releases and waits for however
#long its corresponding key interval timing
for i in range(len(password)):
    keyboard.press(password[i])
    sleep(keypress[i])
    keyboard.release(password[i])
    if i < len(password) - 1:
        sleep(keyinterval[i])
keyboard.press('enter')
