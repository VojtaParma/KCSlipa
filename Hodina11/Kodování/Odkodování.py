nazev_souboru = input("Zadej název souboru (např. zasifrovano.txt): ")

a_pismeno = input("Zadej znak, který odpovídá A: ")

klic = ord(a_pismeno) - ord("A")

try:
    with open(nazev_souboru, "r", encoding="utf-8") as f:
        zasifrovany_text = f.read()

    rozlusteny_text = ""
    for znak in zasifrovany_text:
        rozlusteny_text += chr(ord(znak) - klic)

    print("Rozluštěná zpráva:")
    print(rozlusteny_text)

except FileNotFoundError:
    print(f"Soubor '{nazev_souboru}' nebyl nalezen.")
