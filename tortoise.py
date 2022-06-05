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
        self.head = self
        self.goto(STARTING_POSITION)

    def move(self):
        self.head.setheading(UP)
        self.head.forward(MOVE_DISTANCE)




