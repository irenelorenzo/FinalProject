class Package:
    """This is a class to create the packages in the game. Packages will start on belt0, and move from right to left/
    left to right when they come into contact with Mario or Luigi. They will start and finish moving to the left, but
    move in alternating directions depending on the belt they are on."""
    # First, we will define an __init__ method to initialise the attributes of this class
    def __init__(self):
        """ The init method. Every package will start moving to the left, and they will start at the same x and y
        position. Therefore, there will be no parameters in the init method. The image has to be defined depending on
        the x and y positions of the package, but for the start, all packages will have the same images. We might have
        to create a new method to set the image to what it should be according to the y position"""
        self.direction = "left"
        self.at_truck = False
        self.x = 0
        self.y = 0
        self.image = "empty_package.png"

    # Now, we will add properties and setters for the values in the __init__ method
    @property
    def direction(self) -> str:
        return self.__direction

    @property
    def y(self) -> int:
        return self.__y

    @property
    def x(self) -> int:
        return self.__x

    @property
    def at_truck(self) -> bool:
        return self.__at_truck

    @property
    def image(self) -> str:
        return self.__image

    @direction.setter
    def direction(self, direction: str):
        if not isinstance(direction, str):
            raise TypeError("The direction must be a string")
        if not direction.lower() == "left" and not direction.lower() == "right":
            raise ValueError("The direction must be left or right")
        else:
            self.__direction = direction.lower()

    @y.setter
    def y(self, y: int):
        if not isinstance(y, int):
            raise TypeError("The y must be an int")
        elif y < 0:
            raise ValueError("The y must be >= 0")
        else:
            self.__y = y

    @x.setter
    def x(self, x: int):
        # The first condition that the x must follow is that it must be an integer
        if not isinstance(x, int):
            raise TypeError("The x must be an int")
        # The second condition is that it must be within a range. For now, this means it must be greater than 0
        # Once we figure out the dimensions of our tilemaps, we will be able to determine an upper limit for x too,
        # as well as for y
        elif x < 0:
            raise ValueError("The x must be >= 0")
        else:
            self.__x = x

    @at_truck.setter
    def at_truck(self, at_truck: bool):
        if not isinstance(at_truck, bool):
            raise TypeError("at_truck must be either True or False")
        else:
            self.__at_truck = at_truck

    @image.setter
    def image(self, image: str):
        if not isinstance(image, str):
            raise TypeError("The image must be a string")
        elif image[-4] != ".png":
            raise ValueError("The image must be a png")
        else:
            self.__image = image

    # Now that we have created properties and setters for all the initialised variables, we will define a method for
    # the packages to move one position, depending on the direction. We should also create a method to determine the
    # direction of the package depending on the belt it is on.
    def move_one (self):
        """This method moves the package one position, either to the left or to the right"""
        if self.direction == "left":
            self.x -= 1
        elif self.direction == "right":
            self.x += 1

    def move_several(self, number: int):
        """ This method moves the package several positions, making use of the move_one method previously defined """
        # We reuse the previous one, invoking it 'number' times
        # We use self.name_of_the_method()
        for _ in range(number):
            self.move_one()

    # Apart from the methods to move, we also need to define methods to change belts (move up), fall off the belt, move
    # up, reach the truck (this could be done by checking if the package is in the last belt in a list/tuple of belts in
    # the main code)
    def