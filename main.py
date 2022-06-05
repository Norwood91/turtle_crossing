from turtle import Screen
from tortoise import Tortoise
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

tortoise = Tortoise()

screen.listen()


game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
