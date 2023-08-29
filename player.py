from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.gotToStart()
        self.setheading(90)

    def goUp(self):
        self.forward(MOVE_DISTANCE)

    def gotToStart(self):
        self.goto(STARTING_POSITION)

    def isAtFinishLine(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
