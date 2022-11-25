# This file will be used to create many different golf players and scoring records
class Player:
    rounds = []
    
    def __init__(self, name, age, cap):
        self.name = name
        self.age = age
        self.cap = cap
    
    def __str__(self):
        return f"Name: {self.name} | Age: {self.age} | Handicap: {self.cap}"
        
class Round:

    def __init__(self, score, putts, gir, teeA):
        self.score = score
        self.putts = putts
        self.gir = gir
        self.teeA = teeA


john = Player("John X", 19, 1.3)
john.rounds[i] = Round()

print(john)