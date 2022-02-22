from turtle import Turtle, Screen

screen = Screen()
turtle = Turtle()

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
DISTANCE = 100
CLOCKANGLE = 6

def left():
    turtle.setheading(LEFT)
    turtle.forward(DISTANCE)

def up():
    turtle.setheading(UP)
    turtle.forward(DISTANCE)

def right():
    turtle.setheading(RIGHT)
    turtle.forward(DISTANCE)

def down():
    turtle.setheading(DOWN)
    turtle.forward(DISTANCE)

def clock():
    print("clock")

    turtle.circle(DISTANCE, CLOCKANGLE)

def counterclock():
    print("counterclock")
    turtle.circle(DISTANCE, CLOCKANGLE*-1)

def leftangle():
    turtle.setheading(turtle.heading() - CLOCKANGLE)

def rightangle():
    turtle.setheading(turtle.heading() + CLOCKANGLE)

def go():
    turtle.forward(DISTANCE)

screen.onkey(up, "w")
screen.onkey(left, "a")
screen.onkey(down, "s")
screen.onkey(right, "d")
screen.onkey(clock, "r")
screen.onkey(counterclock, "f")

screen.onkey(leftangle, "z")
screen.onkey(rightangle, "x")
screen.onkey(go, "c")

screen.listen()
screen.exitonclick()