import pyxel
class Package:
    def __init__(self, conveyor: int, side: str):
        self.side = side # The side will be a number, with 0 and odd numbers being the right and even numbers being the
                         # left. This makes it easier to change the image depending on the side the package is on.
        self.at_truck = False
        self.conveyor = conveyor
        # Set a variable called level where depending on the conveyor the package is in either level 0, 1 or 2. This
        # can be used to check the collisions with Mario and Luigi

        self.x_image = 51  # Add x coordinates of package sprites
        self.y_image = 24  # Add y coordinates of package sprites (later on, add a 16 to this attribute when middle of belt is reached)
        self.width = 10
        self.height = 8


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
        # messed everything up, it's better if we just make it so there's a transparent sprite instead)
        if 111 <= x <= 121:
            self.x_image -= 1

        elif 126 <= x <= 136:
            self.x_image += 1

    def update(self, x):
        self.switch_image(x)


    def draw(self, x, y):
        # Display the package on the screen
        pyxel.blt(x, y, 1, self.x_image, self.y_image, self.width, self.height, 0)