from tkinter import *
from get_word import Word
import pygame

BACKGROUND_COLOR = "#B1DDC6"

# def play_noise():
#         pygame.init()
#         sound = pygame.mixer.Sound("noise.wav") 
#         sound.play()
# play_noise()

def new_word():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = Word()
    canvas.itemconfig(lang_text, text="Spanish", fill= 'black')
    canvas.itemconfig(word_text, text=word.spanish, fill='black')
    canvas.itemconfig(card_background, image=front_image)
    flip_timer= window.after(3000, func=flip_card)

def is_known():
    word.known()
    new_word()

def flip_card():
    canvas.itemconfig(lang_text, text="English", fill='white')
    canvas.itemconfig(word_text, text=word.english, fill='white')
    canvas.itemconfig(card_background, image=back_image)
    

window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50)
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="card_front.png")
back_image = PhotoImage(file="card_back.png")
card_background = canvas.create_image(400, 263, image=front_image)
lang_text = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.grid(row=0,column=0, columnspan=2)

new_word()

wrong_image= PhotoImage(file='wrong.png')
unknown_button = Button(image=wrong_image, highlightthickness=0, command=new_word)
unknown_button.grid(row=1, column=0)

right_image = PhotoImage(file='right.png')
known_button = Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

window.mainloop()
