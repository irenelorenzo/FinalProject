# Import all the classes, and pyxel
import pyxel
from finalProject.player import Player
from finalProject.truck import Truck
from finalProject.package import Package
from finalProject.conveyor import Conveyor
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

init_y_list = [24, 24, 40, 56, 72, 88] # This is a list storing the initial y-coordinates of images of the packages
                                       # Will be used both to initialise the variables and reset them after a package
                                       # falls/reaches truck

package0 = Package(0, 0, init_y_list[0], True)
package1 = Package(1, 0, init_y_list[1])
package2 = Package(2, 1, init_y_list[2])
package3 = Package(1, 1, init_y_list[3])
package4 = Package(2, 2, init_y_list[4])
package5 = Package(1, 2, init_y_list[5])

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

    package_reset_needed = False # This will determine if the package cycle has to start over again (at conveyor0)

    # Update the characters
    mario.update()
    luigi.update()

    # First, update conveyor0 and package0 (they don't depend on previous conveyor)
    conveyor0.update(truck.delivering)
    package0.update(conveyor0.x, conveyor0.limit, mario.level, conveyor0.reset)

    # Update the rest of the conveyors and packages
    for index in range(len(conveyors)):
        conveyors[index].update(truck.delivering, packages[index - 1].collision)

        # Luigi handles odd indices, Mario handles even ones
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

    # If a package reaches the truck, trigger package reset
    if truck.package_added:
        package_reset_needed = True

    # Reset all packages/conveyors if needed
    if package_reset_needed:
        for index in range(len(packages)):
            packages[index].reset_packages(init_y_list[index])

        for conveyor in conveyors:
            conveyor.reset_conveyors()

        truck.package_added = False # If this is not set to False, the reset for packages will continue to be triggered

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