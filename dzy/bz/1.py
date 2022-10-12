import math
import turtle


def draw_round(x, y, r):
    turtle.penup()
    turtle.goto(x, y - r)  # 移动到圆心下方
    turtle.pendown()
    turtle.circle(r)


if __name__ == '__main__':
    turtle.pensize(50)
    turtle.speed(50)
    turtle.pencolor('red')
    # 画两个红色的圆
    draw_round(0, 0, 200)
    draw_round(0, 0, 100)
    # 填充蓝色
    turtle.fillcolor('blue')
    turtle.begin_fill()
    turtle.penup()
    draw_round(0, 0, 100)
    turtle.end_fill()
    # 画五角星
    turtle.fillcolor('white')
    turtle.penup()
    turtle.begin_fill()
    turtle.goto(0, 75)
    turtle.right(108)
    turtle.forward(150 * math.sin(72 * math.pi / 180))
    for i in range(4):
        turtle.left(144)
        turtle.forward(150 * math.sin(72 * math.pi / 180))
    turtle.end_fill()
    turtle.done()
