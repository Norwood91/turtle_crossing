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
        self.go_to_start()

    def move(self):
        self.forward(MOVE_DISTANCE)


    def at_finish_line(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)


