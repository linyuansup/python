import turtle


def draw_snack(color):
    turtle.color(color)
    turtle.circle(30, 100)
    turtle.circle(-30, 100)

turtle.speed(0)
turtle.pensize(20)
turtle.seth(-50)
draw_snack("red")
draw_snack("blue")
draw_snack("green")
draw_snack("yellow")
turtle.color("purple")
turtle.seth(0)
turtle.forward(30)
turtle.circle(20, 180)
turtle.forward(30)
turtle.done()