import tkinter as tk
import random as r 
abecade = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

root = tk.Tk()
root.title("Moje aplikace")

def klik():
    print(r.choice(abecade))
btn= tk.Button(root, text="Klikni", command=klik)
btn.pack()

root.mainloop()
