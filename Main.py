#Python Final
#Cameron Westlake

import math
import random
import CardClasses as cc

suits = ("heart", "diamond", "spade", "club")
values = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10" "J", "Q", "K", "A")

AIPlayers = []

names = ("Cameron", "Fluffy", "John", "Sunny", "Simba", "Ivette", "Not you")
player = cc.Player("You", False, 0)

def startGame(players, chips):
    player.chips = chips
    tempnames = []
    tempnames.extend(names)
    while players > 1:
        num = random.randint(0, len(tempnames) - 1)
        AIPlayers.append(cc.Player(tempnames[num], True, chips))
        tempnames.pop(num)
        players -= 1

def isGameGoing():
    activeopponent = False
    for i in AIPlayers:
        if i.chips > 0:
            activeopponent = True
            break
    return player.chips > 0 and activeopponent

def getNextValidPlayer(selected):
    selected += 1
    if(selected >= len(table)):
        selected = 0
    while table[selected].chips <= 0:
        selected += 1
        if(selected >= len(table)):
            selected = 0
    return selected

def fold(pl):
    pl.folded = True

def call(pl, amt):
    diff = min(pl.chips, pl.betted - amt)
    pl.chips -= diff
    pl.betted += diff

def raiseBet(pl, amt):
    diff = min(pl.chips, pl.betted - amt)
    pl.chips -= diff
    pl.betted += diff
    return diff

def getRandomCard(thisdeck):
    x = random.randint(0, len(thisdeck) - 1)
    return thisdeck[x]

deck = []
for i in suits:
    for j in values:
        deck.append(cc.Card(i, j))

startchips = 0
while startchips == 0:
    try:
        startchips = int(input("Enter the amount of chips you want to start with (0 - 10000): "))
        if startchips < 0 or startchips > 10000:
            print("Chip amount is not within a valid range")
            startchips = 0
    except:
        print("Chips must be a number")

playercount = 0
while playercount == 0:
    try:
        playercount = int(input("Enter number of players (2 - 8): "))
        if playercount < 2 or playercount > 8:
            print("Player count is not within a valid range")
            playercount = 0
    except:
        print("Must be a number")

startGame(playercount, startchips)

round = 0
table = [player]
table.extend(AIPlayers)
bblind = 0
while isGameGoing():
    #Setting up the start of the round
    round += 1
    pool = 0
    print("Start of round", round)
    #Big blind always puts in 10 chips, and are where the round starts
    bblind = getNextValidPlayer(bblind)
    c = table[bblind].takeChips(10)
    table[bblind].chips -= c
    pool += c
    bet = 10
    print(table[bblind].name, "Put in", c, "chips as the big blind")
    inround = 1
    currdeck = []
    currdeck.extend(deck)

    #Distributing cards
    for i in table:
        i.cards.append(getRandomCard(currdeck))
        i.cards.append(getRandomCard(currdeck))
    
    print("Your cards:")
    for i in player.cards:
        print(i.suit, i.value)

    tablecards = []
    while inround < 4:
        #Start off by getting the next player in line
        selected = bblind
        selected = getNextValidPlayer(selected)
        while not selected == bblind:
            #Get next move
            if(table[selected].isai):
                #Determine their next move
                decider = random.randint(-50, 50)
                decider += table[selected].mood
                if(decider < -30):#Fold
                    fold(table[selected])
                    print(table[selected].name, "folded")
                elif(decider < 20 or table[selected].chips + table[selected].betted < bet):#Call
                    call(table[selected], bet)
                    print(table[selected].name, "called")
                else:#Raise
                    bet += raiseBet(table[selected], random.randint(1, 5) * 10 + bet)
                    print(table[selected].name, "raised to", bet)
            else:
                #Get user selected option
                sel = 0
                while sel == 0:
                    try:
                        sel = int(input("Select your move:\n1. Fold\n2. Call\n3. Raise\n4. Get Info\n"))
                        assert sel > 0 and sel < 5
                    except:
                        print("Invalid option")
                        sel = 0 
                    if(sel == 1):
                        fold(table[selected])
                        print(table[selected].name, "folded")
                    elif(sel == 2):
                        call(table[selected], bet)
                        print(table[selected].name, "called")
                    elif(sel == 3):
                        raiseby = 0
                        while raiseby == 0:
                            try:
                                raiseby = int(input("Select amount to raise by (0 - 100): "))
                                assert raiseby > 0 and raiseby <= 100
                            except:
                                print("Invalid option")
                                raiseby = 0
                        bet += raiseBet(table[selected], random.randint(1, 5) * 10 + bet)
                        print(table[selected].name, "raised to", bet)
                    else:
                        print("Info")
                        sel = 0
            selected = getNextValidPlayer(selected)
        if inround == 1:
            tablecards.append(getRandomCard(currdeck))
            tablecards.append(getRandomCard(currdeck))
            tablecards.append(getRandomCard(currdeck))
            print("Cards on table: ")
            for i in tablecards:
                print(i.suit, i.value)
        elif inround == 2:
            tablecards.append(getRandomCard(currdeck))
            print("Cards on table: ")
            for i in tablecards:
                print(i.suit, i.value)
        elif inround == 3:
            tablecards.append(getRandomCard(currdeck))
            print("Cards on table: ")
            for i in tablecards:
                print(i.suit, i.value)
        else:
            #Determine winner
            winner = random.randint(0, len(table) - 1)
        inround += 1

if(player.chips > 0):
    print("You Win!")
else:
    print("You Lose!")
                

