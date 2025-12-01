
class Package:
    def __init__(self, conveyor: int, direction:str):
        self.conveyor = 0
        self.position = 0
        self.direction = direction
        self.at_truck = False
        if self.conveyor == 0 or (self.conveyor//2) == 0:
            self.direction = "left"
        else:
            self.direction = "right"
        self.x_image = # Add x coordinates of package sprites
        self.y_image =  # Add y coordinates of package sprites (later on, add a 16 to this attribute when middle of belt is reached)


    @property
    def direction(self)->str:
        return self.__direction

    @property
    def at_truck(self)->bool:
        return self.at_truck

    @property
    def

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


    def move_one (self):
        """This method moves the package one position, either to the left or to the right"""
        if self.direction == "left":
            self.x -= 1
        elif self.direction == "right":
            self.x += 1

    def move_up(self):
            """Move to the next belt above."""
            self.level += 1

    def reached_truck(self, max_level: int) -> bool:
        """Return True if package reached the truck (top belt)."""
        return self.level == max_level















