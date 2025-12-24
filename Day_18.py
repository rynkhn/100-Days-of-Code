color_list = [(70, 94, 136), (23, 32, 54), (126, 150, 177), (24, 34, 29), (37, 52, 116), (36, 33, 24), (145, 166, 152), (171, 172, 130), (94, 120, 174), (85, 103, 93), (101, 100, 69), (158, 152, 62), (202, 203, 146), (31, 25, 29), (73, 79, 32), (112, 138, 124), (214, 214, 187), (104, 136, 145), (196, 214, 199), (52, 71, 59), (192, 206, 221), (178, 201, 181), (95, 87, 93), (170, 185, 223), (45, 71, 77), (162, 153, 160), (174, 198, 203), (214, 205, 211), (85, 54, 46), (72, 58, 64)]

import turtle as t
import random
t.Turtle()
t.penup()
t.hideturtle()

t.setworldcoordinates(-100, -100, 100, 100)
t.colormode(255)

random_color = (random.choice(color_list))
t.penup()
t.speed("fastest")
t.hideturtle()


def left_up():
    t.setheading(90)
    t.forward(10)
    t.setheading(180)


def right_up():
    t.setheading(90)
    t.forward(10)
    t.setheading(0)

t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
for _ in range(5):
    for _ in range(10):
        t.dot(20, (random.choice(color_list)))
        t.setheading(0)
        t.forward(10)
    left_up()
    for _ in range(10):
        t.forward(10)
        t.dot(20, (random.choice(color_list)))
    right_up()


screen = t.Screen()
screen.exitonclick()