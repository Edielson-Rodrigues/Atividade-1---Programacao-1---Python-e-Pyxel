import pyxel

class JogoDaVelha:

    def __init__(self):
        pyxel.init(160, 160)
        pyxel.run(self.update, self.draw)

    def update(self):
        pyxel.cls(4)
    
    def draw(self):
        pyxel.rectb(40, 40, 80, 80, 7)
        pyxel.rectb(40, 67, 80, 80/3, 7)
        pyxel.rectb(67, 40, 80/3, 80, 7)
        
JogoDaVelha()