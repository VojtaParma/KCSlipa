import time as t

kos = int(input("Kolikrat chces opakovat"))

for k in range(kos + 1):
    print(k)
    t.sleep(1)