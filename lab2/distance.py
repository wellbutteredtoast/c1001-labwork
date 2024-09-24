import turtle
import math

# Ask the user to input two points.

x1,y1 = eval(input("Enter x1 and y1 for point 1, separated by comma: "))
x2,y2 = eval(input("Enter x2 and y2 for point 2, separated by comma: "))


# Calculate distance between points.
distance = math.sqrt( (x1-x2)**2 + (y1-y2)**2)

# Draw a line between points.

wn = turtle.Screen()
aTurtle = turtle.Turtle()

aTurtle.penup()
aTurtle.goto(x1,y1)
aTurtle.pendown()
aTurtle.goto(x2,y2)

# Move to the centre of the line.
aTurtle.penup()
aTurtle.goto( (x1+x2)/2, (y1+y2)/2)
aTurtle.write( "Distance = " + str(round(distance,2)), font = 16)

wn.mainloop()