## Domino Game
## Produced By Sepehr Bazyar
## Class 3/7

import pygame as PG, random

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

    h = o.index([6, 6])+1
    copy = o[h:]
    for i in range(len(copy)):
        if(i == 0):
            ID(copy[i][0], 440, 287.5)
            ID(copy[i][1], 475, 287.5)
        elif(i == 1):
            ID(copy[i][0], 515, 287.5)
            ID(copy[i][1], 550, 287.5)
        elif(i == 2):
            ID(copy[i][0], 590, 287.5)
            ID(copy[i][1], 625, 287.5)
        elif(i == 3):
            ID(copy[i][0], 665, 287.5)
            ID(copy[i][1], 700, 287.5)
        elif(i == 4):
            ID(copy[i][0], 740, 287.5)
            ID(copy[i][1], 740, 312.5)
        elif(i == 5):
            ID(copy[i][1], 705, 342.5)
            ID(copy[i][0], 740, 342.5)
        elif(i == 6):
            ID(copy[i][1], 630, 342.5)
            ID(copy[i][0], 665, 342.5)
        elif(i == 7):
            ID(copy[i][1], 555, 342.5)
            ID(copy[i][0], 590, 342.5)
        elif(i == 8):
            ID(copy[i][1], 480, 342.5)
            ID(copy[i][0], 515, 342.5)
        elif(i == 9):
            ID(copy[i][1], 405, 342.5)
            ID(copy[i][0], 440, 342.5)
        elif(i == 10):
            ID(copy[i][1], 330, 342.5)
            ID(copy[i][0], 365, 342.5)
        elif(i == 11):
            ID(copy[i][1], 255, 342.5)
            ID(copy[i][0], 290, 342.5)
        elif(i == 12):
            ID(copy[i][1], 180, 342.5)
            ID(copy[i][0], 215, 342.5)
        elif(i == 13):
            ID(copy[i][1], 105, 342.5)
            ID(copy[i][0], 140, 342.5)
        elif(i == 14):
            ID(copy[i][0], 65, 342.5)
            ID(copy[i][1], 65, 367.5)
        elif(i == 15):
            ID(copy[i][0], 65, 397.5)
            ID(copy[i][1], 100, 397.5)
        elif(i == 16):
            ID(copy[i][0], 140, 397.5)
            ID(copy[i][1], 175, 397.5)
        elif(i == 17):
            ID(copy[i][0], 215, 397.5)
            ID(copy[i][1], 250, 397.5)
        elif(i == 18):
            ID(copy[i][0], 290, 397.5)
            ID(copy[i][1], 325, 397.5)
        elif(i == 19):
            ID(copy[i][0], 365, 397.5)
            ID(copy[i][1], 400, 397.5)
        elif(i == 20):
            ID(copy[i][0], 440, 397.5)
            ID(copy[i][1], 475, 397.5)
        elif(i == 21):
            ID(copy[i][0], 515, 397.5)
            ID(copy[i][1], 550, 397.5)
        elif(i == 22):
            ID(copy[i][0], 590, 397.5)
            ID(copy[i][1], 625, 397.5)
        elif(i == 23):
            ID(copy[i][0], 665, 397.5)
            ID(copy[i][1], 700, 397.5)
        elif(i == 24):
            ID(copy[i][1], 740, 397.5)
            ID(copy[i][0], 740, 422.5)
        elif(i == 25):
            ID(copy[i][1], 705, 472.5)
            ID(copy[i][0], 740, 472.5)
        elif(i == 26):
            ID(copy[i][1], 630, 472.5)
            ID(copy[i][0], 665, 472.5)

    checkQuit()

    h = o.index([6, 6])
    copy2 = o[:h]
    l = len(copy2)
    i = l-1
    while(i>=0):
        if(i == l-1):
            ID(copy2[i][0], 290, 287.5)
            ID(copy2[i][1], 325, 287.5)
        elif(i == l-2):
            ID(copy2[i][0], 215, 287.5)
            ID(copy2[i][1], 250, 287.5)
        elif(i == l-3):
            ID(copy2[i][0], 140, 287.5)
            ID(copy2[i][1], 175, 287.5)
        elif(i == l-4):
            ID(copy2[i][0], 65, 287.5)
            ID(copy2[i][1], 100, 287.5)
        elif(i == l-5):
            ID(copy2[i][0], 25, 262.5)
            ID(copy2[i][1], 25, 287.5)
        elif(i == l-6):
            ID(copy2[i][1], 25, 232.5)
            ID(copy2[i][0], 60, 232.5)
        elif(i == l-7):
            ID(copy2[i][1], 100, 232.5)
            ID(copy2[i][0], 135, 232.5)
        elif(i == l-8):
            ID(copy2[i][1], 175, 232.5)
            ID(copy2[i][0], 210, 232.5)
        elif(i == l-9):
            ID(copy2[i][1], 250, 232.5)
            ID(copy2[i][0], 285, 232.5)
        elif(i == l-10):
            ID(copy2[i][1], 325, 232.5)
            ID(copy2[i][0], 360, 232.5)
        elif(i == l-11):
            ID(copy2[i][1], 400, 232.5)
            ID(copy2[i][0], 435, 232.5)
        elif(i == l-12):
            ID(copy2[i][1], 475, 232.5)
            ID(copy2[i][0], 510, 232.5)
        elif(i == l-13):
            ID(copy2[i][1], 550, 232.5)
            ID(copy2[i][0], 585, 232.5)
        elif(i == l-14):
            ID(copy2[i][1], 625, 232.5)
            ID(copy2[i][0], 660, 232.5)
        elif(i == l-15):
            ID(copy2[i][0], 700, 207.5)
            ID(copy2[i][1], 700, 232.5)
        elif(i == l-16):
            ID(copy2[i][0], 665, 177.5)
            ID(copy2[i][1], 700, 177.5)
        elif(i == l-17):
            ID(copy2[i][0], 590, 177.5)
            ID(copy2[i][1], 625, 177.5)
        elif(i == l-18):
            ID(copy2[i][0], 515, 177.5)
            ID(copy2[i][1], 550, 177.5)
        elif(i == l-19):
            ID(copy2[i][0], 440, 177.5)
            ID(copy2[i][1], 475, 177.5)
        elif(i == l-20):
            ID(copy2[i][0], 365, 177.5)
            ID(copy2[i][1], 400, 177.5)
        elif(i == l-21):
            ID(copy2[i][0], 290, 177.5)
            ID(copy2[i][1], 325, 177.5)
        elif(i == l-22):
            ID(copy2[i][0], 215, 177.5)
            ID(copy2[i][1], 250, 177.5)
        elif(i == l-23):
            ID(copy2[i][0], 140, 177.5)
            ID(copy2[i][1], 175, 177.5)
        elif(i == l-24):
            ID(copy2[i][0], 65, 177.5)
            ID(copy2[i][1], 100, 177.5)
        elif(i == l-25):
            ID(copy2[i][0], 25, 152.5)
            ID(copy2[i][1], 25, 177.5)
        elif(i == l-26):
            ID(copy2[i][0], 25, 122.5)
            ID(copy2[i][1], 60, 122.5)
        elif(i == l-27):
            ID(copy2[i][0], 100, 122.5)
            ID(copy2[i][1], 135, 122.5)
        i -= 1

    checkQuit()
    
    c = 61.75
    k = 0
    for i in range (len(Player1)):
        for j in range(len(Player1[i])):
            ID(Player1[i][j], c, k)
            k += 25
        k = 0
        c += 45

    checkQuit()
    
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

    if(f == 0):
        if((Find(Player1, o[0][0]) == False)and(Find(Player1, o[len(o)-1][1]) == False)):
            f = 1

            PG.mixer.init()
            Sound_P = PG.mixer.Sound("Sounds\\Pass.wav")
            Sound_P.play()

        c = 0
        while(f == 0):
            if(c>0):

                PG.mixer.init()
                Sound_E = PG.mixer.Sound("Sounds\\Error.wav")
                Sound_E.play()

            boolian = False
            while not boolian :

                e = PG.event.get()
    
                ( a, b, c ) = PG.mouse.get_pressed()
                if( a > 0 ):
                    x, y = PG.mouse.get_pos()
        
                    if( 61.75 < x < 96.75 and 0 < y < 50 ):
                        n = 1
                        if(n <= len(Player1) ):
                            boolian = True

                    elif( 107.25 < x < 142.25 and 0 < y < 50 ):
                        n = 2
                        if(n <= len(Player1) ):
                            boolian = True

                    elif( 152.75 < x < 187.75 and 0 < y < 50 ):
                        n = 3
                        if(n <= len(Player1) ):
                            boolian = True

                    elif( 198.25 < x < 233.25 and 0 < y < 50 ):
                        n = 4
                        if(n <= len(Player1) ):
                            boolian = True

                    elif( 243.75 < x < 278.75 and 0 < y < 50 ):
                        n = 5
                        if(n <= len(Player1) ):
                            boolian = True

                    elif( 289.25 < x < 324.25 and 0 < y < 50 ):
                        n = 6
                        if(n <= len(Player1) ):
                            boolian = True

                    elif( 334.75 < x < 369.75 and 0 < y < 50 ):
                        n = 7
                        if(n <= len(Player1) ):
                            boolian = True

                    elif( 380.25 < x < 415.25 and 0 < y < 50 ):
                        n = 8
                        if(n <= len(Player1) ):
                            boolian = True

                    elif( 425.75 < x < 460.75 and 0 < y < 50 ):
                        n = 9
                        if(n <= len(Player1) ):
                            boolian = True

                    elif( 471.25 < x < 506.25 and 0 < y < 50 ):
                        n = 10
                        if(n <= len(Player1) ):
                            boolian = True

                    elif( 516.75 < x < 551.75 and 0 < y < 50 ):
                        n = 11
                        if(n <= len(Player1) ):
                            boolian = True

                    elif( 562.25 < x < 597.25 and 0 < y < 50 ):
                        n = 12
                        if(n <= len(Player1) ):
                            boolian = True

                    elif( 607.75 < x < 642.75 and 0 < y < 50 ):
                        n = 13
                        if(n <= len(Player1) ):
                            boolian = True

                    elif( 653.25 < x < 688.25 and 0 < y < 50 ):
                        n = 14
                        if(n <= len(Player1) ):
                            boolian = True
                            
                checkQuit()

            i = 0
            while(i<100000):
                i+=1
                checkQuit()
            
            boolian = False
            while not boolian :

                e = PG.event.get()
    
                ( a, b, c ) = PG.mouse.get_pressed()
                if( a > 0 ):
                    x, y = PG.mouse.get_pos()

                    if(len(copy) < 5 and len(copy2) < 5):
                        if( x < W/2 and 50 < y < 550 ):
                            w = "L"
                            boolian = True

                        elif( x > W/2 and 50 < y < 550 ):
                            w = "R"
                            boolian = True

                    elif(len(copy) >= 5 or len(copy2) >= 5):
                        if( 50 < y < 300 ):
                            w = "L"
                            boolian = True

                        elif( 300 < y < 550 ):
                            w = "R"
                            boolian = True

                checkQuit()
            
            if(w == "L"):
                if(Player1[n-1][0] == o[0][0]):
                    rvs = list(reversed(Player1[n-1]))
                    o.insert(0, rvs)
                    Player1.pop(n-1)
                    f = 1

                    PG.mixer.init()
                    Sound_C = PG.mixer.Sound("Sounds\\Card.wav")
                    Sound_C.play()
                    
                elif(Player1[n-1][1] == o[0][0]):
                    o.insert(0, Player1[n-1])
                    Player1.pop(n-1)
                    f = 1
                    
                    PG.mixer.init()
                    Sound_C = PG.mixer.Sound("Sounds\\Card.wav")
                    Sound_C.play()

            elif(w == "R"):
                if(Player1[n-1][0] == o[len(o)-1][1]):
                    o.insert(len(o), Player1[n-1])
                    Player1.pop(n-1)
                    f = 1

                    PG.mixer.init()
                    Sound_C = PG.mixer.Sound("Sounds\\Card.wav")
                    Sound_C.play()
                    
                elif(Player1[n-1][1] == o[len(o)-1][1]):
                    rvs = list(reversed(Player1[n-1]))
                    o.insert(len(o), rvs)
                    Player1.pop(n-1)
                    f = 1

                    PG.mixer.init()
                    Sound_C = PG.mixer.Sound("Sounds\\Card.wav")
                    Sound_C.play()
                    
            c += 1

        checkQuit()

    SC.blit(pic, (0, 0))
    SC.blit(user1, (0, 0))
    SC.blit(user2, (0, 550))
    SC.blit(off, (700, 0))
    SC.blit(off, (700, 550))

    SC.blit(six, (W/2, H/2 - 12.5))
    SC.blit(six, (W/2 - 35, H/2 - 12.5))

    h = o.index([6, 6])+1
    copy = o[h:]
    for i in range(len(copy)):
        if(i == 0):
            ID(copy[i][0], 440, 287.5)
            ID(copy[i][1], 475, 287.5)
        elif(i == 1):
            ID(copy[i][0], 515, 287.5)
            ID(copy[i][1], 550, 287.5)
        elif(i == 2):
            ID(copy[i][0], 590, 287.5)
            ID(copy[i][1], 625, 287.5)
        elif(i == 3):
            ID(copy[i][0], 665, 287.5)
            ID(copy[i][1], 700, 287.5)
        elif(i == 4):
            ID(copy[i][0], 740, 287.5)
            ID(copy[i][1], 740, 312.5)
        elif(i == 5):
            ID(copy[i][1], 705, 342.5)
            ID(copy[i][0], 740, 342.5)
        elif(i == 6):
            ID(copy[i][1], 630, 342.5)
            ID(copy[i][0], 665, 342.5)
        elif(i == 7):
            ID(copy[i][1], 555, 342.5)
            ID(copy[i][0], 590, 342.5)
        elif(i == 8):
            ID(copy[i][1], 480, 342.5)
            ID(copy[i][0], 515, 342.5)
        elif(i == 9):
            ID(copy[i][1], 405, 342.5)
            ID(copy[i][0], 440, 342.5)
        elif(i == 10):
            ID(copy[i][1], 330, 342.5)
            ID(copy[i][0], 365, 342.5)
        elif(i == 11):
            ID(copy[i][1], 255, 342.5)
            ID(copy[i][0], 290, 342.5)
        elif(i == 12):
            ID(copy[i][1], 180, 342.5)
            ID(copy[i][0], 215, 342.5)
        elif(i == 13):
            ID(copy[i][1], 105, 342.5)
            ID(copy[i][0], 140, 342.5)
        elif(i == 14):
            ID(copy[i][0], 65, 342.5)
            ID(copy[i][1], 65, 367.5)
        elif(i == 15):
            ID(copy[i][0], 65, 397.5)
            ID(copy[i][1], 100, 397.5)
        elif(i == 16):
            ID(copy[i][0], 140, 397.5)
            ID(copy[i][1], 175, 397.5)
        elif(i == 17):
            ID(copy[i][0], 215, 397.5)
            ID(copy[i][1], 250, 397.5)
        elif(i == 18):
            ID(copy[i][0], 290, 397.5)
            ID(copy[i][1], 325, 397.5)
        elif(i == 19):
            ID(copy[i][0], 365, 397.5)
            ID(copy[i][1], 400, 397.5)
        elif(i == 20):
            ID(copy[i][0], 440, 397.5)
            ID(copy[i][1], 475, 397.5)
        elif(i == 21):
            ID(copy[i][0], 515, 397.5)
            ID(copy[i][1], 550, 397.5)
        elif(i == 22):
            ID(copy[i][0], 590, 397.5)
            ID(copy[i][1], 625, 397.5)
        elif(i == 23):
            ID(copy[i][0], 665, 397.5)
            ID(copy[i][1], 700, 397.5)
        elif(i == 24):
            ID(copy[i][1], 740, 397.5)
            ID(copy[i][0], 740, 422.5)
        elif(i == 25):
            ID(copy[i][1], 705, 472.5)
            ID(copy[i][0], 740, 472.5)
        elif(i == 26):
            ID(copy[i][1], 630, 472.5)
            ID(copy[i][0], 665, 472.5)

    checkQuit()

    h = o.index([6, 6])
    copy2 = o[:h]
    l = len(copy2)
    i = l-1
    while(i>=0):
        if(i == l-1):
            ID(copy2[i][0], 290, 287.5)
            ID(copy2[i][1], 325, 287.5)
        elif(i == l-2):
            ID(copy2[i][0], 215, 287.5)
            ID(copy2[i][1], 250, 287.5)
        elif(i == l-3):
            ID(copy2[i][0], 140, 287.5)
            ID(copy2[i][1], 175, 287.5)
        elif(i == l-4):
            ID(copy2[i][0], 65, 287.5)
            ID(copy2[i][1], 100, 287.5)
        elif(i == l-5):
            ID(copy2[i][0], 25, 262.5)
            ID(copy2[i][1], 25, 287.5)
        elif(i == l-6):
            ID(copy2[i][1], 25, 232.5)
            ID(copy2[i][0], 60, 232.5)
        elif(i == l-7):
            ID(copy2[i][1], 100, 232.5)
            ID(copy2[i][0], 135, 232.5)
        elif(i == l-8):
            ID(copy2[i][1], 175, 232.5)
            ID(copy2[i][0], 210, 232.5)
        elif(i == l-9):
            ID(copy2[i][1], 250, 232.5)
            ID(copy2[i][0], 285, 232.5)
        elif(i == l-10):
            ID(copy2[i][1], 325, 232.5)
            ID(copy2[i][0], 360, 232.5)
        elif(i == l-11):
            ID(copy2[i][1], 400, 232.5)
            ID(copy2[i][0], 435, 232.5)
        elif(i == l-12):
            ID(copy2[i][1], 475, 232.5)
            ID(copy2[i][0], 510, 232.5)
        elif(i == l-13):
            ID(copy2[i][1], 550, 232.5)
            ID(copy2[i][0], 585, 232.5)
        elif(i == l-14):
            ID(copy2[i][1], 625, 232.5)
            ID(copy2[i][0], 660, 232.5)
        elif(i == l-15):
            ID(copy2[i][0], 700, 207.5)
            ID(copy2[i][1], 700, 232.5)
        elif(i == l-16):
            ID(copy2[i][0], 665, 177.5)
            ID(copy2[i][1], 700, 177.5)
        elif(i == l-17):
            ID(copy2[i][0], 590, 177.5)
            ID(copy2[i][1], 625, 177.5)
        elif(i == l-18):
            ID(copy2[i][0], 515, 177.5)
            ID(copy2[i][1], 550, 177.5)
        elif(i == l-19):
            ID(copy2[i][0], 440, 177.5)
            ID(copy2[i][1], 475, 177.5)
        elif(i == l-20):
            ID(copy2[i][0], 365, 177.5)
            ID(copy2[i][1], 400, 177.5)
        elif(i == l-21):
            ID(copy2[i][0], 290, 177.5)
            ID(copy2[i][1], 325, 177.5)
        elif(i == l-22):
            ID(copy2[i][0], 215, 177.5)
            ID(copy2[i][1], 250, 177.5)
        elif(i == l-23):
            ID(copy2[i][0], 140, 177.5)
            ID(copy2[i][1], 175, 177.5)
        elif(i == l-24):
            ID(copy2[i][0], 65, 177.5)
            ID(copy2[i][1], 100, 177.5)
        elif(i == l-25):
            ID(copy2[i][0], 25, 152.5)
            ID(copy2[i][1], 25, 177.5)
        elif(i == l-26):
            ID(copy2[i][0], 25, 122.5)
            ID(copy2[i][1], 60, 122.5)
        elif(i == l-27):
            ID(copy2[i][0], 100, 122.5)
            ID(copy2[i][1], 135, 122.5)
        i -= 1

    checkQuit()
    
    c = 61.75
    k = 0
    for i in range (len(Player1)):
        for j in range(len(Player1[i])):
            ID(Player1[i][j], c, k)
            k += 25
        k = 0
        c += 45

    checkQuit()
    
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

    if(f == 1):
        if((Find(Player2, o[0][0]) == False)and(Find(Player2, o[len(o)-1][1]) == False)):
            f = 0

            PG.mixer.init()
            Sound_P = PG.mixer.Sound("Sounds\\Pass.wav")
            Sound_P.play()
            
        c = 0
        while(f == 1):
            if(c>0):

                PG.mixer.init()
                Sound_E = PG.mixer.Sound("Sounds\\Error.wav")
                Sound_E.play()

            boolian = False
            while not boolian :

                e = PG.event.get()
    
                ( a, b, c ) = PG.mouse.get_pressed()
                if( a > 0 ):
                    x, y = PG.mouse.get_pos()
        
                    if( 61.75 < x < 96.75 and 550 < y < 600 ):
                        n = 1
                        if(n <= len(Player2) ):
                            boolian = True

                    elif( 107.25 < x < 142.25 and 550 < y < 600 ):
                        n = 2
                        if(n <= len(Player2) ):
                            boolian = True

                    elif( 152.75 < x < 187.75 and 550 < y < 600 ):
                        n = 3
                        if(n <= len(Player2) ):
                            boolian = True

                    elif( 198.25 < x < 233.25 and 550 < y < 600 ):
                        n = 4
                        if(n <= len(Player2) ):
                            boolian = True

                    elif( 243.75 < x < 278.75 and 550 < y < 600 ):
                        n = 5
                        if(n <= len(Player2) ):
                            boolian = True

                    elif( 289.25 < x < 324.25 and 550 < y < 600 ):
                        n = 6
                        if(n <= len(Player2) ):
                            boolian = True

                    elif( 334.75 < x < 369.75 and 550 < y < 600 ):
                        n = 7
                        if(n <= len(Player2) ):
                            boolian = True

                    elif( 380.25 < x < 415.25 and 550 < y < 600 ):
                        n = 8
                        if(n <= len(Player2) ):
                            boolian = True

                    elif( 425.75 < x < 460.75 and 550 < y < 600 ):
                        n = 9
                        if(n <= len(Player2) ):
                            boolian = True

                    elif( 471.25 < x < 506.25 and 550 < y < 600 ):
                        n = 10
                        if(n <= len(Player2) ):
                            boolian = True

                    elif( 516.75 < x < 551.75 and 550 < y < 600 ):
                        n = 11
                        if(n <= len(Player2) ):
                            boolian = True

                    elif( 562.25 < x < 597.25 and 550 < y < 600 ):
                        n = 12
                        if(n <= len(Player2) ):
                            boolian = True

                    elif( 607.75 < x < 642.75 and 550 < y < 600 ):
                        n = 13
                        if(n <= len(Player2) ):
                            boolian = True

                    elif( 653.25 < x < 688.25 and 550 < y < 600 ):
                        n = 14
                        if(n <= len(Player2) ):
                            boolian = True
                            
                checkQuit()

            i = 0
            while(i<100000):
                i+=1
                checkQuit()

            boolian = False
            while not boolian :

                e = PG.event.get()
    
                ( a, b, c ) = PG.mouse.get_pressed()
                if( a > 0 ):
                    x, y = PG.mouse.get_pos()
        
                    if(len(copy) < 5 and len(copy2) < 5):
                        if( x < W/2 and 50 < y < 550 ):
                            w = "L"
                            boolian = True

                        elif( x > W/2 and 50 < y < 550 ):
                            w = "R"
                            boolian = True

                    elif(len(copy) >= 5 or len(copy2) >= 5):
                        if( 50 < y < 300 ):
                            w = "L"
                            boolian = True

                        elif( 300 < y < 550 ):
                            w = "R"
                            boolian = True

                checkQuit()

            if(w == "L"):
                if(Player2[n-1][0] == o[0][0]):
                    rvs = list(reversed(Player2[n-1]))
                    o.insert(0, rvs)
                    Player2.pop(n-1)
                    f = 0

                    PG.mixer.init()
                    Sound_C = PG.mixer.Sound("Sounds\\Card.wav")
                    Sound_C.play()
                    
                elif(Player2[n-1][1] == o[0][0]):
                    o.insert(0, Player2[n-1])
                    Player2.pop(n-1)
                    f = 0

                    PG.mixer.init()
                    Sound_C = PG.mixer.Sound("Sounds\\Card.wav")
                    Sound_C.play()
                    
            elif(w == "R"):
                if(Player2[n-1][0] == o[len(o)-1][1]):
                    o.insert(len(o), Player2[n-1])
                    Player2.pop(n-1)
                    f = 0

                    PG.mixer.init()
                    Sound_C = PG.mixer.Sound("Sounds\\Card.wav")
                    Sound_C.play()
                    
                elif(Player2[n-1][1] == o[len(o)-1][1]):
                    rvs = list(reversed(Player2[n-1]))
                    o.insert(len(o), rvs)
                    Player2.pop(n-1)
                    f = 0

                    PG.mixer.init()
                    Sound_C = PG.mixer.Sound("Sounds\\Card.wav")
                    Sound_C.play()
                    
            c += 1

        checkQuit()

    if((len(Player1) == 0) or (len(Player2) == 0)):
        done = True

    if((Find(Player1, o[0][0]) == False)and(Find(Player1, o[len(o)-1][1]) == False))and((Find(Player2, o[0][0]) == False)and(Find(Player2, o[len(o)-1][1]) == False)):
        done = True

    checkQuit()

