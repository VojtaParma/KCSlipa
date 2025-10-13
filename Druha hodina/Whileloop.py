import time as t
x = int(input("Zadejte číslo: "))
counter = 0
while counter < x + 1:
    print("Počítadlo:",counter)
    t.sleep(0.5)
    counter += 1
t.sleep(5)
print("Konec.")
