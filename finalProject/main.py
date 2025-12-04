# Make sure all classes have only the necessary setters (not for read-only attributes)
# Make sure anything within a method that can be replaced by a protected method is replaced by a protected method (e.g.
# if there's too many if statements)

# Import all the classes, and pyxel
import pyxel
from player import Player
from truck import Truck
from newpackage import Package
from newconveyor import Conveyor

# Set the scene with the tilemap
pyxel.init(256, 128)
pyxel.load("../assets/my_resource.pyxres")
pyxel.cls(0)
pyxel.bltm(0, 0, 0, 0, 0, 256, 128)


mario = Player("right")
luigi = Player("left")
truck = Truck()
package = Package(0, 0, True)
package1 = Package(1, 0)
#package2 = Package(2, 1)
#package3 = Package(1, 1)
#package4 = Package(2, 2)
#package5 = Package(1, 2)
conveyor = Conveyor("0", 98)
conveyor1 = Conveyor("odd", 98)
#conveyor2 = Conveyor("even", 82)
#conveyor3 = Conveyor("odd", 66)
#conveyor4 = Conveyor("even", 50)
#conveyor5 = Conveyor("odd", 34)

def update():
    # Use this function to alter mario and luigi's position (add conditions for when 8 packages at truck, etc.)
    mario.update()
    luigi.update()
    conveyor.update()
    package.update(conveyor.x, conveyor.limit, luigi.level)
    conveyor1.update()
    package1.update(conveyor.x, conveyor.limit, luigi.level, package.continuity)

def draw():
    pyxel.cls(0) # Clear the screen
    pyxel.bltm(0, 0, 0, 0, 0, 256, 128) # Redraw the tilemap
    mario.draw() # Draw Mario at its new position
    luigi.draw() # Draw Luigi at its new position
    truck.draw() # Draw the truck
    package.draw(conveyor.x, conveyor.y)



pyxel.run(update, draw) #run the program