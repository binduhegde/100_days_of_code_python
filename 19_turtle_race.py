import turtle as t
import random

screen = t.Screen()
screen.setup(600, 500)

inp = screen.textinput(title="Make your bet", prompt="Which turtle do you think will win? enter a color")
colors = ['red', 'blue', 'green', 'purple', 'orange', 'yellow']
turtles = []


y = -150
for i in range(6):
    tutu = t.Turtle(shape='turtle')
    tutu.color(colors[i])
    tutu.penup()
    tutu.goto(-250, y)
    y += 60
    turtles.append(tutu)

race_on = True
while race_on:
    for turtle in turtles:
        if turtle.xcor() > 300:
            race_on = False
            if turtle.pencolor() == inp:
                print(f'You won! the winner is the {turtle.pencolor()} turtle')
            else:
                print(f'You lost! the winner is the {turtle.pencolor()} turtle')
        turtle.forward(random.randint(0, 10))





screen.exitonclick()