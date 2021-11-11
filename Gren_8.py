from turtle import *

#kanter = 6

penup()
goto(-200,-200)
pendown()

def mangekant(kanter):
    for i in range(kanter):
        forward(100)
        left(360/kanter)

svar = input("kanter??? ")
svar = int(svar) 

mangekant(svar)





