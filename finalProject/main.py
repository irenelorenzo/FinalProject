# Make sure all classes have only the necessary setters (not for read-only attributes)
# Make sure anything within a method that can be replaced by a protected method is replaced by a protected method (e.g.
# if there's too many if statements)
# Make sure all methods have docstrings
# Make sure code is properly commented
# Put conveyors into lists and simplify main code
# Change newconveyor to conveyor, same with newpackage

# Maybe add an if in the for loop related to the conveyors/packages? Like unless a condition is met (like reset = False
# for previous package, the for loop just cycles through without executing something - or stopping when needed)
# And then outside of the for loop, if the reset is true or something like that, make it so that conveyor0 and package0
# are reset

# Import all the classes, and pyxel
import pyxel
from finalProject.player import Player
from finalProject.truck import Truck
from finalProject.newpackage import Package
from finalProject.newconveyor import Conveyor

# Set the scene with the tilemap
pyxel.init(256, 128)
pyxel.load("../assets/my_resource.pyxres")
pyxel.cls(0)
pyxel.bltm(0, 0, 0, 0, 0, 256, 128)

# Create all the object necessary from the imported classes
mario = Player("right")
luigi = Player("left")
truck = Truck()
package = Package(0, 0, True)
package1 = Package(1, 0)
package2 = Package(2, 1)
package3 = Package(1, 1)
package4 = Package(2, 2)
package5 = Package(1, 2)
# Grouping all the packages into a list will make the update function simpler
packages = [package, package1, package2, package3, package4, package5]

conveyor = Conveyor("0", 98)
conveyor1 = Conveyor("odd", 98)
conveyor2 = Conveyor("even", 82)
conveyor3 = Conveyor("odd", 66)
conveyor4 = Conveyor("even", 50)
conveyor5 = Conveyor("odd", 34)
# Grouping all the packages into a list will make the update function simpler
conveyors = [conveyor, conveyor1, conveyor2, conveyor3, conveyor4, conveyor5]


def update():
    # Update the characters
    mario.update()
    luigi.update()
    fallen = False
    # Update the packages and conveyors
    # First, update them for conveyor0, they do not depend on the previous conveyor necessarily
    conveyor.update(truck.package_added, fallen)
    package.update(conveyor.x, conveyor.limit, mario.level, conveyor.reset, False)
    for index in range(len(conveyors)):
        conveyors[index].update(truck.package_added, packages[index - 1].fallen, packages[index - 1].collision)
        if (index + 1) // 2 == 1:
            packages[index].update(conveyors[index].x, conveyors[index].limit, luigi.level,
                                conveyors[index].reset, packages[index - 1].collision)
        else:
            packages[index].update(conveyors[index].x, conveyors[index].limit, mario.level,
                                conveyors[index].reset, packages[index - 1].collision)
        if packages[index].fallen:
            fallen = True
        if packages[index].reset:
            fallen = False

    truck.update(package5.collision)
    # update score depending on if the conveyor belts are active

def draw():
    pyxel.cls(0) # Clear the screen
    pyxel.bltm(0, 0, 0, 0, 0, 256, 128) # Redraw the tilemap
    mario.draw() # Draw Mario at its new position
    luigi.draw() # Draw Luigi at its new position
    truck.draw() # Draw the truck
    # Draw all the packages
    for index in range(len(packages)):
        packages[index].draw(conveyors[index].x, conveyors[index].y)


pyxel.run(update, draw) #run the program