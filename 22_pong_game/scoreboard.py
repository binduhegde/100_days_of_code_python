from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(-100, 260)
        self.l_score = 0
        self.r_score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"{self.l_score}      {self.r_score}", font=("Courier", 40, "normal"))

    