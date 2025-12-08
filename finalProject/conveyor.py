class Conveyor:
    """This class is used to represent the conveyor belts"""
    def __init__(self, belt: str, y: int = 98):
        """This is the init method for the conveyors"""
        self.belt = belt #This attribute discerns between even, odd and 0 conveyor belts
        self.y = y  # y-coordinate just above the conveyor belt (where package will be)
        # The type of the conveyor belt will define its 'limit', the x-coordinate where the package has to be picked up
        # by either one of the characters
        if self.belt == "even":
            self.limit = 172
            self.x = 80 # x-coordinate where the packages will start
            self.direction = "right" # This will be useful in the move function
        elif self.belt == "odd":
            self.limit = 72
            self.x = 168
            self.direction = "left"
        else: # This is the option for conveyor0
            self.limit = 200
            self.x = 248
            self.direction = "left"
        self.reset = False # Remove after check

    # Now, it is time for the properties and setters. Since the only attributes that are modified in main are belt
    # and y, these are the ones that properties and setters will be created for

    @property
    def belt(self) -> str:
        return self.__belt

    @property
    def y(self) -> int:
        return self.__y

    @belt.setter
    def belt(self, belt: str):
        if not isinstance(belt, str):
            raise TypeError("The type of conveyor must be a string")
        elif belt != "even" and belt != "odd" and belt != "0":
            raise ValueError("The type of conveyor must be even, odd, or 0")
        else:
            self.__belt = belt

    @y.setter
    def y(self, y: int):
        if not isinstance(y, int):
            raise TypeError("'y' must be an integer")
        else:
            if not 0 < y < 128:
                raise ValueError("y must be a value between 0 and 128")
            else:
                self.__y = y


    def move_one(self):
        """This method moves the package one position, either to the left or to the right"""
        if self.direction == "left":
            self.x -= 1
        elif self.direction == "right":
            self.x += 1

    def move_several(self, truck_delivering: bool, previous_collision: bool):
        """This method will be used to move the packages consistently, depending on if the previous package has made it
        to this conveyor, and on if the truck is still not delivering. Otherwise, the package at this conveyor will not
        move"""
        if previous_collision and not truck_delivering:
            self.move_one()

    def reset_conveyors(self):
        """This method will be used to reset the x-position of the conveyors when needed"""
        if self.belt == "even":
            self.x = 80
        elif self.belt == "odd":
            self.x = 168
        else:
            self.x = 248

    def update(self, truck_delivering: bool, previous_collision: bool = True):
        """This method will be used to update the position of a package on a conveyor"""
        self.move_several(truck_delivering, previous_collision)