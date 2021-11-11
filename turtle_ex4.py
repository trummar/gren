import turtle
import random

s=turtle.getscreen()
t=turtle.Turtle()

def flytting():       
    for teller in range(1000):
        x = random.randint(-200,400)
        y = random.randint(-200,200)
        white = 10
        
        # (-40,40)
        #sporring()
        if (x < 40 and x > 10) or (y < 40 and y > 10):

            draw(x,y,"blue",10,6)
           

        elif (x < white and x > -white) or (y < white and y > -white):

            draw(x,y,"white",10,6)
            

               
        else:
            draw(x,y,"red",10,6)
            

def sporring():
    print("hei")

def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def fylling():
    t.fillcolor('#00aaff')
    t.begin_fill()

def figur(side,kanter):    
    for i in range(kanter):     
        t.fd(side)
        t.right(360/kanter)

def draw(x,y,farge,lengde,kanter):
    move(x,y)
    t.fillcolor(farge)
    t.begin_fill()
    figur(lengde,kanter)  
    t.end_fill()
        
        
t.speed(800)
flytting()

