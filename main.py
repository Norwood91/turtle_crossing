from turtle import Screen
from tortoise import Tortoise
from cars import Cars
from scoreboard import Scoreboard


import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Crossing by Robert L. Norwood")
screen.tracer(0)

tortoise = Tortoise()
car_manager = Cars()


screen.listen()
screen.onkey(tortoise.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(tortoise) < 20:
            game_is_on = False

    #Detect a successful crossing
    if tortoise.at_finish_line():
        tortoise.go_to_start()
        car_manager.level_up()

screen.exitonclick()
