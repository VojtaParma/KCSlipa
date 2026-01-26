text = input("Zadej text: ")
nazev = input("Zadej název souboru pro uložení (např. zasifrovano.txt): ")
a_pismeno = input("Zadej znak, který má odpovídat A: ")

klic = ord(a_pismeno) - ord("A")

vysledek = ""

for znak in text:
    vysledek += chr(ord(znak) + klic)

with open(nazev, "w", encoding="utf-8") as f:
    f.write(vysledek)
