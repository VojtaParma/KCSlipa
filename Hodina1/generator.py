import random as R
znamenka = ["+", "-", "*"]
znamenko = R.choice(znamenka)
prvni = R.randint(1, 100)
druhe = R.randint(1, 100)
print("napis vysledek", prvni,znamenko, druhe)
odpoved = input()
if znamenko == "+":
    if int(odpoved) == prvni + druhe:
        print("spravne")
    else:
        print("spatne, spravna odpoved je", prvni + druhe)

elif znamenko == "-":
    if int(odpoved) == prvni - druhe:
        print("spravne")
    else:
        print("spatne, spravna odpoved je", prvni - druhe)
elif znamenko == "*":
    if int(odpoved) == prvni * druhe:
        print("spravne")
    else:
        print("spatne, spravna odpoved je", prvni * druhe)
else:
    print("spatne, spravna odpoved je", prvni + druhe)