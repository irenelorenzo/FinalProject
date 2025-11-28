import pyxel

# Reminders:
# Create a dictionary at some point with the location of Mario and Luigi's images --> use this to correct image attribute

class Player:
    """This is a class to represent the characters. In the final game, there will be two characters, Mario and Luigi
    They will be able to move up and down, rest, transfer packages from one belt to the next/to the truck, and get told
    off by their boss for dropping a package"""
    # First, we will define the __init__ method to initialise the attributes needed for the characters
    def __init__(self, side: str):
        """This is the __init__ function for the players
        :param side: str. A string representing the side each of the characters is in. Mario will be on the right side
        of the screen and Luigi on the left. It will determine the x-coordinates of the characters.
        """
        self.side = side
        # y: int. This is the vertical position of the characters. Each character will have three
        # possible values for this parameter, with 0 being the ground floor for them. They will both start at 0
        # Since on each side of the screen, the ground floor is on a different coordinate,
        if side == "right":
            self.x = 192    #The x coordinate of character on right side
            self.min_y = 120   #Lowest y coordinate of character on right side
            self.max_y = 56     # Highest y coordinate of character on right side
        else:
            self.x = 60  # The x coordinate of character on right side
            self.min_y = 92  # Lowest y coordinate of character on right side
            self.max_y = 40  # Highest y coordinate of character on right side

        self.y = self.min_y     # Initialises the position of the character on its ground floor

    # Now that the __init__ method of the class has been defined, and the attributes have been initialised, we must set
    # properties and setters for each of them to ensure their values are correct. We will first define all the
    # properties, and afterward all the setters.
    @property
    def y(self):
      return self.__y

    @property
    def side(self):
        return self.__side

    @property
    def image(self):
        return self.image

    # Now that all the properties of the attributes have been defined, it is time to create their setters.
    @y.setter
    def vertical_pos(self,value):

    @side.setter
    def side(self,value):
      self.__side=value

    @image.setter
    def image(self,value):
      self.image=value


    # Now that all the properties and setters have been created, we need to create a method for the characters' vertical
    # movement
    def vertical_movement(self):
        """ This method moves the characters up and down floors, with different controls depending on the side of the
         screen they are on"""
        if self.side == "left":
            if pyxel.btnp(pyxel.KEY_W) and self.y > self.max_y:
                self.y -= 32
            if pyxel.btnp(pyxel.KEY_S) and self.y < self.min_y:
                self.y += 32
        else:
            if pyxel.btnp(pyxel.KEY_UP) and self.y > self.max_y:
                self.y -= 32
            if pyxel.btnp(pyxel.KEY_DOWN) and self.y < self.min_y:
                self.y += 32

    def draw(self):
        # Display the character on the screen
        pyxel.blt(self.x, self.vertical_pos, 0, 0, 0, 16, 16, 0)
