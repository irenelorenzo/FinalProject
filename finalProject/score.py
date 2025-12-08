import pyxel

class Score:
    """This class will be used to represent the score of the game"""
    def __init__(self):
        """This is the init method for the score"""
        self.total_score = 0 # This will be updated, depending on if the score is modified because the package has
                             # moved onto the next conveyor or because the truck is out for delivery


    def update_conveyor_score(self, next_conveyor: bool):
        """This method will be used to update the score when a package moves onto the next conveyor"""
        if next_conveyor:
            self.total_score += 1 # 1 point is added when moving to new conveyor

    def update_truck_score(self, truck_delivering: bool):
        """This is a method to update the score when the truck goes out for delivery"""
        if truck_delivering:
            self.total_score += 10 # 10 points are added when truck goes out for delivery

    def draw(self):
        """This method will be used to draw the score"""
        pyxel.text(240, 3, f"{self.total_score:03d}", 7)