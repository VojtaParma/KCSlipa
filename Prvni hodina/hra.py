import random
odpoved = ""
nahodneCislo = random.randint(1, 5)
print(nahodneCislo)
while odpoved != str(nahodneCislo):
    print("Spatne, skus znova")
    odpoved = input()