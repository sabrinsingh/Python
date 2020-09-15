class Deck(object):
    #Object Deck Attributes
    def __init__(self):
        #52 Cards
        self.fullDeck = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]*4
        self.cards =    ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]*4
    
    #Define built in methods to be used
    def __len__(self):
        return len(self.cards)
    
    #Take a card out of the deck
    def takeCard(self):
        import random
        c = self.cards.pop(self.cards.index(random.choice(self.cards)))
        return c
    
    #Reset Deck
    def resetDeck(self):
        self.cards = self.fullDeck