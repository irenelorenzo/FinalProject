import pyxel
class Conveyor:
    """This class is used to represent the conveyor belts"""
    def __init__(self, belt: str, y: int = 98):
        self.belt = belt #This attribute discerns between even, odd and 0 conveyor belts
        self.y = y  # y-coordinate just above the conveyor belt (where package will be)
        # The type of the conveyor belt will define its 'limit', the x-coordinate where the package has to be picked up
        # by either one of the characters
        if self.belt == "even":
            self.limit = 176
            self.x = 80
            self.direction = "right"
        elif self.belt == "odd":
            self.limit = 72
            self.x = 168
            self.direction = "left"
        else:
            self.limit = 208
            self.x = 248
            self.direction = "left"

        self.moving = False
        self.pixels_left = 0
        self.move_delay = 0  # counts frames
        self.speed = 3  # move once every 3 frames (slower)


    @property
    def belt(self):
        return self.__belt

    @property
    def direction(self) -> str:
        return self.__direction

    @belt.setter
    def belt(self, value):
        if not isinstance(value, str):
            raise TypeError("The type of conveyor must be a string")
        elif value != "even" and value != "odd" and value != "0":
            raise ValueError("The type of conveyor must be even, odd, or 0")
        else:
            self.__belt = value

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

    def move_several(self):
        self.move_one()
        self.moving = True

    # Edit so it fits program best!!! Only works when p is pressed, we have to get it to move automatically
    def update_movement(self):
        if self.moving:
            # Increase delay counter
            self.move_delay += 1

            # Move only when enough frames have passed
            if self.move_delay >= self.speed:
                self.move_one()  # move 1 pixel
                self.pixels_left -= 1
                self.move_delay = 0  # reset counter

            # Stop when finished
            if self.pixels_left <= 0:
                self.moving = False

    def update(self, previous_collision: bool = True):
        if previous_collision:
            self.move_several()
            self.update_movement()