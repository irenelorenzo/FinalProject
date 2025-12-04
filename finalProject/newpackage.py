import pyxel
# Reminders:
# Create method to check for collisions
# Create method to make it fall
class Package:
    def __init__(self, conveyor: int, level: int, continuity: bool = True, side: str = "left"):

        self.side = side # The side will be a number, with 0 and odd numbers being the right and even numbers being the
                         # left. This makes it easier to change the image depending on the side the package is on.
        self.at_truck = False
        self.conveyor = conveyor
        self.level = level

        self.x_image = 51  # Add x coordinates of package sprites
        self.y_image = 24  # Add y coordinates of package sprites (later on, add a 16 to this attribute when middle of belt is reached)
        self.width = 10
        self.height = 8
        self.collision = False
        self.continuity = continuity # This attribute describes if the package has not been killed prior to getting to
                                     # its current conveyor


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
        if x == 111:
            for _ in range(10):
                self.x_image -= 1

        elif x == 136:
            for _ in range(10):
                self.x_image += 1

    def __eq__(self, player_level):
        """This method will be used to compare the levels that the character is in and the level the package is in,
        checking potential collisions between them"""
        return self.level == player_level

    #def collision_check(self, x, limit, player_level):
        """This method will be used to compare the x-coordinate of the package with the limit of its conveyor"""
        if x > limit and self.level == player_level:
            self.collision = True
        else:
            self.collision = False

    def package_falling(self, x, limit):
        """This method will change the sprite of the package once it reaches the limit of the conveyor"""
        if self.side == "left" and x == limit:
            self.x_image += 48
        else:
            self.x_image += 32
            # Package reaches next level
        # Package disappears

    def package_end(self):
        """This method will either make the package fall or get it to the next conveyor. However, it will be the end of
        the package in that conveyor for now"""


    def update(self, x, limit, player_level):
        #self.collision_check(x, limit, player_level)
        #self.package_falling(x, limit)
        self.switch_image(x)
        self.hide_package(x)


    def draw(self, x, y):
        # Display the package on the screen
        pyxel.blt(x, y, 1, self.x_image, self.y_image, self.width, self.height, 0)