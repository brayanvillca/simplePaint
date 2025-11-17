from turtle import *
from interface_paint import *


v = 0 # velocidad máxima de la tortuga
step = 10 # pasos

t = Turtle()
t.color('black')
t.width(5)
t.shape('circle')
t.pendown()
t.speed(v)


def draw(x, y):
  t.goto(x, y)


def move(x, y):
  t.penup()
  t.goto(x, y)
  t.pendown()


def setRed():
  t.color('red')


def setGreen():
  t.color('green')


def setBlue():
  t.color('blue')


def setOrange():
    t.color('orange')


def setYellow():
    t.color('yellow')


def setLightBlue():
    t.color('light blue')


def setViolet():
    t.color('violet')


def setWidth_1():
    t.width(5)


def setWidth_2():
    t.width(10)


def setWidth_3():
    t.width(18)


def setWidth_4():
    t.width(25)


def setWidth_5():
    t.width(35)    
 
def stepUp():
 t.goto(t.xcor(), t.ycor() + step)
 
def stepDown():
 t.goto(t.xcor(), t.ycor() - step)
 
def stepLeft():
 t.goto(t.xcor() - step, t.ycor())
 
def stepRight():
 t.goto(t.xcor() + step, t.ycor())
 
def startFill():
  t.begin_fill()
 
def endFill():
  t.end_fill()


def background_black():
    scr.bgcolor('black')


def background_white():
    scr.bgcolor('white')


t.ondrag(draw)


scr = t.getscreen()


scr.onscreenclick(move)
scr.onkey(setRed,'r')
scr.onkey(setGreen,'g')
scr.onkey(setBlue,'b')
scr.onkey(setOrange,'o')
scr.onkey(setYellow,'y')
scr.onkey(setLightBlue,'l')
scr.onkey(setViolet,'v')


scr.onkey(setWidth_1,'1')
scr.onkey(setWidth_2,'2')
scr.onkey(setWidth_3,'3')
scr.onkey(setWidth_4,'4')
scr.onkey(setWidth_5,'5')


scr.onkey(stepUp,'Up')
scr.onkey(stepDown,'Down')
scr.onkey(stepLeft,'Left')
scr.onkey(stepRight,'Right')


scr.onkey(startFill,'f')
scr.onkey(endFill,'e')


scr.onkey(background_black,'n')
scr.onkey(background_white,'d')
 
scr.listen()
exitonclick()
