from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.player()

    def player(self):
        self.shape("turtle")
        self.color("black")
        self.pu()

    def up(self):
        pass
