import pyxel

class Background:
    def __init__(self):
        pyxel.init(256, 128)
        pyxel.load("../assets/my_resource.pyxres")

        self.y = 92



        pyxel.run(self.update, self.draw)

    def update(self):
        if self.side == "left"
            if pyxel.btnp(pyxel.KEY_W) and self.y > self.max_y:
                self.y -= 32
            if pyxel.btnp(pyxel.KEY_S) and self.y < self.min_y:
                self.y += 32
        else:
            if pyxel.btnp(pyxel.KEY_UP) and self.y > self.max_y:
                self.y -= 32
            if pyxel.btnp(pyxel.KEY_DOWN) and self.y < self.min_y:
                self.y += 32

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 256, 128)     # draw tilemap
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 0)  # draw player sprite

Game()
