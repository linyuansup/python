import turtle


def draw_round(x, y, r):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(r)


turtle.setup(800, 600)
turtle.speed(50)
for i in range(5):
    for j in range(5 - i):
        draw_round(-300 + 100 * j + 50 * i, 200 - 100 * i, 50)
turtle.done()