pic = PG.image.load("Pictures\\Domino_2.jpg")
pic = PG.transform.scale(pic, (W, H))
SC.blit(pic, (0, 0))
PG.display.update()

if(len(Player1) == 0):

    Msg( " Winner : Red Player ", RED, W/2-100, H/2-50, font)

elif(len(Player2) == 0):

    Msg( " Winner : Blue Player ", BLUE, W/2-100, H/2-50, font)

else:
    if(Plus(Player1) < Plus(Player2)):

        Msg( " Winner : Red Player ", RED, W/2-100, H/2-50, font)

    elif(Plus(Player2) < Plus(Player1)):

        Msg( " Winner : Blue Player ", BLUE, W/2-100, H/2-50, font)

    else:
        if(len(Player1) < len(Player2)):

            Msg( " Winner : Red Player ", RED, W/2-100, H/2-50, font)

        elif(len(Player2) < len(Player1)):

            Msg( " Winner : Blue Player ", BLUE, W/2-100, H/2-50, font)

        else :

            Msg( " EQUAL ", WHITE, W/2-50, H/2-50, font)
            
PG.mixer.init()
Sound_W = PG.mixer.Sound("Sounds\\Win.wav")
Sound_W.play()

SC.blit(PG.image.load("Pictures\\Gold Cup.png"), (W/2 - 60, H/2 ))

