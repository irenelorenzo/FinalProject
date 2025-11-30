class Truck:
    """This is a class to represent the truck. In the game, there will only be one truck. When there are 8 packages in
    the truck, it will move out of frame and become the initial picture again """
    # First, we will define the __init__ method to initialise the attributes needed for the truck
    def __init__(self):
        """This is the __init__ function for the truck
        :param side: str. A string representing the side each of the characters is in. Mario will be on the right side
        of the screen and Luigi on the left. It will determine the x-coordinates of the characters, as well as the
        sprite used for them
        """
