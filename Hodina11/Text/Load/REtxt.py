try:
    with open("soubossr.txt", "r", encoding="utf-8") as f:
        obsah = f.read()
    print(obsah)
except FileNotFoundError:
    print("Soubor nebyl nalezen")