PG.display.update()

qutz = False
while not qutz:

    Msg( " RESTART ", WHITE, W/2-50, H/2 + 200 , font)
    PG.display.update()

    for event in PG.event.get():
        if event.type == PG.QUIT:
            PG.quit()
        if event.type == PG.KEYDOWN:
            if event.key == PG.K_ESCAPE:
                PG.quit()

    ( a, b, c ) = PG.mouse.get_pressed()
    if( a > 0 ):
        x, y = PG.mouse.get_pos()

        checkQuit()

        if( W/2-50 < x < W/2+75 and H/2+200 < y < H/2+225 ):
            
            Msg( " RESTART ", BLACK, W/2-50, H/2 + 200 , font)
            PG.display.update()

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

                h = o.index([6, 6])+1
                copy = o[h:]
                for i in range(len(copy)):
                    if(i == 0):
                        ID(copy[i][0], 440, 287.5)
                        ID(copy[i][1], 475, 287.5)
                    elif(i == 1):
                        ID(copy[i][0], 515, 287.5)
                        ID(copy[i][1], 550, 287.5)
                    elif(i == 2):
                        ID(copy[i][0], 590, 287.5)
                        ID(copy[i][1], 625, 287.5)
                    elif(i == 3):
                        ID(copy[i][0], 665, 287.5)
                        ID(copy[i][1], 700, 287.5)
                    elif(i == 4):
                        ID(copy[i][0], 740, 287.5)
                        ID(copy[i][1], 740, 312.5)
                    elif(i == 5):
                        ID(copy[i][1], 705, 342.5)
                        ID(copy[i][0], 740, 342.5)
                    elif(i == 6):
                        ID(copy[i][1], 630, 342.5)
                        ID(copy[i][0], 665, 342.5)
                    elif(i == 7):
                        ID(copy[i][1], 555, 342.5)
                        ID(copy[i][0], 590, 342.5)
                    elif(i == 8):
                        ID(copy[i][1], 480, 342.5)
                        ID(copy[i][0], 515, 342.5)
                    elif(i == 9):
                        ID(copy[i][1], 405, 342.5)
                        ID(copy[i][0], 440, 342.5)
                    elif(i == 10):
                        ID(copy[i][1], 330, 342.5)
                        ID(copy[i][0], 365, 342.5)
                    elif(i == 11):
                        ID(copy[i][1], 255, 342.5)
                        ID(copy[i][0], 290, 342.5)
                    elif(i == 12):
                        ID(copy[i][1], 180, 342.5)
                        ID(copy[i][0], 215, 342.5)
                    elif(i == 13):
                        ID(copy[i][1], 105, 342.5)
                        ID(copy[i][0], 140, 342.5)
                    elif(i == 14):
                        ID(copy[i][0], 65, 342.5)
                        ID(copy[i][1], 65, 367.5)
                    elif(i == 15):
                        ID(copy[i][0], 65, 397.5)
                        ID(copy[i][1], 100, 397.5)
                    elif(i == 16):
                        ID(copy[i][0], 140, 397.5)
                        ID(copy[i][1], 175, 397.5)
                    elif(i == 17):
                        ID(copy[i][0], 215, 397.5)
                        ID(copy[i][1], 250, 397.5)
                    elif(i == 18):
                        ID(copy[i][0], 290, 397.5)
                        ID(copy[i][1], 325, 397.5)
                    elif(i == 19):
                        ID(copy[i][0], 365, 397.5)
                        ID(copy[i][1], 400, 397.5)
                    elif(i == 20):
                        ID(copy[i][0], 440, 397.5)
                        ID(copy[i][1], 475, 397.5)
                    elif(i == 21):
                        ID(copy[i][0], 515, 397.5)
                        ID(copy[i][1], 550, 397.5)
                    elif(i == 22):
                        ID(copy[i][0], 590, 397.5)
                        ID(copy[i][1], 625, 397.5)
                    elif(i == 23):
                        ID(copy[i][0], 665, 397.5)
                        ID(copy[i][1], 700, 397.5)
                    elif(i == 24):
                        ID(copy[i][1], 740, 397.5)
                        ID(copy[i][0], 740, 422.5)
                    elif(i == 25):
                        ID(copy[i][1], 705, 472.5)
                        ID(copy[i][0], 740, 472.5)
                    elif(i == 26):
                        ID(copy[i][1], 630, 472.5)
                        ID(copy[i][0], 665, 472.5)

                checkQuit()

                h = o.index([6, 6])
                copy2 = o[:h]
                l = len(copy2)
                i = l-1
                while(i>=0):
                    if(i == l-1):
                        ID(copy2[i][0], 290, 287.5)
                        ID(copy2[i][1], 325, 287.5)
                    elif(i == l-2):
                        ID(copy2[i][0], 215, 287.5)
                        ID(copy2[i][1], 250, 287.5)
                    elif(i == l-3):
                        ID(copy2[i][0], 140, 287.5)
                        ID(copy2[i][1], 175, 287.5)
                    elif(i == l-4):
                        ID(copy2[i][0], 65, 287.5)
                        ID(copy2[i][1], 100, 287.5)
                    elif(i == l-5):
                        ID(copy2[i][0], 25, 262.5)
                        ID(copy2[i][1], 25, 287.5)
                    elif(i == l-6):
                        ID(copy2[i][1], 25, 232.5)
                        ID(copy2[i][0], 60, 232.5)
                    elif(i == l-7):
                        ID(copy2[i][1], 100, 232.5)
                        ID(copy2[i][0], 135, 232.5)
                    elif(i == l-8):
                        ID(copy2[i][1], 175, 232.5)
                        ID(copy2[i][0], 210, 232.5)
                    elif(i == l-9):
                        ID(copy2[i][1], 250, 232.5)
                        ID(copy2[i][0], 285, 232.5)
                    elif(i == l-10):
                        ID(copy2[i][1], 325, 232.5)
                        ID(copy2[i][0], 360, 232.5)
                    elif(i == l-11):
                        ID(copy2[i][1], 400, 232.5)
                        ID(copy2[i][0], 435, 232.5)
                    elif(i == l-12):
                        ID(copy2[i][1], 475, 232.5)
                        ID(copy2[i][0], 510, 232.5)
                    elif(i == l-13):
                        ID(copy2[i][1], 550, 232.5)
                        ID(copy2[i][0], 585, 232.5)
                    elif(i == l-14):
                        ID(copy2[i][1], 625, 232.5)
                        ID(copy2[i][0], 660, 232.5)
                    elif(i == l-15):
                        ID(copy2[i][0], 700, 207.5)
                        ID(copy2[i][1], 700, 232.5)
                    elif(i == l-16):
                        ID(copy2[i][0], 665, 177.5)
                        ID(copy2[i][1], 700, 177.5)
                    elif(i == l-17):
                        ID(copy2[i][0], 590, 177.5)
                        ID(copy2[i][1], 625, 177.5)
                    elif(i == l-18):
                        ID(copy2[i][0], 515, 177.5)
                        ID(copy2[i][1], 550, 177.5)
                    elif(i == l-19):
                        ID(copy2[i][0], 440, 177.5)
                        ID(copy2[i][1], 475, 177.5)
                    elif(i == l-20):
                        ID(copy2[i][0], 365, 177.5)
                        ID(copy2[i][1], 400, 177.5)
                    elif(i == l-21):
                        ID(copy2[i][0], 290, 177.5)
                        ID(copy2[i][1], 325, 177.5)
                    elif(i == l-22):
                        ID(copy2[i][0], 215, 177.5)
                        ID(copy2[i][1], 250, 177.5)
                    elif(i == l-23):
                        ID(copy2[i][0], 140, 177.5)
                        ID(copy2[i][1], 175, 177.5)
                    elif(i == l-24):
                        ID(copy2[i][0], 65, 177.5)
                        ID(copy2[i][1], 100, 177.5)
                    elif(i == l-25):
                        ID(copy2[i][0], 25, 152.5)
                        ID(copy2[i][1], 25, 177.5)
                    elif(i == l-26):
                        ID(copy2[i][0], 25, 122.5)
                        ID(copy2[i][1], 60, 122.5)
                    elif(i == l-27):
                        ID(copy2[i][0], 100, 122.5)
                        ID(copy2[i][1], 135, 122.5)
                    i -= 1

                checkQuit()
                
                c = 61.75
                k = 0
                for i in range (len(Player1)):
                    for j in range(len(Player1[i])):
                        ID(Player1[i][j], c, k)
                        k += 25
                    k = 0
                    c += 45

                checkQuit()
                
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

                if(f == 0):
                    if((Find(Player1, o[0][0]) == False)and(Find(Player1, o[len(o)-1][1]) == False)):
                        f = 1

                        PG.mixer.init()
                        Sound_P = PG.mixer.Sound("Sounds\\Pass.wav")
                        Sound_P.play()

                    c = 0
                    while(f == 0):
                        if(c>0):

                            PG.mixer.init()
                            Sound_E = PG.mixer.Sound("Sounds\\Error.wav")
                            Sound_E.play()

                        boolian = False
                        while not boolian :

                            e = PG.event.get()
                
                            ( a, b, c ) = PG.mouse.get_pressed()
                            if( a > 0 ):
                                x, y = PG.mouse.get_pos()
                    
                                if( 61.75 < x < 96.75 and 0 < y < 50 ):
                                    n = 1
                                    if(n <= len(Player1) ):
                                        boolian = True

                                elif( 107.25 < x < 142.25 and 0 < y < 50 ):
                                    n = 2
                                    if(n <= len(Player1) ):
                                        boolian = True

                                elif( 152.75 < x < 187.75 and 0 < y < 50 ):
                                    n = 3
                                    if(n <= len(Player1) ):
                                        boolian = True

                                elif( 198.25 < x < 233.25 and 0 < y < 50 ):
                                    n = 4
                                    if(n <= len(Player1) ):
                                        boolian = True

                                elif( 243.75 < x < 278.75 and 0 < y < 50 ):
                                    n = 5
                                    if(n <= len(Player1) ):
                                        boolian = True

                                elif( 289.25 < x < 324.25 and 0 < y < 50 ):
                                    n = 6
                                    if(n <= len(Player1) ):
                                        boolian = True

                                elif( 334.75 < x < 369.75 and 0 < y < 50 ):
                                    n = 7
                                    if(n <= len(Player1) ):
                                        boolian = True

                                elif( 380.25 < x < 415.25 and 0 < y < 50 ):
                                    n = 8
                                    if(n <= len(Player1) ):
                                        boolian = True

                                elif( 425.75 < x < 460.75 and 0 < y < 50 ):
                                    n = 9
                                    if(n <= len(Player1) ):
                                        boolian = True

                                elif( 471.25 < x < 506.25 and 0 < y < 50 ):
                                    n = 10
                                    if(n <= len(Player1) ):
                                        boolian = True

                                elif( 516.75 < x < 551.75 and 0 < y < 50 ):
                                    n = 11
                                    if(n <= len(Player1) ):
                                        boolian = True

                                elif( 562.25 < x < 597.25 and 0 < y < 50 ):
                                    n = 12
                                    if(n <= len(Player1) ):
                                        boolian = True

                                elif( 607.75 < x < 642.75 and 0 < y < 50 ):
                                    n = 13
                                    if(n <= len(Player1) ):
                                        boolian = True

                                elif( 653.25 < x < 688.25 and 0 < y < 50 ):
                                    n = 14
                                    if(n <= len(Player1) ):
                                        boolian = True
                                        
                            checkQuit()

                        i = 0
                        while(i<100000):
                            i+=1
                            checkQuit()
                        
                        boolian = False
                        while not boolian :

                            e = PG.event.get()
                
                            ( a, b, c ) = PG.mouse.get_pressed()
                            if( a > 0 ):
                                x, y = PG.mouse.get_pos()
                    
                                if(len(copy) < 5):
                                    if( x < W/2 and 50 < y < 550 ):
                                        w = "L"
                                        boolian = True

                                    elif( x > W/2 and 50 < y < 550 ):
                                        w = "R"
                                        boolian = True

                                elif(len(copy) >= 5):
                                    if( 50 < y < 300 ):
                                        w = "L"
                                        boolian = True

                                    elif( 300 < y < 550 ):
                                        w = "R"
                                        boolian = True

                            checkQuit()
                        
                        if(w == "L"):
                            if(Player1[n-1][0] == o[0][0]):
                                rvs = list(reversed(Player1[n-1]))
                                o.insert(0, rvs)
                                Player1.pop(n-1)
                                f = 1

                                PG.mixer.init()
                                Sound_C = PG.mixer.Sound("Sounds\\Card.wav")
                                Sound_C.play()
                                
                            elif(Player1[n-1][1] == o[0][0]):
                                o.insert(0, Player1[n-1])
                                Player1.pop(n-1)
                                f = 1
                                
                                PG.mixer.init()
                                Sound_C = PG.mixer.Sound("Sounds\\Card.wav")
                                Sound_C.play()

                        elif(w == "R"):
                            if(Player1[n-1][0] == o[len(o)-1][1]):
                                o.insert(len(o), Player1[n-1])
                                Player1.pop(n-1)
                                f = 1

                                PG.mixer.init()
                                Sound_C = PG.mixer.Sound("Sounds\\Card.wav")
                                Sound_C.play()
                                
                            elif(Player1[n-1][1] == o[len(o)-1][1]):
                                rvs = list(reversed(Player1[n-1]))
                                o.insert(len(o), rvs)
                                Player1.pop(n-1)
                                f = 1

                                PG.mixer.init()
                                Sound_C = PG.mixer.Sound("Sounds\\Card.wav")
                                Sound_C.play()
                                
                        c += 1

                    checkQuit()

                SC.blit(pic, (0, 0))
                SC.blit(user1, (0, 0))
                SC.blit(user2, (0, 550))
                SC.blit(off, (700, 0))
                SC.blit(off, (700, 550))

                SC.blit(six, (W/2, H/2 - 12.5))
                SC.blit(six, (W/2 - 35, H/2 - 12.5))

                h = o.index([6, 6])+1
                copy = o[h:]
                for i in range(len(copy)):
                    if(i == 0):
                        ID(copy[i][0], 440, 287.5)
                        ID(copy[i][1], 475, 287.5)
                    elif(i == 1):
                        ID(copy[i][0], 515, 287.5)
                        ID(copy[i][1], 550, 287.5)
                    elif(i == 2):
                        ID(copy[i][0], 590, 287.5)
                        ID(copy[i][1], 625, 287.5)
                    elif(i == 3):
                        ID(copy[i][0], 665, 287.5)
                        ID(copy[i][1], 700, 287.5)
                    elif(i == 4):
                        ID(copy[i][0], 740, 287.5)
                        ID(copy[i][1], 740, 312.5)
                    elif(i == 5):
                        ID(copy[i][1], 705, 342.5)
                        ID(copy[i][0], 740, 342.5)
                    elif(i == 6):
                        ID(copy[i][1], 630, 342.5)
                        ID(copy[i][0], 665, 342.5)
                    elif(i == 7):
                        ID(copy[i][1], 555, 342.5)
                        ID(copy[i][0], 590, 342.5)
                    elif(i == 8):
                        ID(copy[i][1], 480, 342.5)
                        ID(copy[i][0], 515, 342.5)
                    elif(i == 9):
                        ID(copy[i][1], 405, 342.5)
                        ID(copy[i][0], 440, 342.5)
                    elif(i == 10):
                        ID(copy[i][1], 330, 342.5)
                        ID(copy[i][0], 365, 342.5)
                    elif(i == 11):
                        ID(copy[i][1], 255, 342.5)
                        ID(copy[i][0], 290, 342.5)
                    elif(i == 12):
                        ID(copy[i][1], 180, 342.5)
                        ID(copy[i][0], 215, 342.5)
                    elif(i == 13):
                        ID(copy[i][1], 105, 342.5)
                        ID(copy[i][0], 140, 342.5)
                    elif(i == 14):
                        ID(copy[i][0], 65, 342.5)
                        ID(copy[i][1], 65, 367.5)
                    elif(i == 15):
                        ID(copy[i][0], 65, 397.5)
                        ID(copy[i][1], 100, 397.5)
                    elif(i == 16):
                        ID(copy[i][0], 140, 397.5)
                        ID(copy[i][1], 175, 397.5)
                    elif(i == 17):
                        ID(copy[i][0], 215, 397.5)
                        ID(copy[i][1], 250, 397.5)
                    elif(i == 18):
                        ID(copy[i][0], 290, 397.5)
                        ID(copy[i][1], 325, 397.5)
                    elif(i == 19):
                        ID(copy[i][0], 365, 397.5)
                        ID(copy[i][1], 400, 397.5)
                    elif(i == 20):
                        ID(copy[i][0], 440, 397.5)
                        ID(copy[i][1], 475, 397.5)
                    elif(i == 21):
                        ID(copy[i][0], 515, 397.5)
                        ID(copy[i][1], 550, 397.5)
                    elif(i == 22):
                        ID(copy[i][0], 590, 397.5)
                        ID(copy[i][1], 625, 397.5)
                    elif(i == 23):
                        ID(copy[i][0], 665, 397.5)
                        ID(copy[i][1], 700, 397.5)
                    elif(i == 24):
                        ID(copy[i][1], 740, 397.5)
                        ID(copy[i][0], 740, 422.5)
                    elif(i == 25):
                        ID(copy[i][1], 705, 472.5)
                        ID(copy[i][0], 740, 472.5)
                    elif(i == 26):
                        ID(copy[i][1], 630, 472.5)
                        ID(copy[i][0], 665, 472.5)
                        
                checkQuit()

                h = o.index([6, 6])
                copy2 = o[:h]
                l = len(copy2)
                i = l-1
                while(i>=0):
                    if(i == l-1):
                        ID(copy2[i][0], 290, 287.5)
                        ID(copy2[i][1], 325, 287.5)
                    elif(i == l-2):
                        ID(copy2[i][0], 215, 287.5)
                        ID(copy2[i][1], 250, 287.5)
                    elif(i == l-3):
                        ID(copy2[i][0], 140, 287.5)
                        ID(copy2[i][1], 175, 287.5)
                    elif(i == l-4):
                        ID(copy2[i][0], 65, 287.5)
                        ID(copy2[i][1], 100, 287.5)
                    elif(i == l-5):
                        ID(copy2[i][0], 25, 262.5)
                        ID(copy2[i][1], 25, 287.5)
                    elif(i == l-6):
                        ID(copy2[i][1], 25, 232.5)
                        ID(copy2[i][0], 60, 232.5)
                    elif(i == l-7):
                        ID(copy2[i][1], 100, 232.5)
                        ID(copy2[i][0], 135, 232.5)
                    elif(i == l-8):
                        ID(copy2[i][1], 175, 232.5)
                        ID(copy2[i][0], 210, 232.5)
                    elif(i == l-9):
                        ID(copy2[i][1], 250, 232.5)
                        ID(copy2[i][0], 285, 232.5)
                    elif(i == l-10):
                        ID(copy2[i][1], 325, 232.5)
                        ID(copy2[i][0], 360, 232.5)
                    elif(i == l-11):
                        ID(copy2[i][1], 400, 232.5)
                        ID(copy2[i][0], 435, 232.5)
                    elif(i == l-12):
                        ID(copy2[i][1], 475, 232.5)
                        ID(copy2[i][0], 510, 232.5)
                    elif(i == l-13):
                        ID(copy2[i][1], 550, 232.5)
                        ID(copy2[i][0], 585, 232.5)
                    elif(i == l-14):
                        ID(copy2[i][1], 625, 232.5)
                        ID(copy2[i][0], 660, 232.5)
                    elif(i == l-15):
                        ID(copy2[i][0], 700, 207.5)
                        ID(copy2[i][1], 700, 232.5)
                    elif(i == l-16):
                        ID(copy2[i][0], 665, 177.5)
                        ID(copy2[i][1], 700, 177.5)
                    elif(i == l-17):
                        ID(copy2[i][0], 590, 177.5)
                        ID(copy2[i][1], 625, 177.5)
                    elif(i == l-18):
                        ID(copy2[i][0], 515, 177.5)
                        ID(copy2[i][1], 550, 177.5)
                    elif(i == l-19):
                        ID(copy2[i][0], 440, 177.5)
                        ID(copy2[i][1], 475, 177.5)
                    elif(i == l-20):
                        ID(copy2[i][0], 365, 177.5)
                        ID(copy2[i][1], 400, 177.5)
                    elif(i == l-21):
                        ID(copy2[i][0], 290, 177.5)
                        ID(copy2[i][1], 325, 177.5)
                    elif(i == l-22):
                        ID(copy2[i][0], 215, 177.5)
                        ID(copy2[i][1], 250, 177.5)
                    elif(i == l-23):
                        ID(copy2[i][0], 140, 177.5)
                        ID(copy2[i][1], 175, 177.5)
                    elif(i == l-24):
                        ID(copy2[i][0], 65, 177.5)
                        ID(copy2[i][1], 100, 177.5)
                    elif(i == l-25):
                        ID(copy2[i][0], 25, 152.5)
                        ID(copy2[i][1], 25, 177.5)
                    elif(i == l-26):
                        ID(copy2[i][0], 25, 122.5)
                        ID(copy2[i][1], 60, 122.5)
                    elif(i == l-27):
                        ID(copy2[i][0], 100, 122.5)
                        ID(copy2[i][1], 135, 122.5)
                    i -= 1

                checkQuit()
                
                c = 61.75
                k = 0
                for i in range (len(Player1)):
                    for j in range(len(Player1[i])):
                        ID(Player1[i][j], c, k)
                        k += 25
                    k = 0
                    c += 45

                checkQuit()
                
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

                if(f == 1):
                    if((Find(Player2, o[0][0]) == False)and(Find(Player2, o[len(o)-1][1]) == False)):
                        f = 0

                        PG.mixer.init()
                        Sound_P = PG.mixer.Sound("Sounds\\Pass.wav")
                        Sound_P.play()
                        
                    c = 0
                    while(f == 1):
                        if(c>0):

                            PG.mixer.init()
                            Sound_E = PG.mixer.Sound("Sounds\\Error.wav")
                            Sound_E.play()

                        boolian = False
                        while not boolian :

                            e = PG.event.get()
                
                            ( a, b, c ) = PG.mouse.get_pressed()
                            if( a > 0 ):
                                x, y = PG.mouse.get_pos()
                    
                                if( 61.75 < x < 96.75 and 550 < y < 600 ):
                                    n = 1
                                    if(n <= len(Player2) ):
                                        boolian = True

                                elif( 107.25 < x < 142.25 and 550 < y < 600 ):
                                    n = 2
                                    if(n <= len(Player2) ):
                                        boolian = True

                                elif( 152.75 < x < 187.75 and 550 < y < 600 ):
                                    n = 3
                                    if(n <= len(Player2) ):
                                        boolian = True

                                elif( 198.25 < x < 233.25 and 550 < y < 600 ):
                                    n = 4
                                    if(n <= len(Player2) ):
                                        boolian = True

                                elif( 243.75 < x < 278.75 and 550 < y < 600 ):
                                    n = 5
                                    if(n <= len(Player2) ):
                                        boolian = True

                                elif( 289.25 < x < 324.25 and 550 < y < 600 ):
                                    n = 6
                                    if(n <= len(Player2) ):
                                        boolian = True

                                elif( 334.75 < x < 369.75 and 550 < y < 600 ):
                                    n = 7
                                    if(n <= len(Player2) ):
                                        boolian = True

                                elif( 380.25 < x < 415.25 and 550 < y < 600 ):
                                    n = 8
                                    if(n <= len(Player2) ):
                                        boolian = True

                                elif( 425.75 < x < 460.75 and 550 < y < 600 ):
                                    n = 9
                                    if(n <= len(Player2) ):
                                        boolian = True

                                elif( 471.25 < x < 506.25 and 550 < y < 600 ):
                                    n = 10
                                    if(n <= len(Player2) ):
                                        boolian = True

                                elif( 516.75 < x < 551.75 and 550 < y < 600 ):
                                    n = 11
                                    if(n <= len(Player2) ):
                                        boolian = True

                                elif( 562.25 < x < 597.25 and 550 < y < 600 ):
                                    n = 12
                                    if(n <= len(Player2) ):
                                        boolian = True

                                elif( 607.75 < x < 642.75 and 550 < y < 600 ):
                                    n = 13
                                    if(n <= len(Player2) ):
                                        boolian = True

                                elif( 653.25 < x < 688.25 and 550 < y < 600 ):
                                    n = 14
                                    if(n <= len(Player2) ):
                                        boolian = True
                                        
                            checkQuit()

                        i = 0
                        while(i<100000):
                            i+=1
                            checkQuit()

                        boolian = False
                        while not boolian :

                            e = PG.event.get()
                
                            ( a, b, c ) = PG.mouse.get_pressed()
                            if( a > 0 ):
                                x, y = PG.mouse.get_pos()
                    
                                if(len(copy) < 5):
                                    if( x < W/2 and 50 < y < 550 ):
                                        w = "L"
                                        boolian = True

                                    elif( x > W/2 and 50 < y < 550 ):
                                        w = "R"
                                        boolian = True

                                elif(len(copy) >= 5):
                                    if( 50 < y < 300 ):
                                        w = "L"
                                        boolian = True

                                    elif( 300 < y < 550 ):
                                        w = "R"
                                        boolian = True
                                        
                            checkQuit()

                        if(w == "L"):
                            if(Player2[n-1][0] == o[0][0]):
                                rvs = list(reversed(Player2[n-1]))
                                o.insert(0, rvs)
                                Player2.pop(n-1)
                                f = 0

                                PG.mixer.init()
                                Sound_C = PG.mixer.Sound("Sounds\\Card.wav")
                                Sound_C.play()
                                
                            elif(Player2[n-1][1] == o[0][0]):
                                o.insert(0, Player2[n-1])
                                Player2.pop(n-1)
                                f = 0

                                PG.mixer.init()
                                Sound_C = PG.mixer.Sound("Sounds\\Card.wav")
                                Sound_C.play()
                                
                        elif(w == "R"):
                            if(Player2[n-1][0] == o[len(o)-1][1]):
                                o.insert(len(o), Player2[n-1])
                                Player2.pop(n-1)
                                f = 0

                                PG.mixer.init()
                                Sound_C = PG.mixer.Sound("Sounds\\Card.wav")
                                Sound_C.play()
                                
                            elif(Player2[n-1][1] == o[len(o)-1][1]):
                                rvs = list(reversed(Player2[n-1]))
                                o.insert(len(o), rvs)
                                Player2.pop(n-1)
                                f = 0

                                PG.mixer.init()
                                Sound_C = PG.mixer.Sound("Sounds\\Card.wav")
                                Sound_C.play()
                                
                        c += 1

                    checkQuit()

                if((len(Player1) == 0) or (len(Player2) == 0)):
                    done = True

                if((Find(Player1, o[0][0]) == False)and(Find(Player1, o[len(o)-1][1]) == False))and((Find(Player2, o[0][0]) == False)and(Find(Player2, o[len(o)-1][1]) == False)):
                    done = True

                checkQuit()

            pic = PG.image.load("Pictures\\Domino_2.jpg")
            pic = PG.transform.scale(pic, (W, H))
            SC.blit(pic, (0, 0))
            PG.display.update()

            if(len(Player1) == 0):

                Msg( " Winner : Red Player ", RED, W/2-100, H/2-50, font)
                
            elif(len(Player2) == 0):

                Msg( " Winner : Blue Player ", BLUE, W/2-100, H/2-50, font)

            else:
                if(Plus(Player1) < Plus(Player2)):

                    Msg( " Winner : Red Player ", RED, W/2-100, H/2-50, font)

                elif(Plus(Player2) < Plus(Player1)):

                    Msg( " Winner : Blue Player ", BLUE, W/2-100, H/2-50, font)

                else:
                    if(len(Player1) < len(Player2)):

                        Msg( " Winner : Red Player ", RED, W/2-100, H/2-50, font)

                    elif(len(Player2) < len(Player1)):

                        Msg( " Winner : Blue Player ", BLUE, W/2-100, H/2-50, font)

                    else :

                        Msg( " EQUAL ", WHITE, W/2-50, H/2-50, font)
                        
            PG.mixer.init()
            Sound_W = PG.mixer.Sound("Sounds\\Win.wav")
            Sound_W.play()

            SC.blit(PG.image.load("Pictures\\Gold Cup.png"), (W/2 - 60, H/2 ))

            PG.display.update()

