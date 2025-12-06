import pyxel
# Reminders:
# If we have time, make it so that the packages disappear gradually at the middle, and make them spend more time falling
# Change sprites according to conveyor level
class Package:
    def __init__(self, conveyor: int, level: int, continuity: bool = False):
        self.conveyor = conveyor # 0 for conveyor0, 1 for odd conveyors, 2 for even conveyors
        self.level = level # Either 0, 1 or 2 - will be used to determine collisions with characters

        self.x_image = 51  # Add x coordinates of package sprites
        self.y_image = 24  # Add y coordinates of package sprites (later on, add a 16 to this attribute when middle of belt is reached)
        self.collision = False # Will become true once package collides with characters
        self.fallen = False # Will become false if package falls
        self.continuity = continuity # This attribute describes if the package has not been killed prior to getting to
                                     # its current conveyor. It is set as False at conveyor0, then depends on previous conveyor
        self.limit_reached = False # This will change to true when package reaches conveyor limit
        self.failures = 0 # Counts if package has fallen to determine lives left
        self.visible = True # Used in the draw() function. Will be set to False when hiding the package
        self.has_reset = False

    @property
    def conveyor(self) -> int:
        return self.__conveyor

    @conveyor.setter
    def conveyor(self, conveyor: int):
        if not isinstance(conveyor, int):
            raise TypeError("'conveyor' must be an integer")
        else:
            self.__conveyor = conveyor


    def switch_image(self, x):
        """Switches sprite to the next when middle of screen is reached, where x is substituted in main code. Also gets
        package to disappear when it reaches the middle section"""
        if x == 128:
            self.y_image += 16 # Changes y-coordinate of image bank

    def hide_package(self, x):
        """This method will hide the package sprite as it goes through the center columns"""
        if 111 <= x <= 136:
                self.visible = False # Since unless visible == True, the draw function won't work, in these coordinates
                                     # of the tilemap the package will be hidden
        else:
                self.visible = True

    def __eq__(self, player_level):
        """This method will be used to compare the levels that the character is in and the level the package is in,
        checking potential collisions between them"""
        return self.level == player_level

    def collision_check(self, x, limit, player_level):
        """This method will be used to compare the x-coordinate of the package with the limit of its conveyor"""
        if not self.collision and not self.fallen:
            if self.conveyor == 0 or self.conveyor == 1: # For conveyor0 and odd conveyors
                if x < limit and self.level == player_level: # Checks if package has passed limit and is on same level as player
                    self.collision = True # Determines package and player have collided (passes package onto next level)
                elif x < limit:
                    self.fallen = True # If package has passed limit and is not on same level as player
                    self.failures += 1 # Add one to failure counter
            else: # For even conveyors
                if x > limit and self.level == player_level:
                    self.collision = True
                elif x > limit:
                    self.fallen = True
                    self.failures += 1


    def package_falling(self, x, limit):
        """This method will change the sprite of the package once it reaches the limit of the conveyor"""
        if x == limit and self.conveyor == 2:
            self.x_image += 32 # Sprite of package falling on right limit
        elif x == limit: # Sprite of package falling from left limit
            self.x_image += 48

    def package_end(self):
        """This method will either make the package fall or get it to the next conveyor. However, it will be the end of
        the package in that conveyor for now"""
        if self.collision:
            self.continuity = True # This will be used to draw the next package
            self.y_image = 0
        elif self.fallen:
            self.continuity = False # Since it is false, the next package will not be drawn
            self.y_image = 0

    def continuity_checker(self, previous_collision: bool):
        if previous_collision:
            self.continuity = True

    def reset_packages(self):
        """This method will be used to reset the package at conveyor0, should a package fall or reach the truck, by
        setting all attributes to their initial values"""
        self.x_image = 51
        self.y_image = 24
        self.collision = False
        self.fallen = False
        if self.conveyor == 0:
            self.continuity = True
        else:
            self.continuity = False
        self.limit_reached = False
        self.visible = True
        self.has_reset = True

    def update(self, x, limit, player_level, previous_collision: bool = True):
        # set a function that sets previous packages' continuity to current
        self.continuity_checker(previous_collision)
        if self.continuity or self.conveyor == 0: # Makes sure sprites only appear if they are on conveyor 0 or if they
                                                  # have been moved up from previous conveyor
            self.switch_image(x)
            self.hide_package(x)
            self.package_falling(x, limit)
            self.collision_check(x, limit, player_level)
            self.package_end()


    def draw(self, x, y):
        # Display the package on the screen
        if self.continuity and self.visible:
            pyxel.blt(x, y, 1, self.x_image, self.y_image, 10, 8, 0)