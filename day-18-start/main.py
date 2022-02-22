import random
from turtle import Turtle, Screen

tuguinha = Turtle()

# for i in range(5):
#     tuguinha.setposition(0, i*100)
#     for _ in range(10):
#         tuguinha.pendown()
#         tuguinha.dot(20, "#000")
#         tuguinha.penup()
#         tuguinha.forward(30)
#


# def draw_shape(qty_sides):
#     tuguinha.color(randint(0, 0), randint(0, 1), randint(0, 1))
#     for __ in range(qty_sides):
#         degree = 360 / qty_sides
#         tuguinha.left(degree)
#         tuguinha.forward(100)
#
#
# for qty_sides in range(3, 10):
#     draw_shape(qty_sides)
#


screen = Screen()

colors = ["#faebd7", "#00ffff", "#7fffd4", "#f0ffff", "#f5f5dc", "#ffe4c4", "#000000", "#ffebcd", "#0000ff", "#8a2be2",
          "#a52a2a"]
tuguinha.pensize(10)
tuguinha.speed(0)

screen.colormode(255)
# for _ in range(100):
#     color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     tuguinha.color(color)
#     tuguinha.setheading(random.choice((0, 90, 180, 270)))
#     tuguinha.forward(30)
#
angle = 10
qty = int(360 / angle);
for _ in range(qty):
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tuguinha.color(color)
    tuguinha.pensize(5)
    tuguinha.circle(200, 360, 360)
    tuguinha.left(angle)

screen.exitonclick()
