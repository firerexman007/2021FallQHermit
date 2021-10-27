from sys import stdin, stdout

key = bytearray(open("key","rb").read())
#print(key)
message=bytearray(stdin.buffer.read())
for i in range(0,len(message)):
    temp=bytes([message[i]^key[i%len(key)]])
    stdout.buffer.write(temp)
