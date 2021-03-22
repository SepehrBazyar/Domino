## Domino Game _ Clinet
## Produced By Sepehr Bazyar
## Class 3/7

import socket, pygame as PG, random

def LIST(String):
    lst = list(String)
    l = len(lst) - 1
    Array = []
    i = 0
    while(i<l):
        Array.append([int(lst[i]), int(lst[i+1])])
        i += 2
    return Array

def Find(Array, value):
    f = 1
    for i in range(len(Array)):
        for j in range(len(Array[i])):
            if(Array[i][j] == value):
                f = 0
    if(f == 0):
        return True
    return False

def Plus(Array):
    c = 0
    for i in range(len(Array)):
        for j in range(len(Array[i])):
            c += Array[i][j]
    return c

def Msg(mes, color, wid, hig, font):
    txt1 = font.render(mes, True, color)
    SC.blit(txt1, [wid, hig])

def checkQuit():
    event = PG.event.poll()
    if event.type == PG.QUIT:
        PG.quit()
        
def ID(i, x, y):
    if(i==0):
        SC.blit(zero, (x, y))
    elif(i==1):
        SC.blit(one, (x, y))
    elif(i==2):
        SC.blit(two, (x, y))
    elif(i==3):
        SC.blit(three, (x, y))
    elif(i==4):
        SC.blit(four, (x, y))
    elif(i==5):
        SC.blit(five, (x, y))
    elif(i==6):
        SC.blit(six, (x, y))

W = 800 
H = 600

PG.init()
SC = PG.display.set_mode((W, H))
PG.display.set_caption(" Domino Game ! ")
PG.display.set_icon(PG.image.load("Pictures\\Icon.jpg"))

font = PG.font.Font("Fonts\\LEELAWDB.TTF", 25)

RED = [255, 0, 0, 255]
GREEN = [0, 255, 0, 255]
BLUE = [0, 0, 255, 255]
WHITE = [255, 255, 255, 255]
BLACK = [0, 0, 0, 255]

done = False
while not done:
    for event in PG.event.get():
        if event.type == PG.KEYDOWN:
            if event.key == PG.K_ESCAPE:
                PG.quit()

    pic = PG.image.load("Pictures\\Domino.jpg")
    pic = PG.transform.scale(pic, (W, H))
    SC.blit(pic, (0, 0))
    Msg( " Play ", WHITE, W/2-25, H/2-115 , font)
    Msg( " About Me ", WHITE, W/2-55, H/2-10 , font)
    Msg( " More Game ", WHITE, W/2-65, H/2+105 , font)
    Msg( " Quit ", WHITE, W/2-30, H/2+220 , font)

    e = PG.event.get()
    
    ( a, b, c ) = PG.mouse.get_pressed()
    if( a > 0 ):
        x, y = PG.mouse.get_pos()

        checkQuit()
        
        if( W/2-50 < x < W/2+80 and H/2-125 < y < H/2-75 ):
           Msg( " Play ", BLACK, W/2-25, H/2-115 , font)
           PG.display.update()
           done = True
           break
            
        
        elif( W/2-50 < x < W/2+75 and H/2-15 < y < H/2+35 ):
            Msg( " About Me ", BLACK, W/2-55, H/2-10 , font)
            PG.display.update()
            pic = PG.image.load("Pictures\\Domino_2.jpg")
            pic = PG.transform.scale(pic, (W, H))
            SC.blit(pic, (0, 0))
            Msg( " Produced By Sepehr Bazyar , Class 3/7 ", WHITE, W/2 - 225, H/2-50, font)
            Msg( " And  thanks  to  Mr . Ghodsi ", WHITE, W/2 - 170, H/2+20, font)
            SC.blit(PG.image.load("Pictures\\ME.png"), (W/2 - 50, H/2 + 100 ))
            PG.display.update()
            i = 0
            while(i<5000000):
                i+=1
                checkQuit()

        elif( W/2-65 < x < W/2-15 and H/2+95 < y < H/2+245 ):
            Msg( " More Game ", BLACK, W/2-65, H/2+105 , font)
            PG.display.update()
            pic = PG.image.load("Pictures\\Domino_2.jpg")
            pic = PG.transform.scale(pic, (W, H))
            SC.blit(pic, (0, 0))
            Msg( " http://bit.ly/1LKptZy ", WHITE, W/2-137, H/2-50, font)
            Msg( " Password : 3Pehr_B@zyR ", WHITE, W/2-150, H/2, font)
            SC.blit(PG.image.load("More Game\\Snake.png"), (W/2 - 50, H/2 + 50 ))
            PG.display.update()
            i = 0
            while(i<10000000):
                i+=1
                checkQuit()

        elif( W/2-40 < x < W/2+60 and H/2+210 < y < H/2+260 ):
            Msg( " Quit ", BLACK, W/2-30, H/2+220 , font)
            PG.display.update()
            PG.quit()

    PG.display.update()
    checkQuit()

host = socket.gethostname()
port = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
   
c = int(s.recv(1024))
s.sendall(b'START')
P1 = s.recv(1024)
s.sendall(b'OK')
P2 = s.recv(1024)
s.sendall(b'END')
f = int(s.recv(1024))

Player1 = LIST(str(int(P1)))
Player2 = LIST(str(int(P2)))
Player1.pop(0)
Player2.pop(0)

if(c % 2 == 1):
    l = len(Player2)
    Player2 = [[0, 0]] * l
elif(c % 2 == 0):
    l = len(Player1)
    Player1 = [[0, 0]] * l

s.close()

pic = PG.image.load("Pictures\\Background.jpg")
pic = PG.transform.scale(pic, (W, H))
user1 = PG.image.load("Pictures\\User_1.png")
user1 = PG.transform.scale(user1, (50, 50))
SC.blit(user1, (0, 0))
user2 = PG.image.load("Pictures\\User_2.png")
user2 = PG.transform.scale(user2, (50, 50))
SC.blit(user2, (0, 550))
off = PG.image.load("Pictures\\Off.png")
on = PG.image.load("Pictures\\On.png")

zero = PG.image.load("Pictures\\Zero.jpg")
one = PG.image.load("Pictures\\One.jpg")
two = PG.image.load("Pictures\\Two.jpg")
three = PG.image.load("Pictures\\Three.jpg")
four = PG.image.load("Pictures\\Four.jpg")
five = PG.image.load("Pictures\\Five.jpg")
six = PG.image.load("Pictures\\Six.jpg")

done = False
while not done :

    checkQuit()

    for event in PG.event.get():
        if event.type == PG.KEYDOWN:
            if event.key == PG.K_ESCAPE:
                PG.quit()
                
    SC.blit(pic, (0, 0))
    SC.blit(user1, (0, 0))
    SC.blit(user2, (0, 550))
    SC.blit(off, (700, 0))
    SC.blit(off, (700, 550))

    SC.blit(six, (W/2, H/2 - 12.5))
    SC.blit(six, (W/2 - 35, H/2 - 12.5))

    checkQuit()

    c = 61.75
    k = 0
    for i in range (len(Player1)):
        for j in range(len(Player1[i])):
            ID(Player1[i][j], c, k)
            k += 25
        k = 0
        c += 45

    c = 61.75
    k = 550
    for i in range (len(Player2)):
        for j in range(len(Player2[i])):
            ID(Player2[i][j], c, k)
            k += 25
        k = 550
        c += 45

    if(f==1):
        SC.blit(on, (700, 550))
            
    elif(f==0):
        SC.blit(on, (700, 0))      

    PG.display.update()

    checkQuit()
