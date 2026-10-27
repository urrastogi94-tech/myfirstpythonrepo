import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Clock")
clock = tk.Label(root, font=("Arial", 48), padx=20, pady=20)
clock.pack()

def update_clock():
    clock.config(text=strftime("%H:%M:%S"))
    root.after(1000, update_clock)

update_clock()
root.mainloop()
 