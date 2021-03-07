import random
from fullDeck import fullDeck, RoundGenerator, deck1

class Player(fullDeck):
    def __init__(self, wallet: int, name: str, state: str):
        fullDeck.__init__(self)
        self.hand = []
        self.points = 0
        self.wallet = wallet
        self.currentBet = 0
        self.name = name
        self.state = 'P'   # 'P' for playing, 'F' for folded.
        self.allCards = []

    def Shuffle(self):
        for c in range(2):
            which = random.choice(deck1.cards)
            self.hand.append(which)
            deck1.removeCard(which)
    
    def printCards(self):
        print("----x----")
        for card in self.hand:
            print(card, end=' ')
        
        print("\n","----x----")

    def roundReset(self):
        self.state = 'P' # Olhar

    def handReset(self):
        self.hand = []
        self.points = 0
        self.currentBet = 0
        self.state = 'P'