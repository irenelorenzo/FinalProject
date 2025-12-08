import pyxel

class Player:
    """This is a class to represent the characters. In the final game, there will be two characters, Mario and Luigi
    They will be able to move up and down, rest, transfer packages from one belt to the next/to the truck, and get told
    off by their boss for dropping a package"""
    # First, we will define the __init__ method to initialise the attributes needed for the characters
    def __init__(self, side: str):
        """This is the __init__ function for the players
        :param side: str. A string representing the side each of the characters is in. Mario will be on the right side
        of the screen and Luigi on the left. It will determine the x-coordinates of the characters, as well as the
        sprite used for them
        """
        self.side = side
        self.level = 0
        if side == "right":
            self.x = 184    # The x coordinate of character on right side
            self.min_y = 108   # Lowest y coordinate of character on right side
            self.max_y = 56     # Highest y coordinate of character on right side
            self.x_image = 16   # The x-coordinate of the sprite in the image bank

        else:
            self.x = 60  # The x coordinate of character on right side
            self.min_y = 92  # Lowest y coordinate of character on right side
            self.max_y = 40  # Highest y coordinate of character on right side
            self.x_image = 0    # The x-coordinate of the sprite in the image bank

        # Create dictionary to store coordinates of the different images
        self.y_images = {"normal": 0, "grab1": 16, "grab2": 32, "lift": 48, "boss": 64, "rest1": 80, "rest2": 96}
        self.y_image = self.y_images["normal"]

        self.y = self.min_y     # Initialises the position of the character on its ground floor



    # Now that the __init__ method of the class has been defined, and the attributes have been initialised, we must set
    # properties and setters for each of them to ensure their values are correct. Since 'side' is the only parameter
    # that can be modified in the main program, se will only create a property and a setter for this parameter

    @property
    def side(self) -> str:
        return self.__side


    @side.setter
    def side(self,side: str):
        if not isinstance(side, str):
            raise TypeError("The side the character is on must be a string") # Makes sure data type is correct
        elif side != "left" and side != "right":
            raise ValueError("The side must be either 'right' or 'left'") # Makes sure value is correct
        else:
            self.__side = side


    # Now that all the properties and setters have been created, we need to create a method for the characters' vertical
    # movement
    def move(self):
        """ This method moves the characters up and down floors, with different controls depending on the side of the
         screen they are on"""
        if self.side == "left":
            if pyxel.btnp(pyxel.KEY_W) and self.y > self.max_y:
                self.y -= 32    # The floors are 32 pixels apart
                self.level += 1 # The level they are on will be used to check the collisions with packages in package
            elif pyxel.btnp(pyxel.KEY_S) and self.y < self.min_y:
                self.y += 32
                self.level -= 1
        else:
            if pyxel.btnp(pyxel.KEY_UP) and self.y > self.max_y:
                self.y -= 32
                self.level += 1
            elif pyxel.btnp(pyxel.KEY_DOWN) and self.y < self.min_y:
                self.y += 32
                self.level -= 1


    def update(self):
        """This method is used to update the state the characters are in. In this case, it only invokes the move method
        to update the characters' position"""
        self.move()

    def draw(self):
        """This method is used to draw the characters on the tilemap, with different orientation if they are on the right
        side and on the ground floor, since there packages emerge from the right instead of the left"""
        if self.side == "right" and self.y == self.min_y:
            pyxel.blt(self.x, self.y, 0, self.x_image - 1, self.y_image, -16, 16, 0)
        else:
            pyxel.blt(self.x, self.y, 0, self.x_image, self.y_image, 16, 16, 0)
        # The last number in the function above means that the background will be transparent


