from turtle import Screen
from tortoise import Tortoise
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Crossing by Robert L. Norwood")
screen.tracer(0)

tortoise = Tortoise()

screen.listen()
screen.onkey(tortoise.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()



screen.exitonclick()
