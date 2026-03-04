import tkinter as tk

def uloz():
    text = text_box.get("1.0", tk.END)
    nazev = nazev_soubor.get()
    a_pismeno = pismeno_a.get()

    klic = ord(a_pismeno) - ord("A")

    vysledek = ""

    for znak in text:
        vysledek += chr(ord(znak) + klic)

    with open(nazev, "w", encoding="utf-8") as f:
        f.write(vysledek)


root = tk.Tk()

text_box = tk.Text(root)
text_box.pack()

nazev_soubor = tk.Entry(root)
nazev_soubor.insert(0, "zasifrovano.txt")
nazev_soubor.pack()

pismeno_a = tk.Entry(root)
pismeno_a.pack()

tk.Button(root, text="Uložit", command=uloz).pack()

root.mainloop()
