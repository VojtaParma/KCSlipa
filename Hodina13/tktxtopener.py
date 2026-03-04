import tkinter as tk
root = tk.Tk()

def open_file():
    with open("poznamka.txt", "r") as f:
        obsah = f.read()

    if obsah =="cervsena":s
        root.config(bg="red")

        
    text.config(text=obsah)


text = tk.Label(root, text="")
text.pack()
tk.Button(root, text="Otevřít soubor", command=open_file).pack()
root.mainloop()