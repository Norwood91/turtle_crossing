from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280
UP = 90

class Tortoise(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("White")
        self.penup()
        self.setheading(UP)
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)




