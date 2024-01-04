import tkinter as tk

window = tk.Tk()
window.geometry("400x400")

label = tk.Label(text="Text", font=("Courier", 24))
label.grid(column=0, row=0)

def button_clicked():
    label.config(text=entry.get())

button = tk.Button(text="old button", command=button_clicked)
button.grid(column=1, row=1)

new_button = tk.Button(text="new button", command=button_clicked)
new_button.grid(column=2, row=0)

entry = tk.Entry()
entry.grid(column=4, row=3)

window.mainloop()