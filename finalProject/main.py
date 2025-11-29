import pyxel
from player import Player

pyxel.init(256, 128)
pyxel.load("../assets/my_resource.pyxres")
pyxel.cls(0)
pyxel.bltm(0, 0, 0, 0, 0, 256, 128)


mario = Player("right")
luigi = Player("left")

def update():
    # Use this function to alter mario and luigi's position (add conditions for when 8 packages at truck, etc.)
    mario.move()
    luigi.move()

def draw():
    pyxel.cls(0) # Clear the screen
    pyxel.bltm(0, 0, 0, 0, 0, 256, 128) # Redraw the tilemap
    mario.draw() # Draw Mario at its new position
    luigi.draw() # Draw Luigi at its new position

pyxel.run(update, draw) #run the program