# TODO: Grow the round attributes to include course names, locations, the dates of the round.
#       Include more scoring features: eagles, birdies, pars, bogeys+.
#       More specifics for tee accuracy
#       Formulas to determine other round statistics like chipping, approach accuracy,          
class Round:

    def __init__(self, courseRating, score, putts, gir, teeA):
        self.courseRating = courseRating
        self.score = score
        self.putts = putts
        self.gir = gir
        self.teeA = teeA
        
    def getPutts(self):
        return self.putts
        
    def getScore(self):
        return self.score

    def getGIRPerc(self):
        return self.gir/18 * 100

    def getTeeAccuracy(self):
        return self.teeA/18 * 100

    def calculateIndex(self):
        return self.score - self.courseRating
    
    def getIndex(self):
        index = self.score - self.courseRating
        if(index < 0):
            return f"+{index * -1:3.1f}"
        else:
            return f"{index:4.1f}"
    
    def __str__(self):
        return f"Score: {self.score:<3} | Putts: {self.putts:<2} | GIR: {self.getGIRPerc():3.0f}% | Tee Accuracy: {self.getTeeAccuracy():3.0f}% | Index: {self.getIndex()}"
