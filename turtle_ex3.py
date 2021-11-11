import turtle
s=turtle.getscreen()
t=turtle.Turtle()


def flytting():
    move(0,250)
    
    for i in range(45):
        t.fillcolor('#00aaff')
        t.begin_fill()
        
        figur(10+i)  # +i
        
        t.end_fill()
        t.penup()
        t.fd(i**1.4) #+i
        t.rt(i)
        t.pendown()

def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def figur(side):    
    for i in range(4):     
        t.fd(side)
        t.right(90)

def sirkel():
    for i in range(360):
        t.fd(1)
        t.right(1)

t.speed(800)
flytting()

