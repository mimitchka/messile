import math
import turtle


window = turtle.Screen()
window.setup(1200, 800 )
window.bgpic('images/background.png')
window.screensize(1200, 800)

BASE_X, BASE_Y = 0, -300

def calc_headong(x1, y1, x2, y2):
    dx = x2 - x1
    lenght = ((x2-x1) ** 2 + (y2-y1) **2) ** 0.5
    cos_alpha = dx / lenght
    alpha = math.acos(cos_alpha)
    alpha = math.degrees(alpha)
    return alpha


def fire_messile(x, y):
    messile = turtle.Turtle()
    messile.color('white')
    messile.penup()
    messile.setpos(x=BASE_X, y=BASE_Y)
    messile.pendown()
    heading = calc_headong(x1=BASE_X, y1=BASE_Y, x2=x, y2=y)
    messile.setheading(heading )
    messile.forward(500)
    messile.shape('circle')
    messile.shapesize(2)
    messile.shapesize(3)
    messile.shapesize(4)
    messile.shapesize(5)
    messile.clear()
    messile.hideturtle()

window.onclick(fire_messile)


while True:
    window.update()







