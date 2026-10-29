import turtle

tu=turtle.Turtle()
tu.color("black", "blue")
tu.penup()
tu.right(30)
tu.forward(32)
tu.pendown()
tu.begin_fill()
for i in range(10):
    tu.forward(150)
    tu.left(45)
tu.end_fill()
turtle.done()
