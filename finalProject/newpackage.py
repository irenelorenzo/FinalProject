import pyxel
# Reminders:
# If we have time, make it so that the packages disappear gradually at the middle, and make them spend more time falling
class Package:
    def __init__(self, conveyor: int, level: int, continuity: bool = False):
        self.at_truck = False
        self.conveyor = conveyor # 0 for conveyor0, 1 for odd conveyors, 2 for even conveyors
        self.level = level

        self.x_image = 51  # Add x coordinates of package sprites
        self.y_image = 24  # Add y coordinates of package sprites (later on, add a 16 to this attribute when middle of belt is reached)
        self.width = 10
        self.height = 8
        self.collision = False
        self.fallen = False
        self.continuity = continuity # This attribute describes if the package has not been killed prior to getting to
                                     # its current conveyor. It is set as False at the beginning
        self.limit_reached = False
        self.failures = 0
        self.visible = True


    @property
    def at_truck(self)->bool:
        return self.__at_truck

    @property
    def conveyor(self) -> int:
        return self.__conveyor

    @at_truck.setter
    def at_truck(self, at_truck:bool):
        if not isinstance(at_truck, bool):
            raise TypeError("'at_truck' must be a boolean")
        else:
            self.__at_truck = at_truck

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
            self.y_image += 16

    def hide_package(self, x):
        """This method will hide the package sprite as it goes through the center columns"""
        # You got the coordinates wrong! 128 is center, 136 right, 120 left. Update accordingly
        # Also, change sprites in image bank so that we don't need to modify width (this changed the x coordinate and
        # messed everything up, it's better if we just make it so there's a transparent sprite instead
        if 111 <= x <= 136:
                self.visible = False
        else:
                self.visible = True

    def __eq__(self, player_level):
        """This method will be used to compare the levels that the character is in and the level the package is in,
        checking potential collisions between them"""
        return self.level == player_level

    def collision_check(self, x, limit, player_level):
        """This method will be used to compare the x-coordinate of the package with the limit of its conveyor"""
        if self.conveyor == 0 or self.conveyor == 1:
            if x < limit and self.level == player_level:
                self.collision = True
            elif x < limit:
                self.fallen = True
                self.failures += 1
        else:
            if x > limit and self.level == player_level:
                self.collision = True
            elif x > limit:
                self.fallen = True
                self.failures += 1


    def package_falling(self, x, limit):
        """This method will change the sprite of the package once it reaches the limit of the conveyor"""
        if x == limit and self.conveyor == 2:
            self.x_image += 32
        elif x == limit:
            self.x_image += 48
            # Package reaches next level
        # Package disappears

    def package_end(self):
        """This method will either make the package fall or get it to the next conveyor. However, it will be the end of
        the package in that conveyor for now"""
        if self.collision:
            self.continuity = True
            self.y_image = 0
        elif self.fallen:
            self.continuity = False
            self.y_image = 0

    def continuity_checker(self, previous_collision: bool):
        if previous_collision:
            self.continuity = True

    def update(self, x, limit, player_level, previous_collision: bool):
        # set a function that sets previous packages' continuity to current
        self.continuity_checker(previous_collision)
        if self.continuity or self.conveyor == 0:
            self.switch_image(x)
            self.hide_package(x)
            self.package_falling(x, limit)
            self.collision_check(x, limit, player_level)
            self.package_end()


    def draw(self, x, y):
        # Display the package on the screen
        if self.continuity and self.visible:
            pyxel.blt(x, y, 1, self.x_image, self.y_image, self.width, self.height, 0)