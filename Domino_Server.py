## Domino Game _ Server
## Produced By Sepehr Bazyar
## Class 3/7

import socket
import random

def SEND_NUM(i):
	conn.sendall(str(i).encode('ascii'))

def SEND_LIST(Array):
    string = ""
    for i in range(len(Array)):
        for j in range(len(Array[i])):
            string += str(Array[i][j])
    SEND_NUM(string)

Array = [[] for i in range(28)]
for i in range(len(Array)):
    Array[i].append(random.randint(0, 6))
    Array[i].append(random.randint(0, 6))
    Array[i].sort()
    if(Array.count(Array[i])>1):
        f = 0
        while(f==0):

            Array[i][0] = random.randint(0, 6)
            Array[i][1] = random.randint(0, 6)
            Array[i].sort()
            if(Array.count(Array[i])==1):
                f = 1
Player1 = Array[:(len(Array))//2]
Player2 = Array[(len(Array))//2:]
Player1.insert(0, "96")
Player2.insert(0, "96")

o = []
f = 1
if(Player1.count([6, 6])==1):
    f = 1
    Player1.remove([6, 6])
    o.append([6, 6])
elif(Player2.count([6, 6])==1):
    f = 0
    Player2.remove([6, 6])
    o.append([6, 6])

host = ''
port = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(2)

c = 1
while True:
        conn, addr = s.accept()
        SEND_NUM(c)
        data = conn.recv(1024)
        c += 1
        SEND_LIST(Player1)
        data = conn.recv(1024)
        SEND_LIST(Player2)
        data = conn.recv(1024)
        SEND_NUM(f)

        conn.close()
