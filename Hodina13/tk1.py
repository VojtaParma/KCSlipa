import tkinter as tk
root = tk.Tk()
root.geometry("200x200")
def cervena():
    root.config(bg="red")
def modra():
    root.config(bg="blue")
tk.Button(root, text="Červená", command=cervena).pack()
tk.Button(root, text="Modrá", command=modra).pack()
root.mainloop()
