import tkinter as tk

window = tk.Tk()
window.geometry("500x200")
window.title("Mile to Km Converter")
window.config(padx=30, pady=50)

l1 = tk.Label(text="Miles", font=("Courier", 24))
l1.grid(column=2, row=0)
l2 = tk.Label(text="is equal to", font=("Courier", 24))
l2.grid(column=0, row=1)
l3 = tk.Label(text="Km", font=("Courier", 24))
l3.grid(column=2, row=1)
answer = tk.Label(text="0", font=("Courier", 24))
answer.grid(column=1, row=1)

def button_clicked():
    km = float(entry.get())*1.60934
    answer.config(text=f"{km:.2f}")

entry = tk.Entry()
entry.grid(column=1, row=0)

button = tk.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()