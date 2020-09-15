#import all methods from the gameMethods file
from gameMethods.gameMethods import *

print("Welcome to BlackJack! To Win you must reach $3000!")
#Initialise create new player and deck
deck, player, game = initialise()

print("Would you like to start now? Y/N")

output = checkYN(input())
# clear_output()
if output == "y":
    print("Dealing you the first card...")
    gameSession(output,deck,player,game)

print("Game Exiting..")
