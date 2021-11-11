import turtle
s = turtle.getscreen()
t = turtle.Turtle()

svar = input("Vil du ha rød, gul eller blå farge? svar r,g eller b: ")
    
if svar == "r":
    print("rød")
    t.color("red")
    for i in range(4):
        t.forward(100)
        t.right(90)
        
elif svar == "g":
    print("gul")
    t.color("yellow")
    for i in range(4):
        t.forward(100)
        t.right(90)
       
elif svar == "b":
    print("blå")
    t.color("blue")
    for i in range(4):
        t.forward(100)
        t.right(90)
    
else:
    print("ugyldig svar")










