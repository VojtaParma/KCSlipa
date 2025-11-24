cislo = int(input("Zadejte číslo: "))


def is_prime(number):
    if number < 2:
            return False
    for i in range(2, number**0.5 + 1):
            if number % i == 0:
                return False
            return True
    
if cislo % 2 == 0:
    print(cislo, "je sudé číslo.")
else:
    print(cislo, "je liché číslo.")

if is_prime(cislo):
    print(cislo, "je prvočíslo.")
else:
    print(cislo, "není prvočíslo.")
