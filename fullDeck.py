import random

suits = 'CDHS'
nums = 'AKQJT98765432'

class fullDeck():
    def __init__(self):
        self.cards = []
        for c in suits:
            for i in nums:
                self.cards.append(c + i)

    def printDeck(self):
        for card in self.cards:
            print(card, end=' ') 
    
    def removeCard(self,which):
        self.cards.remove(which)

    def restartDeck(self):
        self.cards = []
        for c in suits:
            for i in nums:
                self.cards.append(c + i)

class RoundGenerator(fullDeck):
    def __init__(self, pot: int, raised: bool):
        fullDeck.__init__(self)
        self.tableSet = []
        self.pot = pot
        self.raised = raised
        self.raiseAmount = 0

    def tableGen(self):
        for c in range(5):
            which = random.choice(deck1.cards)
            self.tableSet.append(which)
            deck1.removeCard(which)

    def firstReveal(self): 
        firstFlop = []
        print("THE TABLE'S CARDS ARE:")
        for c in range(3):
            firstFlop.append(self.tableSet[c])
        for c in range(3):
            print(firstFlop[c],end=' ')
        print("X X")
        
        return firstFlop
        
    def secondReveal(self):
        secondFlop = []
        print("THE TABLE'S CARDS ARE:")
        for c in range(4):
           secondFlop.append(self.tableSet[c])
        for c in range(4):
            print(secondFlop[c],end=' ')
        print("X")
        
        return secondFlop
    
    def thirdReveal(self):
        print("THE TABLE'S CARDS ARE:")
        for c in range(5):
            print(self.tableSet[c], end=' ')

    def partialReset(self):
        self.raised = False
        self.raiseAmount = 0
    
    def fullReset(self):
        self.tableSet = []
        self.pot = 0
        
    
deck1 = fullDeck()