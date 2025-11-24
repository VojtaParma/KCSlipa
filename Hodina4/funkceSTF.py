def je_kladne(x):
    if x > 0:
        return True  
    else:
        return False  


x = int(input("Zadej číslo: "))

if je_kladne(x):
    print(x, "je kladné číslo.")
else:
    print(x, "není kladné číslo.")