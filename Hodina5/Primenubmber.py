number = int(input("Zadejte číslo: "))

def ff(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

if ff(number):
    print(number, "je prvočíslo.")
else:
    print(number, "není prvočíslo.")
