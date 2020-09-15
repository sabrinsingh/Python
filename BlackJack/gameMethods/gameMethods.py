from gameClasses.deck import Deck
from gameClasses.player import Player
from gameClasses.gameStatus import GameStatus

def initialise():
    deck   = Deck()
    player = Player()
    game   = GameStatus()
    player.printStatus()
    
    return deck, player, game


    
def checkYN(inp):
    while True:
        if inp.lower() in ["y", "n", "yes", "no"]:
            if inp.lower() in ["y", "yes"]:
                return "y"
                break
            else:
                return "n"
                break
        else:
            print("Please enter Y or N, yes or no")
            inp = input()
            
def checkBet(player):
    while True:
        inp = input()
        try: 
            if inp.isdigit and 0<int(inp)<= player.accBal:
                player.betAmount(int(inp))
                break
            else:
                print("Please enter a number that is a whole number and within the range of your account balance")
        except:
            print("Please enter a number that is a whole number and within the range of your account balance")
       
    
def hitOrStand():
    while True:
        inp = input()
        if inp.lower() in ["hit", "stand"]:
            if inp.lower() == "hit":
                return "hit"
                break
            else:
                return "stand"
                break
        else:
            print("Please enter hit or stand")
            continue
    
def checkForBust(p):
    #input will be an array
    A = p.count("A");two = p.count("2");three = p.count("3");four = p.count("4");five = p.count("5");
    six = p.count("6");seven = p.count("7");eight = p.count("8");nine = p.count("9");ten = p.count("10");
    J = p.count("J");Q = p.count("Q");K = p.count("K");
    
    if (A*1 + two*2 + three*3 + four*4 + five*5 + six*6 + seven*7 + eight*8 + nine*9\
        + ten*10 + J*10 + Q*10 + K*10) > 21:
        return True
    else:
        return False


def checkHandOk(player):
    #checks to see if the hand is ok to continue.. ie not bust or over five cards
    if len(player.hand)==5: 
        return "limit_reached"
    #check if hand is Busted
    elif checkForBust(player.hand):
        return "bust"
    elif len(player.hand)==5 and checkForBust(player.hand):
        return "bust_limit"
    else:
        return "ok"

def updateWinLoss(status, player):
    if status == "win":
        #update internal tally
        player.updateCount("win")
        print("Player has won this round!")

        #Update accountBal
        player.changeBal(player.bet*2)

    elif status == "draw":
        #update internal tally
        player.updateCount("draw");
        print("Player has drawn this round")

        #Update accountBal
        player.changeBal(player.bet)

    else:
        player.updateCount("loss")
        print("Player has lost this round... :(")
            
def aRound(deck, player, game):
    import time
    while True:
        #this is where a round of blackjack happens
        #Check hand in round
        if checkHandOk(player)=="ok":
            print("Would you like to hit or stand?")
            output = hitOrStand()
            
            if output == "hit":
                print("Dealing you a card..")
                #get a card from the deck 
                card = deck.takeCard()
                #put it in the players hand
                player.updateHand(card)
                player.showHand()
            else:
                #Player Stand check for win condition
                print("Checking your hand")
                game.updateRoundStatus(player.hand)
                updateWinLoss(game.roundStatus, player)
                
                break
                
        elif checkHandOk(player) == "bust":
            print("Hand is bust.. checking status and updating your profile")
            game.updateRoundStatus(player.hand)
            updateWinLoss(game.roundStatus, player)
            player.updateCount("bust")
            
            break
            
        elif checkHandOk(player) == "limit_reached":
            print("Limit of 5 is reached.. checking status..")
            game.updateRoundStatus(player.hand)
            updateWinLoss(game.roundStatus, player)
            
            break
            
        elif checkHandOk(player) == "bust_limit":
            print("Limit of 5 is reached and you have busted.. checking status..")
            game.updateRoundStatus(player.hand)
            updateWinLoss(game.roundStatus, player)
            player.updateCount("bust")
            break
            
        else:
            break
    

def gameSession(output,deck,player,game):
    import time
    while True:
        #Betting 
        print("How much do you want to bet on this round?")
        checkBet(player)
        #takebet from balance
        player.changeBal(-player.bet)
        
        #Initial dealing of the first card
        card = deck.takeCard()
        #put it in the players hand
        player.updateHand(card)
        player.showHand()
        
        aRound(deck, player, game)
        #wait 3 seconds before clearing the round
        
        time.sleep(3)
        # clear_output()
        player.printStatus()
        
        #reset hand and deck
        player.clearHand()
        deck.resetDeck()
        
        #check Game Status, cond is either true or false, true is end game condition reached
        #false is keep playing
        game.checkGameStatus(player)
        
        
        if game.endGame == False:
            #Need to be able to break gameSession early by quitting after a round finishes
            print("Would you like to play another round? Y/N")
            output = checkYN(input())
            if output == "y":
                continue
            else:
                break
        else:
            break