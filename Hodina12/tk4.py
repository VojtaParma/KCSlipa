import tkinter as tk

root = tk.Tk()

text = tk.Text(root)
text.pack()

def uloz():
    with open("poznamka.txt", "w", encoding="utf8") as f:
        f.write(text.get("1.0", tk.END))

tk.Button(root, text="Uložit", command=uloz).pack()

root.mainloop()
