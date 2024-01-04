# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))
# print(rgb_colors)
import turtle
import random

turtle.colormode(255)
gibbi = turtle.Turtle()
gibbi.pensize(20)
gibbi.speed(0)
screen = turtle.Screen()
screen.setup(700,700)


colors = [(167, 168, 161), (195, 198, 195), (170, 174, 169), (198, 198, 196), (106, 104, 68), (170, 161, 26), (73, 97, 4), (33, 32, 15), (65, 102, 124), (98, 102, 99), (22, 31, 43), (16, 28, 10), (43, 99, 3), (193, 196, 176), (189, 193, 188), (150, 164, 170), (50, 62, 82), (168, 166, 168), (37, 71, 87), (198, 199, 201), (125, 129, 125), (96, 138, 153), (11, 9, 10), (112, 103, 108), (201, 199, 201), (113, 127, 146), (76, 59, 54), (191, 191, 193), (138, 124, 119), (188, 193, 194)]

position = 300
gibbi.penup()

for i in range(10):
    gibbi.goto((-300, position))
    for j in range(10):
        gibbi.color(random.choice(colors))
        gibbi.pendown()
        gibbi.forward(1)
        gibbi.penup()
        gibbi.forward(50)
    position -= 50









screen.exitonclick()