import pyxel
class Package:
    def __init__(self, conveyor: int, side: str):
        self.side = side # The side will be a number, with 0 and odd numbers being the right and even numbers being the
                         # left. This makes it easier to change the image depending on the side the package is on.
        self.at_truck = False
        self.conveyor = conveyor

        self.x_image = 32  # Add x coordinates of package sprites
        self.y_image = 24  # Add y coordinates of package sprites (later on, add a 16 to this attribute when middle of belt is reached)


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
        """Switches sprite to the next when middle of screen is reached, where x is substituted in main code"""
        # Make it so that package disappears as it reaches center

        if x == 120:
            self.y_image += 16


    def update(self, x):
        self.switch_image(x)


    def draw(self, x, y):
        # Display the package on the screen
        pyxel.blt(x, y, 0, self.x_image, self.y_image, 16, 8, 0)