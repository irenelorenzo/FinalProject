import pyxel
# Reminders:
# Get the truck to count the packages that reach it (check collisions on last level)
# When this count == 8, initiate delivery and rest. Also add ten points to score
class Truck:
    """This is a class to represent the truck. In the game, there will only be one truck. When there are 8 packages in
    the truck, it will move out of frame and become the initial picture again """
    # First, we will define the __init__ method to initialise the attributes needed for the truck
    def __init__(self):
        """This is the __init__ function for the truck"""
        self.package_count = 0
        self.image = 0
        self.x = 0
        self.y = 56
        self.delivering = False
        self.package_added = False

    @property
    def y(self):
      return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("The y-coordinate must be an integer")
        # no condition established for the bounds of the value of y, since they are established in the init function
        else:
            self.__y = y

    def added_package(self, last_conveyor_collision: bool):
        """This is a method for when a new package reaches the truck"""
        if last_conveyor_collision:
            self.package_count += 1
            self.image += 32
            self.package_added = True

    def delivery(self):
        self.delivering = True
        if self.package_count == 8:
            for _ in range(48): # When the truck has eight packages, move truck out of screen 1 pixel at a time
                self.x -= 1
            self.package_count = 0
            self.image = 0
            for _ in range(48): # Bring truck back into screen
                self.x += 1

    # Def __eq__ method to check if package is at truck (compare package at truck with True)


    def update(self, last_conveyor_collision):
        self.added_package(last_conveyor_collision)

    def draw(self):
        """This method will display the truck on the screen"""
        pyxel.blt(self.x, self.y, 1, 0, self.image, 50, 34, 0)
