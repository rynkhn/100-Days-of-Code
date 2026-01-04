import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Road Crossing Game")
screen.tracer(0)

screen.listen()
game_is_on = True
Reyan = Player()
screen.onkey(Reyan.go_up, "Up")
screen.onkey(Reyan.go_down, "Down")
cars = []
i = 0
while game_is_on:
    if i == 10:
        i = 0
        new_car = CarManager()
        cars.append(new_car)
    time.sleep(0.1)
    i+= 1
    
    for car in cars:
        car.move()
    for car in cars:
        if car.distance(Reyan) < 20:
            game_over = Turtle()
            game_over.hideturtle()
            game_over.write("Game Over", align="center", font=("Arial", 25, "bold"))

            game_is_on = False
    
    screen.update()

screen.exitonclick()