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
        self.x_images = [8, 18]  # this list will store the x-coordinates within the image bank where the score sprites are
        self.y_images = [147, 147]

    def conveyor_score_update(self, package_at_new_conveyor):
        """This is a method to update the score when a package goes to a new conveyor"""
        if package_at_new_conveyor:
            self.total_score += 1


    def truck_score_update(self, truck_delivering):
        """This is a method to update the score when the truck goes out for delivery"""
        if truck_delivering:
            self.total_score += 10

    #def graphical_representation(self):
        """This is a method that will be used to represent the score graphically"""
        #x_images = []
        #string_score = str(self.total_score)
        #for index in range(len(string_score)):





    def update(self, package_at_new_conveyor, truck_delivering):
        """This method will be used to update the score"""
        self.conveyor_score_update(package_at_new_conveyor)
        self.truck_score_update(truck_delivering)
        self.graphical_representation()

    def draw(self):
        """This method will be used to draw the score, with the info obtained in the graphical_representation method"""
        pyxel.blt(240,3, 0, self.x_images[0], self.y_images[0], 8, 11, 0)
        pyxel.blt(240, 3, 0, self.x_images[1], self.y_images[1], 8, 11, 0)