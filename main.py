import random
from fullDeck import fullDeck, RoundGenerator, deck1
from player import Player


def createPlayers():
    for c in range(number):
        name = input("Choose a player name.")
        player1 = Player(1500,name,'P')
        player1.Shuffle()
        playersList.append(player1)


def roundProgress(flop):

    for player in playersList:
        if round1.raised == True:
            break
        
        if player.wallet > 0 and player.state == 'P':
            print("The current pot is $", round1.pot)
            print("It's",player.name,"'s turn.")
            print("This is your hand! Don't show it to anyone.")
            player.printCards()
            handChecker(flop,player)
            print("--x--")
            playerOptions(player)
    
    if round1.raised == True:
        for player in playersList:
            if player.wallet > 0 and player.state == 'P' and player.currentBet!=round1.raiseAmount:
                print("The current pot is $", round1.pot)
                print("It's",player.name,"'s turn.")
                print("This is your hand! Don't show it to anyone.")
                player.printCards()
                handChecker(flop,player)
                print("--x--")
                playerOptions(player)

        round1.raised = False



def winner():
    points = []
    if foldedPlayers == len(playersList)-1:
        for player in playersList:
            if player.state == 'P':
                print("The winner is {}! You won ${}!".format(player.name, round1.pot))
                player.wallet+=round1.pot
        endRound()
    else:
        for player in playersList:
            points.append(player.points)
        most = max(points)
        if points.count(most)>1:
            round1.pot = round1.pot/points.count(most)
            for player in playersList:
                if player.points == most:
                    print("{} tied! He won ${} of the pot.".format(player.name, round1.pot))
                    player.wallet+=round1.pot
        else:
            for player in playersList:
                if player.points == most:
                    print("{} won! You won ${}.".format(player.name, round1.pot))
                    player.wallet+=round1.pot

def endRound():
    for player in playersList:
        player.handReset()
    round1.fullReset()
    deck1.restartDeck()


# Pair = 1 Two Pairs = 2 Three of a Kind = 3 Straight = 4 Flush = 5 Full House = 6 
# Four of a Kind = 7 Straight Flush = 8 Royal Flush = 9

def handChecker(flop,who):
    
    who.allCards = []
    who.allCards = who.hand.copy()
    who.points = 0
    
    for i in flop:
        who.allCards.append(i)

    pairs = []   #Same rank cards
    ranks_pass = [] # Only ranks list
    suits_pass = [] # Only suits list
    
    for j in who.allCards:
        n_pair = []
        val = 0
        for i in who.allCards:
            if j[1] == i[1] and j[1] not in ranks_pass and j[0]!=i[0]:
                n_pair.append(i)
                val = 1
            
            elif val == 1 and i == who.allCards[-1]:
                n_pair.append(j)

        if n_pair != []:
            pairs.append(n_pair)
        ranks_pass.append(j[1])
        suits_pass.append(j[0])
    
    # Ranks checker:
    
    if len(pairs)>0:
        pairCount = 0
        verif = 0
        for i in pairs:
            if len(i) == 2:
                print("You have a pair of", i[1][1])
                who.points+=1
                verif+= 1
            elif len(i)==3 and verif == 1:
                print("You have a Full House!")
                who.points+=5
                verif+=2
            elif len(i) == 3 and verif == 0:
                print("You have a Three of a Kind!")
                who.points+=3
            elif len(i) == 4:
                print("You have a Four of a Kind!")
                who.points+=7
        if verif == 3:
            print("You have a Full House!")
            who.points = 6

    #Suits checker:
    
    Fchecker = 0
    
    if suits_pass.count('D')==5:
        print("You have a Flush of Diamonds!")
        who.points+=5
        Fchecker = 1
    elif suits_pass.count('S')==5:
        print("You have a Flush of Spades!")
        who.points+=5
        Fchecker = 1
    elif suits_pass.count('H')==5:
        print("You have a Flush of Hearts!")
        who.points+=5
        Fchecker = 1
    elif suits_pass.count('C')==5:
        print("You have a Flush of Clubs!")
        who.points+=5
        Fchecker = 1

    # Sequence checker:^
    sequence = '1234567891011121314'

    ranksStr = '' # If the sequence has an Ace, it will be seen as 1 here.
    ranksStr2 = '' # If the sequence has an Ace, it will be seen as 14 here.
    
    ranks_pass = list(set(ranks_pass))
    # Transforming the ranks list in a int list:        
    for i in ranks_pass:
        if i == 'A':
            where = ranks_pass.index(i)
            ranks_pass.remove(i)
            ranks_pass.insert(where,1)
        elif i == 'J':
            where = ranks_pass.index(i)
            ranks_pass.remove(i)
            ranks_pass.insert(where,11)
        elif i == 'Q':
            where = ranks_pass.index(i)
            ranks_pass.remove(i)
            ranks_pass.insert(where,12)
        elif i == 'K':
            where = ranks_pass.index(i)
            ranks_pass.remove(i)
            ranks_pass.insert(where,13)
        elif i == 'T':
            where = ranks_pass.index(i)
            ranks_pass.remove(i)
            ranks_pass.insert(where,10) 
        else:
            where = ranks_pass.index(i)
            ranks_pass.remove(i)
            ranks_pass.insert(where,int(i))

    
    ranks_passA = ranks_pass.copy()
    for i in ranks_passA:
        if i == 1:
            where = ranks_passA.index(i)
            ranks_passA.remove(i)
            ranks_pass.insert(where,14)   
    
    # Sorting the ranks:    
    
    ranks_pass.sort()
    ranks_passA.sort()
    
    # Transforming the int list in a string:
   
    for c in ranks_pass:
        ranksStr+= str(c)
    for c in ranks_passA:
        ranksStr2+= str(c)
    
    # Checking if the rank string is in the sequence string:
    
    if ranksStr in sequence and Fchecker == 1:
        print("You have a straight flush!")
        who.points+=8
    elif ranksStr in sequence and Fchecker == 0:
        print("You have a straight!")
        who.points+=4

    # Second checker, whenever Ace is 14.    

    if ranksStr2 in sequence and Fchecker == 1:
        print("You have a straight flush!")
        who.points+=8
    elif ranksStr2 in sequence and Fchecker == 0:
        print("You have a straight!")
        who.points+=4
    elif ranksStr2 == '1011121314' and Fchecker == 1:
        print("You have a Royal Flush!")
        who.points+=9
    
    if who.points == 0:
        print("You have no games.")

