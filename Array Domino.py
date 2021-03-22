## Domino Game
## Produced By Sepehr Bazyar
## Class 3/7

import random

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

done = False
while not done :

    if(f == 0):
        if((Find(Player1, o[0][0]) == False)and(Find(Player1, o[len(o)-1][1]) == False)):
            f = 1
            print()
            print(" PASS ")
            print()
        c = 0
        while(f == 0):
            if(c>0):
                print()
                print(" ERROR ")
                print()
                
            print()
            print(o)
            print()
            print("Player 1 : ", Player1)
            n = int(input(" from 1 to "+str(len(Player1))+" = "))
            w = input(" Left(L)or Right(R) = ")
            if(w == "L"):
                if(Player1[n-1][0] == o[0][0]):
                    rvs = list(reversed(Player1[n-1]))
                    o.insert(0, rvs)
                    Player1.pop(n-1)
                    f = 1
                elif(Player1[n-1][1] == o[0][0]):
                    o.insert(0, Player1[n-1])
                    Player1.pop(n-1)
                    f = 1
            elif(w == "R"):
                if(Player1[n-1][0] == o[len(o)-1][1]):
                    o.insert(len(o), Player1[n-1])
                    Player1.pop(n-1)
                    f = 1
                elif(Player1[n-1][1] == o[len(o)-1][1]):
                    rvs = list(reversed(Player1[n-1]))
                    o.insert(len(o), rvs)
                    Player1.pop(n-1)
                    f = 1
            c += 1


    if(f == 1):
        if((Find(Player2, o[0][0]) == False)and(Find(Player2, o[len(o)-1][1]) == False)):
            f = 0
            print()
            print(" PASS ")
            print()
        c = 0
        while(f == 1):
            if(c>0):
                print()
                print(" ERROR ")
                print()

            print()
            print(o)
            print()
            print("Player 2 :", Player2)
            n = int(input(" from 1 to "+str(len(Player2))+" = "))
            w = input(" Left(L)or Right(R) = ")
            if(w == "L"):
                if(Player2[n-1][0] == o[0][0]):
                    rvs = list(reversed(Player2[n-1]))
                    o.insert(0, rvs)
                    Player2.pop(n-1)
                    f = 0
                elif(Player2[n-1][1] == o[0][0]):
                    o.insert(0, Player2[n-1])
                    Player2.pop(n-1)
                    f = 0
            elif(w == "R"):
                if(Player2[n-1][0] == o[len(o)-1][1]):
                    o.insert(len(o), Player2[n-1])
                    Player2.pop(n-1)
                    f = 0
                elif(Player2[n-1][1] == o[len(o)-1][1]):
                    rvs = list(reversed(Player2[n-1]))
                    o.insert(len(o), rvs)
                    Player2.pop(n-1)
                    f = 0
            c += 1

    if((len(Player1) == 0) or (len(Player2) == 0)):
        done = True

    if((Find(Player1, o[0][0]) == False)and(Find(Player1, o[len(o)-1][1]) == False))and((Find(Player2, o[0][0]) == False)and(Find(Player2, o[len(o)-1][1]) == False)):
        done = True

if(len(Player1) == 0):
    print()
    print()
    print(" Winner : Player 1 ")
    print()
    print()
elif(len(Player2) == 0):
    print()
    print()
    print(" Winner : Player 2 ")
    print()
    print()
else:
    if(Plus(Player1) < Plus(Player2)):
        print()
        print()
        print(" Winner : Player 1 ")
        print()
        print()
    elif(Plus(Player2) < Plus(Player1)):
        print()
        print()
        print(" Winner : Player 2 ")
        print()
        print()
    else:
        if(len(Player1) < len(Player2)):
            print()
            print()
            print(" Winner : Player 1 ")
            print()
            print()
        elif(len(Player2) < len(Player1)):
            print()
            print()
            print(" Winner : Player 2 ")
            print()
            print()
        else :
            print()
            print()
            print(" EQUAL ")
            print()
            print()
