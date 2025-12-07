import pyxel
# Reminders:
# Create a methods to modify score according to external variables
# Create a method to graphically represent score
# Set property and setter for score

class Score:
    """This class will be used to represent the score of the game"""
    def __init__(self):
        """This is the init method for the score"""
        self.total_score = 0
        self.modify_score = True # this variable will determine if the graphical determination of the score needs to be
                                 # modified

    def conveyor_score_update(self, package_at_new_conveyor):
        """This is a method to update the score when a package goes to a new conveyor"""
        if package_at_new_conveyor:
            self.total_score += 1
            self.modify_score = True


    def truck_score_update(self, truck_delivering):
        """This is a method to update the score when the truck goes out for delivery"""
        if truck_delivering:
            self.total_score += 10
            self.modify_score = True


    def update_conveyor_score(self, next_conveyor):
        """This method will be used to update the score"""
        self.conveyor_score_update(next_conveyor)

    def update_truck_score(self, truck_delivering):
        self.truck_score_update(truck_delivering)

    def draw(self):
        """This method will be used to draw the score, with the info obtained in the graphical_representation method"""
        pyxel.text(240, 3, f"{self.total_score:03d}", 7)