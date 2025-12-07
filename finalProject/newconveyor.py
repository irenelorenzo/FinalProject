# Reminders:
# Slow speed down a little
# Change right limit

class Conveyor:
    """This class is used to represent the conveyor belts"""
    def __init__(self, belt: str, y: int = 98):
        self.belt = belt #This attribute discerns between even, odd and 0 conveyor belts
        self.y = y  # y-coordinate just above the conveyor belt (where package will be)
        # The type of the conveyor belt will define its 'limit', the x-coordinate where the package has to be picked up
        # by either one of the characters
        if self.belt == "even":
            self.limit = 172
            self.x = 80
            self.direction = "right"
        elif self.belt == "odd":
            self.limit = 72
            self.x = 168
            self.direction = "left"
        else:
            self.limit = 200
            self.x = 248
            self.direction = "left"
        self.reset = False # Remove after check


    @property
    def belt(self):
        return self.__belt

    @property
    def direction(self) -> str:
        return self.__direction

    @belt.setter
    def belt(self, belt):
        if not isinstance(belt, str):
            raise TypeError("The type of conveyor must be a string")
        elif belt != "even" and belt != "odd" and belt != "0":
            raise ValueError("The type of conveyor must be even, odd, or 0")
        else:
            self.__belt = belt

    @direction.setter
    def direction(self, direction: str):
        if not isinstance(direction, str):
            raise TypeError("'direction' must be a string")
        else:
            direction_names = ("left", "right")
            if direction.lower() not in direction_names:
                raise ValueError("'direction' must be either 'left' or 'right'")
            else:
                self.__direction = direction.lower()



    def __eq__(self, other) -> bool:
        return self.limit == other

    def move_one(self):
        """This method moves the package one position, either to the left or to the right"""
        if self.direction == "left":
            self.x -= 1
        elif self.direction == "right":
            self.x += 1

    def move_several(self, truck_delivering, previous_collision):
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

    def update(self, truck_delivering, previous_collision: bool = True):
        self.move_several(truck_delivering, previous_collision)