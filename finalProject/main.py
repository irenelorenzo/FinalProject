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
package0 = Package(0, 0, True)
package1 = Package(1, 0)
package2 = Package(2, 1)
package3 = Package(1, 1)
package4 = Package(2, 2)
package5 = Package(1, 2)
# Grouping all the packages into a list will make the update function simpler
packages = [package0, package1, package2, package3, package4, package5]

conveyor0 = Conveyor("0", 98)
conveyor1 = Conveyor("odd", 98)
conveyor2 = Conveyor("even", 82)
conveyor3 = Conveyor("odd", 66)
conveyor4 = Conveyor("even", 50)
conveyor5 = Conveyor("odd", 34)
# Grouping all the packages into a list will make the update function simpler
conveyors = [conveyor0, conveyor1, conveyor2, conveyor3, conveyor4, conveyor5]


def update():
    # Update the characters
    package_reset_needed = False
    mario.update()
    luigi.update()
    # Update the packages and conveyors
    # First, update them for conveyor0, they do not depend on the previous conveyor necessarily
    conveyor0.update()
    package0.update(conveyor0.x, conveyor0.limit, mario.level, conveyor0.reset)
    for index in range(len(conveyors)):
        conveyors[index].update(packages[index - 1].collision)
        if index % 2 == 1:
            packages[index].update(conveyors[index].x, conveyors[index].limit, luigi.level,
                                packages[index - 1].collision)
        else:
            packages[index].update(conveyors[index].x, conveyors[index].limit, mario.level,
                                packages[index - 1].collision)
        if packages[index - 1].fallen:
            package_reset_needed = True

    truck.update(package5.collision)

    if truck.package_added:
        package_reset_needed = True

    if package_reset_needed:
        for package in packages:
            package.reset_packages()

        for conveyor in conveyors:
            conveyor.reset_conveyors()

        truck.package_added = False
    # update score depending on if the conveyor belts are active
    # Check if the reset function has been executed


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