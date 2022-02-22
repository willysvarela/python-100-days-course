import colorgram
from turtle import Turtle, Screen
import random
colors = colorgram.extract('image.jpg', 25)
colorsRgb = []

for color in colors:
    rgb = (color.rgb.r, color.rgb.g, color.rgb.b)
    colorsRgb.append(rgb)
print(colorsRgb)
turtle = Turtle()
screen = Screen()
screen.colormode(255)
size = 20
gap = size + 20
for i in range(10):
    for j in range(10):
        turtle.pendown()
        turtle.dot(size, random.choice(colorsRgb))
        turtle.penup()
        turtle.forward(gap)
    turtle.goto(0, turtle.ycor()+gap)

screen.exitonclick()