import pyxel 

pyxel.init(160, 120)

def update():
    pyxel.cls(15)
    

def draw():
    pyxel.line(0,0, pyxel.mouse_x, pyxel.mouse_y, 5)

pyxel.run(update, draw)
