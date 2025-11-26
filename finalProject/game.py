import pyxel

class Game:
    def __init__(self):
        pyxel.init(256, 128)
        pyxel.load("../assets/my_resource.pyxres")

        self.x = 40
        self.y = 40

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 1
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 1
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= 1
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 1

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 256, 128)     # draw tilemap
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 0)  # draw player sprite

Game()
