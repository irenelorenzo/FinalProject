
class Package:

    def __init__(self,direction:str, at_truck:bool):
        self.level=0
        self.position=0
        self.direction = direction
        self.at_truck = False
        if self.direction=="right":
            self.image="Package_Right.png"
        else:
            self.image="Package_Left.png"
    @property
    def direction(self)->str:
        return self.__direction

    @property
    def at_truck(self)->bool:
        return self.at_truck

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















