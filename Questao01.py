import pyxel 

pyxel.init(160, 120)

def update():
    pass

def draw():
    pyxel.rect(pyxel.mouse_x, pyxel.mouse_y, 20, 20, 1)

pyxel.run(update, draw)

