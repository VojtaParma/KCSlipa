A = int(input("Zadej prvni cislo: "))
B = int(input("Zadej druhe cislo: "))
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


2