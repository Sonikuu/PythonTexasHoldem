class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Player:
    def __init__(self, name, isai, chips):
        self.name = name
        self.isai = isai
        self.cards = []
        self.mood = 0
        self.chips = chips
        self.folded = False
        self.betted = 0
    def clearCards(self):
        self.cards = []
        self.mood = 0
        self.folded = False
        self.betted = 0

    def takeChips(self, amount):
        return max([0, amount])