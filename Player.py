class Player:
    """This is a class to represent the characters. In the final game, there will be two characters, Mario and Luigi
    They will be able to move up and down, rest, transfer packages from one belt to the next/to the truck, and get told
    off by their boss for dropping a package"""
    # First, we will define the __init__ method to initialise the attributes needed for the characters
    def __init__(self, image: str, side: str):
        # Check if up and down parameters need to be created, or if game can be controlled with arrows. If we cannot
        # figure out how to control the characters with arrows, we might need to add string parameters "up" and "down"
        # describing what controls are used for each character (eg. ws for Luigi and ol for Mario)
        """This is the __init__ function for the players
        :param image: str. A string representing the name of the image used for each player. Depending on if the
        character is Mario or Luigi, they will have a different starting image, since they are different characters.
        The image will change throughout the game depending on if they are picking up a package, resting, being told off...
        :param side: str. A string representing the side each of the characters is in. Mario will be on the right side
        of the screen and Luigi on the left. It will determine the x-coordinates of the characters.
        """
        self.image = image
        self.side = side
        # vertical_pos: int. This is the vertical position of the characters. Each character will have three
        # possible values for this parameter, with 0 being the ground floor for them. They will both start at 0
        self.vertical_pos = 0
        # According to this __init__ method, an example to define Mario and Luigi could be:
        # Mario = Player("mario.jpg","right")
        # Luigi = Player("luigi.jpg","left")

    # Now that the __init__ method of the class has been defined, and the attributes have been initialised, we must set
    # properties and setters for each of them to ensure their values are correct. We will first define all the
    # properties, and afterwards all the setters.
    @property
    def vertical_pos(self):
      return self.vertical_pos

    @property
    def side(self):
        return self.side

    @property
    def image(self):
        return self.image

    # Now that all the properties of the attributes have been defined, it is time to create their setters.
    @vertical_pos.setter
    def vertical_pos(self,value):
      self.vertical_pos=value

    @side.setter
    def side(self,value):
      self.side=value

    @image.setter
    def image(self,value):
      self.image=value


    # Now that all the properties and setters have been created, we need to create a method for the characters' vertical
    # movement
