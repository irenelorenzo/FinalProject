class Conveyor:
    """This class is used to represent the conveyor belts"""
    def __init__(self, belt: str, y: int):
        self.belt = belt #This attribute discerns between even, odd and 0 conveyor belts
        self.y = y  # y-coordinate just above the conveyor belt (where package will be)
        # The type of the conveyor belt will define its 'limit', the x-coordinate where the package has to be picked up
        # by either one of the characters

        if belt == "even":
            self.limit = 176
        elif belt == "odd":
            self.limit = 72
        else:
            self.limit = 224


    @property
    def belt(self):
        return self.__type

    @belt.setter
    def belt(self, value):
        if not isinstance(value, str):
            raise TypeError("The type of conveyor must be a string")
        elif value != "even" and value != "odd" and value != "0":
            raise ValueError("The type of conveyor must be even, odd, or 0")
        else:
            self.__belt = value

    def __eq__(self, other) -> bool:
        return (self.limit == other)