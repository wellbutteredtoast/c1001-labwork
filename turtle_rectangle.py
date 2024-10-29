import turtle

def drawRectangle(width, height):
    wn = turtle.Screen()
    fred = turtle.Turtle()
    fred.penup()
    fred.goto(-100, -100)
    fred.pendown()

    fred.forward(width)
    fred.left(90)
    fred.forward(height)
    fred.left(90)
    fred.forward(width)
    fred.left(90)
    fred.forward(height)
    fred.hideturtle()
    

for i in range(20, 200, 20):
    drawRectangle(i, i*2)

ex = ""
while ex != "y":
    ex = str(input("Exit: "))