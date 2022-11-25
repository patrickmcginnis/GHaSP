import Round

# TODO: Grow the player attributes to include first/last names, origin country, etc. 
#       Add other funcitonality for stats\
#       The 'best functions' can be turned into a function somehow
#       The 'sum' helper functions can be busted down into a single function and just pass the function with the lists.

#helper functions to calcuate totals
def sumScores(r):
    sum = 0
    for i in r:
        sum += i.getScore()
    return sum

def sumIndex(r):
    sum = 0.0
    for i in r:
        sum += i.calculateIndex()
    return sum
def sumPutts(r):
    sum = 0
    for i in r:
        sum += i.getPutts()
    return sum

class Player:
    roundsPlayed = 0
    rounds = []
    handicapRounds = [] # A handicap is calculated from the avg index of your most recent 20 rounds
    cap = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Algortihm uses sliding window to calculate the best consecutive rounds over k period of time
    def calculateStreaks(self, k, stat):
        if(self.getRoundsPlayed() < k):
            print("Not enough rounds")
            return -1 
        streakRounds = self.rounds[:k]
        bestStreak = streakRounds.copy() # make sure to pass by value and not by reference
        for i in self.rounds[k:]:
            streakRounds.pop(0)
            streakRounds.append(i)
            match stat:
                case "score":
                    if(sumScores(streakRounds) < sumScores(bestStreak)):
                        bestStreak = streakRounds
                case "index":
                    if(sumIndex(streakRounds) < sumIndex(bestStreak)):
                        bestStreak = streakRounds
                case "putts":
                    if(sumPutts(streakRounds) < sumPutts(bestStreak)):
                        bestStreak = streakRounds      
        return bestStreak 
    
    def bestTournament(self):
        print("Printing best 4 consecutive rounds based on score:")
        print("With a total of ",  sumScores(streak))
        print(70 * "-")
        streak = self.calculateStreaks(4, "score")
        for i in range(4):
            print(streak[i]) 
        print(70 * "-")

    def bestPutts(self):
        print("Printing best 4 consecutive rounds based on putting:")
        print("With a total of ",  sumPutts(streak))
        print(70 * "-")
        streak = self.calculateStreaks(4, "putts")
        for i in range(4):
            print(streak[i]) 
        print(70 * "-")

    def bestIndex(self):
        print("Printing best handicap acheived:")
        print("With an index of %2.1f" %  (sumIndex(streak)/20))
        print(70 * "-")
        streak = self.calculateStreaks(20, "index")
        for i in range(20):
            print(streak[i]) 
        print(70 * "-")

    def calculateHandicap(self):
        sum = 0
        for i in self.handicapRounds:
            sum += i.calculateIndex()
        self.cap = sum / len(self.handicapRounds)
    
    def addRound(self, round):
        self.rounds.append(round)
        self.roundsPlayed += 1

        if len(self.handicapRounds) > 19:    # implelement a queue to keep track of the LATEST 20 rounds
            self.handicapRounds.pop(0)
            self.handicapRounds.append(round)
        else:
            self.handicapRounds.append(round)
        self.calculateHandicap();           # calculate new handicap as rounds are added
    
    def getRoundsPlayed(self):
        return self.roundsPlayed 

    
    def getHandicap(self):
        if(self.cap < 0):
            return f"+{self.cap * -1:2.1f}"
        else:
            return f"{self.cap:2.1f}"
        
    def printAllRounds(self):
        print("Printing all %d rounds played:" % (self.getRoundsPlayed()))
        print(70 * "-")
        for r in self.rounds:
            print(r)
        print(70 * "-")

    def printHandicapRounds(self):
        print("Printing handicap rounds:")
        print(70 * "-")
        for hr in self.handicapRounds:
            print(hr)
        print(70 * "-")

    def __str__(self):
        return f"Name: {self.name} | Age: {self.age} | Handicap: {self.getHandicap()}"


