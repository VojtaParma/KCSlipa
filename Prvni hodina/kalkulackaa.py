A = input("Zadej prvni cislo: ")
B = input("Zadej druhe cislo: ")
operace = input("Zadej operaci (+, -, *, /): ")
if operace == "+":
    print(int(A) + int(B))
elif operace == "-":
    print(int(A) - int(B))
elif operace == "*":
    print(int(A) * int(B))
elif operace == "/":
    print(int(A) / int(B))
else :
    print("Neznamy operator")


