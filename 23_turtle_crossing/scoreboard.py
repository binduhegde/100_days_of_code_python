from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.level = 1
        self.write_level()

    # goes to the top left corner and writes the level number
    def write_level(self):
        self.goto(-290, 270)
        self.write(f"LEVEL: {self.level}", font=FONT)

    # increases the level by one and wrotes it. it's called when the player crosses the road safely
    def increase_level(self):
        self.clear()
        self.level += 1
        self.write_level()

    # writes "GAME OVER" when the player gets hit by a car
    def game_over(self):
        self.goto(0,30)
        self.write("GAME OVER!", align='center', font=FONT)
