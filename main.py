from turtle import Screen
from tortoise import Tortoise
from cars import Cars
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

screen.exitonclick()
