from turtle import *

v = 200 #velocidad de la tortuga   #cambiar a otroo
step = 15 #pasos de las líneas

t = Turtle()
t.color('blue')
t.width('9')
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

def setYellow():
    t.color('yellow')

def setBlack():
    t.color('black') #añadir mas colores

def setCoral():
    t.color('coral')

def setPurple():
    t.color('purple')

def setMistyrose():
    t.color('mistyrose')

def setNavajowhite():
    t.color('navajowhite')

def setPalegreen():
    t.color('palegreen')

def setPaleturquoise():
    t.color('paleturquoise')

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


t.ondrag(draw)

scr = t.getscreen()
scr.onscreenclick(move)
scr.onkey(setRed, 'r') #visual stude
scr.onkey(setGreen, 'g')
scr.onkey(setBlue, 'b')
scr.onkey(setYellow, 'y') #cambiar las teclas
scr.onkey(setBlack, 'o')
scr.onkey(setCoral, 'c')
scr.onkey(setPurple, 'p')
scr.onkey(setMistyrose, 'm')
scr.onkey(setNavajowhite, 'n')
scr.onkey(setPalegreen, 's')
scr.onkey(setPaleturquoise, 't')
scr.onkey(stepUp, 'Up')
scr.onkey(stepDown, 'Down')
scr.onkey(stepLeft, 'Left') 
scr.onkey(stepRight, 'Right')
scr.onkey(startFill, 'f')
scr.onkey(endFill, 'e')

scr.listen()