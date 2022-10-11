import turtle


def draw_square():
    turtle.forward(150)
    turtle.right(90)
    turtle.circle(-150, 45)
    turtle.right(90)
    turtle.forward(150)


turtle.setup(800, 600)
for i in range(4):
    draw_square()
    turtle.right(45)
turtle.done()