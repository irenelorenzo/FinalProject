import pyxel

# Reminders
# Change package movement so that it moves automatically, and not when key is pressed
# Develop functions for when package moves to another conveyor (change sprites to tilted package, visibly move package)
# Develop function for when package moves
# Create update function (should include move function and anything that a package must do in the main program, really)
# Once the package can move up and down floors upon collision with players, make it so that it doesn't go over the middle
# of the conveyor and goes underneath instead, and change the sprite as it is passing through the middle
# Make packages appear at truck when the final position of the final floor is reached

class Package:
    def __init__(self, conveyor: int):
        self.x = 248
        self.at_truck = False
        self.conveyor = conveyor
        if  self.conveyor == 0 or (self.conveyor//2) != 0:
            self.direction = "left"
            if self.conveyor == 0:
                self.y = 98
            else:
                self.y = 98 + (self.conveyor - 1) * 16
        else:
            self.direction = "right"
            self.y = 98 + (self.conveyor - 1) * 16

        self.x_image = 32 # Add x coordinates of package sprites
        self.y_image = 8 # Add y coordinates of package sprites (later on, add a 16 to this attribute when middle of belt is reached)


    @property
    def direction(self)->str:
        return self.__direction

    @property
    def at_truck(self)->bool:
        return self.__at_truck

    @property
    def conveyor(self) -> int:
        return self.__conveyor

    @direction.setter
    def direction(self,direction:str):
        if not isinstance(direction,str):
            raise TypeError("'direction' must be a string")
        else:
            direction_names=("left","right")
            if direction.lower() not in direction_names:
                raise ValueError("'direction' must be either 'left' or 'right'")
            else:
                self.__direction = direction.lower()

    @at_truck.setter
    def at_truck(self,at_truck:bool):
        if not isinstance(at_truck,bool):
            raise TypeError("'at_truck' must be a boolean")
        else:
            self.__at_truck = at_truck

    @conveyor.setter
    def conveyor(self, conveyor: int):
        if not isinstance(conveyor, int):
            raise TypeError("'conveyor' must be an integer")
        else:
            self.__conveyor = conveyor

    def move_one (self):
        """This method moves the package one position, either to the left or to the right"""
        if self.direction == "left":
            self.x -= 1
        elif self.direction == "right":
            self.x += 1

    def move_several(self):
        if pyxel.btnp(pyxel.KEY_P): # Right now, the package moves when the letter p is pressed, to check the functionality
            for pixel in range (24):
                self.move_one()
            if self.conveyor != 0:
                for pixel in range(72):
                    self.move_one()

    def move_up(self):
            """Move to the next belt"""
            # Add if statement to check collisions
            self.conveyor += 1

    def reached_truck(self, max_level: int) -> bool:
        """Return True if package reached the truck (top belt)."""
        return self.conveyor == max_level

    def draw(self):
        # Display the character on the screen
        pyxel.blt(self.x, self.y, 0, self.x_image, self.y_image, 16, 8, 0)
        # The last number in the function above means that the background will be transparent










