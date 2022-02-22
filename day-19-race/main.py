import random
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)
screen.setup(400, 400)
HEIGHT = (screen.window_height())-40
is_race_on = False

QTY = 6
height_gap = (HEIGHT/QTY)
print("HEIGHT: ", HEIGHT, "GAP: ", height_gap)
value = screen.numinput("Quem vai ganhar essa parada?", "Põe aqui")

tugs = []
for _ in range(QTY):
    tugs.append(Turtle())

x = 0
for tug in tugs:
    pos_y = -HEIGHT/2 + (height_gap)*x
    tug.penup()
    tug.shape("turtle")
    tug.color((random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))
    tug.goto(-screen.window_width()/2 + 20, pos_y)
    print(pos_y)
    x += 1

if value:
    is_race_on = True

while is_race_on:
    for tug in tugs:
        tug.pendown()
        tug.speed(random.randint(0, 5))
        tug.forward(random.randint(0, 20))
        if tug.xcor() > screen.window_width()/2 - 20:
            winner_color = tug.color()
            screen.numinput("Ganhou lol", f"A tortuguita {winner_color} ganhoou lol")
            is_race_on = False
        # tug.goto(screen.window_width()/2, tug.ycor())


# tug.setpos(-screen.window_width()/2+20, 0)

screen.exitonclick()