import Player
import Round
import random

# This file will be used to create many different golf players and individual rounds for those players 
# TODO:
#       Create some big data, Talking 5000 players with 300 rounds each
#       When creating these players need to develop a probability to get some more genuine looking scores *although this isn't important it would be cool to code up*
print(4*"\n")
john = Player.Player("John X", 19)
print(john)

for i in range(200):
    #creating random scores for the player 
    rating = round(random.uniform(67.1, 78.9), 1)
    score = int(random.randint(-5,10) + rating)
    putts = random.randint(24, 40)
    gir = random.randint(6, 15)
    teeA = random.randint(4, 18)

    john.addRound(Round.Round(rating, score, putts, gir, teeA))



john.printAllRounds()
john.printHandicapRounds()
print(john)
john.bestTournament(4) 
john.bestPutts(4)
john.bestIndex(20)

print()