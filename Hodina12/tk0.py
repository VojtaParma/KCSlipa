import tkinter as tk

root = tk.Tk()
root.title("Moje aplikace")

root.label = tk.Label(root, text="Ahoj světe!", font=("Arial", 24))
root.label.pack()

root.mainloop()
