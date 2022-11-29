import Round

# TODO: Grow the player attributes to include first/last names, origin country, etc. 
#       Add other funcitonality for stats\
#       The 'best functions' can be turned into a new function or removed as they are for printing results and
#       

#helper functions to calcuate totals from a short list 
def sum_streak(list, stat):
    sum = 0
    match stat:
        case "score":
            for i in list:
                sum += i.get_score()
        case "index":
            for i in list:
                sum += i.calculate_index()
        case "putts":
            for i in list:
                sum += i.get_putts()
    return sum

# Player class allows for unique stat tracking
class Player:
    rounds_played = 0
    rounds = []
    handicap_rounds = [] # A handicap is calculated from the avg index's of your most recent 20 rounds
    cap = 0
    avg_putts = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Currently learning priority queues for top scores
    def calculate_top_x(self, k, stat):     # Sort algorithm to find top k rounds for the selected stat
        if(self.get_rounds_played() < k):
            print("Not enough rounds")
            return -1 
    
    def sliding_window(self, k, type, stat):    #k is size of window or the length of the streak, type is best/worst window, stat is the stat to measure
        if(self.get_rounds_played() < k):
            print("Not enough rounds")
            return -1
        best_streak = self.rounds[:k].copy()        # take the first k elements and store a copy
        current_window = self.rounds[:k].copy()     # create a copy to iterate over *I think I can just use reference here*
        sum_stat = sum_streak(best_streak, stat)    
        max_sum_stat = sum_stat
        for r in self.rounds[k:]:                   #start moving the window
            current_window.pop(0)
            current_window.append(r)
            match stat:                             
                case "score":
                    sum_stat = sum_stat - current_window[0].get_score() + r.get_score()     
                    if(type):                                                              
                        if(sum_stat <= max_sum_stat):
                            max_sum_stat = sum_stat
                            best_streak = current_window.copy()                             # make a copy of the new window of rounds we want as conditions were met
                    else:
                        if(sum_stat >= max_sum_stat):
                            max_sum_stat = sum_stat
                            best_streak = current_window.copy()
                case "index":
                    sum_stat = sum_stat - current_window[0].calcualte_index() + r.calculate_index()
                    if(type):
                        if(sum_stat <= max_sum_stat):
                            max_sum_stat = sum_stat
                            best_streak = current_window.copy()
                    else:
                        if(sum_stat >= max_sum_stat):
                            max_sum_stat = sum_stat
                            best_streak = current_window.copy()
                case "putts":
                    sum_stat = sum_stat - current_window[0].get_putts() + r.get_putts()
                    if(type):
                        if(sum_stat <= max_sum_stat):
                            max_sum_stat = sum_stat
                            best_streak = current_window.copy()
                    else:
                        if(sum_stat >= max_sum_stat):
                            max_sum_stat = sum_stat
                            best_streak = current_window.copy()
        return best_streak

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
        print(85 * "-")
        for r in self.rounds:
            print(r)
        print(85 * "-")

    def print_handicap_rounds(self):
        print("Printing handicap rounds:")
        print(85 * "-")
        for hr in self.handicap_rounds:
            print(hr)
        print(85 * "-")

    def __str__(self):
        return f"Name: {self.name} | Age: {self.age} | Handicap: {self.get_handicap()}"


