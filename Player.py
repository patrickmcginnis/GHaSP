import Round

# TODO: Grow the player attributes to include first/last names, origin country, etc. 
#       Add other funcitonality for stats\
#       The 'best functions' can be turned into a function somehow
#       The 'sum' helper functions can be busted down into a single function and just pass the function with the lists.

#helper functions to calcuate totals
def sum_scores(r):
    sum = 0
    for i in r:
        sum += i.get_score()
    return sum

def sum_index(r):
    sum = 0.0
    for i in r:
        sum += i.calculate_index()
    return sum
def sums_putts(r):
    sum = 0
    for i in r:
        sum += i.get_putts()
    return sum

class Player:
    rounds_played = 0
    rounds = []
    handicap_rounds = [] # A handicap is calculated from the avg index of your most recent 20 rounds
    cap = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Algortihm uses sliding window to calculate the best consecutive rounds over k period of time
    def calculate_streaks(self, k, stat):

        if(self.get_rounds_played() < k):
            print("Not enough rounds")
            return -1 
        streak_rounds = self.rounds[:k]
        best_streak = streak_rounds.copy() # make sure to pass by value and not by reference
        for i in self.rounds[k:]:
            streak_rounds.pop(0)
            streak_rounds.append(i)
            match stat:                 # need to know which stat we are calculating for the streak
                case "score":
                    if(sum_scores(streak_rounds) < sum_scores(best_streak)):
                        best_streak = streak_rounds.copy()
                case "index":
                    if(sum_index(streak_rounds) < sum_index(best_streak)):
                        best_streak = streak_rounds.copy()
                case "putts":
                    if(sums_putts(streak_rounds) < sums_putts(best_streak)):
                        best_streak = streak_rounds.copy()   
        return best_streak 
    
    def best_tournament(self, k):
        print("Printing best %d consecutive rounds based on score:" % k)
        streak = self.calculate_streaks(k, "score")
        print("With a total of ",  sum_scores(streak))
        print(70 * "-")
        for i in range(k):
            print(streak[i]) 
        print(70 * "-")

    def best_putts(self, k):
        print("Printing best %d consecutive rounds based on putting:" % k)
        streak = self.calculate_streaks(k, "putts")
        print("With a total of ",  sums_putts(streak))
        print(70 * "-")
        for i in range(k):
            print(streak[i]) 
        print(70 * "-")

    def best_index(self, k):
        print("Printing best handicap acheived through %d rounds:"% k)
        streak = self.calculate_streaks(k, "index")
        dex = sum_index(streak)/k
        if(dex < 0):
            i =  f"+{dex * -1:3.1f}"
        else:
            i =  f"{dex:4.1f}"
        print("With an index of: ", i)
        print(70 * "-")
        for i in range(k):
            print(streak[i]) 
        print(70 * "-")

    def calculate_handicap(self):
        sum = 0
        for i in self.handicap_rounds:
            sum += i.calculate_index()
        self.cap = sum / len(self.handicap_rounds)
    
    def add_round(self, round):
        self.rounds.append(round)
        self.rounds_played += 1

        if len(self.handicap_rounds) > 19:    # implelement a queue to keep track of the LATEST 20 rounds
            self.handicap_rounds.pop(0)
            self.handicap_rounds.append(round)
        else:
            self.handicap_rounds.append(round)
        self.calculate_handicap()           # calculate new handicap as rounds are added
    

    def get_rounds_played(self):
        return self.rounds_played 

    
    def get_handicap(self):
        if(self.cap < 0):
            return f"+{self.cap * -1:2.1f}"
        else:
            return f"{self.cap:2.1f}"
        
    def print_all_rounds(self):
        print("Printing all %d rounds played:" % (self.get_rounds_played()))
        print(70 * "-")
        for r in self.rounds:
            print(r)
        print(70 * "-")

    def print_handicap_rounds(self):
        print("Printing handicap rounds:")
        print(70 * "-")
        for hr in self.handicap_rounds:
            print(hr)
        print(70 * "-")

    def __str__(self):
        return f"Name: {self.name} | Age: {self.age} | Handicap: {self.get_handicap()}"


