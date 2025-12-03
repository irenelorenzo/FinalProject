class Conveyor:
    """This class is used to represent the conveyor belts"""
    def __init__(self, type: str, y: int, ):
        self.type = type #This attribute discerns between even, odd and 0 conveyor belts
        self.y = y  # y-coordinate just above the conveyor belt (where package will be)
        # The type of the conveyor belt will define its 'limit', the x-coordinate where the package has to be picked up
        # by either one of the characters

        if type == "even":
            self.limit = 176
        elif type == "odd":
            self.limit = 72
        else:
            self.limit = 224


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        if not isinstance(type, str):
            raise TypeError("The type of conveyor must be a string")
        elif type != "even" and type != "odd" and type != "0":
            raise ValueError("The type of conveyor must be even, odd, or 0")
        else:
            self.__type = value

    def __eq__(self, other):
        # Use eq function to compare conveyor coordinates and player coordinates