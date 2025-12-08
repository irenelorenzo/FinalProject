# Make sure all classes have only the necessary setters (not for read-only attributes)
# Make sure anything within a method that can be replaced by a protected method is replaced by a protected method (e.g.
# if there's too many if statements)
# Make sure all methods have docstrings
# Make sure code is properly commented
# simplify main code
# Change newconveyor to conveyor, same with newpackage

# Import all the classes, and pyxel
import pyxel
from finalProject.player import Player
from finalProject.truck import Truck
from finalProject.newpackage import Package
from finalProject.newconveyor import Conveyor
from score import Score

# Set the scene with the tilemap
pyxel.init(256, 128)
pyxel.load("../assets/my_resource.pyxres")
pyxel.cls(0)
pyxel.bltm(0, 0, 0, 0, 0, 256, 128)

# Create all the objects necessary from the imported classes
mario = Player("right")
luigi = Player("left")
truck = Truck()

init_y_list = [24, 24, 40, 56, 72, 88]

package0 = Package(0, 0, 24, True)
package1 = Package(1, 0, 24)
package2 = Package(2, 1, 40)
package3 = Package(1, 1, 56)
package4 = Package(2, 2, 72)
package5 = Package(1, 2, 88)
# Grouping all the packages into a list will make the update function simpler
packages = [package0, package1, package2, package3, package4, package5]

conveyor0 = Conveyor("0", 106)
conveyor1 = Conveyor("odd", 98)
conveyor2 = Conveyor("even", 82)
conveyor3 = Conveyor("odd", 66)
conveyor4 = Conveyor("even", 50)
conveyor5 = Conveyor("odd", 34)
# Grouping all the conveyors into a list will make the update function simpler
conveyors = [conveyor0, conveyor1, conveyor2, conveyor3, conveyor4, conveyor5]

score = Score()

# GAME STATE
fallen_packages_total = 0   # how many packages have fallen in total
boss_visible = False        # whether the boss is currently shown
boss_timer = 0              # countdown until boss disappears
GAME_OVER = False           # stops update() when true


def update():
    global fallen_packages_total, boss_visible, boss_timer, GAME_OVER

    # If game is over, freeze logic
    if GAME_OVER:
        return

    # Update the characters
    package_reset_needed = False
    mario.update()
    luigi.update()

    # First, update conveyor0 and package0 (they don't depend on previous conveyor)
    conveyor0.update(truck.delivering)
    package0.update(conveyor0.x, conveyor0.limit, mario.level, conveyor0.reset)

    # Update the rest of the conveyors and packages
    for index in range(len(conveyors)):
        conveyors[index].update(truck.delivering, packages[index - 1].collision)

        # Luigi handles odd indices, Mario even (based on your original logic)
        if index % 2 == 1:
            packages[index].update(
                conveyors[index].x,
                conveyors[index].limit,
                luigi.level,
                packages[index - 1].collision,
            )
        else:
            packages[index].update(
                conveyors[index].x,
                conveyors[index].limit,
                mario.level,
                packages[index - 1].collision,
            )

        # If the package on the previous conveyor has fallen, trigger reset and boss
        if packages[index - 1].fallen:
            package_reset_needed = True

            # Handle fallen packages: increase counter, show boss
            fallen_packages_total += 1
            boss_visible = True
            boss_timer = 120  # ~2 seconds at 60 FPS

            # End game after 3 fallen packages
            if fallen_packages_total >= 3:
                GAME_OVER = True

        # Update score when packages move to next conveyor
        score.update_conveyor_score(packages[index].add_score)
        packages[index].add_score = False

    # Update truck and score from truck
    truck.update(package5.collision)
    score.update_truck_score(truck.add_score)

    if truck.package_added:
        package_reset_needed = True

    # Reset all packages/conveyors if needed
    if package_reset_needed:
        for index in range(len(packages)):
            packages[index].reset_packages(init_y_list[index])

        for conveyor in conveyors:
            conveyor.reset_conveyors()

        truck.package_added = False

    # Boss visibility countdown
    if boss_visible:
        boss_timer -= 1
        if boss_timer <= 0:
            boss_visible = False


def draw():
    pyxel.cls(0)  # Clear the screen

    # If game is over, show game over text and exit
    if GAME_OVER:
        pyxel.text(100, 60, "GAME OVER", 7)
        return

    # Redraw the tilemap
    pyxel.bltm(0, 0, 0, 0, 0, 256, 128)

    # Draw characters and truck
    mario.draw()
    luigi.draw()
    truck.draw()

    # Draw all the packages
    for index in range(len(packages)):
        packages[index].draw(conveyors[index].x, conveyors[index].y)

    # Draw boss when triggered
    if boss_visible:
        pyxel.blt(0, 112, 0, 16, 112, 32, 32, 0)

    # Draw score
    score.draw()


pyxel.run(update, draw)  # run the program
