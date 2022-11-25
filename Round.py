# TODO: Grow the round attributes to include course names, locations, the dates of the round.
#       Include more scoring features: eagles, birdies, pars, bogeys+.
#       More specifics for tee accuracy
#       Formulas to determine other round statistics like chipping, approach accuracy,          
class Round:

    def __init__(self, id, courseRating, score, putts, gir, teeA):
        self.u_id = id
        self.course_rating = courseRating
        self.score = score
        self.putts = putts
        self.gir = gir
        self.tee_a = teeA
        
    def get_putts(self):
        return self.putts

    def get_score(self):
        return self.score

    def get_gir_perc(self):
        return self.gir/18 * 100

    def get_tee_accuracy(self):
        return self.tee_a/18 * 100

    def calculate_index(self):
        return self.score - self.course_rating
    
    def get_index(self):
        index = self.score - self.course_rating
        if(index < 0):
            return f"+{index * -1:3.1f}"
        else:
            return f"{index:4.1f}"
    
    def __str__(self):
        return f"Date: {self.u_id:<4} Score: {self.score:<3} | Putts: {self.putts:<2} | GIR: {self.get_gir_perc():3.0f}% | Tee Accuracy: {self.get_tee_accuracy():3.0f}% | Index: {self.get_index()}"
