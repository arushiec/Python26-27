#main.py

from myfunctions import *

bob.speed(0)

turtle.colormode(255)


jump(0,-300)
c = (255, 128, 0)
polygon(200, 4, c)

jump(0,0)
c = (0, 255, 153)
polygon(200, 4, c)

jump(-200, 200)
c = (128, 0, 0)
polygon(200, 4, c)

jump(-400, -300)
c = (255, 153, 153)
polygon(200, 4, c)

jump(0, 0)
c = (255, 153, 153)
bob.begin_fill()
bob.circle(100)
bob.end_fill()

jump(-450,0)
c = (0, 51, 0)
bob.begin_fill()
bob.circle(100)
bob.end_fill()


jump(-400, 0)
c = (204, 0, 24)
polygon(600, 3, c)

jump(400, 0)
c = (204, 0, 24)
polygon(150, 8, c)


