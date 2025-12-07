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
        self.x_image = 0
        self.y_image = 0
        self.x = 0
        self.y = 56
        self.delivering = False
        self.package_added = False
        self.delivery_counter = 0 # this will be updated to time the package being away delivery
        self.add_score = False # This variable will be set to true every time the truck goes out for delivery
                               # and will be used to add 10 to the total score

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
            self.y_image += 32
            self.package_added = True

    def delivery_start(self):
        """This is a method to establish when the truck goes out for delivery"""
        if self.package_count == 8:
            self.delivering = True
            self.add_score = True
            self.x_image = 48
            self.y_image = 96
            self.package_count = 0 # Reset the package count so that another delivery can occur

    def deliver(self):
        """This is the method that graphically represents the truck delivering the packages"""
        if self.delivering and self.delivery_counter < 48:
            if self.delivery_counter == 1:
                self.add_score = False
            self.x -= 1
            self.delivery_counter += 1


    def delivery_end(self):
        """This is a method for when the truck comes back from delivery"""
        if self.delivering and 48 <= self.delivery_counter < 96:
            self.x += 1
            self.delivery_counter += 1
            self.y_image = 128
        elif self.delivery_counter == 96:
            self.delivering = False
            self.package_count = 0
            self.x_image = 0
            self.y_image = 0



    def update(self, last_conveyor_collision):
        """This method will update the state of the truck"""
        self.added_package(last_conveyor_collision)
        self.delivery_start()
        self.deliver()
        self.delivery_end()

    def draw(self):
        """This method will display the truck on the screen"""
        pyxel.blt(self.x, self.y, 1, self.x_image, self.y_image, 50, 34, 0)

