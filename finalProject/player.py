import pyxel
# Reminders:
# Make it so that the sprites change whenever the package is being moved from one place to another

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
            self.x = 184    #The x coordinate of character on right side
            self.min_y = 108   #Lowest y coordinate of character on right side
            self.max_y = 56     # Highest y coordinate of character on right side
            self.x_image = 16

        else:
            self.x = 60  # The x coordinate of character on right side
            self.min_y = 92  # Lowest y coordinate of character on right side
            self.max_y = 40  # Highest y coordinate of character on right side
            self.x_image = 0

        # Create dictionary to store coordinates of image
        self.y_images = {"normal": 0, "grab1": 16, "grab2": 32, "lift": 48, "boss": 64, "rest1": 80, "rest2": 96}
        self.y_image = self.y_images["normal"]

        self.y = self.min_y     # Initialises the position of the character on its ground floor

        self.collision = False
        self.collision_counter = 0

    # Now that the __init__ method of the class has been defined, and the attributes have been initialised, we must set
    # properties and setters for each of them to ensure their values are correct. We will first define all the
    # properties, and afterward all the setters.
    @property
    def y(self):
      return self.__y

    @property
    def side(self):
        return self.__side


    # Now that all the properties of the attributes have been defined, it is time to create their setters.
    @y.setter
    def y(self,y):
        if not isinstance(y, int):
            raise TypeError("The y-coordinate must be an integer")
        # no condition established for the bounds of the value of y, since they are established in the init function
        else:
            self.__y = y

    @side.setter
    def side(self,side):
        if not isinstance(side, str):
            raise TypeError("The side the character is on must be a string")
        elif side != "left" and side != "right":
            raise ValueError("The side must be either 'right' or 'left'")
        else:
            self.__side = side


    # Now that all the properties and setters have been created, we need to create a method for the characters' vertical
    # movement
    def move(self):
        """ This method moves the characters up and down floors, with different controls depending on the side of the
         screen they are on"""
        if self.side == "left":
            if pyxel.btnp(pyxel.KEY_W) and self.y > self.max_y:
                self.y -= 32
                self.level += 1
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


    def check_collision(self, x, limit, conveyor, package_level):
        """This method will be used to check if the character has collided with a packages. It goes hand in hand with
        package.collision_check"""
        if conveyor in (0, 1) and x < limit and self.level == package_level:  # For conveyor0 and odd conveyors
            self.collision = True  # Determines package and player have collided (passes package onto next level)
        elif conveyor == 2 and x > limit and self.level == package_level:
            self.collision = True

    def moving_package(self):
        """This method will change the sprite of the characters when they collide with the packages"""
        if self.collision:
            self.y_image = self.y_images["grab1"]
            self.collision_counter += 1
            if self.collision_counter == 3:
                self.y_image = self.y_images["normal"]
                self.collision =  False

    def update(self):
        self.move()
        self.moving_package()

    def draw(self):
        # Display the character on the screen
        if self.side == "right" and self.y == self.min_y:
            pyxel.blt(self.x, self.y, 0, self.x_image - 1, self.y_image, -16, 16, 0)
        else:
            pyxel.blt(self.x, self.y, 0, self.x_image, self.y_image, 16, 16, 0)
        # The last number in the function above means that the background will be transparent


