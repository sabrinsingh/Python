class GameStatus(object):
    def __init__(self, endGame=False, roundStatus=None):
        self.endGame=endGame
        self.roundStatus=roundStatus
        
        
    def checkGameStatus(self, player): #player is an object
        #checks account to see if we have won or have $0
        #and returns endgame value true or false
        if player.accBal >= 3000:
            print("Congratulations You have won the game! As your account balance is greater than or equal to $3000")
            self.endGame = True
        elif player.accBal <= 0:
            print("Your account balance is less than or equal to $0, You have lost")
            self.endGame = True
        else:
            self.endGame = False

    def updateRoundStatus(self, p): #where p is the player.hand
        #have we won the round to be replaced by AI logic 
        #currently we will just put a dummy in here that says if value is higher than 17 we win
        A = p.count("A");two = p.count("2");three = p.count("3");four = p.count("4");five = p.count("5");
        six = p.count("6");seven = p.count("7");eight = p.count("8");nine = p.count("9");ten = p.count("10");
        J = p.count("J");Q = p.count("Q");K = p.count("K");
        
        total = two*2 + three*3 + four*4 + five*5 + six*6 + seven*7 + eight*8 + nine*9\
                  + ten*10 + J*10 + Q*10 + K*10
        
        #Account for Ace being 1 or 11
        if (21>= total + A*1 > 16) or (21>= total + A*11 > 16):
            self.roundStatus = "win"
        elif total == 16:
            self.roundStatus = "draw"
        else:
            self.roundStatus = "loss"