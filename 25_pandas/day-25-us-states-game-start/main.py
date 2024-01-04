import turtle as t
import pandas as pd
import pygame 

df = pd.read_csv('50_states.csv')

screen = t.Screen()
screen.title("Guess the U.S. States")
screen.setup(725,491) # dimension of the image
screen.addshape('image.gif')

map = t.Turtle()
map.shape('image.gif')


def happy_sound():
    pygame.init()
    sound = pygame.mixer.Sound("happy.wav")
    sound.play()

def sad_sound():
    pygame.init()
    sound = pygame.mixer.Sound("sad.wav")
    sound.play()


def write_on_map(text, x, y):
    screen.tracer(False)
    turtle = t.Turtle()
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(x, y)
    turtle.write(text, align='center', font=("Courier", 12, "normal"))
    screen.tracer(True)

all_states = list(df['state'])
user_states = []
score = 0

while score < 50:
    inp = screen.textinput(f"{score}/50 correct", "Guess a state").title()
    if inp in all_states and inp not in user_states:
        state_data = df[df['state'] == inp]
        # saying state_data.x is as same as state_data['x']
        write_on_map(inp, int(state_data.x), int(state_data.y))
        score += 1
        user_states.append(inp)
        happy_sound()
    elif inp == 'Quit':
        break
    
    else:
        sad_sound()

if score == 50:
    print("Congrats! You named all the states")
else:
    print("You missed these states:")
    for i in all_states:
        if i not in user_states:
            print(i)

screen.mainloop()