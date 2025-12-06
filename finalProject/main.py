# Make sure all classes have only the necessary setters (not for read-only attributes)
# Make sure anything within a method that can be replaced by a protected method is replaced by a protected method (e.g.
# if there's too many if statements)
# Make sure all methods have docstrings
# Make sure code is properly commented
# Put conveyors into lists and simplify main code
# Change newconveyor to conveyor, same with newpackage

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


mario = Player("right")
luigi = Player("left")
truck = Truck()
package = Package(0, 0)
package1 = Package(1, 0)
package2 = Package(2, 1)
package3 = Package(1, 1)
package4 = Package(2, 2)
package5 = Package(1, 2)
# Put conveyors in odd and even list to simplify everything
conveyor = Conveyor("0", 98)
conveyor1 = Conveyor("odd", 98)
conveyor2 = Conveyor("even", 82)
conveyor3 = Conveyor("odd", 66)
conveyor4 = Conveyor("even", 50)
conveyor5 = Conveyor("odd", 34)
conveyors = [conveyor1, conveyor2]

def update():
    # Use this function to alter mario and luigi's position (add conditions for when 8 packages at truck, etc.)
    mario.update()
    luigi.update()
    conveyor.update()

    package.update(conveyor.x, conveyor.limit, mario.level, True)
    # Use for loops to update conveyors to simplify everything

    conveyor1.update(package.collision)
    package1.update(conveyor1.x, conveyor1.limit, luigi.level, package.collision)
    conveyor2.update(package1.collision)
    package2.update(conveyor2.x, conveyor2.limit, mario.level, package1.collision)
    conveyor3.update(package2.collision)
    package3.update(conveyor3.x, conveyor3.limit, luigi.level, package2.collision)
    conveyor4.update(package3.collision)
    package4.update(conveyor4.x, conveyor4.limit, mario.level, package3.collision)
    conveyor5.update(package4.collision)
    package5.update(conveyor5.x, conveyor5.limit, luigi.level, package4.collision)
    truck.update(package5.collision)
    # update score depending on if the conveyor belts are active

def draw():
    pyxel.cls(0) # Clear the screen
    pyxel.bltm(0, 0, 0, 0, 0, 256, 128) # Redraw the tilemap
    mario.draw() # Draw Mario at its new position
    luigi.draw() # Draw Luigi at its new position
    truck.draw() # Draw the truck
    package.draw(conveyor.x, conveyor.y)
    package1.draw(conveyor1.x, conveyor1.y)
    package2.draw(conveyor2.x, conveyor2.y)
    package3.draw(conveyor3.x, conveyor3.y)
    package4.draw(conveyor4.x, conveyor4.y)
    package5.draw(conveyor5.x, conveyor5.y)



pyxel.run(update, draw) #run the program