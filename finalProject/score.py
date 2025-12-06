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
        self.x_images = [1, 9]  # this list will store the x-coordinates within the image bank where the score sprites are
        self.y_images = [3, 3]
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

    def graphical_representation(self):
        """This is a method that will be used to represent the score graphically"""
        if self.modify_score:
            string_score = str(self.total_score)
            for index in range(len(string_score)):
                number = int(string_score[index])
                for count in range(9):
                    if number == count and number != 0:
                        self.y_images[index] += 16
            self.modify_score = False


    def update(self, next_conveyor, truck_delivering):
        """This method will be used to update the score"""
        self.conveyor_score_update(next_conveyor)
        self.truck_score_update(truck_delivering)
        self.graphical_representation()

    def draw(self):
        """This method will be used to draw the score, with the info obtained in the graphical_representation method"""
        pyxel.blt(240,3, 2, self.x_images[0], self.y_images[0], 8, 11, 0)
        pyxel.blt(248, 3, 2, self.x_images[1], self.y_images[1], 8, 11, 0)