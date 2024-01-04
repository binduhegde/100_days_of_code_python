from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('white')
        self.goto(STARTING_POSITION)
        self.left(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    # returns True if player crossed the road safely and False otherwise
    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y
    
    # if is_at_finish_line is True, this will be called which reset's the player's position back to where it began
    def go_to_start(self):
        self.goto(STARTING_POSITION)
            