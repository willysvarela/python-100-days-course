from turtle import Turtle, Screen

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
direction = RIGHT
is_game_on = True

screen = Screen()
snake = Turtle()
snk = []

screen.bgcolor("#000")

for _ in range(3):
    snk.append(Turtle())

x = 0
print(snk)
for square in snk:
    square.setpos(x*20, 0)
    x += 1
    square.penup()
    square.color("#fff")
    square.shape("square")


def moveSnake():


def goRight():
    direction = RIGHT
    print("right")
    moveSnake()

def goUp():
    direction = UP


def goLeft():
    direction = LEFT


def goDown():
    direction = DOWN


def stop():
    is_game_on = False


screen.listen()
screen.onkey(goRight, "d")
screen.onkey(goUp, "w")
screen.onkey(goLeft, "a")
screen.onkey(goDown, "s")

screen.onkey(stop, "c")

screen.exitonclick()
