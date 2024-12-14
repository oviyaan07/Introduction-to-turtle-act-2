import turtle

screen=turtle.Screen()
screen.bgcolor("white")
screen.setup(600, 600)

t=turtle.Turtle()
t.color("yellow")
t.width(7)

t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)

t.penup()
t.right(150)
t.forward(100)
t.right(90)
t.pendown()
t.forward(200)
t.right(120)
t.forward(200)
t.right(120)
t.forward(200)
t.right(120)

screen.mainloop()