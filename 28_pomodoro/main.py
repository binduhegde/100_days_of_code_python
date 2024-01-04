from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#00a23e"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    reset_button.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    label.config(text='Timer')
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        label.config(text='Break', fg = RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        label.config(text='Break', fg = PINK)
    else:
        count_down(WORK_MIN*60)
        label.config(text='Work', fg = GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    mins = count //60
    if len(str(mins)) == 1:
        mins = '0'+ str(mins)
    
    secs = count % 60
    if len(str(secs)) == 1:
        secs = '0'+ str(secs)
    
    canvas.itemconfig(timer_text, text= f"{mins}:{secs}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = "✔️" * (reps//2)
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", font=(FONT_NAME, 35))
label.config(bg=YELLOW, fg=GREEN)
label.grid(row=0, column=1)

start_button = Button(text="Start", font=(FONT_NAME, 20), highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", font=(FONT_NAME, 20), highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = Label(font=(FONT_NAME, 20), bg=YELLOW, fg=GREEN)
check_marks.grid(row=3, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image = tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)
#count_down(5)

window.mainloop()

