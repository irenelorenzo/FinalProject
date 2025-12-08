import pyxel

class Truck:
    """This is a class to represent the truck. In the game, there will only be one truck. When there are 8 packages in
    the truck, it will move out of frame and become the initial picture again """
    # First, we will define the __init__ method to initialise the attributes needed for the truck
    def __init__(self):
        """This is the __init__ function for the truck"""
        self.package_count = 0 # +1 every time a package collides with Luigi on last level (aka reaches truck)
        self.x_image = 0 # x-coordinate of image bank for sprites
        self.y_image = 0 # y-coordinate of image bank for sprites
        self.x = 0 # x-coordinate of truck on tilemap when resting (not delivering)
        self.y = 56 # y-coordinate of truck on tilemap when resting
        self.delivering = False # Will be set to True to start the delivery process
        self.package_added = False # Will be set to true when a package reaches the truck, used in the main code to
                                   # determine if package needs to reappear at conveyor0
        self.delivery_counter = 0 # this will be updated to time the package being away delivery
        self.add_score = False # This variable will be set to true every time the truck goes out for delivery
                               # and will be used to add 10 to the total score

    # The only attribute modified in the main code is truck.package_added, which is why it is the only one which will
    # have properties and setters

    @property
    def package_added(self) -> bool:
      return self.__package_added

    @package_added.setter
    def package_added(self, package_added: bool):
        if not isinstance(package_added, bool):
            raise TypeError("'package_added' must be a boolean")
        else:
            self.__package_added = package_added



    # Now that the properties and setters have been established, the rest of the methods can be defined

    def added_package(self, last_conveyor_collision: bool):
        """This is a method for when a new package reaches the truck"""
        if last_conveyor_collision: # If package has reached truck
            self.package_count += 1 # Package is added to counter
            self.y_image += 32 # Image bank coordinates change to truck sprite with +1 package
            self.package_added = True

    def delivery_start(self):
        """This is a method to trigger the delivery when there are 8 packages on the truck"""
        if self.package_count == 8:
            self.delivering = True
            self.add_score = True
            self.x_image = 48 # x-coordinates of sprite with 8 packages
            self.y_image = 96 # y-coordinates of sprite with 8 packages
            self.package_count = 0 # Reset the package count so that another delivery can occur

    def deliver(self):
        """This is the method that graphically represents the truck leaving to deliver the packages"""
        if self.delivering and self.delivery_counter < 48: # It takes 48 pixels for the truck to no longer be visible
            if self.delivery_counter == 1:
                self.add_score = False # So that 10 points are added to the score only once
            self.x -= 1 # Truck moves 1 pixel to the left (leaving the screen)
            self.delivery_counter += 1 # Since a for loop can't be implemented inside a class without everything
                                       # happening at once in the main code, this counter is implemented for the truck
                                       # to move 48 pixels, one at a time


    def delivery_end(self):
        """This is a method for when the truck comes back from delivery"""
        if self.delivering and 48 <= self.delivery_counter < 96:
            self.x += 1 # Moving one pixel to the right at a time (back into the screen)
            self.delivery_counter += 1 # Keeping the same counter as in deliver() for simplicity
            self.y_image = 128 # y-coordinate in image bank of image with driver in truck but no packages
        elif self.delivery_counter == 96: # Once truck reaches original position, everything resets
            self.delivering = False # No longer delivering (won't trigger deliver() and delivery_end() unless there are
                                    # 8 packages on truck)
            self.package_count = 0 # No packages at truck
            self.x_image = 0 # Image of empty truck
            self.y_image = 0
            self.delivery_counter = 0 # Sets back to 0 to prepare for new delivery

    # Finally, the update and draw methods

    def update(self, last_conveyor_collision: bool):
        """This method will update the state of the truck"""
        self.added_package(last_conveyor_collision)
        self.delivery_start()
        self.deliver()
        self.delivery_end()

    def draw(self):
        """This method will display the truck on the screen"""
        pyxel.blt(self.x, self.y, 1, self.x_image, self.y_image, 50, 34, 0)

