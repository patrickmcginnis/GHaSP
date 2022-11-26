import random
import Player
import Round


# This file will be used to create many different golf players and individual rounds for those players 
# TODO:
#       Create some big data, Talking 5000 players with 300 rounds each
#       When creating these players need to develop a probability to get some more genuine looking scores *although this isn't important it would be cool to code up*
def print_streak(streak):
    for i in streak:
        print(i)

print(2*"\n")
john = Player.Player("John X", 19)
print(john)

print("...Adding Rounds\n")
for i in range(20000):
    #creating random scores for the player 
    rating = round(random.uniform(67.1, 78.9), 1)
    score = int(random.randint(-5,10) + rating)
    putts = random.randint(24, 40)
    gir = random.randint(6, 15)
    teeA = random.randint(4, 18)

    john.add_round(Round.Round(i, rating, score, putts, gir, teeA))


john.print_handicap_rounds() # should always show recent most 20
print(john) # check out his updated stats
worst_window = john.sliding_window(4, 0, "score")
best_window = john.sliding_window(4, 1, "score")
print("\nBest Window:")
print_streak(best_window)
print("Totals: " + str(Player.sum_streak(best_window, "score")) + "\n")
print("Worst Window:")
print_streak(worst_window)
print("Totals: " + str(Player.sum_streak(worst_window, "score"))+ "\n")

print()