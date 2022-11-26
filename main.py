import random
import Player
import Round


# This file will be used to create many different golf players and individual rounds for those players 
# TODO:
#       Create some big data, Talking 5000 players with 300 rounds each
#       When creating these players need to develop a probability to get some more genuine looking scores *although this isn't important it would be cool to code up*
print(4*"\n")
john = Player.Player("John X", 19)
print(john)

for i in range(2000):
    #creating random scores for the player 
    rating = round(random.uniform(67.1, 78.9), 1)
    score = int(random.randint(-5,10) + rating)
    putts = random.randint(24, 40)
    gir = random.randint(6, 15)
    teeA = random.randint(4, 18)

    john.add_round(Round.Round(i, rating, score, putts, gir, teeA))


john.print_handicap_rounds() # should always show recent most 20
print(john)
john.best_tournament(4) 
john.best_putts(4)
john.best_index(20)

print()