import random

maara = int(input("Arvaa arpaluutioinen lukumäärä:"))
summa = 0

for i in range(maara):
    heitto = random.randint(1, 6)
    print(f"noppa {heitto}")
    summa += heitto
print(f"Apakuutioiden summa on {summa}")