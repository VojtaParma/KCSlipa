import tkinter as tk
import random as r

root = tk.Tk()
root.geometry("600x600")

barvy = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
def zmen_barvu():
    barva = r.choice(barvy)
    root.config(bg=barva)

tk.Button(root, text="Změnit barvu", command=zmen_barvu).pack()
root.mainloop()