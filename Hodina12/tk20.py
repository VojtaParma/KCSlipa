import tkinter as tk    
root = tk.Tk()
root.geometry("500x500")

pocet = 0
def klik():
    global pocet
    pocet += 1
    label.config(text=pocet)

label = tk.Label(root, text=0, font=("Arial", 25))
label.pack()

btn = tk.Button(root, text="Přidat", command=klik)
btn.pack()  

root.mainloop()