def playerOptions(who):
    global foldedPlayers    
    if round1.raised == False:
        options = [1,2,3]
        print("Your current wallet is ${}.".format(who.wallet))
        print("Your current bet is ${}.".format(who.currentBet))
        print("Type your choice!\n1. Raise\n2. Check\n3. Fold")
        choice = int(input())
        while choice not in options:
            print("Error! You have to choose one of the options above!")
            print("Type your choice!\n1. Raise\n2. Check\n3. Fold")
            choice = int(input())
        
        if choice == 1:
            amount = int(input("Type your raise amount."))
            round1.pot+=amount
            who.wallet-=amount
            who.currentBet+=amount
            round1.raiseAmount+= amount
            print("You raised. Your current wallet is ${}.".format(who.wallet))
            round1.raised = True

        elif choice == 2:
            print("You checked.")
               
        elif choice == 3:
            print("You folded.")
            who.state = 'F'
            foldedPlayers+=1
    else:
        options = [1,2]
        
        if who.currentBet!=round1.raiseAmount:
            print("There's a raise of {} to be equaled.".format(round1.raiseAmount))
            print("Your current wallet is ${}.".format(who.wallet))
            print("Your current bet is ${}.".format(who.currentBet))
            print("Type your choice!\n1. Bet\n2. Fold")
            choice = int(input())
            
            while choice not in options:
                print("Error! You have to choose one of the options above!")
                print("Type your choice!\n1. Bet\n2. Fold")
                choice = int(input())
        
            if choice == 1:
                amount = round1.raiseAmount - who.currentBet
                round1.pot+=amount
                who.wallet-=amount
                who.currentBet+=amount
                print("You equaled the bet. Your current wallet is ${}.".format(who.wallet))
            
            elif choice == 2:
                print("You folded.")
                who.state = 'F'
                foldedPlayers+=1 



playersList = []
global foldedPlayers
foldedPlayers = 0

print("----x----\nWELCOME TO POKER'N'PYTHON\n----x----")

number = int(input("Type the number of players. It can't be over than 8."))
while number>8:
    print("Error! The number of players can't be over than 8.")
    number = int(input("Type the number of players. It can't be over than 8."))


createPlayers()
round1 = RoundGenerator(0,False)
round1.tableGen()

print("Handing out cards...")
round1.firstReveal()
roundProgress(round1.firstReveal())

if foldedPlayers == len(playersList)-1:
    winner()
    endRound()

else:
    print("Second round starting...")
    round1.secondReveal()
    roundProgress(round1.secondReveal())
    if foldedPlayers == len(playersList)-1:
        winner()
        endRound()
    else:
        print("Last round starting...")
        round1.thirdReveal()
        roundProgress(round1.tableSet)
        winner()
        endRound()