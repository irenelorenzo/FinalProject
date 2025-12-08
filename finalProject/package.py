import pyxel

class Package:
    """This class is used to represent the packages"""
    def __init__(self, conveyor: int, level: int, y_image: int, continuity: bool = False):
        """This is the init method for the packages"""
        self.conveyor = conveyor # 0 for conveyor0, 1 for odd conveyors, 2 for even conveyors
        self.level = level # Either 0, 1 or 2 - will be used to determine collisions with characters

        self.x_image = 51  # Add x coordinates of package sprites
        self.y_image = y_image  # Add y coordinates of package sprites (later on, add a 16 to this attribute when middle of belt is reached)
        self.collision = False # Will become true once package collides with characters
        self.fallen = False # Will become false if package falls
        self.continuity = continuity # This attribute describes if the package has not been killed prior to getting to
                                     # its current conveyor. It is set as False at conveyor0, then depends on previous conveyor
        self.limit_reached = False # This will change to true when package reaches conveyor limit
        self.failures = 0 # Counts if package has fallen to determine lives left
        self.visible = True # Used in the draw() function. Will be set to False when hiding the package
        self.has_reset = False
        self.add_score = False # this will become true when package moves to next conveyor. It will be used to update the
                               # the score


    # Now that the class has been initialised, their attributes need properties and setters. We must create them for the
    # attributes conveyor, level, y_image, and continuity

    @property
    def conveyor(self) -> int:
        return self.__conveyor

    @property
    def level(self) -> int:
        return self.__level

    @property
    def y_image(self) -> int:
        return self.__y_image

    @property
    def continuity(self) -> bool:
        return self.__continuity

    @conveyor.setter
    def conveyor(self, conveyor: int):
        possible_values = (0, 1, 2)
        if not isinstance(conveyor, int):
            raise TypeError("'conveyor' must be an integer")
        elif conveyor not in possible_values:
            raise ValueError("'conveyor' must be either 0, 1 or 2")
        else:
            self.__conveyor = conveyor

    @level.setter
    def level(self, level: int):
        possible_values = (0, 1, 2)
        if not isinstance(level, int):
            raise TypeError("'level' must be an integer")
        elif level not in possible_values:
            raise ValueError("'level' must be either 0, 1 or 2")
        else:
            self.__level = level

    @y_image.setter
    def y_image(self, y_image: int):
        if not isinstance(y_image, int):
            raise TypeError("'y_image' must be an integer")
        if not 0 <= y_image <= 88:
            raise ValueError("'y_image' must be between 0 and 88")
        else:
            self.__y_image = y_image

    @continuity.setter
    def continuity(self, continuity: bool):
        if not isinstance(continuity, bool):
            raise TypeError("'continuity' must be a boolean")
        else:
            self.__continuity = continuity

    # Now that all the necessary properties and setters have been created, it is time to establish the methods

    def switch_image(self, x: int):
        """Switches sprite to the next when middle of screen is reached, where x is substituted in main code. Also gets
        package to disappear when it reaches the middle section"""
        if x == 128 and self.y_image != 88: # Does now work when the y-coordinate of the image bank is 88 because that
                                            # the most evolved version of the package
            self.y_image += 16 # Changes y-coordinate of image bank


    def hide_package(self, x: int):
        """This method will hide the package sprite as it goes through the center columns"""
        if 111 <= x <= 136:
                self.visible = False # Since unless visible == True, the draw function won't work, in these coordinates
                                     # of the tilemap the package will be hidden
        else:
                self.visible = True


    def collision_check(self, x: int, limit: int, player_level: int):
        """This method will be used to compare the x-coordinate of the package with the limit of its conveyor"""
        if not self.collision and not self.fallen: # Both variables will be false before the package reaches the limit
                                                   # of the conveyor. After either variable is set to true, it will stop
                                                   # checking to prevent getting stuck in a loop
            if self.conveyor == 0 or self.conveyor == 1: # For conveyor0 and odd conveyors
                if x < limit and self.level == player_level: # Checks if package has passed limit and is on same level as player
                    self.collision = True # Determines package and player have collided (passes package onto next level)
                    self.add_score = True # Determines that a point needs to be added to the score
                elif x < limit: # Here package has passed limit, but was not on the same level as the player
                    self.fallen = True # If package has passed limit and is not on same level as player
                    self.failures += 1 # Add one to failure counter
            else: # For even conveyors (same procedure as before, except being past limit means x > limit instead of <)
                if x > limit and self.level == player_level:
                    self.collision = True
                    self.add_score = True
                elif x > limit:
                    self.fallen = True
                    self.failures += 1


    def package_falling(self, x: int, limit: int):
        """This method will change the sprite of the package once it reaches the limit of the conveyor"""
        if x == limit and self.conveyor == 2: # Checks for even conveyors
            self.x_image += 32 # Sprite of package falling on right limit
        elif x == limit: # Checks for odd conveyors and conveyor0
            self.x_image += 48 # Sprite of package falling from left limit

    def package_end(self):
        """This method will either make the package fall or get it to the next conveyor. However, it will be the end of
        the package in that conveyor for now"""
        # This is where the booleans from the collision_check method come in (self.fallen and self.collision)
        if self.collision:
            self.continuity = True # This will be used to draw the next package
            self.y_image = 0 # This coordinate in imagebank is just black (package no longer shown)
        elif self.fallen:
            self.continuity = False # Since it is false, the next package will not be drawn
            self.y_image = 0

    def continuity_checker(self, previous_collision: bool):
        """This method is used to determine is the previous package successfully collided with the characters. If it did,
        the current package will appear and run its course"""
        if previous_collision:
            self.continuity = True

    def reset_packages(self, init_y: int):
        """This method will be used to reset the package at conveyor0, should a package fall or reach the truck, by
        setting all attributes to their initial values"""
        self.x_image = 51
        self.y_image = init_y # Initial y-coordinate of the sprite in the image bank (depends on package)
        self.collision = False
        self.fallen = False
        if self.conveyor == 0:
            self.continuity = True
        else:
            self.continuity = False
        self.limit_reached = False
        self.visible = True
        self.has_reset = True # This variable confirms that the reset method has been executed

    def update(self, x: int, limit: int, player_level: int, previous_collision: bool = True):
        """This method updates the state of the packages"""
        self.continuity_checker(previous_collision) # First checks the continuity of the packages to see if they have
                                                    # to be updated via the other methods or if they are inactive
        if self.continuity or self.conveyor == 0: # Makes sure sprites only appear if they are on conveyor 0 or if they
                                                  # have been moved up from previous conveyor
            self.switch_image(x)
            self.hide_package(x)
            self.package_falling(x, limit)
            self.collision_check(x, limit, player_level)
            self.package_end()


    def draw(self, x: int, y: int):
        """This method will be used to display the package on the screen, only if it has successfully been passed on from
        the previous conveyor (self.continuity == True) and if it is not passing through the  middle of the screen
        (self.visible)"""
        if self.continuity and self.visible:
            pyxel.blt(x, y, 1, self.x_image, self.y_image, 10, 8, 0)