class Player(object):
    def __init__(self, accBal=1000, wins=0, losses=0, draws=0, busts=0, bet=0,hand=[]):
        self.accBal = accBal
        self.wins   = wins
        self.losses = losses
        self.draws  = draws
        self.busts  = busts
        self.bet    = bet
        self.hand   = hand
        
    #method to add or remove account money
    def changeBal(self, amt):
        self.accBal += amt
        
    #Change count for wins etc
    def updateCount(self, typ):
        if  typ == "win":
            self.wins += 1
        
        elif typ == "loss":
            self.losses += 1
            
        elif typ == "draw":
            self.draws += 1
        else:
            self.busts += 1
    
    #Print Status
    def printStatus(self):
        print("""   
Account Balance:  ${}
Number of Wins:   {}
Number of Losses: {}
Number of Draws:  {}
Number of Busts:  {}
        """.format(self.accBal, self.wins, self.losses, self.draws, self.busts))
    
    #Update the players hand when dealt a card
    def updateHand(self, card):
        self.hand.append(card)
    
    def clearHand(self):
        self.hand = []
        
    def showHand(self):
        print(self.hand)
        
    #Betting    
    def betAmount(self, amt):
        self.bet = amt